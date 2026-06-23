from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TagResponse(AdditionalDataHolder, Parsable):
    """
    API response containing business tag data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The archivedAt property
    archived_at: Optional[datetime.datetime] = None
    # The businessId property
    business_id: Optional[str] = None
    # The color property
    color: Optional[str] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # The isArchived property
    is_archived: Optional[bool] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # The name property
    name: Optional[str] = None
    # The normalizedName property
    normalized_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TagResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TagResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TagResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "archivedAt": lambda n : setattr(self, 'archived_at', n.get_datetime_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "normalizedName": lambda n : setattr(self, 'normalized_name', n.get_str_value()),
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
        writer.write_datetime_value("archivedAt", self.archived_at)
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("color", self.color)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_str_value("description", self.description)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_str_value("normalizedName", self.normalized_name)
        writer.write_additional_data_value(self.additional_data)
    

