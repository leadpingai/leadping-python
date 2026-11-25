from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_channel_item_request_builder import WithChannelItemRequestBuilder

class WithLeadItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /suppressions/admin/leads/{leadId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithLeadItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/suppressions/admin/leads/{leadId}", path_parameters)
    
    def by_channel(self,channel: str) -> WithChannelItemRequestBuilder:
        """
        Gets an item from the leadping.suppressions.admin.leads.item.item collection
        param channel: Unique identifier of the item
        Returns: WithChannelItemRequestBuilder
        """
        if channel is None:
            raise TypeError("channel cannot be null.")
        from .item.with_channel_item_request_builder import WithChannelItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["channel"] = channel
        return WithChannelItemRequestBuilder(self.request_adapter, url_tpl_params)
    

