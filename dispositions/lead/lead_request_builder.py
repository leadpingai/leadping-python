from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_lead_item_request_builder import WithLeadItemRequestBuilder

class LeadRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /dispositions/lead
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LeadRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/dispositions/lead", path_parameters)
    
    def by_lead_id(self,lead_id: str) -> WithLeadItemRequestBuilder:
        """
        Gets an item from the leadping.dispositions.lead.item collection
        param lead_id: The ID of the lead to get dispositions for.
        Returns: WithLeadItemRequestBuilder
        """
        if lead_id is None:
            raise TypeError("lead_id cannot be null.")
        from .item.with_lead_item_request_builder import WithLeadItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["leadId"] = lead_id
        return WithLeadItemRequestBuilder(self.request_adapter, url_tpl_params)
    

