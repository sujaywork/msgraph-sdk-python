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
    from .....models import mail_folder, mail_folder_collection_response
    from .....models.o_data_errors import o_data_error
    from .count import count_request_builder
    from .delta import delta_request_builder
    from .item import mail_folder_item_request_builder

class ChildFoldersRequestBuilder():
    """
    Provides operations to manage the childFolders property of the microsoft.graph.mailFolder entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ChildFoldersRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/mailFolders/{mailFolder%2Did}/childFolders{?%24top,%24skip,%24filter,%24count,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def by_mail_folder_id1(self,mail_folder_id1: str) -> mail_folder_item_request_builder.MailFolderItemRequestBuilder:
        """
        Provides operations to manage the childFolders property of the microsoft.graph.mailFolder entity.
        Args:
            mail_folder_id1: Unique identifier of the item
        Returns: mail_folder_item_request_builder.MailFolderItemRequestBuilder
        """
        if not mail_folder_id1:
            raise TypeError("mail_folder_id1 cannot be null.")
        from .item import mail_folder_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mailFolder%2Did1"] = mail_folder_id1
        return mail_folder_item_request_builder.MailFolderItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ChildFoldersRequestBuilderGetRequestConfiguration] = None) -> Optional[mail_folder_collection_response.MailFolderCollectionResponse]:
        """
        Get the folder collection under the specified folder. You can use the `.../me/mailFolders` shortcut to get the top-level folder collection and navigate to another folder. By default, this operation does not return hidden folders. Use a query parameter _includeHiddenFolders_ to include them in the response.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[mail_folder_collection_response.MailFolderCollectionResponse]
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
        from .....models import mail_folder_collection_response

        return await self.request_adapter.send_async(request_info, mail_folder_collection_response.MailFolderCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[mail_folder.MailFolder] = None, request_configuration: Optional[ChildFoldersRequestBuilderPostRequestConfiguration] = None) -> Optional[mail_folder.MailFolder]:
        """
        Use this API to create a new child mailFolder. If you intend a new folder to be hidden, you must set the **isHidden** property to `true` on creation.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[mail_folder.MailFolder]
        """
        if not body:
            raise TypeError("body cannot be null.")
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
        from .....models import mail_folder

        return await self.request_adapter.send_async(request_info, mail_folder.MailFolder, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[ChildFoldersRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the folder collection under the specified folder. You can use the `.../me/mailFolders` shortcut to get the top-level folder collection and navigate to another folder. By default, this operation does not return hidden folders. Use a query parameter _includeHiddenFolders_ to include them in the response.
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
    
    def to_post_request_information(self,body: Optional[mail_folder.MailFolder] = None, request_configuration: Optional[ChildFoldersRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Use this API to create a new child mailFolder. If you intend a new folder to be hidden, you must set the **isHidden** property to `true` on creation.
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
    def delta(self) -> delta_request_builder.DeltaRequestBuilder:
        """
        Provides operations to call the delta method.
        """
        from .delta import delta_request_builder

        return delta_request_builder.DeltaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ChildFoldersRequestBuilderGetQueryParameters():
        """
        Get the folder collection under the specified folder. You can use the `.../me/mailFolders` shortcut to get the top-level folder collection and navigate to another folder. By default, this operation does not return hidden folders. Use a query parameter _includeHiddenFolders_ to include them in the response.
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
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
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

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class ChildFoldersRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ChildFoldersRequestBuilder.ChildFoldersRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ChildFoldersRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

