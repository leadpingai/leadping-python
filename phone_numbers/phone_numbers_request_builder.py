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
    from ..models.phone_number_request import PhoneNumberRequest
    from ..models.phone_number_response import PhoneNumberResponse
    from ..models.problem_details import ProblemDetails
    from .all.all_request_builder import AllRequestBuilder
    from .is_available_for_purchase.is_available_for_purchase_request_builder import IsAvailableForPurchaseRequestBuilder
    from .item.phone_number_item_request_builder import PhoneNumberItemRequestBuilder
    from .outgoing.outgoing_request_builder import OutgoingRequestBuilder
    from .search.search_request_builder import SearchRequestBuilder

class PhoneNumbersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /phone-numbers
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PhoneNumbersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/phone-numbers", path_parameters)
    
    def by_phone_number_id(self,phone_number_id: str) -> PhoneNumberItemRequestBuilder:
        """
        Gets an item from the leadping.phoneNumbers.item collection
        param phone_number_id: The phone number identifier.
        Returns: PhoneNumberItemRequestBuilder
        """
        if phone_number_id is None:
            raise TypeError("phone_number_id cannot be null.")
        from .item.phone_number_item_request_builder import PhoneNumberItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["phoneNumber%2Did"] = phone_number_id
        return PhoneNumberItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: PhoneNumberRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PhoneNumberResponse]:
        """
        Purchases or creates a phone number for the current business so it can be assigned to messaging, calls, and lead follow-up.
        param body: Request schema for the Leadping API phone number update request, including the fields clients can send.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PhoneNumberResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "500": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.phone_number_response import PhoneNumberResponse

        return await self.request_adapter.send_async(request_info, PhoneNumberResponse, error_mapping)
    
    def to_post_request_information(self,body: PhoneNumberRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Purchases or creates a phone number for the current business so it can be assigned to messaging, calls, and lead follow-up.
        param body: Request schema for the Leadping API phone number update request, including the fields clients can send.
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
    
    def with_url(self,raw_url: str) -> PhoneNumbersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PhoneNumbersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PhoneNumbersRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def all(self) -> AllRequestBuilder:
        """
        The all property
        """
        from .all.all_request_builder import AllRequestBuilder

        return AllRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_available_for_purchase(self) -> IsAvailableForPurchaseRequestBuilder:
        """
        The isAvailableForPurchase property
        """
        from .is_available_for_purchase.is_available_for_purchase_request_builder import IsAvailableForPurchaseRequestBuilder

        return IsAvailableForPurchaseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def outgoing(self) -> OutgoingRequestBuilder:
        """
        The outgoing property
        """
        from .outgoing.outgoing_request_builder import OutgoingRequestBuilder

        return OutgoingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search(self) -> SearchRequestBuilder:
        """
        The search property
        """
        from .search.search_request_builder import SearchRequestBuilder

        return SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PhoneNumbersRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

