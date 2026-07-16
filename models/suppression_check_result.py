from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SuppressionCheckResult(AdditionalDataHolder, Parsable):
    """
    API response containing suppression check result data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether this ion check result allows ed.
    allowed: Optional[bool] = None
    # The business ID associated with this ion check result.
    business_id: Optional[str] = None
    # The channel value for this ion check result.
    channel: Optional[str] = None
    # The human-readable customer reason explaining this ion check result.
    customer_reason: Optional[str] = None
    # The normalized email value for this ion check result.
    normalized_email: Optional[str] = None
    # The phone number associated with this ion check result.
    normalized_phone_number: Optional[str] = None
    # The recipient identifier value for this ion check result.
    recipient_identifier: Optional[str] = None
    # The source value on the active suppression entry that blocked this check.
    source: Optional[str] = None
    # The date and time the blocking suppression became active.
    suppressed_at: Optional[datetime.datetime] = None
    # The suppression entry ID associated with this ion check result.
    suppression_entry_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SuppressionCheckResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SuppressionCheckResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SuppressionCheckResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowed": lambda n : setattr(self, 'allowed', n.get_bool_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "channel": lambda n : setattr(self, 'channel', n.get_str_value()),
            "customerReason": lambda n : setattr(self, 'customer_reason', n.get_str_value()),
            "normalizedEmail": lambda n : setattr(self, 'normalized_email', n.get_str_value()),
            "normalizedPhoneNumber": lambda n : setattr(self, 'normalized_phone_number', n.get_str_value()),
            "recipientIdentifier": lambda n : setattr(self, 'recipient_identifier', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "suppressedAt": lambda n : setattr(self, 'suppressed_at', n.get_datetime_value()),
            "suppressionEntryId": lambda n : setattr(self, 'suppression_entry_id', n.get_str_value()),
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
        writer.write_bool_value("allowed", self.allowed)
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("channel", self.channel)
        writer.write_str_value("customerReason", self.customer_reason)
        writer.write_str_value("normalizedEmail", self.normalized_email)
        writer.write_str_value("normalizedPhoneNumber", self.normalized_phone_number)
        writer.write_str_value("recipientIdentifier", self.recipient_identifier)
        writer.write_str_value("source", self.source)
        writer.write_datetime_value("suppressedAt", self.suppressed_at)
        writer.write_str_value("suppressionEntryId", self.suppression_entry_id)
        writer.write_additional_data_value(self.additional_data)
    

