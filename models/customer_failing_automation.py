from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CustomerFailingAutomation(AdditionalDataHolder, Parsable):
    """
    Represents customer failing automation data exposed by Leadping analytics.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Unique identifier of the automation associated with this Leadping customer failing automation.
    automation_id: Optional[str] = None
    # Error associated with this Leadping customer failing automation.
    error: Optional[str] = None
    # Date and time when the customer failing automation failed.
    failed_at: Optional[datetime.datetime] = None
    # Human-readable name of the customer failing automation.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerFailingAutomation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerFailingAutomation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerFailingAutomation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "automationId": lambda n : setattr(self, 'automation_id', n.get_str_value()),
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "failedAt": lambda n : setattr(self, 'failed_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_str_value("automationId", self.automation_id)
        writer.write_str_value("error", self.error)
        writer.write_datetime_value("failedAt", self.failed_at)
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

