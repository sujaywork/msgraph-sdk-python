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
    from .....models.o_data_errors.o_data_error import ODataError
    from .recent_get_response import RecentGetResponse

class RecentRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the recent method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new RecentRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/activities/recent(){?%24top,%24skip,%24search,%24filter,%24count,%24select,%24orderby}", path_parameters)
    
    async def get(self,request_configuration: Optional[RecentRequestBuilderGetRequestConfiguration] = None) -> Optional[RecentGetResponse]:
        """
        Get recent activities for a given user. This OData function has some default behaviors included to make it operate like a 'most recently used' API. The service queries for the most recent historyItems, and then pull those related activities. Activities are sorted according to the most recent lastModified on the historyItem. This means that activities without historyItems won't be included in the response. The UserActivity.ReadWrite.CreatedByApp permission will also apply extra filtering to the response, so that only activities created by your application are returned. This server-side filtering might result in empty pages if the user is active and other applications have created more recent activities. To get your application's activities, use the nextLink property to paginate.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RecentGetResponse]
        Find more info here: https://learn.microsoft.com/graph/api/projectrome-get-recent-activities?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .recent_get_response import RecentGetResponse

        return await self.request_adapter.send_async(request_info, RecentGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RecentRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get recent activities for a given user. This OData function has some default behaviors included to make it operate like a 'most recently used' API. The service queries for the most recent historyItems, and then pull those related activities. Activities are sorted according to the most recent lastModified on the historyItem. This means that activities without historyItems won't be included in the response. The UserActivity.ReadWrite.CreatedByApp permission will also apply extra filtering to the response, so that only activities created by your application are returned. This server-side filtering might result in empty pages if the user is active and other applications have created more recent activities. To get your application's activities, use the nextLink property to paginate.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> RecentRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RecentRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return RecentRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class RecentRequestBuilderGetQueryParameters():
        """
        Get recent activities for a given user. This OData function has some default behaviors included to make it operate like a 'most recently used' API. The service queries for the most recent historyItems, and then pull those related activities. Activities are sorted according to the most recent lastModified on the historyItem. This means that activities without historyItems won't be included in the response. The UserActivity.ReadWrite.CreatedByApp permission will also apply extra filtering to the response, so that only activities created by your application are returned. This server-side filtering might result in empty pages if the user is active and other applications have created more recent activities. To get your application's activities, use the nextLink property to paginate.
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
    class RecentRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[RecentRequestBuilder.RecentRequestBuilderGetQueryParameters] = None

    

