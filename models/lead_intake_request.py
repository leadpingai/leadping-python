from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_intake_request_company import LeadIntakeRequest_company
    from .lead_intake_request_consent_certificate_type import LeadIntakeRequest_consentCertificateType
    from .lead_intake_request_contact_preferences import LeadIntakeRequest_contactPreferences
    from .lead_intake_request_custom_fields import LeadIntakeRequest_customFields
    from .lead_intake_request_inquiry import LeadIntakeRequest_inquiry
    from .lead_intake_request_profile import LeadIntakeRequest_profile
    from .lead_intake_request_service_address import LeadIntakeRequest_serviceAddress
    from .lead_intake_request_source_metadata import LeadIntakeRequest_sourceMetadata

@dataclass
class LeadIntakeRequest(AdditionalDataHolder, Parsable):
    """
    Defines the fields clients can send when working with lead intake.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # First street address line submitted by the lead intake source.
    address1: Optional[str] = None
    # Second street address line submitted by the lead intake source.
    address2: Optional[str] = None
    # Lead birth date used for demographic matching and insurance intake workflows.
    birth_date: Optional[datetime.date] = None
    # Original visitor IP as reported by the source.
    capture_ip_address: Optional[str] = None
    # Original visitor user agent as reported by the source.
    capture_user_agent: Optional[str] = None
    # Original source capture timestamp.
    captured_at: Optional[datetime.datetime] = None
    # City for the lead or organization postal address.
    city: Optional[str] = None
    # Business represented by a lead contact.
    company: Optional[LeadIntakeRequest_company] = None
    # The provider responsible for a lead's consent certificate.
    consent_certificate_type: Optional[LeadIntakeRequest_consentCertificateType] = None
    # Certificate URL used as proof of consumer consent.
    consent_certificate_url: Optional[str] = None
    # Preferred contact language, channel, and callback windows; does not grant consent.
    contact_preferences: Optional[LeadIntakeRequest_contactPreferences] = None
    # ISO 3166-1 alpha-2 contact address country code.
    country: Optional[str] = None
    # ISO 4217 acquisition price currency.
    currency: Optional[str] = None
    # Industry-specific JSON scalar or scalar-array answers; keys are stable field identifiers.
    custom_fields: Optional[LeadIntakeRequest_customFields] = None
    # Lead date of birth supplied by intake sources and normalized into the lead profile.
    date_of_birth: Optional[datetime.date] = None
    # Alias for price. When both are supplied, their amounts must agree.
    direct_post_price: Optional[float] = None
    # Email address for the person represented by this lead intake request.
    email: Optional[str] = None
    # External system identifier used to reconcile this lead intake request across integrations.
    external_id: Optional[str] = None
    # First name of the lead, user, or contact represented by this lead intake request.
    first_name: Optional[str] = None
    # Lead gender supplied by intake sources and normalized when possible.
    gender: Optional[str] = None
    # Stable delivery key reused when retrying the same lead submission to this source.
    idempotency_key: Optional[str] = None
    # The service or purchase requested by a lead.
    inquiry: Optional[LeadIntakeRequest_inquiry] = None
    # Landing page URL where the lead submitted their information.
    landing_page: Optional[str] = None
    # Last name of the lead, user, or contact represented by this lead intake request.
    last_name: Optional[str] = None
    # Contact phone number. Use E.164 with a leading + for international numbers.
    phone: Optional[str] = None
    # Source-provided phone type, such as mobile, landline, or VoIP, used during lead intake normalization.
    phone_type: Optional[str] = None
    # Postal code for the lead or organization address.
    postal_code: Optional[str] = None
    # Lead price or transaction price supplied to the Leadping API.
    price: Optional[float] = None
    # Product or offer associated with the lead or source.
    product: Optional[str] = None
    # Public Leadping API schema for lead demographic profile data.
    profile: Optional[LeadIntakeRequest_profile] = None
    # Publisher identifier.
    pub_id: Optional[str] = None
    # Referring page or traffic source that sent the lead into Leadping.
    referrer: Optional[str] = None
    # Seller-provided lead identifier used to deduplicate and reconcile lead delivery.
    seller_lead_id: Optional[str] = None
    # Alternate seller-provided lead identifier used during intake normalization.
    seller_lead_identifier: Optional[str] = None
    # Describes a physical or mailing address using international locality, administrative-area, postal-code, and country fields.
    service_address: Optional[LeadIntakeRequest_serviceAddress] = None
    # Source-provided key-value metadata retained for lead attribution and integration troubleshooting.
    source_metadata: Optional[LeadIntakeRequest_sourceMetadata] = None
    # State, province, or region for the lead or organization postal address.
    state: Optional[str] = None
    # Affiliate or publisher sub ID captured for lead attribution.
    sub_id: Optional[str] = None
    # Tag IDs assigned to or filtered against this lead.
    tag_ids: Optional[list[str]] = None
    # Tag names assigned to this lead when matching existing tags by name.
    tag_names: Optional[list[str]] = None
    # Contact time zone identifier.
    time_zone_id: Optional[str] = None
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadIntakeRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadIntakeRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadIntakeRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lead_intake_request_company import LeadIntakeRequest_company
        from .lead_intake_request_consent_certificate_type import LeadIntakeRequest_consentCertificateType
        from .lead_intake_request_contact_preferences import LeadIntakeRequest_contactPreferences
        from .lead_intake_request_custom_fields import LeadIntakeRequest_customFields
        from .lead_intake_request_inquiry import LeadIntakeRequest_inquiry
        from .lead_intake_request_profile import LeadIntakeRequest_profile
        from .lead_intake_request_service_address import LeadIntakeRequest_serviceAddress
        from .lead_intake_request_source_metadata import LeadIntakeRequest_sourceMetadata

        from .lead_intake_request_company import LeadIntakeRequest_company
        from .lead_intake_request_consent_certificate_type import LeadIntakeRequest_consentCertificateType
        from .lead_intake_request_contact_preferences import LeadIntakeRequest_contactPreferences
        from .lead_intake_request_custom_fields import LeadIntakeRequest_customFields
        from .lead_intake_request_inquiry import LeadIntakeRequest_inquiry
        from .lead_intake_request_profile import LeadIntakeRequest_profile
        from .lead_intake_request_service_address import LeadIntakeRequest_serviceAddress
        from .lead_intake_request_source_metadata import LeadIntakeRequest_sourceMetadata

        fields: dict[str, Callable[[Any], None]] = {
            "address1": lambda n : setattr(self, 'address1', n.get_str_value()),
            "address2": lambda n : setattr(self, 'address2', n.get_str_value()),
            "birthDate": lambda n : setattr(self, 'birth_date', n.get_date_value()),
            "captureIpAddress": lambda n : setattr(self, 'capture_ip_address', n.get_str_value()),
            "captureUserAgent": lambda n : setattr(self, 'capture_user_agent', n.get_str_value()),
            "capturedAt": lambda n : setattr(self, 'captured_at', n.get_datetime_value()),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "company": lambda n : setattr(self, 'company', n.get_object_value(LeadIntakeRequest_company)),
            "consentCertificateType": lambda n : setattr(self, 'consent_certificate_type', n.get_enum_value(LeadIntakeRequest_consentCertificateType)),
            "consentCertificateUrl": lambda n : setattr(self, 'consent_certificate_url', n.get_str_value()),
            "contactPreferences": lambda n : setattr(self, 'contact_preferences', n.get_object_value(LeadIntakeRequest_contactPreferences)),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "customFields": lambda n : setattr(self, 'custom_fields', n.get_object_value(LeadIntakeRequest_customFields)),
            "dateOfBirth": lambda n : setattr(self, 'date_of_birth', n.get_date_value()),
            "directPostPrice": lambda n : setattr(self, 'direct_post_price', n.get_float_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "gender": lambda n : setattr(self, 'gender', n.get_str_value()),
            "idempotencyKey": lambda n : setattr(self, 'idempotency_key', n.get_str_value()),
            "inquiry": lambda n : setattr(self, 'inquiry', n.get_object_value(LeadIntakeRequest_inquiry)),
            "landingPage": lambda n : setattr(self, 'landing_page', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "phoneType": lambda n : setattr(self, 'phone_type', n.get_str_value()),
            "postalCode": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
            "product": lambda n : setattr(self, 'product', n.get_str_value()),
            "profile": lambda n : setattr(self, 'profile', n.get_object_value(LeadIntakeRequest_profile)),
            "pubId": lambda n : setattr(self, 'pub_id', n.get_str_value()),
            "referrer": lambda n : setattr(self, 'referrer', n.get_str_value()),
            "sellerLeadId": lambda n : setattr(self, 'seller_lead_id', n.get_str_value()),
            "sellerLeadIdentifier": lambda n : setattr(self, 'seller_lead_identifier', n.get_str_value()),
            "serviceAddress": lambda n : setattr(self, 'service_address', n.get_object_value(LeadIntakeRequest_serviceAddress)),
            "sourceMetadata": lambda n : setattr(self, 'source_metadata', n.get_object_value(LeadIntakeRequest_sourceMetadata)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "subId": lambda n : setattr(self, 'sub_id', n.get_str_value()),
            "tagIds": lambda n : setattr(self, 'tag_ids', n.get_collection_of_primitive_values(str)),
            "tagNames": lambda n : setattr(self, 'tag_names', n.get_collection_of_primitive_values(str)),
            "timeZoneId": lambda n : setattr(self, 'time_zone_id', n.get_str_value()),
            "utmCampaign": lambda n : setattr(self, 'utm_campaign', n.get_str_value()),
            "utmContent": lambda n : setattr(self, 'utm_content', n.get_str_value()),
            "utmMedium": lambda n : setattr(self, 'utm_medium', n.get_str_value()),
            "utmSource": lambda n : setattr(self, 'utm_source', n.get_str_value()),
            "utmTerm": lambda n : setattr(self, 'utm_term', n.get_str_value()),
            "vertical": lambda n : setattr(self, 'vertical', n.get_str_value()),
            "zip": lambda n : setattr(self, 'zip', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("address1", self.address1)
        writer.write_str_value("address2", self.address2)
        writer.write_date_value("birthDate", self.birth_date)
        writer.write_str_value("captureIpAddress", self.capture_ip_address)
        writer.write_str_value("captureUserAgent", self.capture_user_agent)
        writer.write_datetime_value("capturedAt", self.captured_at)
        writer.write_str_value("city", self.city)
        writer.write_object_value("company", self.company)
        writer.write_enum_value("consentCertificateType", self.consent_certificate_type)
        writer.write_str_value("consentCertificateUrl", self.consent_certificate_url)
        writer.write_object_value("contactPreferences", self.contact_preferences)
        writer.write_str_value("country", self.country)
        writer.write_str_value("currency", self.currency)
        writer.write_object_value("customFields", self.custom_fields)
        writer.write_date_value("dateOfBirth", self.date_of_birth)
        writer.write_float_value("directPostPrice", self.direct_post_price)
        writer.write_str_value("email", self.email)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("gender", self.gender)
        writer.write_str_value("idempotencyKey", self.idempotency_key)
        writer.write_object_value("inquiry", self.inquiry)
        writer.write_str_value("landingPage", self.landing_page)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("phoneType", self.phone_type)
        writer.write_str_value("postalCode", self.postal_code)
        writer.write_float_value("price", self.price)
        writer.write_str_value("product", self.product)
        writer.write_object_value("profile", self.profile)
        writer.write_str_value("pubId", self.pub_id)
        writer.write_str_value("referrer", self.referrer)
        writer.write_str_value("sellerLeadId", self.seller_lead_id)
        writer.write_str_value("sellerLeadIdentifier", self.seller_lead_identifier)
        writer.write_object_value("serviceAddress", self.service_address)
        writer.write_object_value("sourceMetadata", self.source_metadata)
        writer.write_str_value("state", self.state)
        writer.write_str_value("subId", self.sub_id)
        writer.write_collection_of_primitive_values("tagIds", self.tag_ids)
        writer.write_collection_of_primitive_values("tagNames", self.tag_names)
        writer.write_str_value("timeZoneId", self.time_zone_id)
        writer.write_str_value("utmCampaign", self.utm_campaign)
        writer.write_str_value("utmContent", self.utm_content)
        writer.write_str_value("utmMedium", self.utm_medium)
        writer.write_str_value("utmSource", self.utm_source)
        writer.write_str_value("utmTerm", self.utm_term)
        writer.write_str_value("vertical", self.vertical)
        writer.write_str_value("zip", self.zip)
        writer.write_additional_data_value(self.additional_data)
    

