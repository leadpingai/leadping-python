from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_conversation_item_request_builder import WithConversationItemRequestBuilder

class ConversationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /events/conversations
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConversationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/events/conversations", path_parameters)
    
    def by_conversation_id(self,conversation_id: str) -> WithConversationItemRequestBuilder:
        """
        Gets an item from the leadping.events.conversations.item collection
        param conversation_id: The ID of the conversation.
        Returns: WithConversationItemRequestBuilder
        """
        if conversation_id is None:
            raise TypeError("conversation_id cannot be null.")
        from .item.with_conversation_item_request_builder import WithConversationItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["conversationId"] = conversation_id
        return WithConversationItemRequestBuilder(self.request_adapter, url_tpl_params)
    

