from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AnalyticsDateRange(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The bucketSize property
    bucket_size: Optional[int] = None
    # The endAt property
    end_at: Optional[datetime.datetime] = None
    # The startAt property
    start_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalyticsDateRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalyticsDateRange
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalyticsDateRange()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "bucketSize": lambda n : setattr(self, 'bucket_size', n.get_int_value()),
            "endAt": lambda n : setattr(self, 'end_at', n.get_datetime_value()),
            "startAt": lambda n : setattr(self, 'start_at', n.get_datetime_value()),
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
        writer.write_int_value("bucketSize", self.bucket_size)
        writer.write_datetime_value("endAt", self.end_at)
        writer.write_datetime_value("startAt", self.start_at)
        writer.write_additional_data_value(self.additional_data)
    

