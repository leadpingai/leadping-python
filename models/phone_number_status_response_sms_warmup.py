from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sms_readiness_status_response import SmsReadinessStatusResponse

from .sms_readiness_status_response import SmsReadinessStatusResponse

@dataclass
class PhoneNumberStatusResponse_smsWarmup(SmsReadinessStatusResponse, Parsable):
    """
    SMS warmup status for this phone number.
    """
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberStatusResponse_smsWarmup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberStatusResponse_smsWarmup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberStatusResponse_smsWarmup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sms_readiness_status_response import SmsReadinessStatusResponse

        from .sms_readiness_status_response import SmsReadinessStatusResponse

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
    

