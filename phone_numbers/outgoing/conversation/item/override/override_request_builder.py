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
    from ......models.outgoing_number_manual_override_request import OutgoingNumberManualOverrideRequest
    from ......models.outgoing_number_selection_response import OutgoingNumberSelectionResponse
    from ......models.problem_details import ProblemDetails

class OverrideRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /phone-numbers/outgoing/conversation/{conversationId}/override
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OverrideRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/phone-numbers/outgoing/conversation/{conversationId}/override", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[OutgoingNumberSelectionResponse]:
        """
        Clears a conversation's outgoing-number override so future lead messages return to automatic number selection.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OutgoingNumberSelectionResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "401": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.outgoing_number_selection_response import OutgoingNumberSelectionResponse

        return await self.request_adapter.send_async(request_info, OutgoingNumberSelectionResponse, error_mapping)
    
    async def post(self,body: OutgoingNumberManualOverrideRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[OutgoingNumberSelectionResponse]:
        """
        Sets the outgoing phone number override for a conversation so future lead messages use the selected eligible number.
        param body: Request schema for the Leadping API outgoing number manual override request, including the fields clients can send.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OutgoingNumberSelectionResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "401": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.outgoing_number_selection_response import OutgoingNumberSelectionResponse

        return await self.request_adapter.send_async(request_info, OutgoingNumberSelectionResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Clears a conversation's outgoing-number override so future lead messages return to automatic number selection.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: OutgoingNumberManualOverrideRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Sets the outgoing phone number override for a conversation so future lead messages use the selected eligible number.
        param body: Request schema for the Leadping API outgoing number manual override request, including the fields clients can send.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> OverrideRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OverrideRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return OverrideRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class OverrideRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OverrideRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

