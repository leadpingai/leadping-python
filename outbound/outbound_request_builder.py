from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_phone_number_item_request_builder import WithPhoneNumberItemRequestBuilder
    from .overview.overview_request_builder import OverviewRequestBuilder

class OutboundRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /outbound
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OutboundRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/outbound", path_parameters)
    
    def by_phone_number_id(self,phone_number_id: str) -> WithPhoneNumberItemRequestBuilder:
        """
        Gets an item from the leadping.outbound.item collection
        param phone_number_id: The ID of the phone number whose outbound capacity should be retrieved.
        Returns: WithPhoneNumberItemRequestBuilder
        """
        if phone_number_id is None:
            raise TypeError("phone_number_id cannot be null.")
        from .item.with_phone_number_item_request_builder import WithPhoneNumberItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["phoneNumberId"] = phone_number_id
        return WithPhoneNumberItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def overview(self) -> OverviewRequestBuilder:
        """
        The overview property
        """
        from .overview.overview_request_builder import OverviewRequestBuilder

        return OverviewRequestBuilder(self.request_adapter, self.path_parameters)
    

