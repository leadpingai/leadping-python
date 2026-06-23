from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ..models.disposition_request import DispositionRequest
    from ..models.disposition_response import DispositionResponse
    from ..models.problem_details import ProblemDetails
    from .item.dispositions_item_request_builder import DispositionsItemRequestBuilder
    from .lead.lead_request_builder import LeadRequestBuilder

class DispositionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /dispositions
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DispositionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/dispositions", path_parameters)
    
    def by_id(self,id: str) -> DispositionsItemRequestBuilder:
        """
        Gets an item from the leadping.dispositions.item collection
        param id: The ID of the disposition.
        Returns: DispositionsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.dispositions_item_request_builder import DispositionsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return DispositionsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: DispositionRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DispositionResponse]:
        """
        Sets a lead's current structured outcome while recording the disposition change in history for audit, automation, and reporting.
        param body: Request model for creating or updating a disposition.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DispositionResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.disposition_response import DispositionResponse

        return await self.request_adapter.send_async(request_info, DispositionResponse, error_mapping)
    
    def to_post_request_information(self,body: DispositionRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Sets a lead's current structured outcome while recording the disposition change in history for audit, automation, and reporting.
        param body: Request model for creating or updating a disposition.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> DispositionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DispositionsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DispositionsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def lead(self) -> LeadRequestBuilder:
        """
        The lead property
        """
        from .lead.lead_request_builder import LeadRequestBuilder

        return LeadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DispositionsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

