from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_contact import LeadContact
    from .lead_metadata import LeadMetadata
    from .lead_profile import LeadProfile
    from .lead_response_admin_enablement_override import LeadResponse_adminEnablementOverride
    from .lead_response_current_disposition import LeadResponse_currentDisposition
    from .tag_summary import TagSummary

@dataclass
class LeadResponse(AdditionalDataHolder, Parsable):
    """
    Response schema for the Leadping API lead response returned to authenticated clients.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Admin override that can enable or disable this record independently of normal status checks.
    admin_enablement_override: Optional[LeadResponse_adminEnablementOverride] = None
    # Optional note explaining why the lead was archived.
    archive_note: Optional[str] = None
    # Defines why a lead was removed from the active working pipeline.
    archive_reason: Optional[int] = None
    # UTC timestamp when this record was archived.
    archived_at: Optional[datetime.datetime] = None
    # User ID of the person who archived this record.
    archived_by_user_id: Optional[str] = None
    # Contact details for the lead or customer represented by this lead response.
    contact: Optional[LeadContact] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # Current disposition summary that describes the lead outcome.
    current_disposition: Optional[LeadResponse_currentDisposition] = None
    # Demographic profile details for the lead represented by this lead response.
    customer: Optional[LeadProfile] = None
    # Indicates whether this lead response is active and available in the Leadping API.
    enabled: Optional[bool] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # The isArchived property
    is_archived: Optional[bool] = None
    # Structured metadata used for attribution, integrations, and reporting on this lead response.
    metadata: Optional[LeadMetadata] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
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
        from .lead_profile import LeadProfile
        from .lead_response_admin_enablement_override import LeadResponse_adminEnablementOverride
        from .lead_response_current_disposition import LeadResponse_currentDisposition
        from .tag_summary import TagSummary

        from .lead_contact import LeadContact
        from .lead_metadata import LeadMetadata
        from .lead_profile import LeadProfile
        from .lead_response_admin_enablement_override import LeadResponse_adminEnablementOverride
        from .lead_response_current_disposition import LeadResponse_currentDisposition
        from .tag_summary import TagSummary

        fields: dict[str, Callable[[Any], None]] = {
            "adminEnablementOverride": lambda n : setattr(self, 'admin_enablement_override', n.get_object_value(LeadResponse_adminEnablementOverride)),
            "archiveNote": lambda n : setattr(self, 'archive_note', n.get_str_value()),
            "archiveReason": lambda n : setattr(self, 'archive_reason', n.get_int_value()),
            "archivedAt": lambda n : setattr(self, 'archived_at', n.get_datetime_value()),
            "archivedByUserId": lambda n : setattr(self, 'archived_by_user_id', n.get_str_value()),
            "contact": lambda n : setattr(self, 'contact', n.get_object_value(LeadContact)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "currentDisposition": lambda n : setattr(self, 'current_disposition', n.get_object_value(LeadResponse_currentDisposition)),
            "customer": lambda n : setattr(self, 'customer', n.get_object_value(LeadProfile)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(LeadMetadata)),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
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
        writer.write_str_value("archiveNote", self.archive_note)
        writer.write_int_value("archiveReason", self.archive_reason)
        writer.write_datetime_value("archivedAt", self.archived_at)
        writer.write_str_value("archivedByUserId", self.archived_by_user_id)
        writer.write_object_value("contact", self.contact)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_object_value("currentDisposition", self.current_disposition)
        writer.write_object_value("customer", self.customer)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_object_value("metadata", self.metadata)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_collection_of_object_values("tags", self.tags)
        writer.write_additional_data_value(self.additional_data)
    

