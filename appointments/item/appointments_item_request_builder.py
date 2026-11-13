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
    from ...models.appointment_request import AppointmentRequest
    from ...models.appointment_response import AppointmentResponse
    from ...models.problem_details import ProblemDetails
    from .cancel.cancel_request_builder import CancelRequestBuilder
    from .complete.complete_request_builder import CompleteRequestBuilder
    from .dismiss.dismiss_request_builder import DismissRequestBuilder
    from .snooze.snooze_request_builder import SnoozeRequestBuilder

class AppointmentsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /appointments/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AppointmentsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/appointments/{id}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AppointmentResponse]:
        """
        Returns an appointment and its history, subject to lead and organization access.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AppointmentResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
            "403": ProblemDetails,
            "429": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.appointment_response import AppointmentResponse

        return await self.request_adapter.send_async(request_info, AppointmentResponse, error_mapping)
    
    async def put(self,body: AppointmentRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AppointmentResponse]:
        """
        Updates an appointment using the expected revision to detect concurrent changes.
        param body: Creates or reschedules an agent's callback appointment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AppointmentResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ...models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
            "403": ProblemDetails,
            "429": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.appointment_response import AppointmentResponse

        return await self.request_adapter.send_async(request_info, AppointmentResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns an appointment and its history, subject to lead and organization access.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: AppointmentRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates an appointment using the expected revision to detect concurrent changes.
        param body: Creates or reschedules an agent's callback appointment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> AppointmentsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AppointmentsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AppointmentsItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def cancel(self) -> CancelRequestBuilder:
        """
        The cancel property
        """
        from .cancel.cancel_request_builder import CancelRequestBuilder

        return CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def complete(self) -> CompleteRequestBuilder:
        """
        The complete property
        """
        from .complete.complete_request_builder import CompleteRequestBuilder

        return CompleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dismiss(self) -> DismissRequestBuilder:
        """
        The dismiss property
        """
        from .dismiss.dismiss_request_builder import DismissRequestBuilder

        return DismissRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def snooze(self) -> SnoozeRequestBuilder:
        """
        The snooze property
        """
        from .snooze.snooze_request_builder import SnoozeRequestBuilder

        return SnoozeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AppointmentsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AppointmentsItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

