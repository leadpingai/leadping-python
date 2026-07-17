from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_workflow_action_response import AutomationWorkflowActionResponse
    from .automation_workflow_event_response import AutomationWorkflowEventResponse
    from .automation_workflow_run_response_automation import AutomationWorkflowRunResponse_automation
    from .automation_workflow_run_response_current_step import AutomationWorkflowRunResponse_currentStep

@dataclass
class AutomationWorkflowRunResponse(AdditionalDataHolder, Parsable):
    """
    User-safe automation workflow run status returned for a lead.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Collection of actions included with this Leadping automation workflow run.
    actions: Optional[list[AutomationWorkflowActionResponse]] = None
    # The ID and name for this automation.
    automation: Optional[AutomationWorkflowRunResponse_automation] = None
    # Unique identifier of the business associated with this Leadping automation workflow run.
    business_id: Optional[str] = None
    # Date and time when the automation workflow run was cancelled.
    cancelled_at: Optional[datetime.datetime] = None
    # Date and time when the automation workflow run completed.
    completed_at: Optional[datetime.datetime] = None
    # The ID and name for this currentStep.
    current_step: Optional[AutomationWorkflowRunResponse_currentStep] = None
    # Collection of events included with this Leadping automation workflow run.
    events: Optional[list[AutomationWorkflowEventResponse]] = None
    # Date and time when the automation workflow run failed.
    failed_at: Optional[datetime.datetime] = None
    # Unique Leadping identifier for the automation workflow run.
    id: Optional[str] = None
    # Human-readable last action summary for this Leadping automation workflow run.
    last_action_summary: Optional[str] = None
    # Reason or diagnostic code that explains the current outcome for this Leadping automation workflow run.
    last_error_code: Optional[str] = None
    # Human-readable last error message for this Leadping automation workflow run.
    last_error_message: Optional[str] = None
    # Date and time of the most recent execution for this Leadping automation workflow run.
    last_execution_at: Optional[datetime.datetime] = None
    # Unique identifier of the lead associated with this Leadping automation workflow run.
    lead_id: Optional[str] = None
    # Total number of max retry records represented by this Leadping automation workflow run.
    max_retry_count: Optional[int] = None
    # Date and time when the next execution is scheduled.
    next_execution_at: Optional[datetime.datetime] = None
    # Date and time when the next retry is scheduled.
    next_retry_at: Optional[datetime.datetime] = None
    # Total number of retry records represented by this Leadping automation workflow run.
    retry_count: Optional[int] = None
    # Reason or diagnostic code that explains the current outcome for this Leadping automation workflow run.
    skip_reason_code: Optional[str] = None
    # Human-readable skip reason display for this Leadping automation workflow run.
    skip_reason_display: Optional[str] = None
    # Date and time when the automation workflow run started.
    started_at: Optional[datetime.datetime] = None
    # Current status for this Leadping automation workflow run.
    status: Optional[str] = None
    # Human-readable status display for this Leadping automation workflow run.
    status_display: Optional[str] = None
    # Human-readable trigger display for this Leadping automation workflow run.
    trigger_display: Optional[str] = None
    # Trigger type classification for this Leadping automation workflow run.
    trigger_type: Optional[str] = None
    # Date and time when the automation workflow run was last updated.
    updated_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationWorkflowRunResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationWorkflowRunResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationWorkflowRunResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automation_workflow_action_response import AutomationWorkflowActionResponse
        from .automation_workflow_event_response import AutomationWorkflowEventResponse
        from .automation_workflow_run_response_automation import AutomationWorkflowRunResponse_automation
        from .automation_workflow_run_response_current_step import AutomationWorkflowRunResponse_currentStep

        from .automation_workflow_action_response import AutomationWorkflowActionResponse
        from .automation_workflow_event_response import AutomationWorkflowEventResponse
        from .automation_workflow_run_response_automation import AutomationWorkflowRunResponse_automation
        from .automation_workflow_run_response_current_step import AutomationWorkflowRunResponse_currentStep

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(AutomationWorkflowActionResponse)),
            "automation": lambda n : setattr(self, 'automation', n.get_object_value(AutomationWorkflowRunResponse_automation)),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "cancelledAt": lambda n : setattr(self, 'cancelled_at', n.get_datetime_value()),
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "currentStep": lambda n : setattr(self, 'current_step', n.get_object_value(AutomationWorkflowRunResponse_currentStep)),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(AutomationWorkflowEventResponse)),
            "failedAt": lambda n : setattr(self, 'failed_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lastActionSummary": lambda n : setattr(self, 'last_action_summary', n.get_str_value()),
            "lastErrorCode": lambda n : setattr(self, 'last_error_code', n.get_str_value()),
            "lastErrorMessage": lambda n : setattr(self, 'last_error_message', n.get_str_value()),
            "lastExecutionAt": lambda n : setattr(self, 'last_execution_at', n.get_datetime_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "maxRetryCount": lambda n : setattr(self, 'max_retry_count', n.get_int_value()),
            "nextExecutionAt": lambda n : setattr(self, 'next_execution_at', n.get_datetime_value()),
            "nextRetryAt": lambda n : setattr(self, 'next_retry_at', n.get_datetime_value()),
            "retryCount": lambda n : setattr(self, 'retry_count', n.get_int_value()),
            "skipReasonCode": lambda n : setattr(self, 'skip_reason_code', n.get_str_value()),
            "skipReasonDisplay": lambda n : setattr(self, 'skip_reason_display', n.get_str_value()),
            "startedAt": lambda n : setattr(self, 'started_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "statusDisplay": lambda n : setattr(self, 'status_display', n.get_str_value()),
            "triggerDisplay": lambda n : setattr(self, 'trigger_display', n.get_str_value()),
            "triggerType": lambda n : setattr(self, 'trigger_type', n.get_str_value()),
            "updatedAt": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
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
        writer.write_collection_of_object_values("actions", self.actions)
        writer.write_object_value("automation", self.automation)
        writer.write_str_value("businessId", self.business_id)
        writer.write_datetime_value("cancelledAt", self.cancelled_at)
        writer.write_datetime_value("completedAt", self.completed_at)
        writer.write_object_value("currentStep", self.current_step)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_datetime_value("failedAt", self.failed_at)
        writer.write_str_value("id", self.id)
        writer.write_str_value("lastActionSummary", self.last_action_summary)
        writer.write_str_value("lastErrorCode", self.last_error_code)
        writer.write_str_value("lastErrorMessage", self.last_error_message)
        writer.write_datetime_value("lastExecutionAt", self.last_execution_at)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_int_value("maxRetryCount", self.max_retry_count)
        writer.write_datetime_value("nextExecutionAt", self.next_execution_at)
        writer.write_datetime_value("nextRetryAt", self.next_retry_at)
        writer.write_int_value("retryCount", self.retry_count)
        writer.write_str_value("skipReasonCode", self.skip_reason_code)
        writer.write_str_value("skipReasonDisplay", self.skip_reason_display)
        writer.write_datetime_value("startedAt", self.started_at)
        writer.write_str_value("status", self.status)
        writer.write_str_value("statusDisplay", self.status_display)
        writer.write_str_value("triggerDisplay", self.trigger_display)
        writer.write_str_value("triggerType", self.trigger_type)
        writer.write_datetime_value("updatedAt", self.updated_at)
        writer.write_additional_data_value(self.additional_data)
    

