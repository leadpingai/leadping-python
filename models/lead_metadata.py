from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_metadata_source_metadata import LeadMetadata_sourceMetadata

@dataclass
class LeadMetadata(AdditionalDataHolder, Parsable):
    """
    Public Leadping API schema for lead attribution metadata data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Phone number ID assigned to the lead, business, or source.
    assigned_phone_number_id: Optional[str] = None
    # Business ID that owns this lead's attribution metadata.
    business_id: Optional[str] = None
    # Reason Leadping blocked this operation for compliance.
    compliance_blocked_reason: Optional[str] = None
    # Compliance status used to decide whether Leadping can send messages.
    compliance_status: Optional[str] = None
    # UTC timestamp when this lead attribution metadata was created.
    created_at: Optional[datetime.datetime] = None
    # External system identifier used to reconcile this lead attribution metadata across integrations.
    external_id: Optional[str] = None
    # Bulk import batch ID that created or updated this lead.
    import_batch_id: Optional[str] = None
    # IP address captured with the request for audit and compliance review.
    ip_address: Optional[str] = None
    # Indicates whether this lead was imported rather than captured through a live source.
    is_imported: Optional[bool] = None
    # Landing page URL where the lead submitted their information.
    landing_page: Optional[str] = None
    # System or workflow that created this event.
    origin: Optional[str] = None
    # Product or offer associated with the lead or source.
    product: Optional[str] = None
    # Publisher ID supplied by the lead source for attribution.
    pub_id: Optional[str] = None
    # Referring page or traffic source that sent the lead into Leadping.
    referrer: Optional[str] = None
    # Seller-provided lead identifier used to deduplicate and reconcile lead delivery.
    seller_lead_id: Optional[str] = None
    # Phone number where SMS consent was captured or evaluated.
    sms_consent_phone_number: Optional[str] = None
    # Current SMS consent status recorded for this lead.
    sms_consent_status: Optional[str] = None
    # UTC timestamp when the lead requested SMS help instructions.
    sms_help_requested_at: Optional[datetime.datetime] = None
    # UTC timestamp when the lead opted in to SMS communication.
    sms_opt_in_at: Optional[datetime.datetime] = None
    # UTC timestamp when the lead opted out of SMS communication.
    sms_opt_out_at: Optional[datetime.datetime] = None
    # Indicates whether the lead has opted out of SMS communication.
    sms_opted_out: Optional[bool] = None
    # Source-provided key-value metadata retained for lead attribution and integration troubleshooting.
    source_metadata: Optional[LeadMetadata_sourceMetadata] = None
    # Affiliate or publisher sub ID captured for lead attribution.
    sub_id: Optional[str] = None
    # TrustedForm certificate URL used as proof of consumer consent.
    trusted_form_url: Optional[str] = None
    # Browser or client user agent captured when this lead attribution metadata was submitted.
    user_agent: Optional[str] = None
    # User ID associated with this lead's attribution metadata.
    user_id: Optional[str] = None
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lead_metadata_source_metadata import LeadMetadata_sourceMetadata

        from .lead_metadata_source_metadata import LeadMetadata_sourceMetadata

        fields: dict[str, Callable[[Any], None]] = {
            "assignedPhoneNumberId": lambda n : setattr(self, 'assigned_phone_number_id', n.get_str_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "complianceBlockedReason": lambda n : setattr(self, 'compliance_blocked_reason', n.get_str_value()),
            "complianceStatus": lambda n : setattr(self, 'compliance_status', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "importBatchId": lambda n : setattr(self, 'import_batch_id', n.get_str_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "isImported": lambda n : setattr(self, 'is_imported', n.get_bool_value()),
            "landingPage": lambda n : setattr(self, 'landing_page', n.get_str_value()),
            "origin": lambda n : setattr(self, 'origin', n.get_str_value()),
            "product": lambda n : setattr(self, 'product', n.get_str_value()),
            "pubId": lambda n : setattr(self, 'pub_id', n.get_str_value()),
            "referrer": lambda n : setattr(self, 'referrer', n.get_str_value()),
            "sellerLeadId": lambda n : setattr(self, 'seller_lead_id', n.get_str_value()),
            "smsConsentPhoneNumber": lambda n : setattr(self, 'sms_consent_phone_number', n.get_str_value()),
            "smsConsentStatus": lambda n : setattr(self, 'sms_consent_status', n.get_str_value()),
            "smsHelpRequestedAt": lambda n : setattr(self, 'sms_help_requested_at', n.get_datetime_value()),
            "smsOptInAt": lambda n : setattr(self, 'sms_opt_in_at', n.get_datetime_value()),
            "smsOptOutAt": lambda n : setattr(self, 'sms_opt_out_at', n.get_datetime_value()),
            "smsOptedOut": lambda n : setattr(self, 'sms_opted_out', n.get_bool_value()),
            "sourceMetadata": lambda n : setattr(self, 'source_metadata', n.get_object_value(LeadMetadata_sourceMetadata)),
            "subId": lambda n : setattr(self, 'sub_id', n.get_str_value()),
            "trustedFormUrl": lambda n : setattr(self, 'trusted_form_url', n.get_str_value()),
            "userAgent": lambda n : setattr(self, 'user_agent', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "utmCampaign": lambda n : setattr(self, 'utm_campaign', n.get_str_value()),
            "utmContent": lambda n : setattr(self, 'utm_content', n.get_str_value()),
            "utmMedium": lambda n : setattr(self, 'utm_medium', n.get_str_value()),
            "utmSource": lambda n : setattr(self, 'utm_source', n.get_str_value()),
            "utmTerm": lambda n : setattr(self, 'utm_term', n.get_str_value()),
            "vertical": lambda n : setattr(self, 'vertical', n.get_str_value()),
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
        writer.write_str_value("assignedPhoneNumberId", self.assigned_phone_number_id)
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("complianceBlockedReason", self.compliance_blocked_reason)
        writer.write_str_value("complianceStatus", self.compliance_status)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("importBatchId", self.import_batch_id)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_bool_value("isImported", self.is_imported)
        writer.write_str_value("landingPage", self.landing_page)
        writer.write_str_value("origin", self.origin)
        writer.write_str_value("product", self.product)
        writer.write_str_value("pubId", self.pub_id)
        writer.write_str_value("referrer", self.referrer)
        writer.write_str_value("sellerLeadId", self.seller_lead_id)
        writer.write_str_value("smsConsentPhoneNumber", self.sms_consent_phone_number)
        writer.write_str_value("smsConsentStatus", self.sms_consent_status)
        writer.write_datetime_value("smsHelpRequestedAt", self.sms_help_requested_at)
        writer.write_datetime_value("smsOptInAt", self.sms_opt_in_at)
        writer.write_datetime_value("smsOptOutAt", self.sms_opt_out_at)
        writer.write_bool_value("smsOptedOut", self.sms_opted_out)
        writer.write_object_value("sourceMetadata", self.source_metadata)
        writer.write_str_value("subId", self.sub_id)
        writer.write_str_value("trustedFormUrl", self.trusted_form_url)
        writer.write_str_value("userAgent", self.user_agent)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("utmCampaign", self.utm_campaign)
        writer.write_str_value("utmContent", self.utm_content)
        writer.write_str_value("utmMedium", self.utm_medium)
        writer.write_str_value("utmSource", self.utm_source)
        writer.write_str_value("utmTerm", self.utm_term)
        writer.write_str_value("vertical", self.vertical)
        writer.write_additional_data_value(self.additional_data)
    

