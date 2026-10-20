from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_contact import LeadContact
    from .lead_metadata import LeadMetadata
    from .lead_request_company import LeadRequest_company
    from .lead_request_contact_preferences import LeadRequest_contactPreferences
    from .lead_request_custom_fields import LeadRequest_customFields
    from .lead_request_inquiry import LeadRequest_inquiry
    from .lead_request_profile import LeadRequest_profile
    from .lead_request_service_address import LeadRequest_serviceAddress

@dataclass
class LeadRequest(AdditionalDataHolder, Parsable):
    """
    Defines the fields clients can send when working with lead.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Business represented by a lead contact.
    company: Optional[LeadRequest_company] = None
    # Public Leadping API schema for lead contact profile data.
    contact: Optional[LeadContact] = None
    # Preferred contact language, channel, and callback windows; does not grant consent.
    contact_preferences: Optional[LeadRequest_contactPreferences] = None
    # Industry-specific JSON scalar or scalar-array answers; keys are stable field identifiers.
    custom_fields: Optional[LeadRequest_customFields] = None
    # Whether the lead is enabled.
    enabled: Optional[bool] = None
    # Stable unique identifier of an existing resource to update; omit it when the API assigns an identifier during creation.
    id: Optional[str] = None
    # The service or purchase requested by a lead.
    inquiry: Optional[LeadRequest_inquiry] = None
    # Public Leadping API schema for lead attribution metadata data.
    metadata: Optional[LeadMetadata] = None
    # Public Leadping API schema for lead demographic profile data.
    profile: Optional[LeadRequest_profile] = None
    # Describes a physical or mailing address using international locality, administrative-area, postal-code, and country fields.
    service_address: Optional[LeadRequest_serviceAddress] = None
    # Optional tag IDs assigned to this lead. Defaults to an empty list when omitted.
    tag_ids: Optional[list[str]] = None
    # Optional tag names matched against existing tags. Defaults to an empty list when omitted.
    tag_names: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lead_contact import LeadContact
        from .lead_metadata import LeadMetadata
        from .lead_request_company import LeadRequest_company
        from .lead_request_contact_preferences import LeadRequest_contactPreferences
        from .lead_request_custom_fields import LeadRequest_customFields
        from .lead_request_inquiry import LeadRequest_inquiry
        from .lead_request_profile import LeadRequest_profile
        from .lead_request_service_address import LeadRequest_serviceAddress

        from .lead_contact import LeadContact
        from .lead_metadata import LeadMetadata
        from .lead_request_company import LeadRequest_company
        from .lead_request_contact_preferences import LeadRequest_contactPreferences
        from .lead_request_custom_fields import LeadRequest_customFields
        from .lead_request_inquiry import LeadRequest_inquiry
        from .lead_request_profile import LeadRequest_profile
        from .lead_request_service_address import LeadRequest_serviceAddress

        fields: dict[str, Callable[[Any], None]] = {
            "company": lambda n : setattr(self, 'company', n.get_object_value(LeadRequest_company)),
            "contact": lambda n : setattr(self, 'contact', n.get_object_value(LeadContact)),
            "contactPreferences": lambda n : setattr(self, 'contact_preferences', n.get_object_value(LeadRequest_contactPreferences)),
            "customFields": lambda n : setattr(self, 'custom_fields', n.get_object_value(LeadRequest_customFields)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "inquiry": lambda n : setattr(self, 'inquiry', n.get_object_value(LeadRequest_inquiry)),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(LeadMetadata)),
            "profile": lambda n : setattr(self, 'profile', n.get_object_value(LeadRequest_profile)),
            "serviceAddress": lambda n : setattr(self, 'service_address', n.get_object_value(LeadRequest_serviceAddress)),
            "tagIds": lambda n : setattr(self, 'tag_ids', n.get_collection_of_primitive_values(str)),
            "tagNames": lambda n : setattr(self, 'tag_names', n.get_collection_of_primitive_values(str)),
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
        writer.write_object_value("company", self.company)
        writer.write_object_value("contact", self.contact)
        writer.write_object_value("contactPreferences", self.contact_preferences)
        writer.write_object_value("customFields", self.custom_fields)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_object_value("inquiry", self.inquiry)
        writer.write_object_value("metadata", self.metadata)
        writer.write_object_value("profile", self.profile)
        writer.write_object_value("serviceAddress", self.service_address)
        writer.write_collection_of_primitive_values("tagIds", self.tag_ids)
        writer.write_collection_of_primitive_values("tagNames", self.tag_names)
        writer.write_additional_data_value(self.additional_data)
    

