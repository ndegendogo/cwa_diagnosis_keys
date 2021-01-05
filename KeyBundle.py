# wrapper class to parse a downloaded key file.
# The protobuf spec is generated from SAP/external/exposurenotification
# these files are as of cwa v1.9.1 (ENF v2).

import collections

import external.exposurenotification.temporary_exposure_key_export_pb2 as tek

class KeyBundle:
    def __init__(self, path):
        self.key_bundle = tek.TemporaryExposureKeyExport()
        data = read_file(path)
        if (verify_header(data)):
            self.key_bundle.ParseFromString(data[16:])
        else:
            print('Error')


    def number_of_keys(self):
        return len(self.key_bundle.keys)


    def get_first_key(self):
        return self.key_bundle.keys[0]


    def check_risk_levels(self):
        for key in self.key_bundle.keys:
            transmission_risk_level = self.get_key_trl(key)
            report_type = self.get_key_rt(key)
            days_since_onset_of_symptoms = self.get_key_dsos(key)
            encoded_risk_level = encode_risk_level(report_type, days_since_onset_of_symptoms)
            if encoded_risk_level != transmission_risk_level:
                print(f'Inconsistent encoding: TRL = {transmission_risk_level}, RT = {report_type}, DSOS = {days_since_onset_of_symptoms}')


    def number_of_revised_keys(self):
        return len(self.key_bundle.revised_keys)


    def report_numbers(self):
        counter = collections.Counter({})
        for key in self.key_bundle.keys:
            counter[key.report_type] += 1
        return counter


    def get_key_trl(self, key):
        return key.transmission_risk_level


    def get_key_dsos(self, key):
        return key.days_since_onset_of_symptoms


    def get_key_rt(self, key):
        return key.report_type


# the two fields (report type, days since onset of symptoms) are (mis-)used to encode 8 values for the risk level
def encode_risk_level(report_type, days_since_onset_of_symptoms):
    return (4 - report_type) * 2 + days_since_onset_of_symptoms


def read_file(path):
    with open(path, 'rb') as file:
        return file.read()


# The .bin file begins with a 16-byte header
# 'EK Export v1' (UTF-8) encoding, right-padded with whitespace characters.
def verify_header(data):
    return data[:16] == 'EK Export v1'.ljust(16).encode()
