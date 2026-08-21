from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.api_keys_item_request_builder import ApiKeysItemRequestBuilder
    from .my.my_request_builder import MyRequestBuilder

class ApiKeysRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /organizations/api-keys
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ApiKeysRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/organizations/api-keys", path_parameters)
    
    def by_id(self,id: str) -> ApiKeysItemRequestBuilder:
        """
        Gets an item from the leadping.organizations.apiKeys.item collection
        param id: The API key ID.
        Returns: ApiKeysItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.api_keys_item_request_builder import ApiKeysItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return ApiKeysItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def my(self) -> MyRequestBuilder:
        """
        The my property
        """
        from .my.my_request_builder import MyRequestBuilder

        return MyRequestBuilder(self.request_adapter, self.path_parameters)
    

