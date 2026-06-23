from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .all.all_request_builder import AllRequestBuilder
    from .businesses.businesses_request_builder import BusinessesRequestBuilder
    from .calls.calls_request_builder import CallsRequestBuilder
    from .conversations.conversations_request_builder import ConversationsRequestBuilder
    from .item.with_event_item_request_builder import WithEventItemRequestBuilder
    from .leads.leads_request_builder import LeadsRequestBuilder
    from .sms.sms_request_builder import SmsRequestBuilder

class EventsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /events
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EventsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/events", path_parameters)
    
    def by_event_id(self,event_id: str) -> WithEventItemRequestBuilder:
        """
        Gets an item from the leadping.events.item collection
        param event_id: The ID of the event.
        Returns: WithEventItemRequestBuilder
        """
        if event_id is None:
            raise TypeError("event_id cannot be null.")
        from .item.with_event_item_request_builder import WithEventItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["eventId"] = event_id
        return WithEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def all(self) -> AllRequestBuilder:
        """
        The all property
        """
        from .all.all_request_builder import AllRequestBuilder

        return AllRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def businesses(self) -> BusinessesRequestBuilder:
        """
        The businesses property
        """
        from .businesses.businesses_request_builder import BusinessesRequestBuilder

        return BusinessesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calls(self) -> CallsRequestBuilder:
        """
        The calls property
        """
        from .calls.calls_request_builder import CallsRequestBuilder

        return CallsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conversations(self) -> ConversationsRequestBuilder:
        """
        The conversations property
        """
        from .conversations.conversations_request_builder import ConversationsRequestBuilder

        return ConversationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def leads(self) -> LeadsRequestBuilder:
        """
        The leads property
        """
        from .leads.leads_request_builder import LeadsRequestBuilder

        return LeadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sms(self) -> SmsRequestBuilder:
        """
        The sms property
        """
        from .sms.sms_request_builder import SmsRequestBuilder

        return SmsRequestBuilder(self.request_adapter, self.path_parameters)
    

