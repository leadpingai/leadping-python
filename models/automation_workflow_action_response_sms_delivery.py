from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_sms_delivery_record import AutomationSmsDeliveryRecord

from .automation_sms_delivery_record import AutomationSmsDeliveryRecord

@dataclass
class AutomationWorkflowActionResponse_smsDelivery(AutomationSmsDeliveryRecord, Parsable):
    """
    Delivery outcome of the persisted SMS. Workflow steps advance on command acceptance, without waiting for delivery.
    """
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationWorkflowActionResponse_smsDelivery:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationWorkflowActionResponse_smsDelivery
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationWorkflowActionResponse_smsDelivery()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automation_sms_delivery_record import AutomationSmsDeliveryRecord

        from .automation_sms_delivery_record import AutomationSmsDeliveryRecord

        fields: dict[str, Callable[[Any], None]] = {
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

