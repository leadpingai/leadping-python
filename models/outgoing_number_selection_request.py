from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .outgoing_number_selection_request_channel import OutgoingNumberSelectionRequest_channel

@dataclass
class OutgoingNumberSelectionRequest(AdditionalDataHolder, Parsable):
    """
    Request payload for outgoing number selection.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The campaign ID associated with this outgoing number selection.
    campaign_id: Optional[str] = None
    # Defines the supported Outgoing Number Channel values.
    channel: Optional[OutgoingNumberSelectionRequest_channel] = None
    # The conversation ID associated with this outgoing number selection.
    conversation_id: Optional[str] = None
    # The lead ID associated with this outgoing number selection.
    lead_id: Optional[str] = None
    # The recipient phone number value for this outgoing number selection.
    recipient_phone_number: Optional[str] = None
    # The source ID associated with this outgoing number selection.
    source_id: Optional[str] = None
    # The team ID associated with this outgoing number selection.
    team_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OutgoingNumberSelectionRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutgoingNumberSelectionRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OutgoingNumberSelectionRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .outgoing_number_selection_request_channel import OutgoingNumberSelectionRequest_channel

        from .outgoing_number_selection_request_channel import OutgoingNumberSelectionRequest_channel

        fields: dict[str, Callable[[Any], None]] = {
            "campaignId": lambda n : setattr(self, 'campaign_id', n.get_str_value()),
            "channel": lambda n : setattr(self, 'channel', n.get_enum_value(OutgoingNumberSelectionRequest_channel)),
            "conversationId": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "recipientPhoneNumber": lambda n : setattr(self, 'recipient_phone_number', n.get_str_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "teamId": lambda n : setattr(self, 'team_id', n.get_str_value()),
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
        writer.write_str_value("campaignId", self.campaign_id)
        writer.write_enum_value("channel", self.channel)
        writer.write_str_value("conversationId", self.conversation_id)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_str_value("recipientPhoneNumber", self.recipient_phone_number)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_str_value("teamId", self.team_id)
        writer.write_additional_data_value(self.additional_data)
    

