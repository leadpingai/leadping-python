from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BrowserCallApproval(AdditionalDataHolder, Parsable):
    """
    Server-approved parameters for one outbound browser call.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The callerNumber property
    caller_number: Optional[str] = None
    # The clientState property
    client_state: Optional[str] = None
    # The destinationNumber property
    destination_number: Optional[str] = None
    # The expiresAt property
    expires_at: Optional[datetime.datetime] = None
    # The maximumDurationSeconds property
    maximum_duration_seconds: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BrowserCallApproval:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BrowserCallApproval
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BrowserCallApproval()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "callerNumber": lambda n : setattr(self, 'caller_number', n.get_str_value()),
            "clientState": lambda n : setattr(self, 'client_state', n.get_str_value()),
            "destinationNumber": lambda n : setattr(self, 'destination_number', n.get_str_value()),
            "expiresAt": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "maximumDurationSeconds": lambda n : setattr(self, 'maximum_duration_seconds', n.get_int_value()),
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
        writer.write_str_value("callerNumber", self.caller_number)
        writer.write_str_value("clientState", self.client_state)
        writer.write_str_value("destinationNumber", self.destination_number)
        writer.write_datetime_value("expiresAt", self.expires_at)
        writer.write_int_value("maximumDurationSeconds", self.maximum_duration_seconds)
        writer.write_additional_data_value(self.additional_data)
    

