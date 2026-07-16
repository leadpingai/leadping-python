from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_warmup_health_status import PhoneNumberWarmup_healthStatus
    from .phone_number_warmup_state import PhoneNumberWarmup_state

@dataclass
class PhoneNumberWarmup(AdditionalDataHolder, Parsable):
    """
    Warmup state for a Leadping phone number.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether the phone number warmup is enabled in Leadping.
    enabled: Optional[bool] = None
    # Current warmup health score used to assess phone number readiness.
    health_score: Optional[int] = None
    # Defines the supported SMS Warmup Health State values.
    health_status: Optional[PhoneNumberWarmup_healthStatus] = None
    # Warmup completion percentage, from 0 through 100.
    progress_percent: Optional[int] = None
    # Defines the supported SMS Warmup Health State values.
    state: Optional[PhoneNumberWarmup_state] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberWarmup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberWarmup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberWarmup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_warmup_health_status import PhoneNumberWarmup_healthStatus
        from .phone_number_warmup_state import PhoneNumberWarmup_state

        from .phone_number_warmup_health_status import PhoneNumberWarmup_healthStatus
        from .phone_number_warmup_state import PhoneNumberWarmup_state

        fields: dict[str, Callable[[Any], None]] = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "healthScore": lambda n : setattr(self, 'health_score', n.get_int_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(PhoneNumberWarmup_healthStatus)),
            "progressPercent": lambda n : setattr(self, 'progress_percent', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(PhoneNumberWarmup_state)),
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
        writer.write_bool_value("enabled", self.enabled)
        writer.write_int_value("healthScore", self.health_score)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_int_value("progressPercent", self.progress_percent)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

