from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .........models import planner_progress_task_board_task_format
    from .........models.o_data_errors import o_data_error

class ProgressTaskBoardFormatRequestBuilder():
    """
    Provides operations to manage the progressTaskBoardFormat property of the microsoft.graph.plannerTask entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ProgressTaskBoardFormatRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/planner/plans/{plannerPlan%2Did}/buckets/{plannerBucket%2Did}/tasks/{plannerTask%2Did}/progressTaskBoardFormat{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ProgressTaskBoardFormatRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property progressTaskBoardFormat for planner
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ProgressTaskBoardFormatRequestBuilderGetRequestConfiguration] = None) -> Optional[planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat]:
        """
        Retrieve the properties and relationships of **plannerProgressTaskBoardTaskFormat** object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models import planner_progress_task_board_task_format

        return await self.request_adapter.send_async(request_info, planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat, error_mapping)
    
    async def patch(self,body: Optional[planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat] = None, request_configuration: Optional[ProgressTaskBoardFormatRequestBuilderPatchRequestConfiguration] = None) -> Optional[planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat]:
        """
        Update the navigation property progressTaskBoardFormat in planner
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models import planner_progress_task_board_task_format

        return await self.request_adapter.send_async(request_info, planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ProgressTaskBoardFormatRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property progressTaskBoardFormat for planner
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
    
    def to_get_request_information(self,request_configuration: Optional[ProgressTaskBoardFormatRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of **plannerProgressTaskBoardTaskFormat** object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat] = None, request_configuration: Optional[ProgressTaskBoardFormatRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property progressTaskBoardFormat in planner
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class ProgressTaskBoardFormatRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ProgressTaskBoardFormatRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of **plannerProgressTaskBoardTaskFormat** object.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
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

    
    @dataclass
    class ProgressTaskBoardFormatRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ProgressTaskBoardFormatRequestBuilder.ProgressTaskBoardFormatRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ProgressTaskBoardFormatRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

