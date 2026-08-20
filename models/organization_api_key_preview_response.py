from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .id_name_pair import IdNamePair

@dataclass
class OrganizationApiKeyPreviewResponse(AdditionalDataHolder, Parsable):
    """
    Safe identifying and usage metadata for an organization API key. This model never contains the secret credential.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Date and time when Leadping began tracking the API key.
    created_at: Optional[datetime.datetime] = None
    # Whether the API key can currently authenticate requests.
    enabled: Optional[bool] = None
    # Date and time when the API key expires, or null when it does not expire.
    expires_at: Optional[datetime.datetime] = None
    # Date and time when the API key was first used.
    first_used_at: Optional[datetime.datetime] = None
    # Unique identifier of the API key.
    id: Optional[str] = None
    # Date and time when the API key was issued.
    issued_at: Optional[datetime.datetime] = None
    # Date and time when the API key was last used.
    last_used_at: Optional[datetime.datetime] = None
    # Date and time when the tracked API-key metadata was last modified.
    modified_at: Optional[datetime.datetime] = None
    # Human-readable name of the API key.
    name: Optional[str] = None
    # Organization that owns the API key.
    organization: Optional[IdNamePair] = None
    # Permission slugs granted to the API key.
    permissions: Optional[list[str]] = None
    # Masked value that can be used to identify the key without revealing its secret.
    preview: Optional[str] = None
    # Total number of tracked uses.
    total_uses: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationApiKeyPreviewResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationApiKeyPreviewResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationApiKeyPreviewResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .id_name_pair import IdNamePair

        from .id_name_pair import IdNamePair

        fields: dict[str, Callable[[Any], None]] = {
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "expiresAt": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "firstUsedAt": lambda n : setattr(self, 'first_used_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "issuedAt": lambda n : setattr(self, 'issued_at', n.get_datetime_value()),
            "lastUsedAt": lambda n : setattr(self, 'last_used_at', n.get_datetime_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_object_value(IdNamePair)),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_primitive_values(str)),
            "preview": lambda n : setattr(self, 'preview', n.get_str_value()),
            "totalUses": lambda n : setattr(self, 'total_uses', n.get_int_value()),
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
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_datetime_value("expiresAt", self.expires_at)
        writer.write_datetime_value("firstUsedAt", self.first_used_at)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("issuedAt", self.issued_at)
        writer.write_datetime_value("lastUsedAt", self.last_used_at)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_object_value("organization", self.organization)
        writer.write_collection_of_primitive_values("permissions", self.permissions)
        writer.write_str_value("preview", self.preview)
        writer.write_int_value("totalUses", self.total_uses)
        writer.write_additional_data_value(self.additional_data)
    

