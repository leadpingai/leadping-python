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
    from ..models.organization_invitation_table_row import OrganizationInvitationTableRow
    from ..models.problem_details import ProblemDetails
    from .decline.decline_request_builder import DeclineRequestBuilder
    from .item.invitations_item_request_builder import InvitationsItemRequestBuilder

class InvitationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /invitations
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InvitationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/invitations{?token*}", path_parameters)
    
    def by_id(self,id: str) -> InvitationsItemRequestBuilder:
        """
        Gets an item from the leadping.invitations.item collection
        param id: Unique identifier of the item
        Returns: InvitationsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.invitations_item_request_builder import InvitationsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return InvitationsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[InvitationsRequestBuilderGetQueryParameters]] = None) -> Optional[list[OrganizationInvitationTableRow]]:
        """
        Get
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[OrganizationInvitationTableRow]]
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
        from ..models.organization_invitation_table_row import OrganizationInvitationTableRow

        return await self.request_adapter.send_collection_async(request_info, OrganizationInvitationTableRow, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[InvitationsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> InvitationsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: InvitationsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return InvitationsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def decline(self) -> DeclineRequestBuilder:
        """
        The decline property
        """
        from .decline.decline_request_builder import DeclineRequestBuilder

        return DeclineRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class InvitationsRequestBuilderGetQueryParameters():
        """
        Get
        """
        token: Optional[str] = None

    
    @dataclass
    class InvitationsRequestBuilderGetRequestConfiguration(RequestConfiguration[InvitationsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

