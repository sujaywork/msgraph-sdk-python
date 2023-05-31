from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import synchronization_job, synchronization_job_collection_response
    from .....models.o_data_errors import o_data_error
    from .count import count_request_builder
    from .item import synchronization_job_item_request_builder
    from .validate_credentials import validate_credentials_request_builder

class JobsRequestBuilder():
    """
    Provides operations to manage the jobs property of the microsoft.graph.synchronization entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new JobsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/synchronization/jobs{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def by_synchronization_job_id(self,synchronization_job_id: str) -> synchronization_job_item_request_builder.SynchronizationJobItemRequestBuilder:
        """
        Provides operations to manage the jobs property of the microsoft.graph.synchronization entity.
        Args:
            synchronization_job_id: Unique identifier of the item
        Returns: synchronization_job_item_request_builder.SynchronizationJobItemRequestBuilder
        """
        if synchronization_job_id is None:
            raise Exception("synchronization_job_id cannot be undefined")
        from .item import synchronization_job_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["synchronizationJob%2Did"] = synchronization_job_id
        return synchronization_job_item_request_builder.SynchronizationJobItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[JobsRequestBuilderGetRequestConfiguration] = None) -> Optional[synchronization_job_collection_response.SynchronizationJobCollectionResponse]:
        """
        Get jobs from servicePrincipals
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[synchronization_job_collection_response.SynchronizationJobCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import synchronization_job_collection_response

        return await self.request_adapter.send_async(request_info, synchronization_job_collection_response.SynchronizationJobCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[synchronization_job.SynchronizationJob] = None, request_configuration: Optional[JobsRequestBuilderPostRequestConfiguration] = None) -> Optional[synchronization_job.SynchronizationJob]:
        """
        Create new navigation property to jobs for servicePrincipals
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[synchronization_job.SynchronizationJob]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import synchronization_job

        return await self.request_adapter.send_async(request_info, synchronization_job.SynchronizationJob, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[JobsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get jobs from servicePrincipals
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
    
    def to_post_request_information(self,body: Optional[synchronization_job.SynchronizationJob] = None, request_configuration: Optional[JobsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to jobs for servicePrincipals
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count import count_request_builder

        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_credentials(self) -> validate_credentials_request_builder.ValidateCredentialsRequestBuilder:
        """
        Provides operations to call the validateCredentials method.
        """
        from .validate_credentials import validate_credentials_request_builder

        return validate_credentials_request_builder.ValidateCredentialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class JobsRequestBuilderGetQueryParameters():
        """
        Get jobs from servicePrincipals
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
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

    
    @dataclass
    class JobsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[JobsRequestBuilder.JobsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class JobsRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
