from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .item.with_request_item_request_builder import WithRequestItemRequestBuilder

class RunRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /automations/{id}/leads/{leadId}/run
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RunRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/automations/{id}/leads/{leadId}/run", path_parameters)
    
    def by_request_id(self,request_id: UUID) -> WithRequestItemRequestBuilder:
        """
        Gets an item from the leadping.automations.item.leads.item.run.item collection
        param request_id: Unique identifier of the item
        Returns: WithRequestItemRequestBuilder
        """
        if request_id is None:
            raise TypeError("request_id cannot be null.")
        from .item.with_request_item_request_builder import WithRequestItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["requestId"] = request_id
        return WithRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    

