from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .disposition_export_row import DispositionExportRow

@dataclass
class DispositionExportResponse(AdditionalDataHolder, Parsable):
    """
    API response containing disposition export data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The content type classification for this disposition export.
    content_type: Optional[str] = None
    # The csv value for this disposition export.
    csv: Optional[str] = None
    # The file name value for this disposition export.
    file_name: Optional[str] = None
    # The rows included with this disposition export.
    rows: Optional[list[DispositionExportRow]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DispositionExportResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DispositionExportResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DispositionExportResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .disposition_export_row import DispositionExportRow

        from .disposition_export_row import DispositionExportRow

        fields: dict[str, Callable[[Any], None]] = {
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "csv": lambda n : setattr(self, 'csv', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "rows": lambda n : setattr(self, 'rows', n.get_collection_of_object_values(DispositionExportRow)),
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
        writer.write_str_value("csv", self.csv)
        writer.write_str_value("fileName", self.file_name)
        writer.write_collection_of_object_values("rows", self.rows)
        writer.write_additional_data_value(self.additional_data)
    

