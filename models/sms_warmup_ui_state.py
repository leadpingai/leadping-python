from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sms_warmup_health_state import SmsWarmupHealthState

@dataclass
class SmsWarmupUiState(AdditionalDataHolder, Parsable):
    """
    API DTO containing SMS warmup ui state data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The human-readable description of this SMS warmup UI state.
    description: Optional[str] = None
    # The human-readable label shown for this SMS warmup UI state.
    label: Optional[SmsWarmupHealthState] = None
    # The tone value for this SMS warmup UI state.
    tone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SmsWarmupUiState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SmsWarmupUiState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SmsWarmupUiState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sms_warmup_health_state import SmsWarmupHealthState

        from .sms_warmup_health_state import SmsWarmupHealthState

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "label": lambda n : setattr(self, 'label', n.get_enum_value(SmsWarmupHealthState)),
            "tone": lambda n : setattr(self, 'tone', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_enum_value("label", self.label)
        writer.write_str_value("tone", self.tone)
        writer.write_additional_data_value(self.additional_data)
    

