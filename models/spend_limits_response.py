from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SpendLimitsResponse(AdditionalDataHolder, Parsable):
    """
    UTC calendar usage budgets, settled spend, and pending usage reservations in USD.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The dailyLimit property
    daily_limit: Optional[float] = None
    # The dailyResetsAt property
    daily_resets_at: Optional[datetime.datetime] = None
    # The dailySpent property
    daily_spent: Optional[float] = None
    # The monthlyLimit property
    monthly_limit: Optional[float] = None
    # The monthlyResetsAt property
    monthly_resets_at: Optional[datetime.datetime] = None
    # The monthlySpent property
    monthly_spent: Optional[float] = None
    # The reserved property
    reserved: Optional[float] = None
    
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
        fields: dict[str, Callable[[Any], None]] = {
            "dailyLimit": lambda n : setattr(self, 'daily_limit', n.get_float_value()),
            "dailyResetsAt": lambda n : setattr(self, 'daily_resets_at', n.get_datetime_value()),
            "dailySpent": lambda n : setattr(self, 'daily_spent', n.get_float_value()),
            "monthlyLimit": lambda n : setattr(self, 'monthly_limit', n.get_float_value()),
            "monthlyResetsAt": lambda n : setattr(self, 'monthly_resets_at', n.get_datetime_value()),
            "monthlySpent": lambda n : setattr(self, 'monthly_spent', n.get_float_value()),
            "reserved": lambda n : setattr(self, 'reserved', n.get_float_value()),
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
        writer.write_float_value("dailyLimit", self.daily_limit)
        writer.write_datetime_value("dailyResetsAt", self.daily_resets_at)
        writer.write_float_value("dailySpent", self.daily_spent)
        writer.write_float_value("monthlyLimit", self.monthly_limit)
        writer.write_datetime_value("monthlyResetsAt", self.monthly_resets_at)
        writer.write_float_value("monthlySpent", self.monthly_spent)
        writer.write_float_value("reserved", self.reserved)
        writer.write_additional_data_value(self.additional_data)
    

