from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .transaction_status import TransactionStatus
    from .transaction_table_row_billable_unit import TransactionTableRow_billableUnit
    from .transaction_table_row_billing_channel import TransactionTableRow_billingChannel
    from .transaction_table_row_business import TransactionTableRow_business
    from .transaction_table_row_lead import TransactionTableRow_lead
    from .transaction_type import TransactionType

@dataclass
class TransactionTableRow(AdditionalDataHolder, Parsable):
    """
    List item schema for Leadping API billing transaction table row results shown in searchable tables.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Monetary amount for this billing transaction or wallet operation.
    amount: Optional[float] = None
    # Defines the supported Billable Unit values.
    billable_unit: Optional[TransactionTableRow_billableUnit] = None
    # The billedAmount property
    billed_amount: Optional[float] = None
    # Defines the supported Usage Channel values.
    billing_channel: Optional[TransactionTableRow_billingChannel] = None
    # The ID and name for this business.
    business: Optional[TransactionTableRow_business] = None
    # UTC timestamp when this billing transaction table row was created.
    created_at: Optional[datetime.datetime] = None
    # Human-readable description that explains this billing transaction table row to API users.
    description: Optional[str] = None
    # Unique Leadping identifier for this billing transaction table row.
    id: Optional[str] = None
    # The ID and name for this lead.
    lead: Optional[TransactionTableRow_lead] = None
    # Net monetary amount after fees, credits, or adjustments.
    net_amount: Optional[float] = None
    # Masked or human-readable payment method shown for this transaction.
    payment_method_display: Optional[str] = None
    # The pricingVersion property
    pricing_version: Optional[str] = None
    # The quantity property
    quantity: Optional[float] = None
    # The sourceEventId property
    source_event_id: Optional[str] = None
    # The sourceEventType property
    source_event_type: Optional[str] = None
    # Processing status for this wallet transaction.
    transaction_status: Optional[TransactionStatus] = None
    # Debit or credit classification for this wallet transaction.
    transaction_type: Optional[TransactionType] = None
    # The unitPrice property
    unit_price: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TransactionTableRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TransactionTableRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TransactionTableRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .transaction_status import TransactionStatus
        from .transaction_table_row_billable_unit import TransactionTableRow_billableUnit
        from .transaction_table_row_billing_channel import TransactionTableRow_billingChannel
        from .transaction_table_row_business import TransactionTableRow_business
        from .transaction_table_row_lead import TransactionTableRow_lead
        from .transaction_type import TransactionType

        from .transaction_status import TransactionStatus
        from .transaction_table_row_billable_unit import TransactionTableRow_billableUnit
        from .transaction_table_row_billing_channel import TransactionTableRow_billingChannel
        from .transaction_table_row_business import TransactionTableRow_business
        from .transaction_table_row_lead import TransactionTableRow_lead
        from .transaction_type import TransactionType

        fields: dict[str, Callable[[Any], None]] = {
            "amount": lambda n : setattr(self, 'amount', n.get_float_value()),
            "billableUnit": lambda n : setattr(self, 'billable_unit', n.get_enum_value(TransactionTableRow_billableUnit)),
            "billedAmount": lambda n : setattr(self, 'billed_amount', n.get_float_value()),
            "billingChannel": lambda n : setattr(self, 'billing_channel', n.get_enum_value(TransactionTableRow_billingChannel)),
            "business": lambda n : setattr(self, 'business', n.get_object_value(TransactionTableRow_business)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lead": lambda n : setattr(self, 'lead', n.get_object_value(TransactionTableRow_lead)),
            "netAmount": lambda n : setattr(self, 'net_amount', n.get_float_value()),
            "paymentMethodDisplay": lambda n : setattr(self, 'payment_method_display', n.get_str_value()),
            "pricingVersion": lambda n : setattr(self, 'pricing_version', n.get_str_value()),
            "quantity": lambda n : setattr(self, 'quantity', n.get_float_value()),
            "sourceEventId": lambda n : setattr(self, 'source_event_id', n.get_str_value()),
            "sourceEventType": lambda n : setattr(self, 'source_event_type', n.get_str_value()),
            "transactionStatus": lambda n : setattr(self, 'transaction_status', n.get_enum_value(TransactionStatus)),
            "transactionType": lambda n : setattr(self, 'transaction_type', n.get_enum_value(TransactionType)),
            "unitPrice": lambda n : setattr(self, 'unit_price', n.get_float_value()),
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
        writer.write_enum_value("billableUnit", self.billable_unit)
        writer.write_float_value("billedAmount", self.billed_amount)
        writer.write_enum_value("billingChannel", self.billing_channel)
        writer.write_object_value("business", self.business)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("description", self.description)
        writer.write_str_value("id", self.id)
        writer.write_object_value("lead", self.lead)
        writer.write_float_value("netAmount", self.net_amount)
        writer.write_str_value("paymentMethodDisplay", self.payment_method_display)
        writer.write_str_value("pricingVersion", self.pricing_version)
        writer.write_float_value("quantity", self.quantity)
        writer.write_str_value("sourceEventId", self.source_event_id)
        writer.write_str_value("sourceEventType", self.source_event_type)
        writer.write_enum_value("transactionStatus", self.transaction_status)
        writer.write_enum_value("transactionType", self.transaction_type)
        writer.write_float_value("unitPrice", self.unit_price)
        writer.write_additional_data_value(self.additional_data)
    

