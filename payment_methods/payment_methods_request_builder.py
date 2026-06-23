from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.payment_methods_item_request_builder import PaymentMethodsItemRequestBuilder

class PaymentMethodsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /payment-methods
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PaymentMethodsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/payment-methods", path_parameters)
    
    def by_id(self,id: str) -> PaymentMethodsItemRequestBuilder:
        """
        Gets an item from the leadping.paymentMethods.item collection
        param id: The ID of the payment method to retrieve.
        Returns: PaymentMethodsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.payment_methods_item_request_builder import PaymentMethodsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return PaymentMethodsItemRequestBuilder(self.request_adapter, url_tpl_params)
    

