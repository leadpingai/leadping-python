from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.wallets_item_request_builder import WalletsItemRequestBuilder
    from .me.me_request_builder import MeRequestBuilder

class WalletsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /wallets
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WalletsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/wallets", path_parameters)
    
    def by_id(self,id: str) -> WalletsItemRequestBuilder:
        """
        Gets an item from the leadping.wallets.item collection
        param id: The ID of the wallet to retrieve.
        Returns: WalletsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.wallets_item_request_builder import WalletsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return WalletsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def me(self) -> MeRequestBuilder:
        """
        The me property
        """
        from .me.me_request_builder import MeRequestBuilder

        return MeRequestBuilder(self.request_adapter, self.path_parameters)
    

