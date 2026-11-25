from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_opted_in_item_request_builder import WithOptedInItemRequestBuilder

class WithChannelItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /suppressions/admin/leads/{leadId}/{channel}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithChannelItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/suppressions/admin/leads/{leadId}/{channel}", path_parameters)
    
    def by_opted_in(self,opted_in: bool) -> WithOptedInItemRequestBuilder:
        """
        Gets an item from the leadping.suppressions.admin.leads.item.item.item collection
        param opted_in: Unique identifier of the item
        Returns: WithOptedInItemRequestBuilder
        """
        if opted_in is None:
            raise TypeError("opted_in cannot be null.")
        from .item.with_opted_in_item_request_builder import WithOptedInItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["optedIn"] = opted_in
        return WithOptedInItemRequestBuilder(self.request_adapter, url_tpl_params)
    

