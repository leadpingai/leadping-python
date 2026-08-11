from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_status_change_export_row import LeadStatusChangeExportRow

@dataclass
class LeadStatusChangeExportResponse(AdditionalDataHolder, Parsable):
    """
    Describes lead status change export data returned by Leadping.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # MIME content type of the exported document.
    content_type: Optional[str] = None
    # Complete comma-separated values content encoded as text.
    csv: Optional[str] = None
    # Suggested file name for the exported CSV document.
    file_name: Optional[str] = None
    # The rows included with this lead status change export.
    rows: Optional[list[LeadStatusChangeExportRow]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadStatusChangeExportResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadStatusChangeExportResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadStatusChangeExportResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lead_status_change_export_row import LeadStatusChangeExportRow

        from .lead_status_change_export_row import LeadStatusChangeExportRow

        fields: dict[str, Callable[[Any], None]] = {
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "csv": lambda n : setattr(self, 'csv', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "rows": lambda n : setattr(self, 'rows', n.get_collection_of_object_values(LeadStatusChangeExportRow)),
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
    

