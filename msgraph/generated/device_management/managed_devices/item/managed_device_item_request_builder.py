from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.managed_device import ManagedDevice
    from ....models.o_data_errors.o_data_error import ODataError
    from .bypass_activation_lock.bypass_activation_lock_request_builder import BypassActivationLockRequestBuilder
    from .clean_windows_device.clean_windows_device_request_builder import CleanWindowsDeviceRequestBuilder
    from .delete_user_from_shared_apple_device.delete_user_from_shared_apple_device_request_builder import DeleteUserFromSharedAppleDeviceRequestBuilder
    from .device_category.device_category_request_builder import DeviceCategoryRequestBuilder
    from .device_compliance_policy_states.device_compliance_policy_states_request_builder import DeviceCompliancePolicyStatesRequestBuilder
    from .device_configuration_states.device_configuration_states_request_builder import DeviceConfigurationStatesRequestBuilder
    from .disable_lost_mode.disable_lost_mode_request_builder import DisableLostModeRequestBuilder
    from .locate_device.locate_device_request_builder import LocateDeviceRequestBuilder
    from .logout_shared_apple_device_active_user.logout_shared_apple_device_active_user_request_builder import LogoutSharedAppleDeviceActiveUserRequestBuilder
    from .log_collection_requests.log_collection_requests_request_builder import LogCollectionRequestsRequestBuilder
    from .reboot_now.reboot_now_request_builder import RebootNowRequestBuilder
    from .recover_passcode.recover_passcode_request_builder import RecoverPasscodeRequestBuilder
    from .remote_lock.remote_lock_request_builder import RemoteLockRequestBuilder
    from .request_remote_assistance.request_remote_assistance_request_builder import RequestRemoteAssistanceRequestBuilder
    from .reset_passcode.reset_passcode_request_builder import ResetPasscodeRequestBuilder
    from .retire.retire_request_builder import RetireRequestBuilder
    from .shut_down.shut_down_request_builder import ShutDownRequestBuilder
    from .sync_device.sync_device_request_builder import SyncDeviceRequestBuilder
    from .update_windows_device_account.update_windows_device_account_request_builder import UpdateWindowsDeviceAccountRequestBuilder
    from .users.users_request_builder import UsersRequestBuilder
    from .windows_defender_scan.windows_defender_scan_request_builder import WindowsDefenderScanRequestBuilder
    from .windows_defender_update_signatures.windows_defender_update_signatures_request_builder import WindowsDefenderUpdateSignaturesRequestBuilder
    from .windows_protection_state.windows_protection_state_request_builder import WindowsProtectionStateRequestBuilder
    from .wipe.wipe_request_builder import WipeRequestBuilder

class ManagedDeviceItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the managedDevices property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ManagedDeviceItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/managedDevices/{managedDevice%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Deletes a managedDevice.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/intune-devices-manageddevice-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderGetRequestConfiguration] = None) -> Optional[ManagedDevice]:
        """
        Read properties and relationships of the managedDevice object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagedDevice]
        Find more info here: https://learn.microsoft.com/graph/api/intune-devices-manageddevice-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.managed_device import ManagedDevice

        return await self.request_adapter.send_async(request_info, ManagedDevice, error_mapping)
    
    async def patch(self,body: Optional[ManagedDevice] = None, request_configuration: Optional[ManagedDeviceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[ManagedDevice]:
        """
        Update the properties of a managedDevice object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagedDevice]
        Find more info here: https://learn.microsoft.com/graph/api/intune-devices-manageddevice-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.managed_device import ManagedDevice

        return await self.request_adapter.send_async(request_info, ManagedDevice, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Deletes a managedDevice.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read properties and relationships of the managedDevice object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[ManagedDevice] = None, request_configuration: Optional[ManagedDeviceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a managedDevice object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ManagedDeviceItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ManagedDeviceItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ManagedDeviceItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bypass_activation_lock(self) -> BypassActivationLockRequestBuilder:
        """
        Provides operations to call the bypassActivationLock method.
        """
        from .bypass_activation_lock.bypass_activation_lock_request_builder import BypassActivationLockRequestBuilder

        return BypassActivationLockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clean_windows_device(self) -> CleanWindowsDeviceRequestBuilder:
        """
        Provides operations to call the cleanWindowsDevice method.
        """
        from .clean_windows_device.clean_windows_device_request_builder import CleanWindowsDeviceRequestBuilder

        return CleanWindowsDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delete_user_from_shared_apple_device(self) -> DeleteUserFromSharedAppleDeviceRequestBuilder:
        """
        Provides operations to call the deleteUserFromSharedAppleDevice method.
        """
        from .delete_user_from_shared_apple_device.delete_user_from_shared_apple_device_request_builder import DeleteUserFromSharedAppleDeviceRequestBuilder

        return DeleteUserFromSharedAppleDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_category(self) -> DeviceCategoryRequestBuilder:
        """
        Provides operations to manage the deviceCategory property of the microsoft.graph.managedDevice entity.
        """
        from .device_category.device_category_request_builder import DeviceCategoryRequestBuilder

        return DeviceCategoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_states(self) -> DeviceCompliancePolicyStatesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicyStates property of the microsoft.graph.managedDevice entity.
        """
        from .device_compliance_policy_states.device_compliance_policy_states_request_builder import DeviceCompliancePolicyStatesRequestBuilder

        return DeviceCompliancePolicyStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_states(self) -> DeviceConfigurationStatesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationStates property of the microsoft.graph.managedDevice entity.
        """
        from .device_configuration_states.device_configuration_states_request_builder import DeviceConfigurationStatesRequestBuilder

        return DeviceConfigurationStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def disable_lost_mode(self) -> DisableLostModeRequestBuilder:
        """
        Provides operations to call the disableLostMode method.
        """
        from .disable_lost_mode.disable_lost_mode_request_builder import DisableLostModeRequestBuilder

        return DisableLostModeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def locate_device(self) -> LocateDeviceRequestBuilder:
        """
        Provides operations to call the locateDevice method.
        """
        from .locate_device.locate_device_request_builder import LocateDeviceRequestBuilder

        return LocateDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log_collection_requests(self) -> LogCollectionRequestsRequestBuilder:
        """
        Provides operations to manage the logCollectionRequests property of the microsoft.graph.managedDevice entity.
        """
        from .log_collection_requests.log_collection_requests_request_builder import LogCollectionRequestsRequestBuilder

        return LogCollectionRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logout_shared_apple_device_active_user(self) -> LogoutSharedAppleDeviceActiveUserRequestBuilder:
        """
        Provides operations to call the logoutSharedAppleDeviceActiveUser method.
        """
        from .logout_shared_apple_device_active_user.logout_shared_apple_device_active_user_request_builder import LogoutSharedAppleDeviceActiveUserRequestBuilder

        return LogoutSharedAppleDeviceActiveUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reboot_now(self) -> RebootNowRequestBuilder:
        """
        Provides operations to call the rebootNow method.
        """
        from .reboot_now.reboot_now_request_builder import RebootNowRequestBuilder

        return RebootNowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recover_passcode(self) -> RecoverPasscodeRequestBuilder:
        """
        Provides operations to call the recoverPasscode method.
        """
        from .recover_passcode.recover_passcode_request_builder import RecoverPasscodeRequestBuilder

        return RecoverPasscodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_lock(self) -> RemoteLockRequestBuilder:
        """
        Provides operations to call the remoteLock method.
        """
        from .remote_lock.remote_lock_request_builder import RemoteLockRequestBuilder

        return RemoteLockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def request_remote_assistance(self) -> RequestRemoteAssistanceRequestBuilder:
        """
        Provides operations to call the requestRemoteAssistance method.
        """
        from .request_remote_assistance.request_remote_assistance_request_builder import RequestRemoteAssistanceRequestBuilder

        return RequestRemoteAssistanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_passcode(self) -> ResetPasscodeRequestBuilder:
        """
        Provides operations to call the resetPasscode method.
        """
        from .reset_passcode.reset_passcode_request_builder import ResetPasscodeRequestBuilder

        return ResetPasscodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retire(self) -> RetireRequestBuilder:
        """
        Provides operations to call the retire method.
        """
        from .retire.retire_request_builder import RetireRequestBuilder

        return RetireRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shut_down(self) -> ShutDownRequestBuilder:
        """
        Provides operations to call the shutDown method.
        """
        from .shut_down.shut_down_request_builder import ShutDownRequestBuilder

        return ShutDownRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sync_device(self) -> SyncDeviceRequestBuilder:
        """
        Provides operations to call the syncDevice method.
        """
        from .sync_device.sync_device_request_builder import SyncDeviceRequestBuilder

        return SyncDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_windows_device_account(self) -> UpdateWindowsDeviceAccountRequestBuilder:
        """
        Provides operations to call the updateWindowsDeviceAccount method.
        """
        from .update_windows_device_account.update_windows_device_account_request_builder import UpdateWindowsDeviceAccountRequestBuilder

        return UpdateWindowsDeviceAccountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> UsersRequestBuilder:
        """
        Provides operations to manage the users property of the microsoft.graph.managedDevice entity.
        """
        from .users.users_request_builder import UsersRequestBuilder

        return UsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_defender_scan(self) -> WindowsDefenderScanRequestBuilder:
        """
        Provides operations to call the windowsDefenderScan method.
        """
        from .windows_defender_scan.windows_defender_scan_request_builder import WindowsDefenderScanRequestBuilder

        return WindowsDefenderScanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_defender_update_signatures(self) -> WindowsDefenderUpdateSignaturesRequestBuilder:
        """
        Provides operations to call the windowsDefenderUpdateSignatures method.
        """
        from .windows_defender_update_signatures.windows_defender_update_signatures_request_builder import WindowsDefenderUpdateSignaturesRequestBuilder

        return WindowsDefenderUpdateSignaturesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_protection_state(self) -> WindowsProtectionStateRequestBuilder:
        """
        Provides operations to manage the windowsProtectionState property of the microsoft.graph.managedDevice entity.
        """
        from .windows_protection_state.windows_protection_state_request_builder import WindowsProtectionStateRequestBuilder

        return WindowsProtectionStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wipe(self) -> WipeRequestBuilder:
        """
        Provides operations to call the wipe method.
        """
        from .wipe.wipe_request_builder import WipeRequestBuilder

        return WipeRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ManagedDeviceItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class ManagedDeviceItemRequestBuilderGetQueryParameters():
        """
        Read properties and relationships of the managedDevice object.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ManagedDeviceItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[ManagedDeviceItemRequestBuilder.ManagedDeviceItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ManagedDeviceItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

