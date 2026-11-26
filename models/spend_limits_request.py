from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .spend_period import SpendPeriod

@dataclass
class SpendLimitsRequest(AdditionalDataHolder, Parsable):
    """
    Organization usage budgets in USD. Null removes a limit; zero stops new paid usage.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Optional calling budget in USD.
    calling_limit: Optional[float] = None
    # Calendar period for an organization channel budget, in UTC.
    calling_period: Optional[SpendPeriod] = None
    # Daily usage budget in USD for the UTC calendar day. Null removes the limit; zero stops new paid usage.
    daily_limit: Optional[float] = None
    # Monthly usage budget in USD for the UTC calendar month. Null removes the limit; zero stops new paid usage.
    monthly_limit: Optional[float] = None
    # Optional texting budget in USD.
    texting_limit: Optional[float] = None
    # Calendar period for an organization channel budget, in UTC.
    texting_period: Optional[SpendPeriod] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpendLimitsRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpendLimitsRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SpendLimitsRequest()
    
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
            "dailyLimit": lambda n : setattr(self, 'daily_limit', n.get_float_value()),
            "monthlyLimit": lambda n : setattr(self, 'monthly_limit', n.get_float_value()),
            "textingLimit": lambda n : setattr(self, 'texting_limit', n.get_float_value()),
            "textingPeriod": lambda n : setattr(self, 'texting_period', n.get_enum_value(SpendPeriod)),
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
        writer.write_float_value("dailyLimit", self.daily_limit)
        writer.write_float_value("monthlyLimit", self.monthly_limit)
        writer.write_float_value("textingLimit", self.texting_limit)
        writer.write_enum_value("textingPeriod", self.texting_period)
        writer.write_additional_data_value(self.additional_data)
    

