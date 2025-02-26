# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: draft/protos/ydb_maintenance.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.v5.protos.annotations import validation_pb2 as protos_dot_annotations_dot_validation__pb2
from ydb._grpc.v5.protos import ydb_status_codes_pb2 as protos_dot_ydb__status__codes__pb2
from ydb._grpc.v5.protos import ydb_discovery_pb2 as protos_dot_ydb__discovery__pb2
from ydb._grpc.v5.protos import ydb_operation_pb2 as protos_dot_ydb__operation__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"draft/protos/ydb_maintenance.proto\x12\x0fYdb.Maintenance\x1a#protos/annotations/validation.proto\x1a\x1dprotos/ydb_status_codes.proto\x1a\x1aprotos/ydb_discovery.proto\x1a\x1aprotos/ydb_operation.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf0\x02\n\x04Node\x12\x0f\n\x07node_id\x18\x01 \x01(\r\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\r\x12-\n\x08location\x18\x04 \x01(\x0b\x32\x1b.Ydb.Discovery.NodeLocation\x12)\n\x05state\x18\x05 \x01(\x0e\x32\x1a.Ydb.Maintenance.ItemState\x12\x34\n\x07storage\x18\x06 \x01(\x0b\x32!.Ydb.Maintenance.Node.StorageNodeH\x00\x12\x34\n\x07\x64ynamic\x18\x07 \x01(\x0b\x32!.Ydb.Maintenance.Node.DynamicNodeH\x00\x12.\n\nstart_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07version\x18\t \x01(\t\x1a\r\n\x0bStorageNode\x1a\x1d\n\x0b\x44ynamicNode\x12\x0e\n\x06tenant\x18\x01 \x01(\tB\x06\n\x04type\"T\n\x17ListClusterNodesRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\">\n\x16ListClusterNodesResult\x12$\n\x05nodes\x18\x01 \x03(\x0b\x32\x15.Ydb.Maintenance.Node\"H\n\x18ListClusterNodesResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\xc3\x01\n\x16MaintenanceTaskOptions\x12\x19\n\x08task_uid\x18\x01 \x01(\tB\x07\xa2\xe6*\x03\x18\x80\x01\x12\x1c\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x07\xa2\xe6*\x03\x18\x80\x01\x12<\n\x11\x61vailability_mode\x18\x03 \x01(\x0e\x32!.Ydb.Maintenance.AvailabilityMode\x12\x0f\n\x07\x64ry_run\x18\x04 \x01(\x08\x12!\n\x08priority\x18\x05 \x01(\x05\x42\x0f\xb2\xe6*\x0b[-100; 100]\"B\n\x0b\x41\x63tionScope\x12\x11\n\x07node_id\x18\x01 \x01(\rH\x00\x12\x17\n\x04host\x18\x02 \x01(\tB\x07\xa2\xe6*\x03\x18\xff\x01H\x00\x42\x07\n\x05scope\"f\n\nLockAction\x12+\n\x05scope\x18\x01 \x01(\x0b\x32\x1c.Ydb.Maintenance.ActionScope\x12+\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"F\n\x06\x41\x63tion\x12\x32\n\x0block_action\x18\x01 \x01(\x0b\x32\x1b.Ydb.Maintenance.LockActionH\x00\x42\x08\n\x06\x61\x63tion\"?\n\x0b\x41\x63tionGroup\x12\x30\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32\x17.Ydb.Maintenance.ActionB\x06\x9a\xe6*\x02(\x01\"\xd5\x01\n\x1c\x43reateMaintenanceTaskRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12=\n\x0ctask_options\x18\x02 \x01(\x0b\x32\'.Ydb.Maintenance.MaintenanceTaskOptions\x12;\n\raction_groups\x18\x03 \x03(\x0b\x32\x1c.Ydb.Maintenance.ActionGroupB\x06\x9a\xe6*\x02(\x01\"u\n\x1dRefreshMaintenanceTaskRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x19\n\x08task_uid\x18\x02 \x01(\tB\x07\xa2\xe6*\x03\x18\x80\x01\"]\n\tActionUid\x12\x19\n\x08task_uid\x18\x01 \x01(\tB\x07\xa2\xe6*\x03\x18\x80\x01\x12\x19\n\x08group_id\x18\x02 \x01(\tB\x07\xa2\xe6*\x03\x18\x80\x01\x12\x1a\n\taction_id\x18\x03 \x01(\tB\x07\xa2\xe6*\x03\x18\x80\x01\"\x8f\x06\n\x0b\x41\x63tionState\x12\'\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32\x17.Ydb.Maintenance.Action\x12.\n\naction_uid\x18\x02 \x01(\x0b\x32\x1a.Ydb.Maintenance.ActionUid\x12\x39\n\x06status\x18\x03 \x01(\x0e\x32).Ydb.Maintenance.ActionState.ActionStatus\x12\x39\n\x06reason\x18\x04 \x01(\x0e\x32).Ydb.Maintenance.ActionState.ActionReason\x12\x16\n\x0ereason_details\x18\x06 \x01(\t\x12,\n\x08\x64\x65\x61\x64line\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"e\n\x0c\x41\x63tionStatus\x12\x1d\n\x19\x41\x43TION_STATUS_UNSPECIFIED\x10\x00\x12\x19\n\x15\x41\x43TION_STATUS_PENDING\x10\x01\x12\x1b\n\x17\x41\x43TION_STATUS_PERFORMED\x10\x02\"\x83\x03\n\x0c\x41\x63tionReason\x12\x1d\n\x19\x41\x43TION_REASON_UNSPECIFIED\x10\x00\x12\x14\n\x10\x41\x43TION_REASON_OK\x10\x01\x12-\n)ACTION_REASON_TOO_MANY_UNAVAILABLE_VDISKS\x10\x02\x12:\n6ACTION_REASON_TOO_MANY_UNAVAILABLE_STATE_STORAGE_RINGS\x10\x03\x12.\n*ACTION_REASON_DISABLED_NODES_LIMIT_REACHED\x10\x04\x12\x35\n1ACTION_REASON_TENANT_DISABLED_NODES_LIMIT_REACHED\x10\x05\x12\x1f\n\x1b\x41\x43TION_REASON_WRONG_REQUEST\x10\x06\x12\x30\n,ACTION_REASON_SYS_TABLETS_NODE_LIMIT_REACHED\x10\x07\x12\x19\n\x15\x41\x43TION_REASON_GENERIC\x10\x08\"H\n\x11\x41\x63tionGroupStates\x12\x33\n\raction_states\x18\x01 \x03(\x0b\x32\x1c.Ydb.Maintenance.ActionState\"\xb0\x01\n\x15MaintenanceTaskResult\x12\x10\n\x08task_uid\x18\x01 \x01(\t\x12?\n\x13\x61\x63tion_group_states\x18\x02 \x03(\x0b\x32\".Ydb.Maintenance.ActionGroupStates\x12\x34\n\x0bretry_after\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x42\x0e\n\x0c_retry_after\"G\n\x17MaintenanceTaskResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"q\n\x19GetMaintenanceTaskRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x19\n\x08task_uid\x18\x02 \x01(\tB\x07\xa2\xe6*\x03\x18\x80\x01\"\x9a\x01\n\x18GetMaintenanceTaskResult\x12=\n\x0ctask_options\x18\x01 \x01(\x0b\x32\'.Ydb.Maintenance.MaintenanceTaskOptions\x12?\n\x13\x61\x63tion_group_states\x18\x02 \x03(\x0b\x32\".Ydb.Maintenance.ActionGroupStates\"J\n\x1aGetMaintenanceTaskResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"t\n\x1bListMaintenanceTasksRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x11\n\x04user\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_user\"0\n\x1aListMaintenanceTasksResult\x12\x12\n\ntasks_uids\x18\x01 \x03(\t\"L\n\x1cListMaintenanceTasksResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"r\n\x1a\x44ropMaintenanceTaskRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x19\n\x08task_uid\x18\x02 \x01(\tB\x07\xa2\xe6*\x03\x18\x80\x01\"M\n\x1dManageMaintenanceTaskResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\x8b\x01\n\x15\x43ompleteActionRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x37\n\x0b\x61\x63tion_uids\x18\x02 \x03(\x0b\x32\x1a.Ydb.Maintenance.ActionUidB\x06\x9a\xe6*\x02(\x01\"\xbe\x01\n\x12ManageActionResult\x12\x43\n\x0f\x61\x63tion_statuses\x18\x01 \x03(\x0b\x32*.Ydb.Maintenance.ManageActionResult.Status\x1a\x63\n\x06Status\x12.\n\naction_uid\x18\x01 \x01(\x0b\x32\x1a.Ydb.Maintenance.ActionUid\x12)\n\x06status\x18\x02 \x01(\x0e\x32\x19.Ydb.StatusIds.StatusCode\"D\n\x14ManageActionResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation*k\n\tItemState\x12\x1a\n\x16ITEM_STATE_UNSPECIFIED\x10\x00\x12\x11\n\rITEM_STATE_UP\x10\x01\x12\x1a\n\x16ITEM_STATE_MAINTENANCE\x10\x02\x12\x13\n\x0fITEM_STATE_DOWN\x10\x03*\x8c\x01\n\x10\x41vailabilityMode\x12!\n\x1d\x41VAILABILITY_MODE_UNSPECIFIED\x10\x00\x12\x1c\n\x18\x41VAILABILITY_MODE_STRONG\x10\x01\x12\x1a\n\x16\x41VAILABILITY_MODE_WEAK\x10\x02\x12\x1b\n\x17\x41VAILABILITY_MODE_FORCE\x10\x03\x42n\n#tech.ydb.proto.draft.maintenance.v1ZDgithub.com/ydb-platform/ydb-go-genproto/draft/protos/Ydb_Maintenance\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'draft.protos.ydb_maintenance_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#tech.ydb.proto.draft.maintenance.v1ZDgithub.com/ydb-platform/ydb-go-genproto/draft/protos/Ydb_Maintenance\370\001\001'
  _MAINTENANCETASKOPTIONS.fields_by_name['task_uid']._options = None
  _MAINTENANCETASKOPTIONS.fields_by_name['task_uid']._serialized_options = b'\242\346*\003\030\200\001'
  _MAINTENANCETASKOPTIONS.fields_by_name['description']._options = None
  _MAINTENANCETASKOPTIONS.fields_by_name['description']._serialized_options = b'\242\346*\003\030\200\001'
  _MAINTENANCETASKOPTIONS.fields_by_name['priority']._options = None
  _MAINTENANCETASKOPTIONS.fields_by_name['priority']._serialized_options = b'\262\346*\013[-100; 100]'
  _ACTIONSCOPE.fields_by_name['host']._options = None
  _ACTIONSCOPE.fields_by_name['host']._serialized_options = b'\242\346*\003\030\377\001'
  _ACTIONGROUP.fields_by_name['actions']._options = None
  _ACTIONGROUP.fields_by_name['actions']._serialized_options = b'\232\346*\002(\001'
  _CREATEMAINTENANCETASKREQUEST.fields_by_name['action_groups']._options = None
  _CREATEMAINTENANCETASKREQUEST.fields_by_name['action_groups']._serialized_options = b'\232\346*\002(\001'
  _REFRESHMAINTENANCETASKREQUEST.fields_by_name['task_uid']._options = None
  _REFRESHMAINTENANCETASKREQUEST.fields_by_name['task_uid']._serialized_options = b'\242\346*\003\030\200\001'
  _ACTIONUID.fields_by_name['task_uid']._options = None
  _ACTIONUID.fields_by_name['task_uid']._serialized_options = b'\242\346*\003\030\200\001'
  _ACTIONUID.fields_by_name['group_id']._options = None
  _ACTIONUID.fields_by_name['group_id']._serialized_options = b'\242\346*\003\030\200\001'
  _ACTIONUID.fields_by_name['action_id']._options = None
  _ACTIONUID.fields_by_name['action_id']._serialized_options = b'\242\346*\003\030\200\001'
  _GETMAINTENANCETASKREQUEST.fields_by_name['task_uid']._options = None
  _GETMAINTENANCETASKREQUEST.fields_by_name['task_uid']._serialized_options = b'\242\346*\003\030\200\001'
  _DROPMAINTENANCETASKREQUEST.fields_by_name['task_uid']._options = None
  _DROPMAINTENANCETASKREQUEST.fields_by_name['task_uid']._serialized_options = b'\242\346*\003\030\200\001'
  _COMPLETEACTIONREQUEST.fields_by_name['action_uids']._options = None
  _COMPLETEACTIONREQUEST.fields_by_name['action_uids']._serialized_options = b'\232\346*\002(\001'
  _ITEMSTATE._serialized_start=4082
  _ITEMSTATE._serialized_end=4189
  _AVAILABILITYMODE._serialized_start=4192
  _AVAILABILITYMODE._serialized_end=4332
  _NODE._serialized_start=245
  _NODE._serialized_end=613
  _NODE_STORAGENODE._serialized_start=561
  _NODE_STORAGENODE._serialized_end=574
  _NODE_DYNAMICNODE._serialized_start=576
  _NODE_DYNAMICNODE._serialized_end=605
  _LISTCLUSTERNODESREQUEST._serialized_start=615
  _LISTCLUSTERNODESREQUEST._serialized_end=699
  _LISTCLUSTERNODESRESULT._serialized_start=701
  _LISTCLUSTERNODESRESULT._serialized_end=763
  _LISTCLUSTERNODESRESPONSE._serialized_start=765
  _LISTCLUSTERNODESRESPONSE._serialized_end=837
  _MAINTENANCETASKOPTIONS._serialized_start=840
  _MAINTENANCETASKOPTIONS._serialized_end=1035
  _ACTIONSCOPE._serialized_start=1037
  _ACTIONSCOPE._serialized_end=1103
  _LOCKACTION._serialized_start=1105
  _LOCKACTION._serialized_end=1207
  _ACTION._serialized_start=1209
  _ACTION._serialized_end=1279
  _ACTIONGROUP._serialized_start=1281
  _ACTIONGROUP._serialized_end=1344
  _CREATEMAINTENANCETASKREQUEST._serialized_start=1347
  _CREATEMAINTENANCETASKREQUEST._serialized_end=1560
  _REFRESHMAINTENANCETASKREQUEST._serialized_start=1562
  _REFRESHMAINTENANCETASKREQUEST._serialized_end=1679
  _ACTIONUID._serialized_start=1681
  _ACTIONUID._serialized_end=1774
  _ACTIONSTATE._serialized_start=1777
  _ACTIONSTATE._serialized_end=2560
  _ACTIONSTATE_ACTIONSTATUS._serialized_start=2069
  _ACTIONSTATE_ACTIONSTATUS._serialized_end=2170
  _ACTIONSTATE_ACTIONREASON._serialized_start=2173
  _ACTIONSTATE_ACTIONREASON._serialized_end=2560
  _ACTIONGROUPSTATES._serialized_start=2562
  _ACTIONGROUPSTATES._serialized_end=2634
  _MAINTENANCETASKRESULT._serialized_start=2637
  _MAINTENANCETASKRESULT._serialized_end=2813
  _MAINTENANCETASKRESPONSE._serialized_start=2815
  _MAINTENANCETASKRESPONSE._serialized_end=2886
  _GETMAINTENANCETASKREQUEST._serialized_start=2888
  _GETMAINTENANCETASKREQUEST._serialized_end=3001
  _GETMAINTENANCETASKRESULT._serialized_start=3004
  _GETMAINTENANCETASKRESULT._serialized_end=3158
  _GETMAINTENANCETASKRESPONSE._serialized_start=3160
  _GETMAINTENANCETASKRESPONSE._serialized_end=3234
  _LISTMAINTENANCETASKSREQUEST._serialized_start=3236
  _LISTMAINTENANCETASKSREQUEST._serialized_end=3352
  _LISTMAINTENANCETASKSRESULT._serialized_start=3354
  _LISTMAINTENANCETASKSRESULT._serialized_end=3402
  _LISTMAINTENANCETASKSRESPONSE._serialized_start=3404
  _LISTMAINTENANCETASKSRESPONSE._serialized_end=3480
  _DROPMAINTENANCETASKREQUEST._serialized_start=3482
  _DROPMAINTENANCETASKREQUEST._serialized_end=3596
  _MANAGEMAINTENANCETASKRESPONSE._serialized_start=3598
  _MANAGEMAINTENANCETASKRESPONSE._serialized_end=3675
  _COMPLETEACTIONREQUEST._serialized_start=3678
  _COMPLETEACTIONREQUEST._serialized_end=3817
  _MANAGEACTIONRESULT._serialized_start=3820
  _MANAGEACTIONRESULT._serialized_end=4010
  _MANAGEACTIONRESULT_STATUS._serialized_start=3911
  _MANAGEACTIONRESULT_STATUS._serialized_end=4010
  _MANAGEACTIONRESPONSE._serialized_start=4012
  _MANAGEACTIONRESPONSE._serialized_end=4080
# @@protoc_insertion_point(module_scope)
