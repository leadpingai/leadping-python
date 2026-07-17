from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .billable_unit import BillableUnit
    from .usage_channel import UsageChannel
    from .usage_ledger_table_row_business import UsageLedgerTableRow_business
    from .usage_ledger_table_row_lead import UsageLedgerTableRow_lead
    from .usage_ledger_table_row_user import UsageLedgerTableRow_user
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
    # The ID and name for this business.
    business: Optional[UsageLedgerTableRow_business] = None
    # The channel value for this usage ledger.
    channel: Optional[UsageChannel] = None
    # The date and time for the created at value on this usage ledger.
    created_at: Optional[datetime.datetime] = None
    # The monetary customer charge amount for this usage ledger.
    customer_charge_amount: Optional[float] = None
    # The human-readable description of this usage ledger.
    description: Optional[str] = None
    # The unique ID for this usage ledger.
    id: Optional[str] = None
    # Whether this usage ledger is billable.
    is_billable: Optional[bool] = None
    # The ID and name for this lead.
    lead: Optional[UsageLedgerTableRow_lead] = None
    # The phone number associated with this usage ledger.
    phone_number: Optional[str] = None
    # The phone number ID associated with this usage ledger.
    phone_number_id: Optional[str] = None
    # The quantity value for this usage ledger.
    quantity: Optional[float] = None
    # The current status for this usage ledger.
    status: Optional[UsageRecordStatus] = None
    # The unit price value for this usage ledger.
    unit_price: Optional[float] = None
    # The ID and name for this user.
    user: Optional[UsageLedgerTableRow_user] = None
    
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
        from .usage_ledger_table_row_business import UsageLedgerTableRow_business
        from .usage_ledger_table_row_lead import UsageLedgerTableRow_lead
        from .usage_ledger_table_row_user import UsageLedgerTableRow_user
        from .usage_record_status import UsageRecordStatus

        from .billable_unit import BillableUnit
        from .usage_channel import UsageChannel
        from .usage_ledger_table_row_business import UsageLedgerTableRow_business
        from .usage_ledger_table_row_lead import UsageLedgerTableRow_lead
        from .usage_ledger_table_row_user import UsageLedgerTableRow_user
        from .usage_record_status import UsageRecordStatus

        fields: dict[str, Callable[[Any], None]] = {
            "billableUnit": lambda n : setattr(self, 'billable_unit', n.get_enum_value(BillableUnit)),
            "business": lambda n : setattr(self, 'business', n.get_object_value(UsageLedgerTableRow_business)),
            "channel": lambda n : setattr(self, 'channel', n.get_enum_value(UsageChannel)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "customerChargeAmount": lambda n : setattr(self, 'customer_charge_amount', n.get_float_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isBillable": lambda n : setattr(self, 'is_billable', n.get_bool_value()),
            "lead": lambda n : setattr(self, 'lead', n.get_object_value(UsageLedgerTableRow_lead)),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "phoneNumberId": lambda n : setattr(self, 'phone_number_id', n.get_str_value()),
            "quantity": lambda n : setattr(self, 'quantity', n.get_float_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(UsageRecordStatus)),
            "unitPrice": lambda n : setattr(self, 'unit_price', n.get_float_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(UsageLedgerTableRow_user)),
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
        writer.write_object_value("business", self.business)
        writer.write_enum_value("channel", self.channel)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_float_value("customerChargeAmount", self.customer_charge_amount)
        writer.write_str_value("description", self.description)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isBillable", self.is_billable)
        writer.write_object_value("lead", self.lead)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("phoneNumberId", self.phone_number_id)
        writer.write_float_value("quantity", self.quantity)
        writer.write_enum_value("status", self.status)
        writer.write_float_value("unitPrice", self.unit_price)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    

