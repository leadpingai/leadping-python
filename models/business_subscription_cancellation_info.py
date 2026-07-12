from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BusinessSubscriptionCancellationInfo(AdditionalDataHolder, Parsable):
    """
    Captured subscription cancellation feedback for retention and churn analysis.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether the cancellation was scheduled for period end.
    cancel_at_period_end: Optional[bool] = None
    # The competitor named by the user, when applicable.
    competitor: Optional[str] = None
    # The missing feature named by the user, when applicable.
    missing_feature: Optional[str] = None
    # Additional cancellation notes supplied by the user.
    notes: Optional[str] = None
    # The human-readable cancellation reason selected by the user.
    reason: Optional[str] = None
    # The normalized cancellation reason code selected by the user.
    reason_code: Optional[str] = None
    # The date and time when cancellation was requested.
    requested_at: Optional[datetime.datetime] = None
    # The user who requested cancellation.
    requested_by_user_id: Optional[str] = None
    # The technical issue details supplied by the user, when applicable.
    technical_issues: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessSubscriptionCancellationInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessSubscriptionCancellationInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessSubscriptionCancellationInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cancelAtPeriodEnd": lambda n : setattr(self, 'cancel_at_period_end', n.get_bool_value()),
            "competitor": lambda n : setattr(self, 'competitor', n.get_str_value()),
            "missingFeature": lambda n : setattr(self, 'missing_feature', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "reasonCode": lambda n : setattr(self, 'reason_code', n.get_str_value()),
            "requestedAt": lambda n : setattr(self, 'requested_at', n.get_datetime_value()),
            "requestedByUserId": lambda n : setattr(self, 'requested_by_user_id', n.get_str_value()),
            "technicalIssues": lambda n : setattr(self, 'technical_issues', n.get_str_value()),
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
        writer.write_bool_value("cancelAtPeriodEnd", self.cancel_at_period_end)
        writer.write_str_value("competitor", self.competitor)
        writer.write_str_value("missingFeature", self.missing_feature)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("reasonCode", self.reason_code)
        writer.write_datetime_value("requestedAt", self.requested_at)
        writer.write_str_value("requestedByUserId", self.requested_by_user_id)
        writer.write_str_value("technicalIssues", self.technical_issues)
        writer.write_additional_data_value(self.additional_data)
    

