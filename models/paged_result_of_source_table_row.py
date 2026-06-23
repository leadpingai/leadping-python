from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .source_table_row import SourceTableRow

@dataclass
class PagedResultOfSourceTableRow(AdditionalDataHolder, Parsable):
    """
    A generic container for paginated results returned to the client.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Opaque storage continuation token. ‑ `null` → the current page was the last page.
    continuation_token: Optional[str] = None
    # The subset of items returned for the current page.
    items: Optional[list[SourceTableRow]] = None
    # The number of items returned per page in the response. This may reflect the client's requested page size, or a server-defined default or limit.
    page_size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PagedResultOfSourceTableRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PagedResultOfSourceTableRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PagedResultOfSourceTableRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .source_table_row import SourceTableRow

        from .source_table_row import SourceTableRow

        fields: dict[str, Callable[[Any], None]] = {
            "continuationToken": lambda n : setattr(self, 'continuation_token', n.get_str_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(SourceTableRow)),
            "pageSize": lambda n : setattr(self, 'page_size', n.get_int_value()),
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
        writer.write_str_value("continuationToken", self.continuation_token)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_int_value("pageSize", self.page_size)
        writer.write_additional_data_value(self.additional_data)
    

