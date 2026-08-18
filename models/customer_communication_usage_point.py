from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CustomerCommunicationUsagePoint(AdditionalDataHolder, Parsable):
    """
    Represents customer communication usage point data exposed by Leadping analytics.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Total connected call duration, in minutes, during the reporting period.
    call_minutes: Optional[float] = None
    # Number of calls represented by this Leadping customer communication usage point.
    calls: Optional[int] = None
    # Date and time when this Leadping customer communication usage point was end.
    end_at: Optional[datetime.datetime] = None
    # Human-readable label for this Leadping customer communication usage point.
    label: Optional[str] = None
    # Number of SMS messages received during the reporting period.
    sms_received: Optional[int] = None
    # Number of SMS messages sent during the reporting period.
    sms_sent: Optional[int] = None
    # Spend represented by this Leadping customer communication usage point.
    spend: Optional[float] = None
    # Date and time when this Leadping customer communication usage point was start.
    start_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerCommunicationUsagePoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerCommunicationUsagePoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerCommunicationUsagePoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "callMinutes": lambda n : setattr(self, 'call_minutes', n.get_float_value()),
            "calls": lambda n : setattr(self, 'calls', n.get_int_value()),
            "endAt": lambda n : setattr(self, 'end_at', n.get_datetime_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "smsReceived": lambda n : setattr(self, 'sms_received', n.get_int_value()),
            "smsSent": lambda n : setattr(self, 'sms_sent', n.get_int_value()),
            "spend": lambda n : setattr(self, 'spend', n.get_float_value()),
            "startAt": lambda n : setattr(self, 'start_at', n.get_datetime_value()),
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
        writer.write_float_value("callMinutes", self.call_minutes)
        writer.write_int_value("calls", self.calls)
        writer.write_datetime_value("endAt", self.end_at)
        writer.write_str_value("label", self.label)
        writer.write_int_value("smsReceived", self.sms_received)
        writer.write_int_value("smsSent", self.sms_sent)
        writer.write_float_value("spend", self.spend)
        writer.write_datetime_value("startAt", self.start_at)
        writer.write_additional_data_value(self.additional_data)
    

