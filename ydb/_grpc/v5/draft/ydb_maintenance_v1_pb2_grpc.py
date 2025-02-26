# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ydb._grpc.v5.draft.protos import ydb_maintenance_pb2 as draft_dot_protos_dot_ydb__maintenance__pb2


class MaintenanceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListClusterNodes = channel.unary_unary(
                '/Ydb.Maintenance.V1.MaintenanceService/ListClusterNodes',
                request_serializer=draft_dot_protos_dot_ydb__maintenance__pb2.ListClusterNodesRequest.SerializeToString,
                response_deserializer=draft_dot_protos_dot_ydb__maintenance__pb2.ListClusterNodesResponse.FromString,
                )
        self.CreateMaintenanceTask = channel.unary_unary(
                '/Ydb.Maintenance.V1.MaintenanceService/CreateMaintenanceTask',
                request_serializer=draft_dot_protos_dot_ydb__maintenance__pb2.CreateMaintenanceTaskRequest.SerializeToString,
                response_deserializer=draft_dot_protos_dot_ydb__maintenance__pb2.MaintenanceTaskResponse.FromString,
                )
        self.RefreshMaintenanceTask = channel.unary_unary(
                '/Ydb.Maintenance.V1.MaintenanceService/RefreshMaintenanceTask',
                request_serializer=draft_dot_protos_dot_ydb__maintenance__pb2.RefreshMaintenanceTaskRequest.SerializeToString,
                response_deserializer=draft_dot_protos_dot_ydb__maintenance__pb2.MaintenanceTaskResponse.FromString,
                )
        self.GetMaintenanceTask = channel.unary_unary(
                '/Ydb.Maintenance.V1.MaintenanceService/GetMaintenanceTask',
                request_serializer=draft_dot_protos_dot_ydb__maintenance__pb2.GetMaintenanceTaskRequest.SerializeToString,
                response_deserializer=draft_dot_protos_dot_ydb__maintenance__pb2.GetMaintenanceTaskResponse.FromString,
                )
        self.ListMaintenanceTasks = channel.unary_unary(
                '/Ydb.Maintenance.V1.MaintenanceService/ListMaintenanceTasks',
                request_serializer=draft_dot_protos_dot_ydb__maintenance__pb2.ListMaintenanceTasksRequest.SerializeToString,
                response_deserializer=draft_dot_protos_dot_ydb__maintenance__pb2.ListMaintenanceTasksResponse.FromString,
                )
        self.DropMaintenanceTask = channel.unary_unary(
                '/Ydb.Maintenance.V1.MaintenanceService/DropMaintenanceTask',
                request_serializer=draft_dot_protos_dot_ydb__maintenance__pb2.DropMaintenanceTaskRequest.SerializeToString,
                response_deserializer=draft_dot_protos_dot_ydb__maintenance__pb2.ManageMaintenanceTaskResponse.FromString,
                )
        self.CompleteAction = channel.unary_unary(
                '/Ydb.Maintenance.V1.MaintenanceService/CompleteAction',
                request_serializer=draft_dot_protos_dot_ydb__maintenance__pb2.CompleteActionRequest.SerializeToString,
                response_deserializer=draft_dot_protos_dot_ydb__maintenance__pb2.ManageActionResponse.FromString,
                )


class MaintenanceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListClusterNodes(self, request, context):
        """List cluster nodes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateMaintenanceTask(self, request, context):
        """Create maintenance task.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RefreshMaintenanceTask(self, request, context):
        """Try to perform maintenance task's actions (polling).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMaintenanceTask(self, request, context):
        """Get detailed task information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMaintenanceTasks(self, request, context):
        """List maintenance tasks.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DropMaintenanceTask(self, request, context):
        """Drop maintenance task.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteAction(self, request, context):
        """Mark action as completed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MaintenanceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListClusterNodes': grpc.unary_unary_rpc_method_handler(
                    servicer.ListClusterNodes,
                    request_deserializer=draft_dot_protos_dot_ydb__maintenance__pb2.ListClusterNodesRequest.FromString,
                    response_serializer=draft_dot_protos_dot_ydb__maintenance__pb2.ListClusterNodesResponse.SerializeToString,
            ),
            'CreateMaintenanceTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateMaintenanceTask,
                    request_deserializer=draft_dot_protos_dot_ydb__maintenance__pb2.CreateMaintenanceTaskRequest.FromString,
                    response_serializer=draft_dot_protos_dot_ydb__maintenance__pb2.MaintenanceTaskResponse.SerializeToString,
            ),
            'RefreshMaintenanceTask': grpc.unary_unary_rpc_method_handler(
                    servicer.RefreshMaintenanceTask,
                    request_deserializer=draft_dot_protos_dot_ydb__maintenance__pb2.RefreshMaintenanceTaskRequest.FromString,
                    response_serializer=draft_dot_protos_dot_ydb__maintenance__pb2.MaintenanceTaskResponse.SerializeToString,
            ),
            'GetMaintenanceTask': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMaintenanceTask,
                    request_deserializer=draft_dot_protos_dot_ydb__maintenance__pb2.GetMaintenanceTaskRequest.FromString,
                    response_serializer=draft_dot_protos_dot_ydb__maintenance__pb2.GetMaintenanceTaskResponse.SerializeToString,
            ),
            'ListMaintenanceTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.ListMaintenanceTasks,
                    request_deserializer=draft_dot_protos_dot_ydb__maintenance__pb2.ListMaintenanceTasksRequest.FromString,
                    response_serializer=draft_dot_protos_dot_ydb__maintenance__pb2.ListMaintenanceTasksResponse.SerializeToString,
            ),
            'DropMaintenanceTask': grpc.unary_unary_rpc_method_handler(
                    servicer.DropMaintenanceTask,
                    request_deserializer=draft_dot_protos_dot_ydb__maintenance__pb2.DropMaintenanceTaskRequest.FromString,
                    response_serializer=draft_dot_protos_dot_ydb__maintenance__pb2.ManageMaintenanceTaskResponse.SerializeToString,
            ),
            'CompleteAction': grpc.unary_unary_rpc_method_handler(
                    servicer.CompleteAction,
                    request_deserializer=draft_dot_protos_dot_ydb__maintenance__pb2.CompleteActionRequest.FromString,
                    response_serializer=draft_dot_protos_dot_ydb__maintenance__pb2.ManageActionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Ydb.Maintenance.V1.MaintenanceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MaintenanceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListClusterNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Maintenance.V1.MaintenanceService/ListClusterNodes',
            draft_dot_protos_dot_ydb__maintenance__pb2.ListClusterNodesRequest.SerializeToString,
            draft_dot_protos_dot_ydb__maintenance__pb2.ListClusterNodesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateMaintenanceTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Maintenance.V1.MaintenanceService/CreateMaintenanceTask',
            draft_dot_protos_dot_ydb__maintenance__pb2.CreateMaintenanceTaskRequest.SerializeToString,
            draft_dot_protos_dot_ydb__maintenance__pb2.MaintenanceTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RefreshMaintenanceTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Maintenance.V1.MaintenanceService/RefreshMaintenanceTask',
            draft_dot_protos_dot_ydb__maintenance__pb2.RefreshMaintenanceTaskRequest.SerializeToString,
            draft_dot_protos_dot_ydb__maintenance__pb2.MaintenanceTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMaintenanceTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Maintenance.V1.MaintenanceService/GetMaintenanceTask',
            draft_dot_protos_dot_ydb__maintenance__pb2.GetMaintenanceTaskRequest.SerializeToString,
            draft_dot_protos_dot_ydb__maintenance__pb2.GetMaintenanceTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMaintenanceTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Maintenance.V1.MaintenanceService/ListMaintenanceTasks',
            draft_dot_protos_dot_ydb__maintenance__pb2.ListMaintenanceTasksRequest.SerializeToString,
            draft_dot_protos_dot_ydb__maintenance__pb2.ListMaintenanceTasksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DropMaintenanceTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Maintenance.V1.MaintenanceService/DropMaintenanceTask',
            draft_dot_protos_dot_ydb__maintenance__pb2.DropMaintenanceTaskRequest.SerializeToString,
            draft_dot_protos_dot_ydb__maintenance__pb2.ManageMaintenanceTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CompleteAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Maintenance.V1.MaintenanceService/CompleteAction',
            draft_dot_protos_dot_ydb__maintenance__pb2.CompleteActionRequest.SerializeToString,
            draft_dot_protos_dot_ydb__maintenance__pb2.ManageActionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
