from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_contact import LeadContact
    from .lead_metadata import LeadMetadata
    from .lead_profile import LeadProfile

@dataclass
class LeadRequest(AdditionalDataHolder, Parsable):
    """
    Request schema for the Leadping API lead request, including the fields clients can send.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contact details for the lead or customer represented by this lead request.
    contact: Optional[LeadContact] = None
    # Demographic profile details for the lead represented by this lead request.
    customer: Optional[LeadProfile] = None
    # Indicates whether this lead request is active and available in the Leadping API.
    enabled: Optional[bool] = None
    # The unique identifier for the entity, when updating an existing entity.
    id: Optional[str] = None
    # Structured metadata used for attribution, integrations, and reporting on this lead request.
    metadata: Optional[LeadMetadata] = None
    # Tag IDs assigned to or filtered against this lead.
    tag_ids: Optional[list[str]] = None
    # Tag names assigned to this lead when matching existing tags by name.
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

        from .lead_contact import LeadContact
        from .lead_metadata import LeadMetadata
        from .lead_profile import LeadProfile

        fields: dict[str, Callable[[Any], None]] = {
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
        writer.write_object_value("contact", self.contact)
        writer.write_object_value("customer", self.customer)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_object_value("metadata", self.metadata)
        writer.write_collection_of_primitive_values("tagIds", self.tag_ids)
        writer.write_collection_of_primitive_values("tagNames", self.tag_names)
        writer.write_additional_data_value(self.additional_data)
    

