from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AutomationWorkflowActionResponse(AdditionalDataHolder, Parsable):
    """
    User-safe action status returned for lead automation workflow visibility.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Action type classification for this Leadping automation workflow action.
    action_type: Optional[str] = None
    # Human-readable action type display for this Leadping automation workflow action.
    action_type_display: Optional[str] = None
    # Date and time when the automation workflow action completed.
    completed_at: Optional[datetime.datetime] = None
    # Date and time when the automation workflow action failed.
    failed_at: Optional[datetime.datetime] = None
    # Reason or diagnostic code that explains the current outcome for this Leadping automation workflow action.
    failure_code: Optional[str] = None
    # Unique Leadping identifier for the automation workflow action.
    id: Optional[str] = None
    # Date and time when the next retry is scheduled.
    next_retry_at: Optional[datetime.datetime] = None
    # Total number of retry records represented by this Leadping automation workflow action.
    retry_count: Optional[int] = None
    # Safe reason associated with this Leadping automation workflow action.
    safe_reason: Optional[str] = None
    # Date and time when the automation workflow action was scheduled.
    scheduled_at: Optional[datetime.datetime] = None
    # Date and time when the workflow action was skipped.
    skipped_at: Optional[datetime.datetime] = None
    # Date and time when the automation workflow action started.
    started_at: Optional[datetime.datetime] = None
    # Current status for this Leadping automation workflow action.
    status: Optional[str] = None
    # Human-readable status display for this Leadping automation workflow action.
    status_display: Optional[str] = None
    # Human-readable step display name associated with this Leadping automation workflow action.
    step_display_name: Optional[str] = None
    # Unique identifier of the step associated with this Leadping automation workflow action.
    step_id: Optional[str] = None
    # Step order associated with this Leadping automation workflow action.
    step_order: Optional[int] = None
    # Human-readable user summary for this Leadping automation workflow action.
    user_summary: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationWorkflowActionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationWorkflowActionResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationWorkflowActionResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "actionType": lambda n : setattr(self, 'action_type', n.get_str_value()),
            "actionTypeDisplay": lambda n : setattr(self, 'action_type_display', n.get_str_value()),
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "failedAt": lambda n : setattr(self, 'failed_at', n.get_datetime_value()),
            "failureCode": lambda n : setattr(self, 'failure_code', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "nextRetryAt": lambda n : setattr(self, 'next_retry_at', n.get_datetime_value()),
            "retryCount": lambda n : setattr(self, 'retry_count', n.get_int_value()),
            "safeReason": lambda n : setattr(self, 'safe_reason', n.get_str_value()),
            "scheduledAt": lambda n : setattr(self, 'scheduled_at', n.get_datetime_value()),
            "skippedAt": lambda n : setattr(self, 'skipped_at', n.get_datetime_value()),
            "startedAt": lambda n : setattr(self, 'started_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "statusDisplay": lambda n : setattr(self, 'status_display', n.get_str_value()),
            "stepDisplayName": lambda n : setattr(self, 'step_display_name', n.get_str_value()),
            "stepId": lambda n : setattr(self, 'step_id', n.get_str_value()),
            "stepOrder": lambda n : setattr(self, 'step_order', n.get_int_value()),
            "userSummary": lambda n : setattr(self, 'user_summary', n.get_str_value()),
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
        writer.write_str_value("actionType", self.action_type)
        writer.write_str_value("actionTypeDisplay", self.action_type_display)
        writer.write_datetime_value("completedAt", self.completed_at)
        writer.write_datetime_value("failedAt", self.failed_at)
        writer.write_str_value("failureCode", self.failure_code)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("nextRetryAt", self.next_retry_at)
        writer.write_int_value("retryCount", self.retry_count)
        writer.write_str_value("safeReason", self.safe_reason)
        writer.write_datetime_value("scheduledAt", self.scheduled_at)
        writer.write_datetime_value("skippedAt", self.skipped_at)
        writer.write_datetime_value("startedAt", self.started_at)
        writer.write_str_value("status", self.status)
        writer.write_str_value("statusDisplay", self.status_display)
        writer.write_str_value("stepDisplayName", self.step_display_name)
        writer.write_str_value("stepId", self.step_id)
        writer.write_int_value("stepOrder", self.step_order)
        writer.write_str_value("userSummary", self.user_summary)
        writer.write_additional_data_value(self.additional_data)
    

