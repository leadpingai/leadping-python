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
    from ...models.conversation_response import ConversationResponse
    from ...models.problem_details import ProblemDetails
    from .mark_read.mark_read_request_builder import MarkReadRequestBuilder
    from .outbound_readiness.outbound_readiness_request_builder import OutboundReadinessRequestBuilder

class ConversationsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /conversations/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConversationsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/conversations/{id}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ConversationResponse]:
        """
        Returns a conversation accessible to the current user, including its current event version for tracking inbox updates.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConversationResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
            "403": ProblemDetails,
            "404": ProblemDetails,
            "429": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.conversation_response import ConversationResponse

        return await self.request_adapter.send_async(request_info, ConversationResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a conversation accessible to the current user, including its current event version for tracking inbox updates.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> ConversationsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ConversationsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ConversationsItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def mark_read(self) -> MarkReadRequestBuilder:
        """
        The markRead property
        """
        from .mark_read.mark_read_request_builder import MarkReadRequestBuilder

        return MarkReadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def outbound_readiness(self) -> OutboundReadinessRequestBuilder:
        """
        The outboundReadiness property
        """
        from .outbound_readiness.outbound_readiness_request_builder import OutboundReadinessRequestBuilder

        return OutboundReadinessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ConversationsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

