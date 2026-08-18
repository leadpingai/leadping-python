from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_status_category import LeadStatusCategory

@dataclass
class LeadStatusResponse(AdditionalDataHolder, Parsable):
    """
    Represents a configurable status that can be assigned to leads.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # LeadStatusChange category represented by the lead status.
    category: Optional[LeadStatusCategory] = None
    # Display color assigned to the lead status.
    color: Optional[str] = None
    # Unique identifier for the lead status.
    id: Optional[str] = None
    # Indicates whether the lead status has been archived.
    is_archived: Optional[bool] = None
    # Date and time when the lead status was last modified.
    modified_at: Optional[datetime.datetime] = None
    # Display name of the lead status.
    name: Optional[str] = None
    # Identifier of the organization that owns the lead status.
    organization_id: Optional[str] = None
    # Relative display order of the lead status.
    sort_order: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadStatusResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadStatusResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadStatusResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lead_status_category import LeadStatusCategory

        from .lead_status_category import LeadStatusCategory

        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(LeadStatusCategory)),
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "organizationId": lambda n : setattr(self, 'organization_id', n.get_str_value()),
            "sortOrder": lambda n : setattr(self, 'sort_order', n.get_int_value()),
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
        writer.write_enum_value("category", self.category)
        writer.write_str_value("color", self.color)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_str_value("organizationId", self.organization_id)
        writer.write_int_value("sortOrder", self.sort_order)
        writer.write_additional_data_value(self.additional_data)
    

