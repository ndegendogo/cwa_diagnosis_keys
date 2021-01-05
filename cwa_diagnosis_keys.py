## Download and extract a file with diagnose keys from the cwa server.

from io import BytesIO
import json
import os
from pathlib import Path
import requests
from zipfile import ZipFile

from KeyBundle import KeyBundle


host = 'https://svc90.main.px.t-online.de'


def main():
    # download the key files from the server:
    for country in ['DE', 'EUR']:
        get_all_available_files_for_country(country)
    # parse daily key files and print number of keys
    for country in ['DE', 'EUR']:
        print_daily_key_numbers_for_country(country)
    # check if number of keys match between daily and hourly files
    for country in ['DE', 'EUR']:
        check_key_numbers_for_country(country)
    # check if the risk level is encoded consistently in (report type + days of symptoms onset)
    for day in available_days('EUR'):
        check_risk_levels('EUR', day)


# it fetches hourly files only for full days
def get_all_available_files_for_country(country):
    for day in available_days(country):
        get_all_available_files_for_country_of_day(country, day)


def get_all_available_files_for_country_of_day(country, day):
    get_key_file(country, day)
    for hour in available_hours(country, day):
        get_key_file(country, day, hour)


def print_daily_key_numbers_for_country(country):
    print(country)
    for day in available_days(country):
        print(f'{day}: {get_daily_key_count(country, day)} keys')


def check_key_numbers_for_country(country):
    for day in available_days(country):
        if not check_key_numbers_for_country_of_day(country, day):
            print(f'mismatch key count: {country}:{day}')


def check_key_numbers_for_country_of_day(country, day):
    daily_key_count = get_daily_key_count(country, day)
    hourly_key_counts = get_hourly_key_counts(country, day)
#    print(f'{country}:{day}:')
#    print(daily_key_count, hourly_key_counts)
    return (daily_key_count == sum(hourly_key_counts))


def available_days(country):
    return available_items(uri_for_days(country))


def available_hours(country, date):
    return available_items(uri_for_hours(country, date))


def available_items(uri):
    r = requests.get(uri)
    return json.loads(r.text)


def uri_for_days(country):
    # uri = '%s/version/v1/diagnosis-keys/country/%s/date' % (host, country)        ## old-style formatting (python 2)
    # uri = '{}/version/v1/diagnosis-keys/country/{}/date'.format(host, country)    ## python-3 style
    # uri = f'{host}/version/v1/diagnosis-keys/country/{country}/date'              ## >= python-3.6
    return f'{host}/version/v1/diagnosis-keys/country/{country}/date'


def uri_for_hours(country, date):
    return f'{host}/version/v1/diagnosis-keys/country/{country}/date/{date}/hour'


def uri_for_keys(country, date, hour=None):
    if (hour == None):
        return uri_for_keys_by_date(country, date)
    else:
        return uri_for_keys_by_hour(country, date, hour)


def uri_for_keys_by_date(country, date):
    return f'{host}/version/v1/diagnosis-keys/country/{country}/date/{date}'


def uri_for_keys_by_hour(country, date, hour):
    return f'{host}/version/v1/diagnosis-keys/country/{country}/date/{date}/hour/{hour}'


def path_for_keys(country, date, hour=None):
    if (hour == None):
        return path_for_daily_keys(country, date)
    else:
        return path_for_hourly_keys(country, date, hour)


def path_for_daily_keys(country, date):
    return Path(country) / date


def path_for_hourly_keys(country, date, hour):
    return Path(country) / date / str(hour)


def filename_for_keys(country, date, hour=None):
    return path_for_keys(country, date, hour) / 'export.bin'


def get_key_file(country, date, hour=None):
    path = path_for_keys(country, date, hour)
    if (not os.path.exists(path / 'export.bin')):
        uri = uri_for_keys(country, date, hour)
        r = requests.get(uri)
        if (r.status_code == 200):
            zipfile = ZipFile(BytesIO(r.content))
            zipfile.extract('export.bin', path)
        else:
            print(f'Error:{r.status_code}:{country}:{date}:{hour}')


def get_daily_key_count(country, day):
    return KeyBundle(filename_for_keys(country, day)).number_of_keys()


def get_hourly_key_counts(country, day):
    return [KeyBundle(filename_for_keys(country, day, hour)).number_of_keys() for hour in range(24)]


def check_risk_levels(country, day):
    bundle = KeyBundle(filename_for_keys(country, day))
    bundle.check_risk_levels()


#### main
if __name__ == "__main__":
    # execute only if run as a script
    main()
