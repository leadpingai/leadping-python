from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .id_name_pair import IdNamePair

@dataclass
class MobileDevicePreferences(AdditionalDataHolder, Parsable):
    """
    API DTO containing Leadping mobile preferences for a single user device.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The ID and name for this device.
    device: Optional[IdNamePair] = None
    # Whether inbound phone calls are enabled for this user device.
    inbound_phone_calls_enabled: Optional[bool] = None
    # The date and time this device preference was last updated.
    updated_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileDevicePreferences:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileDevicePreferences
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileDevicePreferences()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .id_name_pair import IdNamePair

        from .id_name_pair import IdNamePair

        fields: dict[str, Callable[[Any], None]] = {
            "device": lambda n : setattr(self, 'device', n.get_object_value(IdNamePair)),
            "inboundPhoneCallsEnabled": lambda n : setattr(self, 'inbound_phone_calls_enabled', n.get_bool_value()),
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
        writer.write_object_value("device", self.device)
        writer.write_bool_value("inboundPhoneCallsEnabled", self.inbound_phone_calls_enabled)
        writer.write_datetime_value("updatedAt", self.updated_at)
        writer.write_additional_data_value(self.additional_data)
    

