from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MessageMediaAttachment(AdditionalDataHolder, Parsable):
    """
    Media attached to an SMS/MMS conversation event.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # MIME content type of the media attachment.
    content_type: Optional[str] = None
    # Original file name of the media attachment, when available.
    file_name: Optional[str] = None
    # SHA-256 digest of the media content, when available.
    sha256: Optional[str] = None
    # Size of the media attachment in bytes.
    size: Optional[int] = None
    # URL from which the media attachment can be retrieved.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MessageMediaAttachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MessageMediaAttachment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MessageMediaAttachment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "sha256": lambda n : setattr(self, 'sha256', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_str_value("contentType", self.content_type)
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("sha256", self.sha256)
        writer.write_int_value("size", self.size)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    

