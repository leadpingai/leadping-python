from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_organization_item_request_builder import WithOrganizationItemRequestBuilder

class OrganizationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /events/organizations
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OrganizationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/events/organizations", path_parameters)
    
    def by_organization_id(self,organization_id: str) -> WithOrganizationItemRequestBuilder:
        """
        Gets an item from the leadping.events.organizations.item collection
        param organization_id: The organization identifier.
        Returns: WithOrganizationItemRequestBuilder
        """
        if organization_id is None:
            raise TypeError("organization_id cannot be null.")
        from .item.with_organization_item_request_builder import WithOrganizationItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["organizationId"] = organization_id
        return WithOrganizationItemRequestBuilder(self.request_adapter, url_tpl_params)
    

