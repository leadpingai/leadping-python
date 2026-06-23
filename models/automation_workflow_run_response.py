from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_workflow_action_response import AutomationWorkflowActionResponse
    from .automation_workflow_event_response import AutomationWorkflowEventResponse

@dataclass
class AutomationWorkflowRunResponse(AdditionalDataHolder, Parsable):
    """
    User-safe automation workflow run status returned for a lead.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The actions property
    actions: Optional[list[AutomationWorkflowActionResponse]] = None
    # The automationId property
    automation_id: Optional[str] = None
    # The automationName property
    automation_name: Optional[str] = None
    # The businessId property
    business_id: Optional[str] = None
    # The cancelledAt property
    cancelled_at: Optional[datetime.datetime] = None
    # The completedAt property
    completed_at: Optional[datetime.datetime] = None
    # The correlationId property
    correlation_id: Optional[str] = None
    # The currentStepId property
    current_step_id: Optional[str] = None
    # The currentStepName property
    current_step_name: Optional[str] = None
    # The events property
    events: Optional[list[AutomationWorkflowEventResponse]] = None
    # The executionKey property
    execution_key: Optional[str] = None
    # The failedAt property
    failed_at: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The internalErrorDetails property
    internal_error_details: Optional[str] = None
    # The lastActionSummary property
    last_action_summary: Optional[str] = None
    # The lastErrorCode property
    last_error_code: Optional[str] = None
    # The lastErrorMessage property
    last_error_message: Optional[str] = None
    # The lastExecutionAt property
    last_execution_at: Optional[datetime.datetime] = None
    # The leadId property
    lead_id: Optional[str] = None
    # The maxRetryCount property
    max_retry_count: Optional[int] = None
    # The nextExecutionAt property
    next_execution_at: Optional[datetime.datetime] = None
    # The nextRetryAt property
    next_retry_at: Optional[datetime.datetime] = None
    # The retryCount property
    retry_count: Optional[int] = None
    # The skipReasonCode property
    skip_reason_code: Optional[str] = None
    # The skipReasonDisplay property
    skip_reason_display: Optional[str] = None
    # The sourceEventId property
    source_event_id: Optional[str] = None
    # The startedAt property
    started_at: Optional[datetime.datetime] = None
    # The status property
    status: Optional[str] = None
    # The statusDisplay property
    status_display: Optional[str] = None
    # The triggerDisplay property
    trigger_display: Optional[str] = None
    # The triggerType property
    trigger_type: Optional[str] = None
    # The updatedAt property
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

        from .automation_workflow_action_response import AutomationWorkflowActionResponse
        from .automation_workflow_event_response import AutomationWorkflowEventResponse

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(AutomationWorkflowActionResponse)),
            "automationId": lambda n : setattr(self, 'automation_id', n.get_str_value()),
            "automationName": lambda n : setattr(self, 'automation_name', n.get_str_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "cancelledAt": lambda n : setattr(self, 'cancelled_at', n.get_datetime_value()),
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "currentStepId": lambda n : setattr(self, 'current_step_id', n.get_str_value()),
            "currentStepName": lambda n : setattr(self, 'current_step_name', n.get_str_value()),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(AutomationWorkflowEventResponse)),
            "executionKey": lambda n : setattr(self, 'execution_key', n.get_str_value()),
            "failedAt": lambda n : setattr(self, 'failed_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "internalErrorDetails": lambda n : setattr(self, 'internal_error_details', n.get_str_value()),
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
            "sourceEventId": lambda n : setattr(self, 'source_event_id', n.get_str_value()),
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
        writer.write_str_value("automationId", self.automation_id)
        writer.write_str_value("automationName", self.automation_name)
        writer.write_str_value("businessId", self.business_id)
        writer.write_datetime_value("cancelledAt", self.cancelled_at)
        writer.write_datetime_value("completedAt", self.completed_at)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_str_value("currentStepId", self.current_step_id)
        writer.write_str_value("currentStepName", self.current_step_name)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_str_value("executionKey", self.execution_key)
        writer.write_datetime_value("failedAt", self.failed_at)
        writer.write_str_value("id", self.id)
        writer.write_str_value("internalErrorDetails", self.internal_error_details)
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
        writer.write_str_value("sourceEventId", self.source_event_id)
        writer.write_datetime_value("startedAt", self.started_at)
        writer.write_str_value("status", self.status)
        writer.write_str_value("statusDisplay", self.status_display)
        writer.write_str_value("triggerDisplay", self.trigger_display)
        writer.write_str_value("triggerType", self.trigger_type)
        writer.write_datetime_value("updatedAt", self.updated_at)
        writer.write_additional_data_value(self.additional_data)
    

