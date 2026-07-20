from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .disposition_category import DispositionCategory

@dataclass
class LeadStatusResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The businessId property
    business_id: Optional[str] = None
    # Controlled disposition categories used for reporting, automation, and analytics.
    category: Optional[DispositionCategory] = None
    # The color property
    color: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The isArchived property
    is_archived: Optional[bool] = None
    # The modifiedAt property
    modified_at: Optional[datetime.datetime] = None
    # The name property
    name: Optional[str] = None
    # The sortOrder property
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
        from .disposition_category import DispositionCategory

        from .disposition_category import DispositionCategory

        fields: dict[str, Callable[[Any], None]] = {
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(DispositionCategory)),
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_str_value("businessId", self.business_id)
        writer.write_enum_value("category", self.category)
        writer.write_str_value("color", self.color)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_int_value("sortOrder", self.sort_order)
        writer.write_additional_data_value(self.additional_data)
    

