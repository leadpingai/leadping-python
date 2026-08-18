from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_event_item_request_builder import WithEventItemRequestBuilder

class DetailRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /events/detail
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DetailRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/events/detail", path_parameters)
    
    def by_event_id(self,event_id: str) -> WithEventItemRequestBuilder:
        """
        Gets an item from the leadping.events.detail.item collection
        param event_id: The ID of the event.
        Returns: WithEventItemRequestBuilder
        """
        if event_id is None:
            raise TypeError("event_id cannot be null.")
        from .item.with_event_item_request_builder import WithEventItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["eventId"] = event_id
        return WithEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    

