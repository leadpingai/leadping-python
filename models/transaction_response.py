from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .transaction_response_metadata import TransactionResponse_metadata
    from .transaction_status import TransactionStatus
    from .transaction_type import TransactionType

@dataclass
class TransactionResponse(AdditionalDataHolder, Parsable):
    """
    API response containing transaction data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The account ID associated with this transaction.
    account_id: Optional[str] = None
    # The account name value for this transaction.
    account_name: Optional[str] = None
    # The monetary amount for this transaction.
    amount: Optional[float] = None
    # The business ID associated with this transaction.
    business_id: Optional[str] = None
    # The business name value for this transaction.
    business_name: Optional[str] = None
    # The correlation ID associated with this transaction.
    correlation_id: Optional[str] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # The date and time for the created by value on this transaction.
    created_by: Optional[str] = None
    # The human-readable description of this transaction.
    description: Optional[str] = None
    # The gateway ID associated with this transaction.
    gateway_id: Optional[str] = None
    # The current gateway status for this transaction.
    gateway_status: Optional[str] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # The lead ID associated with this transaction.
    lead_id: Optional[str] = None
    # The lead name value for this transaction.
    lead_name: Optional[str] = None
    # Provider and wallet audit metadata for this transaction.
    metadata: Optional[TransactionResponse_metadata] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # The modified by value for this transaction.
    modified_by: Optional[str] = None
    # The monetary net amount for this transaction.
    net_amount: Optional[float] = None
    # The operator or customer notes recorded for this transaction.
    notes: Optional[str] = None
    # The payment method display value for this transaction.
    payment_method_display: Optional[str] = None
    # The current transaction status for this transaction.
    transaction_status: Optional[TransactionStatus] = None
    # The transaction type classification for this transaction.
    transaction_type: Optional[TransactionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TransactionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TransactionResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TransactionResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .transaction_response_metadata import TransactionResponse_metadata
        from .transaction_status import TransactionStatus
        from .transaction_type import TransactionType

        from .transaction_response_metadata import TransactionResponse_metadata
        from .transaction_status import TransactionStatus
        from .transaction_type import TransactionType

        fields: dict[str, Callable[[Any], None]] = {
            "accountId": lambda n : setattr(self, 'account_id', n.get_str_value()),
            "accountName": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "amount": lambda n : setattr(self, 'amount', n.get_float_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "businessName": lambda n : setattr(self, 'business_name', n.get_str_value()),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "gatewayId": lambda n : setattr(self, 'gateway_id', n.get_str_value()),
            "gatewayStatus": lambda n : setattr(self, 'gateway_status', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "leadName": lambda n : setattr(self, 'lead_name', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(TransactionResponse_metadata)),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "modifiedBy": lambda n : setattr(self, 'modified_by', n.get_str_value()),
            "netAmount": lambda n : setattr(self, 'net_amount', n.get_float_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "paymentMethodDisplay": lambda n : setattr(self, 'payment_method_display', n.get_str_value()),
            "transactionStatus": lambda n : setattr(self, 'transaction_status', n.get_enum_value(TransactionStatus)),
            "transactionType": lambda n : setattr(self, 'transaction_type', n.get_enum_value(TransactionType)),
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
        writer.write_str_value("accountId", self.account_id)
        writer.write_str_value("accountName", self.account_name)
        writer.write_float_value("amount", self.amount)
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("businessName", self.business_name)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_str_value("description", self.description)
        writer.write_str_value("gatewayId", self.gateway_id)
        writer.write_str_value("gatewayStatus", self.gateway_status)
        writer.write_str_value("id", self.id)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_str_value("leadName", self.lead_name)
        writer.write_object_value("metadata", self.metadata)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("modifiedBy", self.modified_by)
        writer.write_float_value("netAmount", self.net_amount)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("paymentMethodDisplay", self.payment_method_display)
        writer.write_enum_value("transactionStatus", self.transaction_status)
        writer.write_enum_value("transactionType", self.transaction_type)
        writer.write_additional_data_value(self.additional_data)
    

