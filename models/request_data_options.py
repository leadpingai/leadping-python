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
    Defines cursor pagination, sorting, search, exact-match filters, and range filters for a structured API query.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Opaque cursor returned by the previous paged response; omit it when requesting the first page and do not parse or modify it.
    continuation_token: Optional[str] = None
    # Exact-match conditions that require each named field to equal its supplied value.
    filters: Optional[list[ExactMatchFilter]] = None
    # Whether the response should include the total number of matching records; counting may increase query cost or latency.
    include_count: Optional[bool] = None
    # Sort instructions applied in priority order, with the first entry acting as the primary sort.
    order_by: Optional[list[OrderByOption]] = None
    # Maximum number of items requested for one page; the server may enforce a lower maximum or apply a default.
    page_size: Optional[int] = None
    # Range conditions that constrain comparable fields with inclusive or exclusive lower and upper bounds.
    range_filters: Optional[list[RangeFilter]] = None
    # Free-text search term applied to the configured SearchFields.
    search: Optional[str] = None
    # Serializable string field names searched for Search; supported names are determined by the queried resource.
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
    

