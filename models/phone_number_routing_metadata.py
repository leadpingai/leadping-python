from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PhoneNumberRoutingMetadata(AdditionalDataHolder, Parsable):
    """
    API DTO containing phone number routing metadata data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The campaign ID associated with this phone number routing metadata.
    campaign_id: Optional[str] = None
    # Whether internal test only applies to this phone number routing metadata.
    internal_test_only: Optional[bool] = None
    # The messaging profile ID associated with this phone number routing metadata.
    messaging_profile_id: Optional[str] = None
    # Whether SMS is enabled for this phone number routing metadata.
    sms_enabled: Optional[bool] = None
    # The source ID associated with this phone number routing metadata.
    source_id: Optional[str] = None
    # The team ID associated with this phone number routing metadata.
    team_id: Optional[str] = None
    # The voice connection ID associated with this phone number routing metadata.
    voice_connection_id: Optional[str] = None
    # Whether voice is enabled for this phone number routing metadata.
    voice_enabled: Optional[bool] = None
    # Whether warmup only applies to this phone number routing metadata.
    warmup_only: Optional[bool] = None
    
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
            "internalTestOnly": lambda n : setattr(self, 'internal_test_only', n.get_bool_value()),
            "messagingProfileId": lambda n : setattr(self, 'messaging_profile_id', n.get_str_value()),
            "smsEnabled": lambda n : setattr(self, 'sms_enabled', n.get_bool_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "teamId": lambda n : setattr(self, 'team_id', n.get_str_value()),
            "voiceConnectionId": lambda n : setattr(self, 'voice_connection_id', n.get_str_value()),
            "voiceEnabled": lambda n : setattr(self, 'voice_enabled', n.get_bool_value()),
            "warmupOnly": lambda n : setattr(self, 'warmup_only', n.get_bool_value()),
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
        writer.write_bool_value("internalTestOnly", self.internal_test_only)
        writer.write_str_value("messagingProfileId", self.messaging_profile_id)
        writer.write_bool_value("smsEnabled", self.sms_enabled)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_str_value("teamId", self.team_id)
        writer.write_str_value("voiceConnectionId", self.voice_connection_id)
        writer.write_bool_value("voiceEnabled", self.voice_enabled)
        writer.write_bool_value("warmupOnly", self.warmup_only)
        writer.write_additional_data_value(self.additional_data)
    

