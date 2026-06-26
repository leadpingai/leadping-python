from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_table_row_admin_enablement_override import LeadTableRow_adminEnablementOverride
    from .lead_table_row_current_disposition import LeadTableRow_currentDisposition
    from .tag_summary import TagSummary

@dataclass
class LeadTableRow(AdditionalDataHolder, Parsable):
    """
    List item schema for Leadping API lead table row results shown in searchable tables.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Admin override that can enable or disable this record independently of normal status checks.
    admin_enablement_override: Optional[LeadTableRow_adminEnablementOverride] = None
    # Defines why a lead was removed from the active working pipeline.
    archive_reason: Optional[int] = None
    # UTC timestamp when this record was archived.
    archived_at: Optional[datetime.datetime] = None
    # User ID of the person who archived this record.
    archived_by_user_id: Optional[str] = None
    # Business ID that owns this lead.
    business_id: Optional[str] = None
    # Business display name shown for this lead.
    business_name: Optional[str] = None
    # UTC timestamp when this lead table row was created.
    created_at: Optional[datetime.datetime] = None
    # Current disposition summary that describes the lead outcome.
    current_disposition: Optional[LeadTableRow_currentDisposition] = None
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
    # Phone details for the lead, user, or business represented by this lead table row.
    phone: Optional[str] = None
    # Lead source ID that created or supplied this lead.
    source_id: Optional[str] = None
    # Lead source display name shown for this lead.
    source_name: Optional[str] = None
    # Current lifecycle status for this lead table row in the Leadping API.
    status: Optional[str] = None
    # Presentation tone that helps clients style the current status of this lead table row.
    status_tone: Optional[str] = None
    # Tags currently attached to this lead, source, or record.
    tags: Optional[list[TagSummary]] = None
    
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
        from .lead_table_row_admin_enablement_override import LeadTableRow_adminEnablementOverride
        from .lead_table_row_current_disposition import LeadTableRow_currentDisposition
        from .tag_summary import TagSummary

        from .lead_table_row_admin_enablement_override import LeadTableRow_adminEnablementOverride
        from .lead_table_row_current_disposition import LeadTableRow_currentDisposition
        from .tag_summary import TagSummary

        fields: dict[str, Callable[[Any], None]] = {
            "adminEnablementOverride": lambda n : setattr(self, 'admin_enablement_override', n.get_object_value(LeadTableRow_adminEnablementOverride)),
            "archiveReason": lambda n : setattr(self, 'archive_reason', n.get_int_value()),
            "archivedAt": lambda n : setattr(self, 'archived_at', n.get_datetime_value()),
            "archivedByUserId": lambda n : setattr(self, 'archived_by_user_id', n.get_str_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "businessName": lambda n : setattr(self, 'business_name', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "currentDisposition": lambda n : setattr(self, 'current_disposition', n.get_object_value(LeadTableRow_currentDisposition)),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "sourceName": lambda n : setattr(self, 'source_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "statusTone": lambda n : setattr(self, 'status_tone', n.get_str_value()),
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
        writer.write_object_value("adminEnablementOverride", self.admin_enablement_override)
        writer.write_int_value("archiveReason", self.archive_reason)
        writer.write_datetime_value("archivedAt", self.archived_at)
        writer.write_str_value("archivedByUserId", self.archived_by_user_id)
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("businessName", self.business_name)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_object_value("currentDisposition", self.current_disposition)
        writer.write_str_value("email", self.email)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_str_value("sourceName", self.source_name)
        writer.write_str_value("status", self.status)
        writer.write_str_value("statusTone", self.status_tone)
        writer.write_collection_of_object_values("tags", self.tags)
        writer.write_additional_data_value(self.additional_data)
    

