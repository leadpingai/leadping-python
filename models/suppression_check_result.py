from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SuppressionCheckResult(AdditionalDataHolder, Parsable):
    """
    Reports whether Leadping may contact a recipient and identifies the active suppression when contact is blocked.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether outreach to the recipient is allowed for the requested channel.
    allowed: Optional[bool] = None
    # Communication channel evaluated by the suppression check.
    channel: Optional[str] = None
    # Customer-safe explanation of why contact is blocked or allowed.
    customer_reason: Optional[str] = None
    # Email address used for matching, normalized for comparison.
    normalized_email: Optional[str] = None
    # Phone number used for matching, normalized to a consistent format.
    normalized_phone_number: Optional[str] = None
    # Identifier of the organization whose suppression list was checked.
    organization_id: Optional[str] = None
    # Provider or customer identifier used to match the recipient.
    recipient_identifier: Optional[str] = None
    # The source value on the active suppression entry that blocked this check.
    source: Optional[str] = None
    # The date and time the blocking suppression became active.
    suppressed_at: Optional[datetime.datetime] = None
    # Identifier of the active suppression that blocked contact, when one matched.
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
            "channel": lambda n : setattr(self, 'channel', n.get_str_value()),
            "customerReason": lambda n : setattr(self, 'customer_reason', n.get_str_value()),
            "normalizedEmail": lambda n : setattr(self, 'normalized_email', n.get_str_value()),
            "normalizedPhoneNumber": lambda n : setattr(self, 'normalized_phone_number', n.get_str_value()),
            "organizationId": lambda n : setattr(self, 'organization_id', n.get_str_value()),
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
        writer.write_str_value("channel", self.channel)
        writer.write_str_value("customerReason", self.customer_reason)
        writer.write_str_value("normalizedEmail", self.normalized_email)
        writer.write_str_value("normalizedPhoneNumber", self.normalized_phone_number)
        writer.write_str_value("organizationId", self.organization_id)
        writer.write_str_value("recipientIdentifier", self.recipient_identifier)
        writer.write_str_value("source", self.source)
        writer.write_datetime_value("suppressedAt", self.suppressed_at)
        writer.write_str_value("suppressionEntryId", self.suppression_entry_id)
        writer.write_additional_data_value(self.additional_data)
    

