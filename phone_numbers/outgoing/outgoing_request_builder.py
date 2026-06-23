from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conversation.conversation_request_builder import ConversationRequestBuilder
    from .manual_override.manual_override_request_builder import ManualOverrideRequestBuilder
    from .new.new_request_builder import NewRequestBuilder

class OutgoingRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /phone-numbers/outgoing
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OutgoingRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/phone-numbers/outgoing", path_parameters)
    
    @property
    def conversation(self) -> ConversationRequestBuilder:
        """
        The conversation property
        """
        from .conversation.conversation_request_builder import ConversationRequestBuilder

        return ConversationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def manual_override(self) -> ManualOverrideRequestBuilder:
        """
        The manualOverride property
        """
        from .manual_override.manual_override_request_builder import ManualOverrideRequestBuilder

        return ManualOverrideRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def new(self) -> NewRequestBuilder:
        """
        The new property
        """
        from .new.new_request_builder import NewRequestBuilder

        return NewRequestBuilder(self.request_adapter, self.path_parameters)
    

