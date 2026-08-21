from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .all.all_request_builder import AllRequestBuilder
    from .item.transactions_item_request_builder import TransactionsItemRequestBuilder

class TransactionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /transactions
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TransactionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/transactions", path_parameters)
    
    def by_id(self,id: str) -> TransactionsItemRequestBuilder:
        """
        Gets an item from the leadping.transactions.item collection
        param id: The ID of the transaction to retrieve.
        Returns: TransactionsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.transactions_item_request_builder import TransactionsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return TransactionsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def all(self) -> AllRequestBuilder:
        """
        The all property
        """
        from .all.all_request_builder import AllRequestBuilder

        return AllRequestBuilder(self.request_adapter, self.path_parameters)
    

