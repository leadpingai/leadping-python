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
    from ..models.lead_request import LeadRequest
    from ..models.lead_response import LeadResponse
    from ..models.problem_details import ProblemDetails
    from .all.all_request_builder import AllRequestBuilder
    from .intake.intake_request_builder import IntakeRequestBuilder
    from .item.leads_item_request_builder import LeadsItemRequestBuilder

class LeadsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /leads
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LeadsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/leads{?sourceKey*}", path_parameters)
    
    def by_id(self,id: str) -> LeadsItemRequestBuilder:
        """
        Gets an item from the leadping.leads.item collection
        param id: The ID of the lead to retrieve.
        Returns: LeadsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.leads_item_request_builder import LeadsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return LeadsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: LeadRequest, request_configuration: Optional[RequestConfiguration[LeadsRequestBuilderPostQueryParameters]] = None) -> Optional[LeadResponse]:
        """
        Creates a source-authenticated lead captured outside Leadping, starting follow-up, routing, and automation from structured lead data.
        param body: Request schema for the Leadping API lead request, including the fields clients can send.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LeadResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "401": ProblemDetails,
            "403": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.lead_response import LeadResponse

        return await self.request_adapter.send_async(request_info, LeadResponse, error_mapping)
    
    def to_post_request_information(self,body: LeadRequest, request_configuration: Optional[RequestConfiguration[LeadsRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Creates a source-authenticated lead captured outside Leadping, starting follow-up, routing, and automation from structured lead data.
        param body: Request schema for the Leadping API lead request, including the fields clients can send.
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
    
    def with_url(self,raw_url: str) -> LeadsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LeadsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LeadsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def all(self) -> AllRequestBuilder:
        """
        The all property
        """
        from .all.all_request_builder import AllRequestBuilder

        return AllRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intake(self) -> IntakeRequestBuilder:
        """
        The intake property
        """
        from .intake.intake_request_builder import IntakeRequestBuilder

        return IntakeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class LeadsRequestBuilderPostQueryParameters():
        """
        Creates a source-authenticated lead captured outside Leadping, starting follow-up, routing, and automation from structured lead data.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "source_key":
                return "sourceKey"
            return original_name
        
        # The Leadping source key supplied as a query string parameter.
        source_key: Optional[str] = None

    
    @dataclass
    class LeadsRequestBuilderPostRequestConfiguration(RequestConfiguration[LeadsRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

