from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .customer_communication_usage_point import CustomerCommunicationUsagePoint

@dataclass
class CustomerCommunicationUsage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The answeredCalls property
    answered_calls: Optional[int] = None
    # The callMinutes property
    call_minutes: Optional[float] = None
    # The callsPlaced property
    calls_placed: Optional[int] = None
    # The callsReceived property
    calls_received: Optional[int] = None
    # The failedOrBlockedSms property
    failed_or_blocked_sms: Optional[int] = None
    # The missedCalls property
    missed_calls: Optional[int] = None
    # The smsReceived property
    sms_received: Optional[int] = None
    # The smsSent property
    sms_sent: Optional[int] = None
    # The trend property
    trend: Optional[list[CustomerCommunicationUsagePoint]] = None
    # The usageSpend property
    usage_spend: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerCommunicationUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerCommunicationUsage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerCommunicationUsage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .customer_communication_usage_point import CustomerCommunicationUsagePoint

        from .customer_communication_usage_point import CustomerCommunicationUsagePoint

        fields: dict[str, Callable[[Any], None]] = {
            "answeredCalls": lambda n : setattr(self, 'answered_calls', n.get_int_value()),
            "callMinutes": lambda n : setattr(self, 'call_minutes', n.get_float_value()),
            "callsPlaced": lambda n : setattr(self, 'calls_placed', n.get_int_value()),
            "callsReceived": lambda n : setattr(self, 'calls_received', n.get_int_value()),
            "failedOrBlockedSms": lambda n : setattr(self, 'failed_or_blocked_sms', n.get_int_value()),
            "missedCalls": lambda n : setattr(self, 'missed_calls', n.get_int_value()),
            "smsReceived": lambda n : setattr(self, 'sms_received', n.get_int_value()),
            "smsSent": lambda n : setattr(self, 'sms_sent', n.get_int_value()),
            "trend": lambda n : setattr(self, 'trend', n.get_collection_of_object_values(CustomerCommunicationUsagePoint)),
            "usageSpend": lambda n : setattr(self, 'usage_spend', n.get_float_value()),
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
        writer.write_int_value("answeredCalls", self.answered_calls)
        writer.write_float_value("callMinutes", self.call_minutes)
        writer.write_int_value("callsPlaced", self.calls_placed)
        writer.write_int_value("callsReceived", self.calls_received)
        writer.write_int_value("failedOrBlockedSms", self.failed_or_blocked_sms)
        writer.write_int_value("missedCalls", self.missed_calls)
        writer.write_int_value("smsReceived", self.sms_received)
        writer.write_int_value("smsSent", self.sms_sent)
        writer.write_collection_of_object_values("trend", self.trend)
        writer.write_float_value("usageSpend", self.usage_spend)
        writer.write_additional_data_value(self.additional_data)
    

