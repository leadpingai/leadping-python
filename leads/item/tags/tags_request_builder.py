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
    from ....models.lead_response import LeadResponse
    from ....models.lead_tags_request import LeadTagsRequest
    from ....models.problem_details import ProblemDetails
    from .item.with_tag_item_request_builder import WithTagItemRequestBuilder

class TagsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /leads/{id}/tags
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TagsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/leads/{id}/tags", path_parameters)
    
    def by_tag_id(self,tag_id: str) -> WithTagItemRequestBuilder:
        """
        Gets an item from the leadping.leads.item.tags.item collection
        param tag_id: Unique identifier of the item
        Returns: WithTagItemRequestBuilder
        """
        if tag_id is None:
            raise TypeError("tag_id cannot be null.")
        from .item.with_tag_item_request_builder import WithTagItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tagId"] = tag_id
        return WithTagItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: LeadTagsRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LeadResponse]:
        """
        Adds one or more current-business tags to a lead so users can segment, filter, route, and review follow-up work.
        param body: Request schema for the Leadping API lead tag update request, including the fields clients can send.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LeadResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.lead_response import LeadResponse

        return await self.request_adapter.send_async(request_info, LeadResponse, error_mapping)
    
    async def put(self,body: LeadTagsRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LeadResponse]:
        """
        Replaces all tags on a lead with the supplied current-business tags, keeping segmentation and routing labels in sync.
        param body: Request schema for the Leadping API lead tag update request, including the fields clients can send.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LeadResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.lead_response import LeadResponse

        return await self.request_adapter.send_async(request_info, LeadResponse, error_mapping)
    
    def to_post_request_information(self,body: LeadTagsRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Adds one or more current-business tags to a lead so users can segment, filter, route, and review follow-up work.
        param body: Request schema for the Leadping API lead tag update request, including the fields clients can send.
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
    
    def to_put_request_information(self,body: LeadTagsRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Replaces all tags on a lead with the supplied current-business tags, keeping segmentation and routing labels in sync.
        param body: Request schema for the Leadping API lead tag update request, including the fields clients can send.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> TagsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TagsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TagsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TagsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TagsRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

