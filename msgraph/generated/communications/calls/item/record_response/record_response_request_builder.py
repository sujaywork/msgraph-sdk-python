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
    from . import record_response_post_request_body
    from .....models import record_operation
    from .....models.o_data_errors import o_data_error

class RecordResponseRequestBuilder():
    """
    Provides operations to call the recordResponse method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new RecordResponseRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/communications/calls/{call%2Did}/recordResponse"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def post(self,body: Optional[record_response_post_request_body.RecordResponsePostRequestBody] = None, request_configuration: Optional[RecordResponseRequestBuilderPostRequestConfiguration] = None) -> Optional[record_operation.RecordOperation]:
        """
        Records a short audio response from the caller.A bot can utilize this to capture a voice response from a caller after they are prompted for a response. For further information on how to handle operations, please review commsOperation This action is not intended to record the entire call. The maximum length of recording is 2 minutes. The recording is not saved permanently by the Cloud Communications Platform and is discarded shortly after the call ends. The bot must download the recording promptly after the recording operation finishes by using the recordingLocation value that's given in the completed notification.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[record_operation.RecordOperation]
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
        from .....models import record_operation

        return await self.request_adapter.send_async(request_info, record_operation.RecordOperation, error_mapping)
    
    def to_post_request_information(self,body: Optional[record_response_post_request_body.RecordResponsePostRequestBody] = None, request_configuration: Optional[RecordResponseRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Records a short audio response from the caller.A bot can utilize this to capture a voice response from a caller after they are prompted for a response. For further information on how to handle operations, please review commsOperation This action is not intended to record the entire call. The maximum length of recording is 2 minutes. The recording is not saved permanently by the Cloud Communications Platform and is discarded shortly after the call ends. The bot must download the recording promptly after the recording operation finishes by using the recordingLocation value that's given in the completed notification.
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
    class RecordResponseRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

