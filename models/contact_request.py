from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ContactRequest(AdditionalDataHolder, Parsable):
    """
    Request model for submitting a contact form.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The email address associated with this contact.
    email: Optional[str] = None
    # The message value for this contact.
    message: Optional[str] = None
    # The human-readable name shown for this contact.
    name: Optional[str] = None
    # The token supplied to authorize or complete this contact.
    token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContactRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContactRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContactRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
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
        writer.write_str_value("email", self.email)
        writer.write_str_value("message", self.message)
        writer.write_str_value("name", self.name)
        writer.write_str_value("token", self.token)
        writer.write_additional_data_value(self.additional_data)
    

