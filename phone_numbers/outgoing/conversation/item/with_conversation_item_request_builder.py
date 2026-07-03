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
    from .....models.outgoing_number_selection_request import OutgoingNumberSelectionRequest
    from .....models.outgoing_number_selection_response import OutgoingNumberSelectionResponse
    from .....models.problem_details import ProblemDetails
    from .override.override_request_builder import OverrideRequestBuilder

class WithConversationItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /phone-numbers/outgoing/conversation/{conversationId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithConversationItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/phone-numbers/outgoing/conversation/{conversationId}", path_parameters)
    
    async def post(self,body: OutgoingNumberSelectionRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[OutgoingNumberSelectionResponse]:
        """
        Selects the outgoing phone number for an existing conversation, considering assignments, overrides, and delivery eligibility.
        param body: Request schema for the Leadping API outgoing number selection request, including the fields clients can send.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OutgoingNumberSelectionResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "401": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.outgoing_number_selection_response import OutgoingNumberSelectionResponse

        return await self.request_adapter.send_async(request_info, OutgoingNumberSelectionResponse, error_mapping)
    
    def to_post_request_information(self,body: OutgoingNumberSelectionRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Selects the outgoing phone number for an existing conversation, considering assignments, overrides, and delivery eligibility.
        param body: Request schema for the Leadping API outgoing number selection request, including the fields clients can send.
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
    
    def with_url(self,raw_url: str) -> WithConversationItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithConversationItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithConversationItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def override(self) -> OverrideRequestBuilder:
        """
        The override property
        """
        from .override.override_request_builder import OverrideRequestBuilder

        return OverrideRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithConversationItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

