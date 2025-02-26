# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/ydb_discovery.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.v5.protos import ydb_operation_pb2 as protos_dot_ydb__operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aprotos/ydb_discovery.proto\x12\rYdb.Discovery\x1a\x1aprotos/ydb_operation.proto\"9\n\x14ListEndpointsRequest\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x03(\t\"\xc3\x01\n\x0c\x45ndpointInfo\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x13\n\x0bload_factor\x18\x03 \x01(\x02\x12\x0b\n\x03ssl\x18\x04 \x01(\x08\x12\x0f\n\x07service\x18\x05 \x03(\t\x12\x10\n\x08location\x18\x06 \x01(\t\x12\x0f\n\x07node_id\x18\x07 \x01(\r\x12\r\n\x05ip_v4\x18\x08 \x03(\t\x12\r\n\x05ip_v6\x18\t \x03(\t\x12 \n\x18ssl_target_name_override\x18\n \x01(\t\"\\\n\x13ListEndpointsResult\x12.\n\tendpoints\x18\x01 \x03(\x0b\x32\x1b.Ydb.Discovery.EndpointInfo\x12\x15\n\rself_location\x18\x02 \x01(\t\"E\n\x15ListEndpointsResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\'\n\rWhoAmIRequest\x12\x16\n\x0einclude_groups\x18\x01 \x01(\x08\",\n\x0cWhoAmIResult\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06groups\x18\x02 \x03(\t\">\n\x0eWhoAmIResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\xe0\x02\n\x0cNodeLocation\x12 \n\x0f\x64\x61ta_center_num\x18\x01 \x01(\rB\x02\x18\x01H\x00\x88\x01\x01\x12\x19\n\x08room_num\x18\x02 \x01(\rB\x02\x18\x01H\x01\x88\x01\x01\x12\x19\n\x08rack_num\x18\x03 \x01(\rB\x02\x18\x01H\x02\x88\x01\x01\x12\x19\n\x08\x62ody_num\x18\x04 \x01(\rB\x02\x18\x01H\x03\x88\x01\x01\x12\x17\n\x04\x62ody\x18\x94\x91\x06 \x01(\rB\x02\x18\x01H\x04\x88\x01\x01\x12\x18\n\x0b\x64\x61ta_center\x18\n \x01(\tH\x05\x88\x01\x01\x12\x13\n\x06module\x18\x14 \x01(\tH\x06\x88\x01\x01\x12\x11\n\x04rack\x18\x1e \x01(\tH\x07\x88\x01\x01\x12\x11\n\x04unit\x18( \x01(\tH\x08\x88\x01\x01\x42\x12\n\x10_data_center_numB\x0b\n\t_room_numB\x0b\n\t_rack_numB\x0b\n\t_body_numB\x07\n\x05_bodyB\x0e\n\x0c_data_centerB\t\n\x07_moduleB\x07\n\x05_rackB\x07\n\x05_unitBl\n\x18tech.ydb.proto.discoveryB\x0f\x44iscoveryProtosZ<github.com/ydb-platform/ydb-go-genproto/protos/Ydb_Discovery\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.ydb_discovery_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030tech.ydb.proto.discoveryB\017DiscoveryProtosZ<github.com/ydb-platform/ydb-go-genproto/protos/Ydb_Discovery\370\001\001'
  _NODELOCATION.fields_by_name['data_center_num']._options = None
  _NODELOCATION.fields_by_name['data_center_num']._serialized_options = b'\030\001'
  _NODELOCATION.fields_by_name['room_num']._options = None
  _NODELOCATION.fields_by_name['room_num']._serialized_options = b'\030\001'
  _NODELOCATION.fields_by_name['rack_num']._options = None
  _NODELOCATION.fields_by_name['rack_num']._serialized_options = b'\030\001'
  _NODELOCATION.fields_by_name['body_num']._options = None
  _NODELOCATION.fields_by_name['body_num']._serialized_options = b'\030\001'
  _NODELOCATION.fields_by_name['body']._options = None
  _NODELOCATION.fields_by_name['body']._serialized_options = b'\030\001'
  _LISTENDPOINTSREQUEST._serialized_start=73
  _LISTENDPOINTSREQUEST._serialized_end=130
  _ENDPOINTINFO._serialized_start=133
  _ENDPOINTINFO._serialized_end=328
  _LISTENDPOINTSRESULT._serialized_start=330
  _LISTENDPOINTSRESULT._serialized_end=422
  _LISTENDPOINTSRESPONSE._serialized_start=424
  _LISTENDPOINTSRESPONSE._serialized_end=493
  _WHOAMIREQUEST._serialized_start=495
  _WHOAMIREQUEST._serialized_end=534
  _WHOAMIRESULT._serialized_start=536
  _WHOAMIRESULT._serialized_end=580
  _WHOAMIRESPONSE._serialized_start=582
  _WHOAMIRESPONSE._serialized_end=644
  _NODELOCATION._serialized_start=647
  _NODELOCATION._serialized_end=999
# @@protoc_insertion_point(module_scope)
