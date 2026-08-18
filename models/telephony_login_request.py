from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .telephony_login_request_device import TelephonyLoginRequest_device

@dataclass
class TelephonyLoginRequest(AdditionalDataHolder, Parsable):
    """
    Identifies the Leadping user and calling context for which a short-lived telephony client token should be issued.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier and display name of the related device.
    device: Optional[TelephonyLoginRequest_device] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TelephonyLoginRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TelephonyLoginRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TelephonyLoginRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .telephony_login_request_device import TelephonyLoginRequest_device

        from .telephony_login_request_device import TelephonyLoginRequest_device

        fields: dict[str, Callable[[Any], None]] = {
            "device": lambda n : setattr(self, 'device', n.get_object_value(TelephonyLoginRequest_device)),
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
        writer.write_object_value("device", self.device)
        writer.write_additional_data_value(self.additional_data)
    

