from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, Union

from ....models import unified_role_management_policy
from ....models.o_data_errors import o_data_error
from .effective_rules import effective_rules_request_builder
from .effective_rules.item import unified_role_management_policy_rule_item_request_builder
from .rules import rules_request_builder
from .rules.item import unified_role_management_policy_rule_item_request_builder

class UnifiedRoleManagementPolicyItemRequestBuilder():
    """
    Provides operations to manage the roleManagementPolicies property of the microsoft.graph.policyRoot entity.
    """
    def effective_rules(self) -> effective_rules_request_builder.EffectiveRulesRequestBuilder:
        """
        Provides operations to manage the effectiveRules property of the microsoft.graph.unifiedRoleManagementPolicy entity.
        """
        return effective_rules_request_builder.EffectiveRulesRequestBuilder(self.request_adapter, self.path_parameters)

    def rules(self) -> rules_request_builder.RulesRequestBuilder:
        """
        Provides operations to manage the rules property of the microsoft.graph.unifiedRoleManagementPolicy entity.
        """
        return rules_request_builder.RulesRequestBuilder(self.request_adapter, self.path_parameters)

    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UnifiedRoleManagementPolicyItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise Exception("path_parameters cannot be undefined")
        if not request_adapter:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/policies/roleManagementPolicies/{unifiedRoleManagementPolicy%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter

    def create_delete_request_information(self,request_configuration: Optional[UnifiedRoleManagementPolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property roleManagementPolicies for policies
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info

    def create_get_request_information(self,request_configuration: Optional[UnifiedRoleManagementPolicyItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Specifies the various policies associated with scopes and roles.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info

    def create_patch_request_information(self,body: Optional[unified_role_management_policy.UnifiedRoleManagementPolicy] = None, request_configuration: Optional[UnifiedRoleManagementPolicyItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property roleManagementPolicies in policies
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info

    async def delete(self,request_configuration: Optional[UnifiedRoleManagementPolicyItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property roleManagementPolicies for policies
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)

    def effective_rules_by_id(self,id: str) -> unified_role_management_policy_rule_item_request_builder.UnifiedRoleManagementPolicyRuleItemRequestBuilder:
        """
        Provides operations to manage the effectiveRules property of the microsoft.graph.unifiedRoleManagementPolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_management_policy_rule_item_request_builder.UnifiedRoleManagementPolicyRuleItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleManagementPolicyRule%2Did"] = id
        return unified_role_management_policy_rule_item_request_builder.UnifiedRoleManagementPolicyRuleItemRequestBuilder(self.request_adapter, url_tpl_params)

    async def get(self,request_configuration: Optional[UnifiedRoleManagementPolicyItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[unified_role_management_policy.UnifiedRoleManagementPolicy]:
        """
        Specifies the various policies associated with scopes and roles.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[unified_role_management_policy.UnifiedRoleManagementPolicy]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, unified_role_management_policy.UnifiedRoleManagementPolicy, response_handler, error_mapping)

    async def patch(self,body: Optional[unified_role_management_policy.UnifiedRoleManagementPolicy] = None, request_configuration: Optional[UnifiedRoleManagementPolicyItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[unified_role_management_policy.UnifiedRoleManagementPolicy]:
        """
        Update the navigation property roleManagementPolicies in policies
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[unified_role_management_policy.UnifiedRoleManagementPolicy]
        """
        if not body:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, unified_role_management_policy.UnifiedRoleManagementPolicy, response_handler, error_mapping)

    def rules_by_id(self,id: str) -> unified_role_management_policy_rule_item_request_builder.UnifiedRoleManagementPolicyRuleItemRequestBuilder:
        """
        Provides operations to manage the rules property of the microsoft.graph.unifiedRoleManagementPolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_management_policy_rule_item_request_builder.UnifiedRoleManagementPolicyRuleItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleManagementPolicyRule%2Did"] = id
        return unified_role_management_policy_rule_item_request_builder.UnifiedRoleManagementPolicyRuleItemRequestBuilder(self.request_adapter, url_tpl_params)

    @dataclass
    class UnifiedRoleManagementPolicyItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UnifiedRoleManagementPolicyItemRequestBuilderGetQueryParameters():
        """
        Specifies the various policies associated with scopes and roles.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name

    
    @dataclass
    class UnifiedRoleManagementPolicyItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[UnifiedRoleManagementPolicyItemRequestBuilder.UnifiedRoleManagementPolicyItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class UnifiedRoleManagementPolicyItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
