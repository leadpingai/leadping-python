from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TenDlcApplicationDraft(AdditionalDataHolder, Parsable):
    """
    API DTO containing ten dlc application draft data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The company name value for this 10DLC application draft.
    company_name: Optional[str] = None
    # The compliance warnings included with this 10DLC application draft.
    compliance_warnings: Optional[list[str]] = None
    # The contact email value for this 10DLC application draft.
    contact_email: Optional[str] = None
    # The contact name value for this 10DLC application draft.
    contact_name: Optional[str] = None
    # The contact phone value for this 10DLC application draft.
    contact_phone: Optional[str] = None
    # The EIN value for this 10DLC application draft.
    ein: Optional[str] = None
    # The industry value for this 10DLC application draft.
    industry: Optional[str] = None
    # The date and time for the last submitted at value on this 10DLC application draft.
    last_submitted_at: Optional[datetime.datetime] = None
    # The lead source value for this 10DLC application draft.
    lead_source: Optional[str] = None
    # The message examples included with this 10DLC application draft.
    message_examples: Optional[list[str]] = None
    # The missing fields included with this 10DLC application draft.
    missing_fields: Optional[list[str]] = None
    # The opt in language value for this 10DLC application draft.
    opt_in_language: Optional[str] = None
    # The URL associated with this 10DLC application draft.
    privacy_policy_url: Optional[str] = None
    # The human-readable rejection reason explaining this 10DLC application draft.
    rejection_reason: Optional[str] = None
    # The URL associated with this 10DLC application draft.
    terms_url: Optional[str] = None
    # Whether TrustedForm required applies to this 10DLC application draft.
    trusted_form_required: Optional[bool] = None
    # The date and time for the updated at value on this 10DLC application draft.
    updated_at: Optional[datetime.datetime] = None
    # The use case value for this 10DLC application draft.
    use_case: Optional[str] = None
    # The use case description value for this 10DLC application draft.
    use_case_description: Optional[str] = None
    # The version value for this 10DLC application draft.
    version: Optional[int] = None
    # The URL associated with this 10DLC application draft.
    website_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenDlcApplicationDraft:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenDlcApplicationDraft
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenDlcApplicationDraft()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "complianceWarnings": lambda n : setattr(self, 'compliance_warnings', n.get_collection_of_primitive_values(str)),
            "contactEmail": lambda n : setattr(self, 'contact_email', n.get_str_value()),
            "contactName": lambda n : setattr(self, 'contact_name', n.get_str_value()),
            "contactPhone": lambda n : setattr(self, 'contact_phone', n.get_str_value()),
            "ein": lambda n : setattr(self, 'ein', n.get_str_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_str_value()),
            "lastSubmittedAt": lambda n : setattr(self, 'last_submitted_at', n.get_datetime_value()),
            "leadSource": lambda n : setattr(self, 'lead_source', n.get_str_value()),
            "messageExamples": lambda n : setattr(self, 'message_examples', n.get_collection_of_primitive_values(str)),
            "missingFields": lambda n : setattr(self, 'missing_fields', n.get_collection_of_primitive_values(str)),
            "optInLanguage": lambda n : setattr(self, 'opt_in_language', n.get_str_value()),
            "privacyPolicyUrl": lambda n : setattr(self, 'privacy_policy_url', n.get_str_value()),
            "rejectionReason": lambda n : setattr(self, 'rejection_reason', n.get_str_value()),
            "termsUrl": lambda n : setattr(self, 'terms_url', n.get_str_value()),
            "trustedFormRequired": lambda n : setattr(self, 'trusted_form_required', n.get_bool_value()),
            "updatedAt": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
            "useCase": lambda n : setattr(self, 'use_case', n.get_str_value()),
            "useCaseDescription": lambda n : setattr(self, 'use_case_description', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "websiteUrl": lambda n : setattr(self, 'website_url', n.get_str_value()),
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
        writer.write_str_value("companyName", self.company_name)
        writer.write_collection_of_primitive_values("complianceWarnings", self.compliance_warnings)
        writer.write_str_value("contactEmail", self.contact_email)
        writer.write_str_value("contactName", self.contact_name)
        writer.write_str_value("contactPhone", self.contact_phone)
        writer.write_str_value("ein", self.ein)
        writer.write_str_value("industry", self.industry)
        writer.write_datetime_value("lastSubmittedAt", self.last_submitted_at)
        writer.write_str_value("leadSource", self.lead_source)
        writer.write_collection_of_primitive_values("messageExamples", self.message_examples)
        writer.write_collection_of_primitive_values("missingFields", self.missing_fields)
        writer.write_str_value("optInLanguage", self.opt_in_language)
        writer.write_str_value("privacyPolicyUrl", self.privacy_policy_url)
        writer.write_str_value("rejectionReason", self.rejection_reason)
        writer.write_str_value("termsUrl", self.terms_url)
        writer.write_bool_value("trustedFormRequired", self.trusted_form_required)
        writer.write_datetime_value("updatedAt", self.updated_at)
        writer.write_str_value("useCase", self.use_case)
        writer.write_str_value("useCaseDescription", self.use_case_description)
        writer.write_int_value("version", self.version)
        writer.write_str_value("websiteUrl", self.website_url)
        writer.write_additional_data_value(self.additional_data)
    

