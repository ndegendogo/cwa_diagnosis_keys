# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: external/exposurenotification/temporary_exposure_key_export.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from external.exposurenotification import diagnosis_key_batch_pb2 as external_dot_exposurenotification_dot_diagnosis__key__batch__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='external/exposurenotification/temporary_exposure_key_export.proto',
  package='SAP.external.exposurenotification',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nAexternal/exposurenotification/temporary_exposure_key_export.proto\x12!SAP.external.exposurenotification\x1a\x37\x65xternal/exposurenotification/diagnosis_key_batch.proto\"\xe4\x02\n\x1aTemporaryExposureKeyExport\x12\x17\n\x0fstart_timestamp\x18\x01 \x01(\x06\x12\x15\n\rend_timestamp\x18\x02 \x01(\x06\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\x11\n\tbatch_num\x18\x04 \x01(\x05\x12\x12\n\nbatch_size\x18\x05 \x01(\x05\x12I\n\x0fsignature_infos\x18\x06 \x03(\x0b\x32\x30.SAP.external.exposurenotification.SignatureInfo\x12\x45\n\x04keys\x18\x07 \x03(\x0b\x32\x37.SAP.external.exposurenotification.TemporaryExposureKey\x12M\n\x0crevised_keys\x18\x08 \x03(\x0b\x32\x37.SAP.external.exposurenotification.TemporaryExposureKey\"\x9b\x01\n\rSignatureInfo\x12\x15\n\rapp_bundle_id\x18\x01 \x01(\t\x12\x17\n\x0f\x61ndroid_package\x18\x02 \x01(\t\x12 \n\x18verification_key_version\x18\x03 \x01(\t\x12\x1b\n\x13verification_key_id\x18\x04 \x01(\t\x12\x1b\n\x13signature_algorithm\x18\x05 \x01(\t\"\x87\x02\n\x14TemporaryExposureKey\x12\x10\n\x08key_data\x18\x01 \x01(\x0c\x12\x1f\n\x17transmission_risk_level\x18\x02 \x01(\x05\x12%\n\x1drolling_start_interval_number\x18\x03 \x01(\x05\x12\x1b\n\x0erolling_period\x18\x04 \x01(\x05:\x03\x31\x34\x34\x12R\n\x0breport_type\x18\x05 \x01(\x0e\x32-.SAP.external.exposurenotification.ReportType:\x0e\x43ONFIRMED_TEST\x12$\n\x1c\x64\x61ys_since_onset_of_symptoms\x18\x06 \x01(\x11'
  ,
  dependencies=[external_dot_exposurenotification_dot_diagnosis__key__batch__pb2.DESCRIPTOR,])




_TEMPORARYEXPOSUREKEYEXPORT = _descriptor.Descriptor(
  name='TemporaryExposureKeyExport',
  full_name='SAP.external.exposurenotification.TemporaryExposureKeyExport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='SAP.external.exposurenotification.TemporaryExposureKeyExport.start_timestamp', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='SAP.external.exposurenotification.TemporaryExposureKeyExport.end_timestamp', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region', full_name='SAP.external.exposurenotification.TemporaryExposureKeyExport.region', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_num', full_name='SAP.external.exposurenotification.TemporaryExposureKeyExport.batch_num', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='SAP.external.exposurenotification.TemporaryExposureKeyExport.batch_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature_infos', full_name='SAP.external.exposurenotification.TemporaryExposureKeyExport.signature_infos', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keys', full_name='SAP.external.exposurenotification.TemporaryExposureKeyExport.keys', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revised_keys', full_name='SAP.external.exposurenotification.TemporaryExposureKeyExport.revised_keys', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=518,
)


_SIGNATUREINFO = _descriptor.Descriptor(
  name='SignatureInfo',
  full_name='SAP.external.exposurenotification.SignatureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_bundle_id', full_name='SAP.external.exposurenotification.SignatureInfo.app_bundle_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='android_package', full_name='SAP.external.exposurenotification.SignatureInfo.android_package', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='verification_key_version', full_name='SAP.external.exposurenotification.SignatureInfo.verification_key_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='verification_key_id', full_name='SAP.external.exposurenotification.SignatureInfo.verification_key_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature_algorithm', full_name='SAP.external.exposurenotification.SignatureInfo.signature_algorithm', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=521,
  serialized_end=676,
)


_TEMPORARYEXPOSUREKEY = _descriptor.Descriptor(
  name='TemporaryExposureKey',
  full_name='SAP.external.exposurenotification.TemporaryExposureKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_data', full_name='SAP.external.exposurenotification.TemporaryExposureKey.key_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transmission_risk_level', full_name='SAP.external.exposurenotification.TemporaryExposureKey.transmission_risk_level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rolling_start_interval_number', full_name='SAP.external.exposurenotification.TemporaryExposureKey.rolling_start_interval_number', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rolling_period', full_name='SAP.external.exposurenotification.TemporaryExposureKey.rolling_period', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=144,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='report_type', full_name='SAP.external.exposurenotification.TemporaryExposureKey.report_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='days_since_onset_of_symptoms', full_name='SAP.external.exposurenotification.TemporaryExposureKey.days_since_onset_of_symptoms', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=679,
  serialized_end=942,
)

_TEMPORARYEXPOSUREKEYEXPORT.fields_by_name['signature_infos'].message_type = _SIGNATUREINFO
_TEMPORARYEXPOSUREKEYEXPORT.fields_by_name['keys'].message_type = _TEMPORARYEXPOSUREKEY
_TEMPORARYEXPOSUREKEYEXPORT.fields_by_name['revised_keys'].message_type = _TEMPORARYEXPOSUREKEY
_TEMPORARYEXPOSUREKEY.fields_by_name['report_type'].enum_type = external_dot_exposurenotification_dot_diagnosis__key__batch__pb2._REPORTTYPE
DESCRIPTOR.message_types_by_name['TemporaryExposureKeyExport'] = _TEMPORARYEXPOSUREKEYEXPORT
DESCRIPTOR.message_types_by_name['SignatureInfo'] = _SIGNATUREINFO
DESCRIPTOR.message_types_by_name['TemporaryExposureKey'] = _TEMPORARYEXPOSUREKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TemporaryExposureKeyExport = _reflection.GeneratedProtocolMessageType('TemporaryExposureKeyExport', (_message.Message,), {
  'DESCRIPTOR' : _TEMPORARYEXPOSUREKEYEXPORT,
  '__module__' : 'external.exposurenotification.temporary_exposure_key_export_pb2'
  # @@protoc_insertion_point(class_scope:SAP.external.exposurenotification.TemporaryExposureKeyExport)
  })
_sym_db.RegisterMessage(TemporaryExposureKeyExport)

SignatureInfo = _reflection.GeneratedProtocolMessageType('SignatureInfo', (_message.Message,), {
  'DESCRIPTOR' : _SIGNATUREINFO,
  '__module__' : 'external.exposurenotification.temporary_exposure_key_export_pb2'
  # @@protoc_insertion_point(class_scope:SAP.external.exposurenotification.SignatureInfo)
  })
_sym_db.RegisterMessage(SignatureInfo)

TemporaryExposureKey = _reflection.GeneratedProtocolMessageType('TemporaryExposureKey', (_message.Message,), {
  'DESCRIPTOR' : _TEMPORARYEXPOSUREKEY,
  '__module__' : 'external.exposurenotification.temporary_exposure_key_export_pb2'
  # @@protoc_insertion_point(class_scope:SAP.external.exposurenotification.TemporaryExposureKey)
  })
_sym_db.RegisterMessage(TemporaryExposureKey)


# @@protoc_insertion_point(module_scope)
