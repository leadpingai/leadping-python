from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .outgoing_number_selection_request import OutgoingNumberSelectionRequest

@dataclass
class OutgoingNumberManualOverrideRequest(AdditionalDataHolder, Parsable):
    """
    Request schema for the Leadping API outgoing number manual override request, including the fields clients can send.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Sender phone number ID used for this outbound SMS or call.
    from_phone_number_id: Optional[str] = None
    # Selected outgoing number and selection rationale returned by Leadping.
    selection: Optional[OutgoingNumberSelectionRequest] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OutgoingNumberManualOverrideRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutgoingNumberManualOverrideRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OutgoingNumberManualOverrideRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .outgoing_number_selection_request import OutgoingNumberSelectionRequest

        from .outgoing_number_selection_request import OutgoingNumberSelectionRequest

        fields: dict[str, Callable[[Any], None]] = {
            "fromPhoneNumberId": lambda n : setattr(self, 'from_phone_number_id', n.get_str_value()),
            "selection": lambda n : setattr(self, 'selection', n.get_object_value(OutgoingNumberSelectionRequest)),
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
        writer.write_str_value("fromPhoneNumberId", self.from_phone_number_id)
        writer.write_object_value("selection", self.selection)
        writer.write_additional_data_value(self.additional_data)
    

