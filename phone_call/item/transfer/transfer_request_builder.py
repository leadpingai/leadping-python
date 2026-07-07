from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.phone_call_response import PhoneCallResponse
    from ....models.problem_details import ProblemDetails

class TransferRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /phone-call/{callId}/transfer
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TransferRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/phone-call/{callId}/transfer{?newPhoneNumber*}", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[TransferRequestBuilderPostQueryParameters]] = None) -> Optional[PhoneCallResponse]:
        """
        Transfers an active Leadping phone call to a new phone number and returns the updated call record with status and routing details.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PhoneCallResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "401": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.phone_call_response import PhoneCallResponse

        return await self.request_adapter.send_async(request_info, PhoneCallResponse, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[TransferRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Transfers an active Leadping phone call to a new phone number and returns the updated call record with status and routing details.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> TransferRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TransferRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TransferRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TransferRequestBuilderPostQueryParameters():
        """
        Transfers an active Leadping phone call to a new phone number and returns the updated call record with status and routing details.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "new_phone_number":
                return "newPhoneNumber"
            return original_name
        
        # The phone number to transfer the call to.
        new_phone_number: Optional[str] = None

    
    @dataclass
    class TransferRequestBuilderPostRequestConfiguration(RequestConfiguration[TransferRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

