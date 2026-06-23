from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TrustedFormCertificate(AdditionalDataHolder, Parsable):
    """
    API DTO containing trusted form certificate data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date and time for the created at value on this TrustedForm certificate.
    created_at: Optional[datetime.datetime] = None
    # The unique ID for this TrustedForm certificate.
    id: Optional[str] = None
    # The source value for this TrustedForm certificate.
    source: Optional[str] = None
    # The URL associated with this TrustedForm certificate.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TrustedFormCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrustedFormCertificate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TrustedFormCertificate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
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
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("id", self.id)
        writer.write_str_value("source", self.source)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    

