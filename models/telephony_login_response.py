from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TelephonyLoginResponse(AdditionalDataHolder, Parsable):
    """
    Response model for telephony login token generation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The callback token value for this telephony login.
    callback_token: Optional[str] = None
    # The date and time for the expires at value on this telephony login.
    expires_at: Optional[datetime.datetime] = None
    # The password value for this telephony login.
    password: Optional[str] = None
    # The username value for this telephony login.
    username: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TelephonyLoginResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TelephonyLoginResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TelephonyLoginResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "callbackToken": lambda n : setattr(self, 'callback_token', n.get_str_value()),
            "expiresAt": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "username": lambda n : setattr(self, 'username', n.get_str_value()),
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
        writer.write_str_value("callbackToken", self.callback_token)
        writer.write_datetime_value("expiresAt", self.expires_at)
        writer.write_str_value("password", self.password)
        writer.write_str_value("username", self.username)
        writer.write_additional_data_value(self.additional_data)
    

