from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_table_row_current_lead_status import LeadTableRow_currentLeadStatus
    from .lead_table_row_organization import LeadTableRow_organization
    from .lead_table_row_processing_status import LeadTableRow_processingStatus
    from .lead_table_row_source import LeadTableRow_source
    from .tag_summary import TagSummary

@dataclass
class LeadTableRow(AdditionalDataHolder, Parsable):
    """
    Summarizes lead data in paginated and searchable results.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Defines why a lead was removed from the active working pipeline.
    archive_reason: Optional[int] = None
    # UTC timestamp when this record was archived.
    archived_at: Optional[datetime.datetime] = None
    # User ID of the person who archived this record.
    archived_by_user_id: Optional[str] = None
    # UTC timestamp when this lead table row was created.
    created_at: Optional[datetime.datetime] = None
    # Current lead status change summary that describes the lead outcome.
    current_lead_status: Optional[LeadTableRow_currentLeadStatus] = None
    # Email address for the person represented by this lead table row.
    email: Optional[str] = None
    # Indicates whether this lead table row is active and available in the Leadping API.
    enabled: Optional[bool] = None
    # First name of the lead, user, or contact represented by this lead table row.
    first_name: Optional[str] = None
    # Unique Leadping identifier for this lead table row.
    id: Optional[str] = None
    # Whether this lead is archived.
    is_archived: Optional[bool] = None
    # Last name of the lead, user, or contact represented by this lead table row.
    last_name: Optional[str] = None
    # Identifier and display name of the related organization.
    organization: Optional[LeadTableRow_organization] = None
    # Phone details for the lead, user, or organization represented by this lead table row.
    phone: Optional[str] = None
    # Defines the asynchronous verification and enrichment lifecycle for a lead.
    processing_status: Optional[LeadTableRow_processingStatus] = None
    # UTC timestamp when the processing stage last changed.
    processing_status_changed_at: Optional[datetime.datetime] = None
    # Explanation when asynchronous lead processing is blocked or fails.
    processing_status_reason: Optional[str] = None
    # Identifier and display name of the related source.
    source: Optional[LeadTableRow_source] = None
    # Current lifecycle status for this lead table row in the Leadping API.
    status: Optional[str] = None
    # Presentation tone that helps clients style the current status of this lead table row.
    status_tone: Optional[str] = None
    # Tags currently attached to this lead, source, or record.
    tags: Optional[list[TagSummary]] = None
    # UTC timestamp when this lead table row was last updated.
    updated_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadTableRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadTableRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadTableRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lead_table_row_current_lead_status import LeadTableRow_currentLeadStatus
        from .lead_table_row_organization import LeadTableRow_organization
        from .lead_table_row_processing_status import LeadTableRow_processingStatus
        from .lead_table_row_source import LeadTableRow_source
        from .tag_summary import TagSummary

        from .lead_table_row_current_lead_status import LeadTableRow_currentLeadStatus
        from .lead_table_row_organization import LeadTableRow_organization
        from .lead_table_row_processing_status import LeadTableRow_processingStatus
        from .lead_table_row_source import LeadTableRow_source
        from .tag_summary import TagSummary

        fields: dict[str, Callable[[Any], None]] = {
            "archiveReason": lambda n : setattr(self, 'archive_reason', n.get_int_value()),
            "archivedAt": lambda n : setattr(self, 'archived_at', n.get_datetime_value()),
            "archivedByUserId": lambda n : setattr(self, 'archived_by_user_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "currentLeadStatus": lambda n : setattr(self, 'current_lead_status', n.get_object_value(LeadTableRow_currentLeadStatus)),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_object_value(LeadTableRow_organization)),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "processingStatus": lambda n : setattr(self, 'processing_status', n.get_enum_value(LeadTableRow_processingStatus)),
            "processingStatusChangedAt": lambda n : setattr(self, 'processing_status_changed_at', n.get_datetime_value()),
            "processingStatusReason": lambda n : setattr(self, 'processing_status_reason', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_object_value(LeadTableRow_source)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "statusTone": lambda n : setattr(self, 'status_tone', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(TagSummary)),
            "updatedAt": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
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
        writer.write_int_value("archiveReason", self.archive_reason)
        writer.write_datetime_value("archivedAt", self.archived_at)
        writer.write_str_value("archivedByUserId", self.archived_by_user_id)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_object_value("currentLeadStatus", self.current_lead_status)
        writer.write_str_value("email", self.email)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_str_value("lastName", self.last_name)
        writer.write_object_value("organization", self.organization)
        writer.write_str_value("phone", self.phone)
        writer.write_enum_value("processingStatus", self.processing_status)
        writer.write_datetime_value("processingStatusChangedAt", self.processing_status_changed_at)
        writer.write_str_value("processingStatusReason", self.processing_status_reason)
        writer.write_object_value("source", self.source)
        writer.write_str_value("status", self.status)
        writer.write_str_value("statusTone", self.status_tone)
        writer.write_collection_of_object_values("tags", self.tags)
        writer.write_datetime_value("updatedAt", self.updated_at)
        writer.write_additional_data_value(self.additional_data)
    

