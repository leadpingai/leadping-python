from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_contact import LeadContact
    from .lead_metadata import LeadMetadata
    from .lead_profile import LeadProfile
    from .lead_request_admin_enablement_override import LeadRequest_adminEnablementOverride

@dataclass
class LeadRequest(AdditionalDataHolder, Parsable):
    """
    Request payload for lead.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The adminEnablementOverride property
    admin_enablement_override: Optional[LeadRequest_adminEnablementOverride] = None
    # The contact value for this lead.
    contact: Optional[LeadContact] = None
    # The profile value for this lead.
    customer: Optional[LeadProfile] = None
    # The enabled property
    enabled: Optional[bool] = None
    # The unique identifier for the entity, when updating an existing entity.
    id: Optional[str] = None
    # Safe, non-secret metadata associated with this lead.
    metadata: Optional[LeadMetadata] = None
    # Existing business tag ids to apply when the lead is created.
    tag_ids: Optional[list[str]] = None
    # Business tag names to apply when the lead is created. Missing names are created safely by lead creation flows.
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
        from .lead_profile import LeadProfile
        from .lead_request_admin_enablement_override import LeadRequest_adminEnablementOverride

        from .lead_contact import LeadContact
        from .lead_metadata import LeadMetadata
        from .lead_profile import LeadProfile
        from .lead_request_admin_enablement_override import LeadRequest_adminEnablementOverride

        fields: dict[str, Callable[[Any], None]] = {
            "adminEnablementOverride": lambda n : setattr(self, 'admin_enablement_override', n.get_object_value(LeadRequest_adminEnablementOverride)),
            "contact": lambda n : setattr(self, 'contact', n.get_object_value(LeadContact)),
            "customer": lambda n : setattr(self, 'customer', n.get_object_value(LeadProfile)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(LeadMetadata)),
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
        writer.write_object_value("adminEnablementOverride", self.admin_enablement_override)
        writer.write_object_value("contact", self.contact)
        writer.write_object_value("customer", self.customer)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_object_value("metadata", self.metadata)
        writer.write_collection_of_primitive_values("tagIds", self.tag_ids)
        writer.write_collection_of_primitive_values("tagNames", self.tag_names)
        writer.write_additional_data_value(self.additional_data)
    

