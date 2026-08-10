from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .current.current_request_builder import CurrentRequestBuilder
    from .item.with_installation_item_request_builder import WithInstallationItemRequestBuilder

class InstallationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /notifications/push/installations
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InstallationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/notifications/push/installations", path_parameters)
    
    def by_installation_id(self,installation_id: str) -> WithInstallationItemRequestBuilder:
        """
        Gets an item from the leadping.notifications.push.installations.item collection
        param installation_id: Unique identifier of the item
        Returns: WithInstallationItemRequestBuilder
        """
        if installation_id is None:
            raise TypeError("installation_id cannot be null.")
        from .item.with_installation_item_request_builder import WithInstallationItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["installationId"] = installation_id
        return WithInstallationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def current(self) -> CurrentRequestBuilder:
        """
        The current property
        """
        from .current.current_request_builder import CurrentRequestBuilder

        return CurrentRequestBuilder(self.request_adapter, self.path_parameters)
    

