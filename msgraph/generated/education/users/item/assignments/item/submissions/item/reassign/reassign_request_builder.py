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
    from .........models import education_submission
    from .........models.o_data_errors import o_data_error

class ReassignRequestBuilder():
    """
    Provides operations to call the reassign method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ReassignRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/education/users/{educationUser%2Did}/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}/reassign"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def post(self,request_configuration: Optional[ReassignRequestBuilderPostRequestConfiguration] = None) -> Optional[education_submission.EducationSubmission]:
        """
        Reassign the submission to the student with feedback for review. Only teachers can perform this action.  Include the `Prefer: include-unknown-enum-members` header when you call this method; otherwise, a reassigned submission will be treated as a returned submission. This means that the `reassigned` status will be mapped to the `returned` status, and **reassignedDateTime** and **reassignedBy** properties will be mapped to **returnedDateTime** and **returnedBy** respectively. If the header `Prefer: include-unknown-enum-members` is provided, a reassigned submission retains the `reassigned` status. For details, see the examples section.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[education_submission.EducationSubmission]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from .........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models import education_submission

        return await self.request_adapter.send_async(request_info, education_submission.EducationSubmission, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[ReassignRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Reassign the submission to the student with feedback for review. Only teachers can perform this action.  Include the `Prefer: include-unknown-enum-members` header when you call this method; otherwise, a reassigned submission will be treated as a returned submission. This means that the `reassigned` status will be mapped to the `returned` status, and **reassignedDateTime** and **reassignedBy** properties will be mapped to **returnedDateTime** and **returnedBy** respectively. If the header `Prefer: include-unknown-enum-members` is provided, a reassigned submission retains the `reassigned` status. For details, see the examples section.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    @dataclass
    class ReassignRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

