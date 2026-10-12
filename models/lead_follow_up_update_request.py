from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LeadFollowUpUpdateRequest(AdditionalDataHolder, Parsable):
    """
    Completes or reschedules exactly the follow-up version the operator viewed.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The new time, or null to complete the follow-up.
    due_at: Optional[datetime.datetime] = None
    # The expectedRevision property
    expected_revision: Optional[int] = None
    # The expectedStatusId property
    expected_status_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadFollowUpUpdateRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadFollowUpUpdateRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadFollowUpUpdateRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "dueAt": lambda n : setattr(self, 'due_at', n.get_datetime_value()),
            "expectedRevision": lambda n : setattr(self, 'expected_revision', n.get_int_value()),
            "expectedStatusId": lambda n : setattr(self, 'expected_status_id', n.get_str_value()),
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
        writer.write_datetime_value("dueAt", self.due_at)
        writer.write_int_value("expectedRevision", self.expected_revision)
        writer.write_str_value("expectedStatusId", self.expected_status_id)
        writer.write_additional_data_value(self.additional_data)
    

