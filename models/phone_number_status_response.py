from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_messaging_event_response import PhoneNumberMessagingEventResponse
    from .phone_number_opt_out_metrics_response import PhoneNumberOptOutMetricsResponse
    from .phone_number_status_response_call_warmup import PhoneNumberStatusResponse_callWarmup
    from .phone_number_status_response_sms_warmup import PhoneNumberStatusResponse_smsWarmup
    from .phone_number_traffic_metrics_response import PhoneNumberTrafficMetricsResponse

@dataclass
class PhoneNumberStatusResponse(AdditionalDataHolder, Parsable):
    """
    API response containing phone number status data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The voice call warmup value for this phone number status.
    call_warmup: Optional[PhoneNumberStatusResponse_callWarmup] = None
    # The calls possible value for this phone number status.
    calls_possible: Optional[int] = None
    # The messages possible value for this phone number status.
    messages_possible: Optional[int] = None
    # The messages warmed value for this phone number status.
    messages_warmed: Optional[int] = None
    # The number value for this phone number status.
    number: Optional[str] = None
    # The opt out metrics value for this phone number status.
    opt_out_metrics: Optional[PhoneNumberOptOutMetricsResponse] = None
    # The recent events included with this phone number status.
    recent_events: Optional[list[PhoneNumberMessagingEventResponse]] = None
    # The SMS warmup value for this phone number status.
    sms_warmup: Optional[PhoneNumberStatusResponse_smsWarmup] = None
    # The traffic metrics value for this phone number status.
    traffic_metrics: Optional[PhoneNumberTrafficMetricsResponse] = None
    # The warmup calls made value for this phone number status.
    warmup_calls_made: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberStatusResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberStatusResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberStatusResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_messaging_event_response import PhoneNumberMessagingEventResponse
        from .phone_number_opt_out_metrics_response import PhoneNumberOptOutMetricsResponse
        from .phone_number_status_response_call_warmup import PhoneNumberStatusResponse_callWarmup
        from .phone_number_status_response_sms_warmup import PhoneNumberStatusResponse_smsWarmup
        from .phone_number_traffic_metrics_response import PhoneNumberTrafficMetricsResponse

        from .phone_number_messaging_event_response import PhoneNumberMessagingEventResponse
        from .phone_number_opt_out_metrics_response import PhoneNumberOptOutMetricsResponse
        from .phone_number_status_response_call_warmup import PhoneNumberStatusResponse_callWarmup
        from .phone_number_status_response_sms_warmup import PhoneNumberStatusResponse_smsWarmup
        from .phone_number_traffic_metrics_response import PhoneNumberTrafficMetricsResponse

        fields: dict[str, Callable[[Any], None]] = {
            "callWarmup": lambda n : setattr(self, 'call_warmup', n.get_object_value(PhoneNumberStatusResponse_callWarmup)),
            "callsPossible": lambda n : setattr(self, 'calls_possible', n.get_int_value()),
            "messagesPossible": lambda n : setattr(self, 'messages_possible', n.get_int_value()),
            "messagesWarmed": lambda n : setattr(self, 'messages_warmed', n.get_int_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "optOutMetrics": lambda n : setattr(self, 'opt_out_metrics', n.get_object_value(PhoneNumberOptOutMetricsResponse)),
            "recentEvents": lambda n : setattr(self, 'recent_events', n.get_collection_of_object_values(PhoneNumberMessagingEventResponse)),
            "smsWarmup": lambda n : setattr(self, 'sms_warmup', n.get_object_value(PhoneNumberStatusResponse_smsWarmup)),
            "trafficMetrics": lambda n : setattr(self, 'traffic_metrics', n.get_object_value(PhoneNumberTrafficMetricsResponse)),
            "warmupCallsMade": lambda n : setattr(self, 'warmup_calls_made', n.get_int_value()),
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
        writer.write_object_value("callWarmup", self.call_warmup)
        writer.write_int_value("callsPossible", self.calls_possible)
        writer.write_int_value("messagesPossible", self.messages_possible)
        writer.write_int_value("messagesWarmed", self.messages_warmed)
        writer.write_str_value("number", self.number)
        writer.write_object_value("optOutMetrics", self.opt_out_metrics)
        writer.write_collection_of_object_values("recentEvents", self.recent_events)
        writer.write_object_value("smsWarmup", self.sms_warmup)
        writer.write_object_value("trafficMetrics", self.traffic_metrics)
        writer.write_int_value("warmupCallsMade", self.warmup_calls_made)
        writer.write_additional_data_value(self.additional_data)
    

