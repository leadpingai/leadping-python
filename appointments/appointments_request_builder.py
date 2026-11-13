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
    from ..models.appointment_request import AppointmentRequest
    from ..models.appointment_response import AppointmentResponse
    from ..models.problem_details import ProblemDetails
    from .item.appointments_item_request_builder import AppointmentsItemRequestBuilder

class AppointmentsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /appointments
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AppointmentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/appointments{?adminMode*,dueOnly*,includeClosed*,leadId*}", path_parameters)
    
    def by_id(self,id: str) -> AppointmentsItemRequestBuilder:
        """
        Gets an item from the leadping.appointments.item collection
        param id: The appointment identifier.
        Returns: AppointmentsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.appointments_item_request_builder import AppointmentsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return AppointmentsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AppointmentsRequestBuilderGetQueryParameters]] = None) -> Optional[list[AppointmentResponse]]:
        """
        Returns appointments visible to the current user, with optional lead, reminder, and status filters.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[AppointmentResponse]]
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
        from ..models.appointment_response import AppointmentResponse

        return await self.request_adapter.send_collection_async(request_info, AppointmentResponse, error_mapping)
    
    async def post(self,body: AppointmentRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AppointmentResponse]:
        """
        Schedules a callback appointment for a lead and configures its assigned agent and reminder.
        param body: Creates or reschedules an agent's callback appointment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AppointmentResponse]
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
        from ..models.appointment_response import AppointmentResponse

        return await self.request_adapter.send_async(request_info, AppointmentResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AppointmentsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns appointments visible to the current user, with optional lead, reminder, and status filters.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def to_post_request_information(self,body: AppointmentRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Schedules a callback appointment for a lead and configures its assigned agent and reminder.
        param body: Creates or reschedules an agent's callback appointment.
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
    
    def with_url(self,raw_url: str) -> AppointmentsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AppointmentsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AppointmentsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class AppointmentsRequestBuilderGetQueryParameters():
        """
        Returns appointments visible to the current user, with optional lead, reminder, and status filters.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "admin_mode":
                return "adminMode"
            if original_name == "due_only":
                return "dueOnly"
            if original_name == "include_closed":
                return "includeClosed"
            if original_name == "lead_id":
                return "leadId"
            return original_name
        
        # Whether to browse across organizations. Requires a platform administrator; due-only results remain limited to the current agent.
        admin_mode: Optional[bool] = None

        # Whether to return only due, undismissed reminders assigned to the current agent.
        due_only: Optional[bool] = None

        # Whether to include completed and cancelled appointments. Ignored when dueOnly is true.
        include_closed: Optional[bool] = None

        # An optional lead identifier to filter appointments.
        lead_id: Optional[str] = None

    
    @dataclass
    class AppointmentsRequestBuilderGetRequestConfiguration(RequestConfiguration[AppointmentsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AppointmentsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

