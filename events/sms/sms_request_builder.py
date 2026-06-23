from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .all.all_request_builder import AllRequestBuilder
    from .item.with_sms_event_item_request_builder import WithSmsEventItemRequestBuilder
    from .lead.lead_request_builder import LeadRequestBuilder
    from .phone.phone_request_builder import PhoneRequestBuilder

class SmsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /events/sms
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SmsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/events/sms", path_parameters)
    
    def by_sms_event_id(self,sms_event_id: str) -> WithSmsEventItemRequestBuilder:
        """
        Gets an item from the leadping.events.sms.item collection
        param sms_event_id: The ID of the SMS event to retrieve.
        Returns: WithSmsEventItemRequestBuilder
        """
        if sms_event_id is None:
            raise TypeError("sms_event_id cannot be null.")
        from .item.with_sms_event_item_request_builder import WithSmsEventItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["smsEventId"] = sms_event_id
        return WithSmsEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def all(self) -> AllRequestBuilder:
        """
        The all property
        """
        from .all.all_request_builder import AllRequestBuilder

        return AllRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lead(self) -> LeadRequestBuilder:
        """
        The lead property
        """
        from .lead.lead_request_builder import LeadRequestBuilder

        return LeadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def phone(self) -> PhoneRequestBuilder:
        """
        The phone property
        """
        from .phone.phone_request_builder import PhoneRequestBuilder

        return PhoneRequestBuilder(self.request_adapter, self.path_parameters)
    

