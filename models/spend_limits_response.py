from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .spend_period import SpendPeriod

@dataclass
class SpendLimitsResponse(AdditionalDataHolder, Parsable):
    """
    UTC calendar usage budgets, settled spend, and pending usage reservations in USD.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Optional calling budget in USD.
    calling_limit: Optional[float] = None
    # Calendar period for an organization channel budget, in UTC.
    calling_period: Optional[SpendPeriod] = None
    # Settled calling charges this period plus pending calling reservations.
    calling_used: Optional[float] = None
    # Daily usage budget in USD. Null means no daily limit; zero stops new paid usage.
    daily_limit: Optional[float] = None
    # UTC timestamp when the next calendar day begins and daily spending resets.
    daily_resets_at: Optional[datetime.datetime] = None
    # Settled usage spending in USD for the current UTC calendar day.
    daily_spent: Optional[float] = None
    # Monthly usage budget in USD. Null means no monthly limit; zero stops new paid usage.
    monthly_limit: Optional[float] = None
    # UTC timestamp when the next calendar month begins and monthly spending resets.
    monthly_resets_at: Optional[datetime.datetime] = None
    # Settled usage spending in USD for the current UTC calendar month.
    monthly_spent: Optional[float] = None
    # Pending usage reservations in USD.
    reserved: Optional[float] = None
    # Optional texting budget in USD.
    texting_limit: Optional[float] = None
    # Calendar period for an organization channel budget, in UTC.
    texting_period: Optional[SpendPeriod] = None
    # Settled texting charges this period plus pending texting reservations.
    texting_used: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpendLimitsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpendLimitsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SpendLimitsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .spend_period import SpendPeriod

        from .spend_period import SpendPeriod

        fields: dict[str, Callable[[Any], None]] = {
            "callingLimit": lambda n : setattr(self, 'calling_limit', n.get_float_value()),
            "callingPeriod": lambda n : setattr(self, 'calling_period', n.get_enum_value(SpendPeriod)),
            "callingUsed": lambda n : setattr(self, 'calling_used', n.get_float_value()),
            "dailyLimit": lambda n : setattr(self, 'daily_limit', n.get_float_value()),
            "dailyResetsAt": lambda n : setattr(self, 'daily_resets_at', n.get_datetime_value()),
            "dailySpent": lambda n : setattr(self, 'daily_spent', n.get_float_value()),
            "monthlyLimit": lambda n : setattr(self, 'monthly_limit', n.get_float_value()),
            "monthlyResetsAt": lambda n : setattr(self, 'monthly_resets_at', n.get_datetime_value()),
            "monthlySpent": lambda n : setattr(self, 'monthly_spent', n.get_float_value()),
            "reserved": lambda n : setattr(self, 'reserved', n.get_float_value()),
            "textingLimit": lambda n : setattr(self, 'texting_limit', n.get_float_value()),
            "textingPeriod": lambda n : setattr(self, 'texting_period', n.get_enum_value(SpendPeriod)),
            "textingUsed": lambda n : setattr(self, 'texting_used', n.get_float_value()),
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
        writer.write_float_value("callingLimit", self.calling_limit)
        writer.write_enum_value("callingPeriod", self.calling_period)
        writer.write_float_value("callingUsed", self.calling_used)
        writer.write_float_value("dailyLimit", self.daily_limit)
        writer.write_datetime_value("dailyResetsAt", self.daily_resets_at)
        writer.write_float_value("dailySpent", self.daily_spent)
        writer.write_float_value("monthlyLimit", self.monthly_limit)
        writer.write_datetime_value("monthlyResetsAt", self.monthly_resets_at)
        writer.write_float_value("monthlySpent", self.monthly_spent)
        writer.write_float_value("reserved", self.reserved)
        writer.write_float_value("textingLimit", self.texting_limit)
        writer.write_enum_value("textingPeriod", self.texting_period)
        writer.write_float_value("textingUsed", self.texting_used)
        writer.write_additional_data_value(self.additional_data)
    

