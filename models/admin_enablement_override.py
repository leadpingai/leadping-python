from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AdminEnablementOverride(AdditionalDataHolder, Parsable):
    """
    Admin override that can enable or disable this record independently of normal status checks.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The enabled property
    enabled: Optional[bool] = None
    # The reason property
    reason: Optional[str] = None
    # The updatedAt property
    updated_at: Optional[datetime.datetime] = None
    # The updatedByUserId property
    updated_by_user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AdminEnablementOverride:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdminEnablementOverride
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AdminEnablementOverride()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "updatedAt": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
            "updatedByUserId": lambda n : setattr(self, 'updated_by_user_id', n.get_str_value()),
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
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("reason", self.reason)
        writer.write_datetime_value("updatedAt", self.updated_at)
        writer.write_str_value("updatedByUserId", self.updated_by_user_id)
        writer.write_additional_data_value(self.additional_data)
    

