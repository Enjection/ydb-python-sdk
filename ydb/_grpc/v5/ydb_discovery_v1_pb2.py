# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ydb_discovery_v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.v5.protos import ydb_discovery_pb2 as protos_dot_ydb__discovery__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16ydb_discovery_v1.proto\x12\x10Ydb.Discovery.V1\x1a\x1aprotos/ydb_discovery.proto2\xb5\x01\n\x10\x44iscoveryService\x12Z\n\rListEndpoints\x12#.Ydb.Discovery.ListEndpointsRequest\x1a$.Ydb.Discovery.ListEndpointsResponse\x12\x45\n\x06WhoAmI\x12\x1c.Ydb.Discovery.WhoAmIRequest\x1a\x1d.Ydb.Discovery.WhoAmIResponseBW\n\x1btech.ydb.proto.discovery.v1Z8github.com/ydb-platform/ydb-go-genproto/Ydb_Discovery_V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ydb_discovery_v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033tech.ydb.proto.discovery.v1Z8github.com/ydb-platform/ydb-go-genproto/Ydb_Discovery_V1'
  _DISCOVERYSERVICE._serialized_start=73
  _DISCOVERYSERVICE._serialized_end=254
# @@protoc_insertion_point(module_scope)
