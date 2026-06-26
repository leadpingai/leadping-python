from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_action_run_record import AutomationActionRunRecord
    from .automation_run_record_context_snapshot import AutomationRunRecord_contextSnapshot

@dataclass
class AutomationRunRecord(AdditionalDataHolder, Parsable):
    """
    History record schema for Leadping API automation run record data exposed in automation and audit views.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Automation actions configured or returned for this workflow.
    actions: Optional[list[AutomationActionRunRecord]] = None
    # Automation ID connected to this workflow, run, or event.
    automation_id: Optional[str] = None
    # Business ID that owns this automation run.
    business_id: Optional[str] = None
    # UTC timestamp when processing completed for this automation run record.
    completed_at: Optional[datetime.datetime] = None
    # Snapshot of request context captured when this automation run record was created.
    context_snapshot: Optional[AutomationRunRecord_contextSnapshot] = None
    # Error text returned while processing this automation run record.
    error: Optional[str] = None
    # Idempotency key used to identify a unique automation workflow execution.
    execution_key: Optional[str] = None
    # Execution mode used for automation preview or live workflow processing.
    execution_mode: Optional[str] = None
    # Machine-readable failure code for troubleshooting this automation run record.
    failure_code: Optional[str] = None
    # Unique Leadping identifier for this automation run record.
    id: Optional[str] = None
    # UTC timestamp when Leadping last attempted to process this automation run.
    last_attempt_at: Optional[datetime.datetime] = None
    # Lead ID that triggered this automation run, when the run is lead-based.
    lead_id: Optional[str] = None
    # Number of processing attempts made for this workflow or delivery request.
    processing_attempts: Optional[int] = None
    # Human-readable reason explaining why Leadping skipped this automation run.
    skipped_reason: Optional[str] = None
    # Source event ID that triggered this workflow or outbound delivery.
    source_event_id: Optional[str] = None
    # UTC timestamp when processing started for this automation run record.
    started_at: Optional[datetime.datetime] = None
    # Current lifecycle status for this automation run record in the Leadping API.
    status: Optional[str] = None
    # Automation trigger type that starts the workflow.
    trigger_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationRunRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationRunRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationRunRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automation_action_run_record import AutomationActionRunRecord
        from .automation_run_record_context_snapshot import AutomationRunRecord_contextSnapshot

        from .automation_action_run_record import AutomationActionRunRecord
        from .automation_run_record_context_snapshot import AutomationRunRecord_contextSnapshot

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(AutomationActionRunRecord)),
            "automationId": lambda n : setattr(self, 'automation_id', n.get_str_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "contextSnapshot": lambda n : setattr(self, 'context_snapshot', n.get_object_value(AutomationRunRecord_contextSnapshot)),
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "executionKey": lambda n : setattr(self, 'execution_key', n.get_str_value()),
            "executionMode": lambda n : setattr(self, 'execution_mode', n.get_str_value()),
            "failureCode": lambda n : setattr(self, 'failure_code', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lastAttemptAt": lambda n : setattr(self, 'last_attempt_at', n.get_datetime_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "processingAttempts": lambda n : setattr(self, 'processing_attempts', n.get_int_value()),
            "skippedReason": lambda n : setattr(self, 'skipped_reason', n.get_str_value()),
            "sourceEventId": lambda n : setattr(self, 'source_event_id', n.get_str_value()),
            "startedAt": lambda n : setattr(self, 'started_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "triggerType": lambda n : setattr(self, 'trigger_type', n.get_str_value()),
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
        writer.write_str_value("businessId", self.business_id)
        writer.write_datetime_value("completedAt", self.completed_at)
        writer.write_object_value("contextSnapshot", self.context_snapshot)
        writer.write_str_value("error", self.error)
        writer.write_str_value("executionKey", self.execution_key)
        writer.write_str_value("executionMode", self.execution_mode)
        writer.write_str_value("failureCode", self.failure_code)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("lastAttemptAt", self.last_attempt_at)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_int_value("processingAttempts", self.processing_attempts)
        writer.write_str_value("skippedReason", self.skipped_reason)
        writer.write_str_value("sourceEventId", self.source_event_id)
        writer.write_datetime_value("startedAt", self.started_at)
        writer.write_str_value("status", self.status)
        writer.write_str_value("triggerType", self.trigger_type)
        writer.write_additional_data_value(self.additional_data)
    

