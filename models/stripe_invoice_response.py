from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class StripeInvoiceResponse(AdditionalDataHolder, Parsable):
    """
    Customer-safe Stripe invoice summary for billing history.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The amount property
    amount: Optional[float] = None
    # The createdAt property
    created_at: Optional[datetime.datetime] = None
    # The hostedInvoiceUrl property
    hosted_invoice_url: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The number property
    number: Optional[str] = None
    # The status property
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StripeInvoiceResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StripeInvoiceResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StripeInvoiceResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "amount": lambda n : setattr(self, 'amount', n.get_float_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "hostedInvoiceUrl": lambda n : setattr(self, 'hosted_invoice_url', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_float_value("amount", self.amount)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("hostedInvoiceUrl", self.hosted_invoice_url)
        writer.write_str_value("id", self.id)
        writer.write_str_value("number", self.number)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

