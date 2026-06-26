from __future__ import annotations
import datetime
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
    from ...models.paged_result_of_feedback_response import PagedResultOfFeedbackResponse
    from .item.admin_item_request_builder import AdminItemRequestBuilder

class AdminRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /feedback/admin
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AdminRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/feedback/admin{?Area*,BusinessId*,ContinuationToken*,CreatedEnd*,CreatedStart*,PageSize*,Search*,Status*,Type*}", path_parameters)
    
    def by_id(self,id: str) -> AdminItemRequestBuilder:
        """
        Gets an item from the leadping.feedback.admin.item collection
        param id: Unique identifier of the item
        Returns: AdminItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.admin_item_request_builder import AdminItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return AdminItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AdminRequestBuilderGetQueryParameters]] = None) -> Optional[PagedResultOfFeedbackResponse]:
        """
        Lists submitted feedback for admin triage with query filters, paging, status, and category review fields.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PagedResultOfFeedbackResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.paged_result_of_feedback_response import PagedResultOfFeedbackResponse

        return await self.request_adapter.send_async(request_info, PagedResultOfFeedbackResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AdminRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Lists submitted feedback for admin triage with query filters, paging, status, and category review fields.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> AdminRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AdminRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AdminRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class AdminRequestBuilderGetQueryParameters():
        """
        Lists submitted feedback for admin triage with query filters, paging, status, and category review fields.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "area":
                return "Area"
            if original_name == "business_id":
                return "BusinessId"
            if original_name == "continuation_token":
                return "ContinuationToken"
            if original_name == "created_end":
                return "CreatedEnd"
            if original_name == "created_start":
                return "CreatedStart"
            if original_name == "page_size":
                return "PageSize"
            if original_name == "search":
                return "Search"
            if original_name == "status":
                return "Status"
            if original_name == "type":
                return "Type"
            return original_name
        
        # Product area or app section connected to this feedback admin query request.
        area: Optional[str] = None

        # Business ID used to filter feedback items for admin review.
        business_id: Optional[str] = None

        # Pagination token used to request the next page of Leadping API results.
        continuation_token: Optional[str] = None

        # End of the created-at date range filter for Leadping API results.
        created_end: Optional[datetime.datetime] = None

        # Start of the created-at date range filter for Leadping API results.
        created_start: Optional[datetime.datetime] = None

        # Maximum number of results requested for this Leadping API page.
        page_size: Optional[int] = None

        # Search text used to filter Leadping API results.
        search: Optional[str] = None

        # Current lifecycle status for this feedback admin query request in the Leadping API.
        status: Optional[str] = None

        # Type classification used to route and interpret this feedback admin query request in the Leadping API.
        type: Optional[str] = None

    
    @dataclass
    class AdminRequestBuilderGetRequestConfiguration(RequestConfiguration[AdminRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

