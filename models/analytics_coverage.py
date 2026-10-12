from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AnalyticsCoverage(AdditionalDataHolder, Parsable):
    """
    States whether missing historical evidence can make reported counts incomplete.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The completeFrom property
    complete_from: Optional[datetime.datetime] = None
    # The detail property
    detail: Optional[str] = None
    # The isPartial property
    is_partial: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalyticsCoverage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalyticsCoverage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalyticsCoverage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "completeFrom": lambda n : setattr(self, 'complete_from', n.get_datetime_value()),
            "detail": lambda n : setattr(self, 'detail', n.get_str_value()),
            "isPartial": lambda n : setattr(self, 'is_partial', n.get_bool_value()),
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
        writer.write_datetime_value("completeFrom", self.complete_from)
        writer.write_str_value("detail", self.detail)
        writer.write_bool_value("isPartial", self.is_partial)
        writer.write_additional_data_value(self.additional_data)
    

