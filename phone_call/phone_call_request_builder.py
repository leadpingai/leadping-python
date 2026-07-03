from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .initiate.initiate_request_builder import InitiateRequestBuilder
    from .item.with_call_item_request_builder import WithCallItemRequestBuilder

class PhoneCallRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /phone-call
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PhoneCallRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/phone-call", path_parameters)
    
    def by_call_id(self,call_id: str) -> WithCallItemRequestBuilder:
        """
        Gets an item from the leadping.phoneCall.item collection
        param call_id: The unique identifier of the call to end.
        Returns: WithCallItemRequestBuilder
        """
        if call_id is None:
            raise TypeError("call_id cannot be null.")
        from .item.with_call_item_request_builder import WithCallItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["callId"] = call_id
        return WithCallItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def initiate(self) -> InitiateRequestBuilder:
        """
        The initiate property
        """
        from .initiate.initiate_request_builder import InitiateRequestBuilder

        return InitiateRequestBuilder(self.request_adapter, self.path_parameters)
    

