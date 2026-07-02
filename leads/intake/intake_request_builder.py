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
    from ...models.lead_intake_request import LeadIntakeRequest
    from ...models.lead_response import LeadResponse
    from ...models.problem_details import ProblemDetails

class IntakeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /leads/intake
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IntakeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/leads/intake{?Address1*,Address2*,BirthDate*,City*,DateOfBirth*,DirectPostPrice*,Email*,ExternalId*,FirstName*,Gender*,LandingPage*,LastName*,Phone*,PhoneType*,PostalCode*,Price*,Product*,Referrer*,SellerLeadId*,SellerLeadIdentifier*,SourceMetadata*,State*,SubId*,TagIds*,TagNames*,TrustedFormUrl*,UtmCampaign*,UtmContent*,UtmMedium*,UtmSource*,UtmTerm*,Vertical*,Zip*,sourceKey*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[IntakeRequestBuilderGetQueryParameters]] = None) -> Optional[LeadResponse]:
        """
        Creates a source-authenticated lead from query parameters, supporting simple form posts, tracking metadata, and follow-up automation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LeadResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "401": ProblemDetails,
            "403": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.lead_response import LeadResponse

        return await self.request_adapter.send_async(request_info, LeadResponse, error_mapping)
    
    async def post(self,body: LeadIntakeRequest, request_configuration: Optional[RequestConfiguration[IntakeRequestBuilderPostQueryParameters]] = None) -> Optional[LeadResponse]:
        """
        Creates a source-authenticated lead from a flat intake payload, capturing contact fields, metadata, and automation-ready lead details.
        param body: Request schema for the Leadping API lead intake request, including the fields clients can send.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LeadResponse]
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
            "403": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.lead_response import LeadResponse

        return await self.request_adapter.send_async(request_info, LeadResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[IntakeRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Creates a source-authenticated lead from query parameters, supporting simple form posts, tracking metadata, and follow-up automation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: LeadIntakeRequest, request_configuration: Optional[RequestConfiguration[IntakeRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Creates a source-authenticated lead from a flat intake payload, capturing contact fields, metadata, and automation-ready lead details.
        param body: Request schema for the Leadping API lead intake request, including the fields clients can send.
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
    
    def with_url(self,raw_url: str) -> IntakeRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IntakeRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IntakeRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class IntakeRequestBuilderGetQueryParameters():
        """
        Creates a source-authenticated lead from query parameters, supporting simple form posts, tracking metadata, and follow-up automation.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "address1":
                return "Address1"
            if original_name == "address2":
                return "Address2"
            if original_name == "birth_date":
                return "BirthDate"
            if original_name == "city":
                return "City"
            if original_name == "date_of_birth":
                return "DateOfBirth"
            if original_name == "direct_post_price":
                return "DirectPostPrice"
            if original_name == "email":
                return "Email"
            if original_name == "external_id":
                return "ExternalId"
            if original_name == "first_name":
                return "FirstName"
            if original_name == "gender":
                return "Gender"
            if original_name == "landing_page":
                return "LandingPage"
            if original_name == "last_name":
                return "LastName"
            if original_name == "phone":
                return "Phone"
            if original_name == "phone_type":
                return "PhoneType"
            if original_name == "postal_code":
                return "PostalCode"
            if original_name == "price":
                return "Price"
            if original_name == "product":
                return "Product"
            if original_name == "referrer":
                return "Referrer"
            if original_name == "seller_lead_id":
                return "SellerLeadId"
            if original_name == "seller_lead_identifier":
                return "SellerLeadIdentifier"
            if original_name == "source_key":
                return "sourceKey"
            if original_name == "source_metadata":
                return "SourceMetadata"
            if original_name == "state":
                return "State"
            if original_name == "sub_id":
                return "SubId"
            if original_name == "tag_ids":
                return "TagIds"
            if original_name == "tag_names":
                return "TagNames"
            if original_name == "trusted_form_url":
                return "TrustedFormUrl"
            if original_name == "utm_campaign":
                return "UtmCampaign"
            if original_name == "utm_content":
                return "UtmContent"
            if original_name == "utm_medium":
                return "UtmMedium"
            if original_name == "utm_source":
                return "UtmSource"
            if original_name == "utm_term":
                return "UtmTerm"
            if original_name == "vertical":
                return "Vertical"
            if original_name == "zip":
                return "Zip"
            return original_name
        
        # First street address line submitted by the lead intake source.
        address1: Optional[str] = None

        # Second street address line submitted by the lead intake source.
        address2: Optional[str] = None

        # Lead birth date used for demographic matching and insurance intake workflows.
        birth_date: Optional[datetime.date] = None

        # City for the lead or business postal address.
        city: Optional[str] = None

        # Lead date of birth supplied by intake sources and normalized into the lead profile.
        date_of_birth: Optional[datetime.date] = None

        # Direct-post price supplied by the lead source during intake.
        direct_post_price: Optional[float] = None

        # Email address for the person represented by this lead intake request.
        email: Optional[str] = None

        # External system identifier used to reconcile this lead intake request across integrations.
        external_id: Optional[str] = None

        # First name of the lead, user, or contact represented by this lead intake request.
        first_name: Optional[str] = None

        # Lead gender supplied by intake sources and normalized when possible.
        gender: Optional[str] = None

        # Landing page URL where the lead submitted their information.
        landing_page: Optional[str] = None

        # Last name of the lead, user, or contact represented by this lead intake request.
        last_name: Optional[str] = None

        # Phone details for the lead, user, or business represented by this lead intake request.
        phone: Optional[str] = None

        # Source-provided phone type, such as mobile, landline, or VoIP, used during lead intake normalization.
        phone_type: Optional[str] = None

        # Postal code for the lead or business address.
        postal_code: Optional[str] = None

        # Lead price or transaction price supplied to the Leadping API.
        price: Optional[float] = None

        # Product or offer associated with the lead or source.
        product: Optional[str] = None

        # Referring page or traffic source that sent the lead into Leadping.
        referrer: Optional[str] = None

        # Seller-provided lead identifier used to deduplicate and reconcile lead delivery.
        seller_lead_id: Optional[str] = None

        # Alternate seller-provided lead identifier used during intake normalization.
        seller_lead_identifier: Optional[str] = None

        # The Leadping source key supplied as a query string parameter, or omitted when supplied as Authorization: Bearer lp_src_...
        source_key: Optional[str] = None

        # Source-provided key-value metadata retained for lead attribution and integration troubleshooting.
        source_metadata: Optional[str] = None

        # State, province, or region for the lead or business postal address.
        state: Optional[str] = None

        # Affiliate or publisher sub ID captured for lead attribution.
        sub_id: Optional[str] = None

        # Tag IDs assigned to or filtered against this lead.
        tag_ids: Optional[list[str]] = None

        # Tag names assigned to this lead when matching existing tags by name.
        tag_names: Optional[list[str]] = None

        # TrustedForm certificate URL used as proof of consumer consent.
        trusted_form_url: Optional[str] = None

        # UTM campaign parameter captured for lead attribution reporting.
        utm_campaign: Optional[str] = None

        # UTM content parameter captured for lead attribution reporting.
        utm_content: Optional[str] = None

        # UTM medium parameter captured for lead attribution reporting.
        utm_medium: Optional[str] = None

        # UTM source parameter captured for lead attribution reporting.
        utm_source: Optional[str] = None

        # UTM term parameter captured for lead attribution reporting.
        utm_term: Optional[str] = None

        # Industry vertical used for lead routing, compliance review, and reporting.
        vertical: Optional[str] = None

        # ZIP code submitted by the lead intake source.
        zip: Optional[str] = None

    
    @dataclass
    class IntakeRequestBuilderGetRequestConfiguration(RequestConfiguration[IntakeRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class IntakeRequestBuilderPostQueryParameters():
        """
        Creates a source-authenticated lead from a flat intake payload, capturing contact fields, metadata, and automation-ready lead details.
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
        
        # The Leadping source key supplied as a query string parameter, or omitted when supplied as Authorization: Bearer lp_src_...
        source_key: Optional[str] = None

    
    @dataclass
    class IntakeRequestBuilderPostRequestConfiguration(RequestConfiguration[IntakeRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

