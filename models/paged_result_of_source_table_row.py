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
    Returns one page of query results together with page-size, optional total-count, and opaque continuation-cursor metadata.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Opaque cursor for requesting the next page, or null when no additional page is available; clients must not parse or modify it.
    continuation_token: Optional[str] = None
    # Items included in the current page, in the order determined by the query.
    items: Optional[list[SourceTableRow]] = None
    # Effective page-size limit used for this response, which may differ from the requested size because of server defaults or limits.
    page_size: Optional[int] = None
    # Total number of records matching the query across all pages, or null when counting was not requested or computed.
    total_count: Optional[int] = None
    
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
            "totalCount": lambda n : setattr(self, 'total_count', n.get_int_value()),
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
        writer.write_int_value("totalCount", self.total_count)
        writer.write_additional_data_value(self.additional_data)
    

