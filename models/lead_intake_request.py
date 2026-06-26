from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_intake_request_source_metadata import LeadIntakeRequest_sourceMetadata

@dataclass
class LeadIntakeRequest(AdditionalDataHolder, Parsable):
    """
    Request schema for the Leadping API lead intake request, including the fields clients can send.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

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
    # Product or offer associated with the lead or source.
    product: Optional[str] = None
    # Referring page or traffic source that sent the lead into Leadping.
    referrer: Optional[str] = None
    # Seller-provided lead identifier used to deduplicate and reconcile lead delivery.
    seller_lead_id: Optional[str] = None
    # Alternate seller-provided lead identifier used during intake normalization.
    seller_lead_identifier: Optional[str] = None
    # Source-provided key-value metadata retained for lead attribution and integration troubleshooting.
    source_metadata: Optional[LeadIntakeRequest_sourceMetadata] = None
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
        from .lead_intake_request_source_metadata import LeadIntakeRequest_sourceMetadata

        from .lead_intake_request_source_metadata import LeadIntakeRequest_sourceMetadata

        fields: dict[str, Callable[[Any], None]] = {
            "address1": lambda n : setattr(self, 'address1', n.get_str_value()),
            "address2": lambda n : setattr(self, 'address2', n.get_str_value()),
            "birthDate": lambda n : setattr(self, 'birth_date', n.get_date_value()),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "dateOfBirth": lambda n : setattr(self, 'date_of_birth', n.get_date_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "gender": lambda n : setattr(self, 'gender', n.get_str_value()),
            "landingPage": lambda n : setattr(self, 'landing_page', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "phoneType": lambda n : setattr(self, 'phone_type', n.get_str_value()),
            "postalCode": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "product": lambda n : setattr(self, 'product', n.get_str_value()),
            "referrer": lambda n : setattr(self, 'referrer', n.get_str_value()),
            "sellerLeadId": lambda n : setattr(self, 'seller_lead_id', n.get_str_value()),
            "sellerLeadIdentifier": lambda n : setattr(self, 'seller_lead_identifier', n.get_str_value()),
            "sourceMetadata": lambda n : setattr(self, 'source_metadata', n.get_object_value(LeadIntakeRequest_sourceMetadata)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "subId": lambda n : setattr(self, 'sub_id', n.get_str_value()),
            "tagIds": lambda n : setattr(self, 'tag_ids', n.get_collection_of_primitive_values(str)),
            "tagNames": lambda n : setattr(self, 'tag_names', n.get_collection_of_primitive_values(str)),
            "trustedFormUrl": lambda n : setattr(self, 'trusted_form_url', n.get_str_value()),
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
        writer.write_str_value("city", self.city)
        writer.write_date_value("dateOfBirth", self.date_of_birth)
        writer.write_str_value("email", self.email)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("gender", self.gender)
        writer.write_str_value("landingPage", self.landing_page)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("phoneType", self.phone_type)
        writer.write_str_value("postalCode", self.postal_code)
        writer.write_str_value("product", self.product)
        writer.write_str_value("referrer", self.referrer)
        writer.write_str_value("sellerLeadId", self.seller_lead_id)
        writer.write_str_value("sellerLeadIdentifier", self.seller_lead_identifier)
        writer.write_object_value("sourceMetadata", self.source_metadata)
        writer.write_str_value("state", self.state)
        writer.write_str_value("subId", self.sub_id)
        writer.write_collection_of_primitive_values("tagIds", self.tag_ids)
        writer.write_collection_of_primitive_values("tagNames", self.tag_names)
        writer.write_str_value("trustedFormUrl", self.trusted_form_url)
        writer.write_str_value("utmCampaign", self.utm_campaign)
        writer.write_str_value("utmContent", self.utm_content)
        writer.write_str_value("utmMedium", self.utm_medium)
        writer.write_str_value("utmSource", self.utm_source)
        writer.write_str_value("utmTerm", self.utm_term)
        writer.write_str_value("vertical", self.vertical)
        writer.write_str_value("zip", self.zip)
        writer.write_additional_data_value(self.additional_data)
    

