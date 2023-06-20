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
    from . import mute_post_request_body
    from .....models import mute_participant_operation
    from .....models.o_data_errors import o_data_error

class MuteRequestBuilder():
    """
    Provides operations to call the mute method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MuteRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/communications/calls/{call%2Did}/mute"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def post(self,body: Optional[mute_post_request_body.MutePostRequestBody] = None, request_configuration: Optional[MuteRequestBuilderPostRequestConfiguration] = None) -> Optional[mute_participant_operation.MuteParticipantOperation]:
        """
        Allows the application to mute itself. This is a server mute, meaning that the server will drop all audio packets for this participant, even if the participant continues to stream audio. For more details about how to handle mute operations, see muteParticipantOperation
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[mute_participant_operation.MuteParticipantOperation]
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
        from .....models import mute_participant_operation

        return await self.request_adapter.send_async(request_info, mute_participant_operation.MuteParticipantOperation, error_mapping)
    
    def to_post_request_information(self,body: Optional[mute_post_request_body.MutePostRequestBody] = None, request_configuration: Optional[MuteRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Allows the application to mute itself. This is a server mute, meaning that the server will drop all audio packets for this participant, even if the participant continues to stream audio. For more details about how to handle mute operations, see muteParticipantOperation
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
    
    @dataclass
    class MuteRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

