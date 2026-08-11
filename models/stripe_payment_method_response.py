from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class StripePaymentMethodResponse(AdditionalDataHolder, Parsable):
    """
    Describes stripe payment method data used in Leadping API requests and responses.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Card network brand, such as Visa, Mastercard, or American Express.
    brand: Optional[str] = None
    # UTC timestamp for created at on this Stripe payment method.
    created_at: Optional[datetime.datetime] = None
    # Two-digit month when the card expires.
    exp_month: Optional[int] = None
    # Four-digit year when the card expires.
    exp_year: Optional[int] = None
    # Unique Leadping identifier for this Stripe payment method.
    id: Optional[str] = None
    # Whether this Stripe payment method is default.
    is_default: Optional[bool] = None
    # UTC timestamp for last4 on this Stripe payment method.
    last4: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StripePaymentMethodResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StripePaymentMethodResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StripePaymentMethodResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "brand": lambda n : setattr(self, 'brand', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "expMonth": lambda n : setattr(self, 'exp_month', n.get_int_value()),
            "expYear": lambda n : setattr(self, 'exp_year', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "last4": lambda n : setattr(self, 'last4', n.get_str_value()),
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
        writer.write_str_value("brand", self.brand)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_int_value("expMonth", self.exp_month)
        writer.write_int_value("expYear", self.exp_year)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_str_value("last4", self.last4)
        writer.write_additional_data_value(self.additional_data)
    

