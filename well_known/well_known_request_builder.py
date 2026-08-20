from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent_card_json.agent_card_json_request_builder import AgentCardJsonRequestBuilder

class WellKnownRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /.well-known
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WellKnownRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/.well-known", path_parameters)
    
    @property
    def agent_card_json(self) -> AgentCardJsonRequestBuilder:
        """
        The agentCardJson property
        """
        from .agent_card_json.agent_card_json_request_builder import AgentCardJsonRequestBuilder

        return AgentCardJsonRequestBuilder(self.request_adapter, self.path_parameters)
    

