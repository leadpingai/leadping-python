from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AutomationActionRunRecord(AdditionalDataHolder, Parsable):
    """
    API DTO containing automation action run record data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The action ID associated with this automation action run record.
    action_id: Optional[str] = None
    # The action type classification for this automation action run record.
    action_type: Optional[str] = None
    # The automation run ID associated with this automation action run record.
    automation_run_id: Optional[str] = None
    # The date and time for the completed at value on this automation action run record.
    completed_at: Optional[datetime.datetime] = None
    # The connection key value for this automation action run record.
    connection_key: Optional[str] = None
    # The error value for this automation action run record.
    error: Optional[str] = None
    # The execution key value for this automation action run record.
    execution_key: Optional[str] = None
    # The date and time when this action failed.
    failed_at: Optional[datetime.datetime] = None
    # The failure code value for this automation action run record.
    failure_code: Optional[str] = None
    # The unique ID for this automation action run record.
    id: Optional[str] = None
    # The date and time when this action will retry, if retrying is scheduled.
    next_retry_at: Optional[datetime.datetime] = None
    # The order value for this automation action run record.
    order: Optional[int] = None
    # The output value for this automation action run record.
    output: Optional[str] = None
    # The processing attempts value for this automation action run record.
    processing_attempts: Optional[int] = None
    # The date and time when this action was scheduled to run, if it is delayed.
    scheduled_at: Optional[datetime.datetime] = None
    # The date and time for the started at value on this automation action run record.
    started_at: Optional[datetime.datetime] = None
    # The current status for this automation action run record.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationActionRunRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationActionRunRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationActionRunRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "actionId": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "actionType": lambda n : setattr(self, 'action_type', n.get_str_value()),
            "automationRunId": lambda n : setattr(self, 'automation_run_id', n.get_str_value()),
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "connectionKey": lambda n : setattr(self, 'connection_key', n.get_str_value()),
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "executionKey": lambda n : setattr(self, 'execution_key', n.get_str_value()),
            "failedAt": lambda n : setattr(self, 'failed_at', n.get_datetime_value()),
            "failureCode": lambda n : setattr(self, 'failure_code', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "nextRetryAt": lambda n : setattr(self, 'next_retry_at', n.get_datetime_value()),
            "order": lambda n : setattr(self, 'order', n.get_int_value()),
            "output": lambda n : setattr(self, 'output', n.get_str_value()),
            "processingAttempts": lambda n : setattr(self, 'processing_attempts', n.get_int_value()),
            "scheduledAt": lambda n : setattr(self, 'scheduled_at', n.get_datetime_value()),
            "startedAt": lambda n : setattr(self, 'started_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_str_value("actionType", self.action_type)
        writer.write_str_value("automationRunId", self.automation_run_id)
        writer.write_datetime_value("completedAt", self.completed_at)
        writer.write_str_value("connectionKey", self.connection_key)
        writer.write_str_value("error", self.error)
        writer.write_str_value("executionKey", self.execution_key)
        writer.write_datetime_value("failedAt", self.failed_at)
        writer.write_str_value("failureCode", self.failure_code)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("nextRetryAt", self.next_retry_at)
        writer.write_int_value("order", self.order)
        writer.write_str_value("output", self.output)
        writer.write_int_value("processingAttempts", self.processing_attempts)
        writer.write_datetime_value("scheduledAt", self.scheduled_at)
        writer.write_datetime_value("startedAt", self.started_at)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

