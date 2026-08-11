from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .organization_member_role import OrganizationMemberRole

@dataclass
class OrganizationMemberRequest(AdditionalDataHolder, Parsable):
    """
    Defines the fields clients can send when working with organization user.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Email address for the person represented by this organization user request.
    email: Optional[str] = None
    # Organization role assigned to the user.
    role: Optional[OrganizationMemberRole] = None
    # User ID to add, update, or remove from the organization.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationMemberRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationMemberRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationMemberRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .organization_member_role import OrganizationMemberRole

        from .organization_member_role import OrganizationMemberRole

        fields: dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(OrganizationMemberRole)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_enum_value("role", self.role)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

