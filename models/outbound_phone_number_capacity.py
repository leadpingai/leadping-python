from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_outbound_health_status import PhoneNumberOutboundHealthStatus

@dataclass
class OutboundPhoneNumberCapacity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Defines phone-number outbound health states used by pacing.
    health_status: Optional[PhoneNumberOutboundHealthStatus] = None
    # The phoneNumber property
    phone_number: Optional[str] = None
    # The phoneNumberId property
    phone_number_id: Optional[str] = None
    # The smsRemainingToday property
    sms_remaining_today: Optional[int] = None
    # The voiceRemainingToday property
    voice_remaining_today: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OutboundPhoneNumberCapacity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutboundPhoneNumberCapacity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OutboundPhoneNumberCapacity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_outbound_health_status import PhoneNumberOutboundHealthStatus

        from .phone_number_outbound_health_status import PhoneNumberOutboundHealthStatus

        fields: dict[str, Callable[[Any], None]] = {
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(PhoneNumberOutboundHealthStatus)),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "phoneNumberId": lambda n : setattr(self, 'phone_number_id', n.get_str_value()),
            "smsRemainingToday": lambda n : setattr(self, 'sms_remaining_today', n.get_int_value()),
            "voiceRemainingToday": lambda n : setattr(self, 'voice_remaining_today', n.get_int_value()),
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
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("phoneNumberId", self.phone_number_id)
        writer.write_int_value("smsRemainingToday", self.sms_remaining_today)
        writer.write_int_value("voiceRemainingToday", self.voice_remaining_today)
        writer.write_additional_data_value(self.additional_data)
    

