from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UserIdentity(AdditionalDataHolder, Parsable):
    """
    Represents a user's sign-in identity, including information about the identity provider and method of authentication.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Gets or sets the identity provider that issued the sign-in identity (e.g., "contoso.com" or "facebook.com").
    issuer: Optional[str] = None
    # Gets or sets the unique identifier assigned to the user by the identity provider.
    issuer_assigned_id: Optional[str] = None
    # Gets or sets the method of sign-in used by the identity (e.g., "emailAddress", "userName", or "federated").
    sign_in_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserIdentity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "issuerAssignedId": lambda n : setattr(self, 'issuer_assigned_id', n.get_str_value()),
            "signInType": lambda n : setattr(self, 'sign_in_type', n.get_str_value()),
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
        writer.write_str_value("issuer", self.issuer)
        writer.write_str_value("issuerAssignedId", self.issuer_assigned_id)
        writer.write_str_value("signInType", self.sign_in_type)
        writer.write_additional_data_value(self.additional_data)
    

