from __future__ import annotations
import datetime
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
    from ......models.identity_governance.task_report_collection_response import TaskReportCollectionResponse
    from ......models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.task_report_item_request_builder import TaskReportItemRequestBuilder
    from .microsoft_graph_identity_governance_summary_with_start_date_time_with_end_date_time.microsoft_graph_identity_governance_summary_with_start_date_time_with_end_date_time_request_builder import MicrosoftGraphIdentityGovernanceSummaryWithStartDateTimeWithEndDateTimeRequestBuilder

class TaskReportsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the taskReports property of the microsoft.graph.identityGovernance.workflow entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TaskReportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/workflows/{workflow%2Did}/taskReports{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}", path_parameters)
    
    def by_task_report_id(self,task_report_id: str) -> TaskReportItemRequestBuilder:
        """
        Provides operations to manage the taskReports property of the microsoft.graph.identityGovernance.workflow entity.
        param task_report_id: The unique identifier of taskReport
        Returns: TaskReportItemRequestBuilder
        """
        if not task_report_id:
            raise TypeError("task_report_id cannot be null.")
        from .item.task_report_item_request_builder import TaskReportItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["taskReport%2Did"] = task_report_id
        return TaskReportItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[TaskReportsRequestBuilderGetRequestConfiguration] = None) -> Optional[TaskReportCollectionResponse]:
        """
        Get a list of the taskReport objects and their properties.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TaskReportCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-workflow-list-taskreports?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.identity_governance.task_report_collection_response import TaskReportCollectionResponse

        return await self.request_adapter.send_async(request_info, TaskReportCollectionResponse, error_mapping)
    
    def microsoft_graph_identity_governance_summary_with_start_date_time_with_end_date_time(self,end_date_time: Optional[datetime.datetime] = None, start_date_time: Optional[datetime.datetime] = None) -> MicrosoftGraphIdentityGovernanceSummaryWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the summary method.
        param end_date_time: Usage: endDateTime={endDateTime}
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: MicrosoftGraphIdentityGovernanceSummaryWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if not end_date_time:
            raise TypeError("end_date_time cannot be null.")
        if not start_date_time:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_identity_governance_summary_with_start_date_time_with_end_date_time.microsoft_graph_identity_governance_summary_with_start_date_time_with_end_date_time_request_builder import MicrosoftGraphIdentityGovernanceSummaryWithStartDateTimeWithEndDateTimeRequestBuilder

        return MicrosoftGraphIdentityGovernanceSummaryWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time)
    
    def to_get_request_information(self,request_configuration: Optional[TaskReportsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get a list of the taskReport objects and their properties.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> TaskReportsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TaskReportsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return TaskReportsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TaskReportsRequestBuilderGetQueryParameters():
        """
        Get a list of the taskReport objects and their properties.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TaskReportsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[TaskReportsRequestBuilder.TaskReportsRequestBuilderGetQueryParameters] = None

    

