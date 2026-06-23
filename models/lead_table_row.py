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
    API DTO containing lead data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The admin force enablement override on this lead.
    admin_enablement_override: Optional[LeadTableRow_adminEnablementOverride] = None
    # Defines why a lead was removed from the active working pipeline.
    archive_reason: Optional[int] = None
    # The date and time this lead left the active pipeline.
    archived_at: Optional[datetime.datetime] = None
    # The user who archived the lead, if available.
    archived_by_user_id: Optional[str] = None
    # The business ID associated with this lead.
    business_id: Optional[str] = None
    # The business name value for this lead.
    business_name: Optional[str] = None
    # The date and time for the created at value on this lead.
    created_at: Optional[datetime.datetime] = None
    # The current lifecycle disposition for this lead.
    current_disposition: Optional[LeadTableRow_currentDisposition] = None
    # The email address associated with this lead.
    email: Optional[str] = None
    # Whether this lead is enabled.
    enabled: Optional[bool] = None
    # The first name value for this lead.
    first_name: Optional[str] = None
    # The unique ID for this lead.
    id: Optional[str] = None
    # Whether this lead is archived.
    is_archived: Optional[bool] = None
    # The date and time for the last name value on this lead.
    last_name: Optional[str] = None
    # The phone number associated with this lead.
    phone: Optional[str] = None
    # The source ID associated with this lead.
    source_id: Optional[str] = None
    # The source name value for this lead.
    source_name: Optional[str] = None
    # The current status for this lead.
    status: Optional[str] = None
    # The status tone value for this lead.
    status_tone: Optional[str] = None
    # Compact tags assigned to the lead.
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
    

