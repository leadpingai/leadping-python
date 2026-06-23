from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_phone_number_item_request_builder import WithPhoneNumberItemRequestBuilder

class PhoneRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /events/sms/phone
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PhoneRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/events/sms/phone", path_parameters)
    
    def by_phone_number(self,phone_number: str) -> WithPhoneNumberItemRequestBuilder:
        """
        Gets an item from the leadping.events.sms.phone.item collection
        param phone_number: The phone number to search for.
        Returns: WithPhoneNumberItemRequestBuilder
        """
        if phone_number is None:
            raise TypeError("phone_number cannot be null.")
        from .item.with_phone_number_item_request_builder import WithPhoneNumberItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["phoneNumber"] = phone_number
        return WithPhoneNumberItemRequestBuilder(self.request_adapter, url_tpl_params)
    

