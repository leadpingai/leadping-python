from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_contact import LeadContact
    from .lead_metadata import LeadMetadata
    from .lead_response_assigned_to import LeadResponse_assignedTo
    from .lead_response_company import LeadResponse_company
    from .lead_response_contact_preferences import LeadResponse_contactPreferences
    from .lead_response_current_lead_status import LeadResponse_currentLeadStatus
    from .lead_response_custom_fields import LeadResponse_customFields
    from .lead_response_inquiry import LeadResponse_inquiry
    from .lead_response_phone_identity import LeadResponse_phoneIdentity
    from .lead_response_processing_status import LeadResponse_processingStatus
    from .lead_response_profile import LeadResponse_profile
    from .lead_response_service_address import LeadResponse_serviceAddress
    from .tag_summary import TagSummary

@dataclass
class LeadResponse(AdditionalDataHolder, Parsable):
    """
    Describes lead data returned by Leadping.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Optional note explaining why the lead was archived.
    archive_note: Optional[str] = None
    # Defines why a lead was removed from the active working pipeline.
    archive_reason: Optional[int] = None
    # UTC timestamp when this record was archived.
    archived_at: Optional[datetime.datetime] = None
    # User ID of the person who archived this record.
    archived_by_user_id: Optional[str] = None
    # Provides a compact API reference to another resource using its stable identifier and human-readable display name.
    assigned_to: Optional[LeadResponse_assignedTo] = None
    # Leadping user currently responsible for this lead, or null when it is in the unassigned queue.
    assigned_to_user_id: Optional[str] = None
    # Business represented by a lead contact.
    company: Optional[LeadResponse_company] = None
    # Public Leadping API schema for lead contact profile data.
    contact: Optional[LeadContact] = None
    # Preferred contact language, channel, and callback windows; does not grant consent.
    contact_preferences: Optional[LeadResponse_contactPreferences] = None
    # UTC timestamp when the resource was created.
    created_at: Optional[datetime.datetime] = None
    # Summary schema for Leadping API current lead status change summary data used in dashboards and reports.
    current_lead_status: Optional[LeadResponse_currentLeadStatus] = None
    # Industry-specific JSON scalar or scalar-array answers; keys are stable field identifiers.
    custom_fields: Optional[LeadResponse_customFields] = None
    # UTC timestamp when this lead was soft deleted.
    deleted_at: Optional[datetime.datetime] = None
    # User ID of the person who soft deleted this lead.
    deleted_by_user_id: Optional[str] = None
    # Whether the lead is enabled.
    enabled: Optional[bool] = None
    # Stable unique identifier of the resource.
    id: Optional[str] = None
    # The service or purchase requested by a lead.
    inquiry: Optional[LeadResponse_inquiry] = None
    # Indicates whether the lead has been archived in Leadping.
    is_archived: Optional[bool] = None
    # The isDemo property
    is_demo: Optional[bool] = None
    # Public Leadping API schema for lead attribution metadata data.
    metadata: Optional[LeadMetadata] = None
    # UTC timestamp when the resource was last modified, or null when it has not been updated.
    modified_at: Optional[datetime.datetime] = None
    # Describes Leadping's canonical identity for a phone number, including normalization, carrier, line type, reputation, and lookup history.
    phone_identity: Optional[LeadResponse_phoneIdentity] = None
    # Defines the asynchronous verification and enrichment lifecycle for a lead.
    processing_status: Optional[LeadResponse_processingStatus] = None
    # UTC timestamp when the processing stage last changed.
    processing_status_changed_at: Optional[datetime.datetime] = None
    # Explanation when asynchronous lead processing is blocked or fails.
    processing_status_reason: Optional[str] = None
    # Public Leadping API schema for lead demographic profile data.
    profile: Optional[LeadResponse_profile] = None
    # Describes a physical or mailing address using international locality, administrative-area, postal-code, and country fields.
    service_address: Optional[LeadResponse_serviceAddress] = None
    # Tags currently attached to this lead, source, or record.
    tags: Optional[list[TagSummary]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lead_contact import LeadContact
        from .lead_metadata import LeadMetadata
        from .lead_response_assigned_to import LeadResponse_assignedTo
        from .lead_response_company import LeadResponse_company
        from .lead_response_contact_preferences import LeadResponse_contactPreferences
        from .lead_response_current_lead_status import LeadResponse_currentLeadStatus
        from .lead_response_custom_fields import LeadResponse_customFields
        from .lead_response_inquiry import LeadResponse_inquiry
        from .lead_response_phone_identity import LeadResponse_phoneIdentity
        from .lead_response_processing_status import LeadResponse_processingStatus
        from .lead_response_profile import LeadResponse_profile
        from .lead_response_service_address import LeadResponse_serviceAddress
        from .tag_summary import TagSummary

        from .lead_contact import LeadContact
        from .lead_metadata import LeadMetadata
        from .lead_response_assigned_to import LeadResponse_assignedTo
        from .lead_response_company import LeadResponse_company
        from .lead_response_contact_preferences import LeadResponse_contactPreferences
        from .lead_response_current_lead_status import LeadResponse_currentLeadStatus
        from .lead_response_custom_fields import LeadResponse_customFields
        from .lead_response_inquiry import LeadResponse_inquiry
        from .lead_response_phone_identity import LeadResponse_phoneIdentity
        from .lead_response_processing_status import LeadResponse_processingStatus
        from .lead_response_profile import LeadResponse_profile
        from .lead_response_service_address import LeadResponse_serviceAddress
        from .tag_summary import TagSummary

        fields: dict[str, Callable[[Any], None]] = {
            "archiveNote": lambda n : setattr(self, 'archive_note', n.get_str_value()),
            "archiveReason": lambda n : setattr(self, 'archive_reason', n.get_int_value()),
            "archivedAt": lambda n : setattr(self, 'archived_at', n.get_datetime_value()),
            "archivedByUserId": lambda n : setattr(self, 'archived_by_user_id', n.get_str_value()),
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_object_value(LeadResponse_assignedTo)),
            "assignedToUserId": lambda n : setattr(self, 'assigned_to_user_id', n.get_str_value()),
            "company": lambda n : setattr(self, 'company', n.get_object_value(LeadResponse_company)),
            "contact": lambda n : setattr(self, 'contact', n.get_object_value(LeadContact)),
            "contactPreferences": lambda n : setattr(self, 'contact_preferences', n.get_object_value(LeadResponse_contactPreferences)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "currentLeadStatus": lambda n : setattr(self, 'current_lead_status', n.get_object_value(LeadResponse_currentLeadStatus)),
            "customFields": lambda n : setattr(self, 'custom_fields', n.get_object_value(LeadResponse_customFields)),
            "deletedAt": lambda n : setattr(self, 'deleted_at', n.get_datetime_value()),
            "deletedByUserId": lambda n : setattr(self, 'deleted_by_user_id', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "inquiry": lambda n : setattr(self, 'inquiry', n.get_object_value(LeadResponse_inquiry)),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "isDemo": lambda n : setattr(self, 'is_demo', n.get_bool_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(LeadMetadata)),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "phoneIdentity": lambda n : setattr(self, 'phone_identity', n.get_object_value(LeadResponse_phoneIdentity)),
            "processingStatus": lambda n : setattr(self, 'processing_status', n.get_enum_value(LeadResponse_processingStatus)),
            "processingStatusChangedAt": lambda n : setattr(self, 'processing_status_changed_at', n.get_datetime_value()),
            "processingStatusReason": lambda n : setattr(self, 'processing_status_reason', n.get_str_value()),
            "profile": lambda n : setattr(self, 'profile', n.get_object_value(LeadResponse_profile)),
            "serviceAddress": lambda n : setattr(self, 'service_address', n.get_object_value(LeadResponse_serviceAddress)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(TagSummary)),
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
        writer.write_str_value("archiveNote", self.archive_note)
        writer.write_int_value("archiveReason", self.archive_reason)
        writer.write_datetime_value("archivedAt", self.archived_at)
        writer.write_str_value("archivedByUserId", self.archived_by_user_id)
        writer.write_object_value("assignedTo", self.assigned_to)
        writer.write_str_value("assignedToUserId", self.assigned_to_user_id)
        writer.write_object_value("company", self.company)
        writer.write_object_value("contact", self.contact)
        writer.write_object_value("contactPreferences", self.contact_preferences)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_object_value("currentLeadStatus", self.current_lead_status)
        writer.write_object_value("customFields", self.custom_fields)
        writer.write_datetime_value("deletedAt", self.deleted_at)
        writer.write_str_value("deletedByUserId", self.deleted_by_user_id)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_object_value("inquiry", self.inquiry)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_bool_value("isDemo", self.is_demo)
        writer.write_object_value("metadata", self.metadata)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_object_value("phoneIdentity", self.phone_identity)
        writer.write_enum_value("processingStatus", self.processing_status)
        writer.write_datetime_value("processingStatusChangedAt", self.processing_status_changed_at)
        writer.write_str_value("processingStatusReason", self.processing_status_reason)
        writer.write_object_value("profile", self.profile)
        writer.write_object_value("serviceAddress", self.service_address)
        writer.write_collection_of_object_values("tags", self.tags)
        writer.write_additional_data_value(self.additional_data)
    

