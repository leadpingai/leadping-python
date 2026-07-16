from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PhoneNumberRoutingMetadata(AdditionalDataHolder, Parsable):
    """
    Public Leadping API schema for phone number routing metadata data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Messaging campaign identifier associated with this phone number routing metadata.
    campaign_id: Optional[str] = None
    # Indicates whether the phone number can be used for SMS messaging.
    sms_enabled: Optional[bool] = None
    # Lead source ID assigned to this phone number for attribution and routing.
    source_id: Optional[str] = None
    # Team ID used to route calls and messages for this phone number.
    team_id: Optional[str] = None
    # Indicates whether the phone number can be used for voice calls.
    voice_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberRoutingMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberRoutingMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberRoutingMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "campaignId": lambda n : setattr(self, 'campaign_id', n.get_str_value()),
            "smsEnabled": lambda n : setattr(self, 'sms_enabled', n.get_bool_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "teamId": lambda n : setattr(self, 'team_id', n.get_str_value()),
            "voiceEnabled": lambda n : setattr(self, 'voice_enabled', n.get_bool_value()),
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
        writer.write_bool_value("smsEnabled", self.sms_enabled)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_str_value("teamId", self.team_id)
        writer.write_bool_value("voiceEnabled", self.voice_enabled)
        writer.write_additional_data_value(self.additional_data)
    

