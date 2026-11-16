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
    from ..models.message_template import MessageTemplate
    from ..models.message_template_request import MessageTemplateRequest
    from ..models.problem_details import ProblemDetails
    from .item.message_templates_item_request_builder import MessageTemplatesItemRequestBuilder

class MessageTemplatesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /message-templates
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MessageTemplatesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/message-templates", path_parameters)
    
    def by_id(self,id: str) -> MessageTemplatesItemRequestBuilder:
        """
        Gets an item from the leadping.messageTemplates.item collection
        param id: Unique identifier of the item
        Returns: MessageTemplatesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.message_templates_item_request_builder import MessageTemplatesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return MessageTemplatesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[list[MessageTemplate]]:
        """
        Lists organization templates, including disabled templates.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[MessageTemplate]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
            "403": ProblemDetails,
            "429": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.message_template import MessageTemplate

        return await self.request_adapter.send_collection_async(request_info, MessageTemplate, error_mapping)
    
    async def post(self,body: MessageTemplateRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[MessageTemplate]:
        """
        Creates a disabled organization template.
        param body: The editable fields of an organization message template.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MessageTemplate]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
            "403": ProblemDetails,
            "429": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.message_template import MessageTemplate

        return await self.request_adapter.send_async(request_info, MessageTemplate, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Lists organization templates, including disabled templates.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def to_post_request_information(self,body: MessageTemplateRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a disabled organization template.
        param body: The editable fields of an organization message template.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> MessageTemplatesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MessageTemplatesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MessageTemplatesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MessageTemplatesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MessageTemplatesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

