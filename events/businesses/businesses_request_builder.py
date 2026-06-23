from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_business_item_request_builder import WithBusinessItemRequestBuilder

class BusinessesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /events/businesses
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BusinessesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/events/businesses", path_parameters)
    
    def by_business_id(self,business_id: str) -> WithBusinessItemRequestBuilder:
        """
        Gets an item from the leadping.events.businesses.item collection
        param business_id: The business identifier.
        Returns: WithBusinessItemRequestBuilder
        """
        if business_id is None:
            raise TypeError("business_id cannot be null.")
        from .item.with_business_item_request_builder import WithBusinessItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["businessId"] = business_id
        return WithBusinessItemRequestBuilder(self.request_adapter, url_tpl_params)
    

