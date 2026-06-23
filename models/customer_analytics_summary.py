from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytics_comparison import AnalyticsComparison

@dataclass
class CustomerAnalyticsSummary(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The billingStatus property
    billing_status: Optional[str] = None
    # The callMinutes property
    call_minutes: Optional[float] = None
    # The callsPlaced property
    calls_placed: Optional[int] = None
    # The callsReceived property
    calls_received: Optional[int] = None
    # The leads property
    leads: Optional[int] = None
    # The leadsComparison property
    leads_comparison: Optional[AnalyticsComparison] = None
    # The missedCalls property
    missed_calls: Optional[int] = None
    # The missedLeads property
    missed_leads: Optional[int] = None
    # The respondedWithinFiveMinutesPercent property
    responded_within_five_minutes_percent: Optional[float] = None
    # The smsReceived property
    sms_received: Optional[int] = None
    # The smsSent property
    sms_sent: Optional[int] = None
    # The unreadMessages property
    unread_messages: Optional[int] = None
    # The usageSpend property
    usage_spend: Optional[float] = None
    # The walletBalance property
    wallet_balance: Optional[float] = None
    # The walletStatus property
    wallet_status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerAnalyticsSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerAnalyticsSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerAnalyticsSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analytics_comparison import AnalyticsComparison

        from .analytics_comparison import AnalyticsComparison

        fields: dict[str, Callable[[Any], None]] = {
            "billingStatus": lambda n : setattr(self, 'billing_status', n.get_str_value()),
            "callMinutes": lambda n : setattr(self, 'call_minutes', n.get_float_value()),
            "callsPlaced": lambda n : setattr(self, 'calls_placed', n.get_int_value()),
            "callsReceived": lambda n : setattr(self, 'calls_received', n.get_int_value()),
            "leads": lambda n : setattr(self, 'leads', n.get_int_value()),
            "leadsComparison": lambda n : setattr(self, 'leads_comparison', n.get_object_value(AnalyticsComparison)),
            "missedCalls": lambda n : setattr(self, 'missed_calls', n.get_int_value()),
            "missedLeads": lambda n : setattr(self, 'missed_leads', n.get_int_value()),
            "respondedWithinFiveMinutesPercent": lambda n : setattr(self, 'responded_within_five_minutes_percent', n.get_float_value()),
            "smsReceived": lambda n : setattr(self, 'sms_received', n.get_int_value()),
            "smsSent": lambda n : setattr(self, 'sms_sent', n.get_int_value()),
            "unreadMessages": lambda n : setattr(self, 'unread_messages', n.get_int_value()),
            "usageSpend": lambda n : setattr(self, 'usage_spend', n.get_float_value()),
            "walletBalance": lambda n : setattr(self, 'wallet_balance', n.get_float_value()),
            "walletStatus": lambda n : setattr(self, 'wallet_status', n.get_str_value()),
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
        writer.write_str_value("billingStatus", self.billing_status)
        writer.write_float_value("callMinutes", self.call_minutes)
        writer.write_int_value("callsPlaced", self.calls_placed)
        writer.write_int_value("callsReceived", self.calls_received)
        writer.write_int_value("leads", self.leads)
        writer.write_object_value("leadsComparison", self.leads_comparison)
        writer.write_int_value("missedCalls", self.missed_calls)
        writer.write_int_value("missedLeads", self.missed_leads)
        writer.write_float_value("respondedWithinFiveMinutesPercent", self.responded_within_five_minutes_percent)
        writer.write_int_value("smsReceived", self.sms_received)
        writer.write_int_value("smsSent", self.sms_sent)
        writer.write_int_value("unreadMessages", self.unread_messages)
        writer.write_float_value("usageSpend", self.usage_spend)
        writer.write_float_value("walletBalance", self.wallet_balance)
        writer.write_str_value("walletStatus", self.wallet_status)
        writer.write_additional_data_value(self.additional_data)
    

