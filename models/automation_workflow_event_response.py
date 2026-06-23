from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AutomationWorkflowEventResponse(AdditionalDataHolder, Parsable):
    """
    User-safe workflow history event returned for lead automation status.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The actionId property
    action_id: Optional[str] = None
    # The adminDiagnostics property
    admin_diagnostics: Optional[str] = None
    # The eventType property
    event_type: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The occurredAt property
    occurred_at: Optional[datetime.datetime] = None
    # The reasonCode property
    reason_code: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The statusDisplay property
    status_display: Optional[str] = None
    # The stepId property
    step_id: Optional[str] = None
    # The summary property
    summary: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationWorkflowEventResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationWorkflowEventResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationWorkflowEventResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "actionId": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "adminDiagnostics": lambda n : setattr(self, 'admin_diagnostics', n.get_str_value()),
            "eventType": lambda n : setattr(self, 'event_type', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "occurredAt": lambda n : setattr(self, 'occurred_at', n.get_datetime_value()),
            "reasonCode": lambda n : setattr(self, 'reason_code', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "statusDisplay": lambda n : setattr(self, 'status_display', n.get_str_value()),
            "stepId": lambda n : setattr(self, 'step_id', n.get_str_value()),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
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
        writer.write_str_value("actionId", self.action_id)
        writer.write_str_value("adminDiagnostics", self.admin_diagnostics)
        writer.write_str_value("eventType", self.event_type)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("occurredAt", self.occurred_at)
        writer.write_str_value("reasonCode", self.reason_code)
        writer.write_str_value("status", self.status)
        writer.write_str_value("statusDisplay", self.status_display)
        writer.write_str_value("stepId", self.step_id)
        writer.write_str_value("summary", self.summary)
        writer.write_additional_data_value(self.additional_data)
    

