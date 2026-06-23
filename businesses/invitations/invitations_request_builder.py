from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .accept.accept_request_builder import AcceptRequestBuilder
    from .token.token_request_builder import TokenRequestBuilder

class InvitationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /businesses/invitations
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InvitationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/businesses/invitations", path_parameters)
    
    @property
    def accept(self) -> AcceptRequestBuilder:
        """
        The accept property
        """
        from .accept.accept_request_builder import AcceptRequestBuilder

        return AcceptRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def token(self) -> TokenRequestBuilder:
        """
        The token property
        """
        from .token.token_request_builder import TokenRequestBuilder

        return TokenRequestBuilder(self.request_adapter, self.path_parameters)
    

