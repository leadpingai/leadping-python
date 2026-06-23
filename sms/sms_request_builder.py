from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_sms_event_item_request_builder import WithSmsEventItemRequestBuilder
    from .send.send_request_builder import SendRequestBuilder

class SmsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /sms
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SmsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/sms", path_parameters)
    
    def by_sms_event_id(self,sms_event_id: str) -> WithSmsEventItemRequestBuilder:
        """
        Gets an item from the leadping.sms.item collection
        param sms_event_id: The sms event identifier.
        Returns: WithSmsEventItemRequestBuilder
        """
        if sms_event_id is None:
            raise TypeError("sms_event_id cannot be null.")
        from .item.with_sms_event_item_request_builder import WithSmsEventItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["smsEventId"] = sms_event_id
        return WithSmsEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def send(self) -> SendRequestBuilder:
        """
        The send property
        """
        from .send.send_request_builder import SendRequestBuilder

        return SendRequestBuilder(self.request_adapter, self.path_parameters)
    

