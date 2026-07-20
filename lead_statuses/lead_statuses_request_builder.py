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
    from ..models.lead_status_request import LeadStatusRequest
    from ..models.lead_status_response import LeadStatusResponse
    from .item.lead_statuses_item_request_builder import LeadStatusesItemRequestBuilder

class LeadStatusesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /lead-statuses
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LeadStatusesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/lead-statuses", path_parameters)
    
    def by_id(self,id: str) -> LeadStatusesItemRequestBuilder:
        """
        Gets an item from the leadping.leadStatuses.item collection
        param id: Unique identifier of the item
        Returns: LeadStatusesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.lead_statuses_item_request_builder import LeadStatusesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return LeadStatusesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[list[LeadStatusResponse]]:
        """
        Get all
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[LeadStatusResponse]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.lead_status_response import LeadStatusResponse

        return await self.request_adapter.send_collection_async(request_info, LeadStatusResponse, None)
    
    async def post(self,body: LeadStatusRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LeadStatusResponse]:
        """
        Create
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LeadStatusResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.lead_status_response import LeadStatusResponse

        return await self.request_adapter.send_async(request_info, LeadStatusResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Get all
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: LeadStatusRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> LeadStatusesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LeadStatusesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LeadStatusesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class LeadStatusesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class LeadStatusesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

