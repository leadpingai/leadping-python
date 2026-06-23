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
    Metadata related to the origin, context, and attribution of a submitted lead.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The assigned phone number ID associated with this lead metadata.
    assigned_phone_number_id: Optional[str] = None
    # The business ID associated with this lead metadata.
    business_id: Optional[str] = None
    # The human-readable compliance blocked reason explaining this lead metadata.
    compliance_blocked_reason: Optional[str] = None
    # The current compliance status for this lead metadata.
    compliance_status: Optional[str] = None
    # The date and time for the created at value on this lead metadata.
    created_at: Optional[datetime.datetime] = None
    # The external ID associated with this lead metadata.
    external_id: Optional[str] = None
    # The import batch ID associated with this lead.
    import_batch_id: Optional[str] = None
    # The IP address value for this lead metadata.
    ip_address: Optional[str] = None
    # Whether the lead was imported rather than received as a fresh inbound lead.
    is_imported: Optional[bool] = None
    # The landing page value for this lead metadata.
    landing_page: Optional[str] = None
    # The lead origin used by outbound pacing and automation safeguards.
    origin: Optional[str] = None
    # The product value for this lead metadata.
    product: Optional[str] = None
    # The pub ID associated with this lead metadata.
    pub_id: Optional[str] = None
    # The referrer value for this lead metadata.
    referrer: Optional[str] = None
    # The seller lead ID associated with this lead metadata.
    seller_lead_id: Optional[str] = None
    # The SMS consent phone number value for this lead metadata.
    sms_consent_phone_number: Optional[str] = None
    # The current SMS consent status for this lead metadata.
    sms_consent_status: Optional[str] = None
    # The date and time for the SMS help requested at value on this lead metadata.
    sms_help_requested_at: Optional[datetime.datetime] = None
    # The date and time for the SMS opt in at value on this lead metadata.
    sms_opt_in_at: Optional[datetime.datetime] = None
    # The date and time for the SMS opt out at value on this lead metadata.
    sms_opt_out_at: Optional[datetime.datetime] = None
    # Whether SMS opted out applies to this lead metadata.
    sms_opted_out: Optional[bool] = None
    # The source metadata key-value data carried with this lead metadata; values must be safe to expose in API responses.
    source_metadata: Optional[LeadMetadata_sourceMetadata] = None
    # The sub ID associated with this lead metadata.
    sub_id: Optional[str] = None
    # The URL associated with this lead metadata.
    trusted_form_url: Optional[str] = None
    # The user agent value for this lead metadata.
    user_agent: Optional[str] = None
    # The user ID associated with this lead metadata.
    user_id: Optional[str] = None
    # The utm campaign value for this lead metadata.
    utm_campaign: Optional[str] = None
    # The utm content value for this lead metadata.
    utm_content: Optional[str] = None
    # The utm medium value for this lead metadata.
    utm_medium: Optional[str] = None
    # The utm source value for this lead metadata.
    utm_source: Optional[str] = None
    # The utm term value for this lead metadata.
    utm_term: Optional[str] = None
    # The vertical value for this lead metadata.
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
    

