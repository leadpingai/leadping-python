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
    from ...models.business_request import BusinessRequest
    from ...models.business_response import BusinessResponse
    from ...models.problem_details import ProblemDetails
    from .invitations.invitations_request_builder import InvitationsRequestBuilder
    from .one_zerodlc.one_zerodlc_request_builder import OneZerodlcRequestBuilder
    from .options.options_request_builder import OptionsRequestBuilder
    from .switch.switch_request_builder import SwitchRequestBuilder
    from .users.users_request_builder import UsersRequestBuilder

class MeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /businesses/me
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/businesses/me", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[BusinessResponse]:
        """
        Returns the authenticated user's current business profile, including account settings, billing context, and communication configuration.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BusinessResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.business_response import BusinessResponse

        return await self.request_adapter.send_async(request_info, BusinessResponse, error_mapping)
    
    async def post(self,body: BusinessRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[BusinessResponse]:
        """
        Creates a business account for the authenticated user, assigns them as its owner, and makes it their active business context.
        param body: Request schema for the Leadping API business profile request, including the fields clients can send.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BusinessResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "401": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.business_response import BusinessResponse

        return await self.request_adapter.send_async(request_info, BusinessResponse, error_mapping)
    
    async def put(self,body: BusinessRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[BusinessResponse]:
        """
        Updates the authenticated user's current business profile, including contact, settings, and communication configuration.
        param body: Request schema for the Leadping API business profile request, including the fields clients can send.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BusinessResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ...models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "401": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.business_response import BusinessResponse

        return await self.request_adapter.send_async(request_info, BusinessResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the authenticated user's current business profile, including account settings, billing context, and communication configuration.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: BusinessRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a business account for the authenticated user, assigns them as its owner, and makes it their active business context.
        param body: Request schema for the Leadping API business profile request, including the fields clients can send.
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
    
    def to_put_request_information(self,body: BusinessRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates the authenticated user's current business profile, including contact, settings, and communication configuration.
        param body: Request schema for the Leadping API business profile request, including the fields clients can send.
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
    
    def with_url(self,raw_url: str) -> MeRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MeRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MeRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def invitations(self) -> InvitationsRequestBuilder:
        """
        The invitations property
        """
        from .invitations.invitations_request_builder import InvitationsRequestBuilder

        return InvitationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def one_zerodlc(self) -> OneZerodlcRequestBuilder:
        """
        The OneZerodlc property
        """
        from .one_zerodlc.one_zerodlc_request_builder import OneZerodlcRequestBuilder

        return OneZerodlcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def options_path(self) -> OptionsRequestBuilder:
        """
        The optionsPath property
        """
        from .options.options_request_builder import OptionsRequestBuilder

        return OptionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def switch(self) -> SwitchRequestBuilder:
        """
        The switch property
        """
        from .switch.switch_request_builder import SwitchRequestBuilder

        return SwitchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> UsersRequestBuilder:
        """
        The users property
        """
        from .users.users_request_builder import UsersRequestBuilder

        return UsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MeRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MeRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MeRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

