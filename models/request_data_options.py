from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .exact_match_filter import ExactMatchFilter
    from .order_by_option import OrderByOption
    from .range_filter import RangeFilter

@dataclass
class RequestDataOptions(AdditionalDataHolder, Parsable):
    """
    Options for flexible, efficient, and explicit querying in Cosmos DB or similar repositories.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Opaque Cosmos DB continuation token. ‑ on the **first** request. ‑ Client must echo back the NextToken it received from the previous page.
    continuation_token: Optional[str] = None
    # Key-value exact match filters (e.g., Status = Active).
    filters: Optional[list[ExactMatchFilter]] = None
    # Whether to include the total count in the response (for pagination).
    include_count: Optional[bool] = None
    # List of sort instructions, in priority order.
    order_by: Optional[list[OrderByOption]] = None
    # Maximum items to return in one page
    page_size: Optional[int] = None
    # Advanced range-based filters (e.g., Price > 50 and Price <= 200).
    range_filters: Optional[list[RangeFilter]] = None
    # The search term to filter results (applied to ).
    search: Optional[str] = None
    # The list of fields to apply the Search term to (must be string properties).
    search_fields: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RequestDataOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RequestDataOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RequestDataOptions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .exact_match_filter import ExactMatchFilter
        from .order_by_option import OrderByOption
        from .range_filter import RangeFilter

        from .exact_match_filter import ExactMatchFilter
        from .order_by_option import OrderByOption
        from .range_filter import RangeFilter

        fields: dict[str, Callable[[Any], None]] = {
            "continuationToken": lambda n : setattr(self, 'continuation_token', n.get_str_value()),
            "filters": lambda n : setattr(self, 'filters', n.get_collection_of_object_values(ExactMatchFilter)),
            "includeCount": lambda n : setattr(self, 'include_count', n.get_bool_value()),
            "orderBy": lambda n : setattr(self, 'order_by', n.get_collection_of_object_values(OrderByOption)),
            "pageSize": lambda n : setattr(self, 'page_size', n.get_int_value()),
            "rangeFilters": lambda n : setattr(self, 'range_filters', n.get_collection_of_object_values(RangeFilter)),
            "search": lambda n : setattr(self, 'search', n.get_str_value()),
            "searchFields": lambda n : setattr(self, 'search_fields', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("filters", self.filters)
        writer.write_bool_value("includeCount", self.include_count)
        writer.write_collection_of_object_values("orderBy", self.order_by)
        writer.write_int_value("pageSize", self.page_size)
        writer.write_collection_of_object_values("rangeFilters", self.range_filters)
        writer.write_str_value("search", self.search)
        writer.write_collection_of_primitive_values("searchFields", self.search_fields)
        writer.write_additional_data_value(self.additional_data)
    

