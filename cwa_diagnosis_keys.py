## Download and extract a file with diagnose keys from the cwa server.

import datetime
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
        print(f'downloading missing files ({country})...')
        get_all_available_files_for_country(country)
    # parse daily key files and print number of keys
    for country in ['DE', 'EUR']:
        print_all_key_numbers_for_country(country)
#    print_additional_eur_numbers()
    # check if number of keys match between daily and hourly files
    for country in ['DE', 'EUR']:
        check_key_numbers_for_country(country)
    # check if the risk level is encoded consistently in (report type + days of symptoms onset)
    for day in available_days('EUR'):
        check_risk_levels('EUR', day)


def print_additional_eur_numbers():
    days = available_days('EUR')
    for day in days:
        eur = get_daily_key_count('EUR', day)
        de = get_daily_key_count('DE', day)
        print(f'{day}: diff = {eur - de} keys')


# it fetches hourly files: for all full days, and then for the next day
def get_all_available_files_for_country(country):
    days = available_days(country)
    for day in days:
        get_all_available_files_for_country_of_day(country, day)
    get_available_hourly_files(country, calc_next_day(days[-1]))


# input: a day (ISO format) / output: next day (ISO format)
def calc_next_day(day_string):
    day = datetime.date.fromisoformat(day_string)
    delta = datetime.timedelta(days=1)
    return str(day + delta)


def get_all_available_files_for_country_of_day(country, day):
    get_key_file(country, day)
    get_available_hourly_files(country, day)


def get_available_hourly_files(country, day):
    hours = available_hours(country, day)
    if hours:
        for hour in hours:
            get_key_file(country, day, hour)


def print_all_key_numbers_for_country(country):
    print(country)
    days = available_days(country)
    for day in days:
        print(f'{day}: {get_daily_key_count(country, day)} keys')
    partial_day = calc_next_day(days[-1])
    print(f'{partial_day}: {get_all_hourly_key_counts(country, partial_day)} keys')


def check_key_numbers_for_country(country):
    for day in available_days(country):
        check_key_numbers_for_country_of_day(country, day)


def check_key_numbers_for_country_of_day(country, day):
    daily_key_count = get_daily_key_count(country, day)
    hourly_key_counts = get_all_hourly_key_counts(country, day)
    if len(hourly_key_counts) < 24:
        # do not perform check for partial day
        return True
    if daily_key_count == sum(hourly_key_counts):
        return True
    else:
        print(f'\nmismatch key count:{country}:{day}')
        print(f'  daily count = {daily_key_count}')
        print(f'  hourly counts = {hourly_key_counts}')
        print(f'  sum of hourly counts = {sum(hourly_key_counts)}')
        return False


def available_days(country):
    return available_items(uri_for_days(country))


def available_hours(country, date):
    return available_items(uri_for_hours(country, date))


def available_items(uri):
    try:
        r = requests.get(uri)
        if r.status_code != 200 or not len(r.text):
            return None
        return json.loads(r.text)
    except requests.exceptions.ConnectionError as N:
        print(f'No connection to {uri} - please check your internet connection')
        exit(1)


def uri_for_country(country):
    # uri = '%s/version/v1/diagnosis-keys/country/%s' % (host, country)        ## old-style formatting (python 2)
    # uri = '{}/version/v1/diagnosis-keys/country/{}'.format(host, country)    ## python-3 style
    # uri = f'{host}/version/v1/diagnosis-keys/country/{country}'              ## >= python-3.6
    return f'{host}/version/v1/diagnosis-keys/country/{country}'


def uri_for_days(country):
    # uri = '%s/version/v1/diagnosis-keys/country/%s/date' % (host, country)        ## old-style formatting (python 2)
    # uri = '{}/version/v1/diagnosis-keys/country/{}/date'.format(host, country)    ## python-3 style
    # uri = f'{host}/version/v1/diagnosis-keys/country/{country}/date'              ## >= python-3.6
    return f'{uri_for_country(country)}/date'


def uri_for_hours(country, date):
    return f'{uri_for_country(country)}/date/{date}/hour'


def uri_for_keys(country, date, hour=None):
    if (hour == None):
        return uri_for_keys_by_date(country, date)
    else:
        return uri_for_keys_by_hour(country, date, hour)


def uri_for_keys_by_date(country, date):
    return f'{uri_for_country(country)}/date/{date}'


def uri_for_keys_by_hour(country, date, hour):
    return f'{uri_for_country(country)}/date/{date}/hour/{hour}'


def path_for_keys(country, date, hour=None):
    if (hour == None):
        return path_for_daily_keys(country, date)
    else:
        return path_for_hourly_keys(country, date, hour)


def path_for_daily_keys(country, date):
    return Path(country) / date


def path_for_hourly_keys(country, date, hour):
    return Path(country) / date / str(hour)


def file_for_keys(country, date, hour=None):
    return path_for_keys(country, date, hour) / 'export.bin'


def get_key_file(country, date, hour=None):
    path = path_for_keys(country, date, hour)
    if not os.path.exists(path / 'export.bin'):
        progress(country, date, hour)
        uri = uri_for_keys(country, date, hour)
        r = requests.get(uri)
        if (r.status_code == 200):
            zipfile = ZipFile(BytesIO(r.content))
            zipfile.extract('export.bin', path)
        else:
            print(f'Error:{r.status_code}:{country}:{date}:{hour}')


def progress(country, date, hour):
    if hour is None:
        print(f'.. {country} {date} ..')


def get_daily_key_count(country, day):
    return get_key_count(file_for_keys(country, day))


def get_all_hourly_key_counts(country, day):
    key_counts = []
    for hour in range(24):
        count = get_hourly_key_count(country, day, hour)
        if count != None:
            key_counts.append(count)
    return key_counts


# return number of keys, or None if the file does not exist
def get_hourly_key_count(country, day, hour):
    file = file_for_keys(country, day, hour)
    if file.exists():
        return get_key_count(file)
    else:
        return None


# param file is an *existing* file, referenced as Path or by filename; return number of keys, possibly 0
def get_key_count(file):
    return KeyBundle(file).number_of_keys()


def check_risk_levels(country, day):
    bundle = KeyBundle(file_for_keys(country, day))
    bundle.check_risk_levels()


#### main
if __name__ == "__main__":
    starttime = datetime.datetime.now()
    # execute only if run as a script
    main()
    stoptime = datetime.datetime.now()
    execution_time = stoptime - starttime
    print(f'\nexecution time = {execution_time}')
