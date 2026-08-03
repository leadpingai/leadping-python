from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .media_post_request_body_headers import MediaPostRequestBody_Headers

@dataclass
class MediaPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The ContentDisposition property
    content_disposition: Optional[str] = None
    # The ContentType property
    content_type: Optional[str] = None
    # The FileName property
    file_name: Optional[str] = None
    # The Headers property
    headers: Optional[MediaPostRequestBody_Headers] = None
    # The Length property
    length: Optional[int] = None
    # The Name property
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MediaPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MediaPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MediaPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .media_post_request_body_headers import MediaPostRequestBody_Headers

        from .media_post_request_body_headers import MediaPostRequestBody_Headers

        fields: dict[str, Callable[[Any], None]] = {
            "ContentDisposition": lambda n : setattr(self, 'content_disposition', n.get_str_value()),
            "ContentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "FileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "Headers": lambda n : setattr(self, 'headers', n.get_object_value(MediaPostRequestBody_Headers)),
            "Length": lambda n : setattr(self, 'length', n.get_int_value()),
            "Name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_str_value("ContentDisposition", self.content_disposition)
        writer.write_str_value("ContentType", self.content_type)
        writer.write_str_value("FileName", self.file_name)
        writer.write_object_value("Headers", self.headers)
        writer.write_int_value("Length", self.length)
        writer.write_str_value("Name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

