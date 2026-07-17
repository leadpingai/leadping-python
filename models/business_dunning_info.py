from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BusinessDunningInfo(AdditionalDataHolder, Parsable):
    """
    Dunning state recorded after a failed recurring payment.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Date and time when this Leadping business dunning info was final cancellation.
    final_cancellation_at: Optional[datetime.datetime] = None
    # Date and time when this Leadping business dunning info was grace period ends.
    grace_period_ends_at: Optional[datetime.datetime] = None
    # Current last failed invoice status for this Leadping business dunning info.
    last_failed_invoice_status: Optional[str] = None
    # Date and time when this Leadping business dunning info was last updated.
    last_updated_at: Optional[datetime.datetime] = None
    # Date and time when the next retry is scheduled.
    next_retry_at: Optional[datetime.datetime] = None
    # Date and time when this Leadping business dunning info was outbound restricted.
    outbound_restricted_at: Optional[datetime.datetime] = None
    # Date and time when this Leadping business dunning info was outbound suspended.
    outbound_suspended_at: Optional[datetime.datetime] = None
    # Date and time when this Leadping business dunning info was payment failed.
    payment_failed_at: Optional[datetime.datetime] = None
    # Total number of retry attempt records represented by this Leadping business dunning info.
    retry_attempt_count: Optional[int] = None
    # Current stage for this Leadping business dunning info.
    stage: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessDunningInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessDunningInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessDunningInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "finalCancellationAt": lambda n : setattr(self, 'final_cancellation_at', n.get_datetime_value()),
            "gracePeriodEndsAt": lambda n : setattr(self, 'grace_period_ends_at', n.get_datetime_value()),
            "lastFailedInvoiceStatus": lambda n : setattr(self, 'last_failed_invoice_status', n.get_str_value()),
            "lastUpdatedAt": lambda n : setattr(self, 'last_updated_at', n.get_datetime_value()),
            "nextRetryAt": lambda n : setattr(self, 'next_retry_at', n.get_datetime_value()),
            "outboundRestrictedAt": lambda n : setattr(self, 'outbound_restricted_at', n.get_datetime_value()),
            "outboundSuspendedAt": lambda n : setattr(self, 'outbound_suspended_at', n.get_datetime_value()),
            "paymentFailedAt": lambda n : setattr(self, 'payment_failed_at', n.get_datetime_value()),
            "retryAttemptCount": lambda n : setattr(self, 'retry_attempt_count', n.get_int_value()),
            "stage": lambda n : setattr(self, 'stage', n.get_str_value()),
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
        writer.write_datetime_value("finalCancellationAt", self.final_cancellation_at)
        writer.write_datetime_value("gracePeriodEndsAt", self.grace_period_ends_at)
        writer.write_str_value("lastFailedInvoiceStatus", self.last_failed_invoice_status)
        writer.write_datetime_value("lastUpdatedAt", self.last_updated_at)
        writer.write_datetime_value("nextRetryAt", self.next_retry_at)
        writer.write_datetime_value("outboundRestrictedAt", self.outbound_restricted_at)
        writer.write_datetime_value("outboundSuspendedAt", self.outbound_suspended_at)
        writer.write_datetime_value("paymentFailedAt", self.payment_failed_at)
        writer.write_int_value("retryAttemptCount", self.retry_attempt_count)
        writer.write_str_value("stage", self.stage)
        writer.write_additional_data_value(self.additional_data)
    

