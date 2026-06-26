from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .wallet_response_credit_status import WalletResponse_creditStatus
    from .wallet_response_source_type import WalletResponse_sourceType

@dataclass
class WalletResponse(AdditionalDataHolder, Parsable):
    """
    Response schema for the Leadping API billing wallet response returned to authenticated clients.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # UTC timestamp when Leadping last calculated the wallet balance.
    balance_calculated_at: Optional[datetime.datetime] = None
    # Business ID that owns this wallet balance or credit.
    business_id: Optional[str] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # Defines the lifecycle state for a wallet credit lot.
    credit_status: Optional[WalletResponse_creditStatus] = None
    # ISO currency code used for the monetary amounts in this billing wallet response.
    currency: Optional[str] = None
    # UTC timestamp when the wallet credit expires.
    expires_at: Optional[datetime.datetime] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # The display name for the entity.
    name: Optional[str] = None
    # UTC timestamp when the next wallet credit amount expires.
    next_credit_expiration_at: Optional[datetime.datetime] = None
    # Original wallet transaction ID referenced by a reversal, refund, or adjustment.
    original_transaction_id: Optional[str] = None
    # UTC timestamp when the wallet credit was purchased.
    purchased_at: Optional[datetime.datetime] = None
    # Defines the source that created a wallet credit lot.
    source_type: Optional[WalletResponse_sourceType] = None
    # Stripe charge identifier linked to this billing transaction.
    stripe_charge_id: Optional[str] = None
    # Stripe invoice identifier linked to this billing transaction.
    stripe_invoice_id: Optional[str] = None
    # Stripe payment intent identifier linked to this billing transaction.
    stripe_payment_intent_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WalletResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WalletResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WalletResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .wallet_response_credit_status import WalletResponse_creditStatus
        from .wallet_response_source_type import WalletResponse_sourceType

        from .wallet_response_credit_status import WalletResponse_creditStatus
        from .wallet_response_source_type import WalletResponse_sourceType

        fields: dict[str, Callable[[Any], None]] = {
            "balanceCalculatedAt": lambda n : setattr(self, 'balance_calculated_at', n.get_datetime_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "creditStatus": lambda n : setattr(self, 'credit_status', n.get_enum_value(WalletResponse_creditStatus)),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "expiresAt": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "nextCreditExpirationAt": lambda n : setattr(self, 'next_credit_expiration_at', n.get_datetime_value()),
            "originalTransactionId": lambda n : setattr(self, 'original_transaction_id', n.get_str_value()),
            "purchasedAt": lambda n : setattr(self, 'purchased_at', n.get_datetime_value()),
            "sourceType": lambda n : setattr(self, 'source_type', n.get_enum_value(WalletResponse_sourceType)),
            "stripeChargeId": lambda n : setattr(self, 'stripe_charge_id', n.get_str_value()),
            "stripeInvoiceId": lambda n : setattr(self, 'stripe_invoice_id', n.get_str_value()),
            "stripePaymentIntentId": lambda n : setattr(self, 'stripe_payment_intent_id', n.get_str_value()),
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
        writer.write_datetime_value("balanceCalculatedAt", self.balance_calculated_at)
        writer.write_str_value("businessId", self.business_id)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_enum_value("creditStatus", self.credit_status)
        writer.write_str_value("currency", self.currency)
        writer.write_datetime_value("expiresAt", self.expires_at)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_datetime_value("nextCreditExpirationAt", self.next_credit_expiration_at)
        writer.write_str_value("originalTransactionId", self.original_transaction_id)
        writer.write_datetime_value("purchasedAt", self.purchased_at)
        writer.write_enum_value("sourceType", self.source_type)
        writer.write_str_value("stripeChargeId", self.stripe_charge_id)
        writer.write_str_value("stripeInvoiceId", self.stripe_invoice_id)
        writer.write_str_value("stripePaymentIntentId", self.stripe_payment_intent_id)
        writer.write_additional_data_value(self.additional_data)
    

