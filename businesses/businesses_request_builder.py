from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .api_keys.api_keys_request_builder import ApiKeysRequestBuilder
    from .invitations.invitations_request_builder import InvitationsRequestBuilder
    from .me.me_request_builder import MeRequestBuilder

class BusinessesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /businesses
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BusinessesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/businesses", path_parameters)
    
    @property
    def api_keys(self) -> ApiKeysRequestBuilder:
        """
        The apiKeys property
        """
        from .api_keys.api_keys_request_builder import ApiKeysRequestBuilder

        return ApiKeysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invitations(self) -> InvitationsRequestBuilder:
        """
        The invitations property
        """
        from .invitations.invitations_request_builder import InvitationsRequestBuilder

        return InvitationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def me(self) -> MeRequestBuilder:
        """
        The me property
        """
        from .me.me_request_builder import MeRequestBuilder

        return MeRequestBuilder(self.request_adapter, self.path_parameters)
    

