from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .organization_api_key_preview_response import OrganizationApiKeyPreviewResponse

@dataclass
class OrganizationApiKeyIssueResponse(AdditionalDataHolder, Parsable):
    """
    Returns a newly issued organization API key and its identifying metadata; the secret credential is shown only in this response.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # API key associated with this Leadping organization API key issue.
    api_key: Optional[OrganizationApiKeyPreviewResponse] = None
    # Date and time when the organization API key issue expires.
    expires_at: Optional[datetime.datetime] = None
    # Secret token returned once when the Leadping API key is issued.
    secret: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationApiKeyIssueResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationApiKeyIssueResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationApiKeyIssueResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .organization_api_key_preview_response import OrganizationApiKeyPreviewResponse

        from .organization_api_key_preview_response import OrganizationApiKeyPreviewResponse

        fields: dict[str, Callable[[Any], None]] = {
            "apiKey": lambda n : setattr(self, 'api_key', n.get_object_value(OrganizationApiKeyPreviewResponse)),
            "expiresAt": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "secret": lambda n : setattr(self, 'secret', n.get_str_value()),
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
        writer.write_object_value("apiKey", self.api_key)
        writer.write_datetime_value("expiresAt", self.expires_at)
        writer.write_str_value("secret", self.secret)
        writer.write_additional_data_value(self.additional_data)
    

