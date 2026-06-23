from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .billable_unit import BillableUnit
    from .usage_channel import UsageChannel
    from .usage_record_status import UsageRecordStatus

@dataclass
class UsageLedgerTableRow(AdditionalDataHolder, Parsable):
    """
    API DTO containing usage ledger data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The billable unit value for this usage ledger.
    billable_unit: Optional[BillableUnit] = None
    # The business ID associated with this usage ledger.
    business_id: Optional[str] = None
    # The business name value for this usage ledger.
    business_name: Optional[str] = None
    # The channel value for this usage ledger.
    channel: Optional[UsageChannel] = None
    # The correlation ID associated with this usage ledger.
    correlation_id: Optional[str] = None
    # The date and time for the created at value on this usage ledger.
    created_at: Optional[datetime.datetime] = None
    # The monetary customer charge amount for this usage ledger.
    customer_charge_amount: Optional[float] = None
    # The human-readable description of this usage ledger.
    description: Optional[str] = None
    # The unique ID for this usage ledger.
    id: Optional[str] = None
    # The idempotency key value for this usage ledger.
    idempotency_key: Optional[str] = None
    # Whether this usage ledger is billable.
    is_billable: Optional[bool] = None
    # Whether this usage ledger is internal.
    is_internal: Optional[bool] = None
    # The lead ID associated with this usage ledger.
    lead_id: Optional[str] = None
    # The lead name value for this usage ledger.
    lead_name: Optional[str] = None
    # The phone number associated with this usage ledger.
    phone_number: Optional[str] = None
    # The phone number ID associated with this usage ledger.
    phone_number_id: Optional[str] = None
    # The quantity value for this usage ledger.
    quantity: Optional[float] = None
    # The source event ID associated with this usage ledger.
    source_event_id: Optional[str] = None
    # The current status for this usage ledger.
    status: Optional[UsageRecordStatus] = None
    # The unit price value for this usage ledger.
    unit_price: Optional[float] = None
    # The user ID associated with this usage ledger.
    user_id: Optional[str] = None
    # The user name value for this usage ledger.
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UsageLedgerTableRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UsageLedgerTableRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UsageLedgerTableRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .billable_unit import BillableUnit
        from .usage_channel import UsageChannel
        from .usage_record_status import UsageRecordStatus

        from .billable_unit import BillableUnit
        from .usage_channel import UsageChannel
        from .usage_record_status import UsageRecordStatus

        fields: dict[str, Callable[[Any], None]] = {
            "billableUnit": lambda n : setattr(self, 'billable_unit', n.get_enum_value(BillableUnit)),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "businessName": lambda n : setattr(self, 'business_name', n.get_str_value()),
            "channel": lambda n : setattr(self, 'channel', n.get_enum_value(UsageChannel)),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "customerChargeAmount": lambda n : setattr(self, 'customer_charge_amount', n.get_float_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "idempotencyKey": lambda n : setattr(self, 'idempotency_key', n.get_str_value()),
            "isBillable": lambda n : setattr(self, 'is_billable', n.get_bool_value()),
            "isInternal": lambda n : setattr(self, 'is_internal', n.get_bool_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "leadName": lambda n : setattr(self, 'lead_name', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "phoneNumberId": lambda n : setattr(self, 'phone_number_id', n.get_str_value()),
            "quantity": lambda n : setattr(self, 'quantity', n.get_float_value()),
            "sourceEventId": lambda n : setattr(self, 'source_event_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(UsageRecordStatus)),
            "unitPrice": lambda n : setattr(self, 'unit_price', n.get_float_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_enum_value("billableUnit", self.billable_unit)
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("businessName", self.business_name)
        writer.write_enum_value("channel", self.channel)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_float_value("customerChargeAmount", self.customer_charge_amount)
        writer.write_str_value("description", self.description)
        writer.write_str_value("id", self.id)
        writer.write_str_value("idempotencyKey", self.idempotency_key)
        writer.write_bool_value("isBillable", self.is_billable)
        writer.write_bool_value("isInternal", self.is_internal)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_str_value("leadName", self.lead_name)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("phoneNumberId", self.phone_number_id)
        writer.write_float_value("quantity", self.quantity)
        writer.write_str_value("sourceEventId", self.source_event_id)
        writer.write_enum_value("status", self.status)
        writer.write_float_value("unitPrice", self.unit_price)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
        writer.write_additional_data_value(self.additional_data)
    

