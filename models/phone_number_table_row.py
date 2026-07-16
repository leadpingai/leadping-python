from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_warmup import PhoneNumberWarmup

@dataclass
class PhoneNumberTableRow(AdditionalDataHolder, Parsable):
    """
    List item schema for Leadping API phone number table row results shown in searchable tables.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Business summary connected to this phone number table row.
    business: Optional[str] = None
    # Unique Leadping business identifier connected to this phone number table row.
    business_id: Optional[str] = None
    # Indicates whether this phone number table row is active and available in the Leadping API.
    enabled: Optional[bool] = None
    # Unique Leadping identifier for this phone number table row.
    id: Optional[str] = None
    # Geographic location metadata for the phone number, lead, or lookup result.
    location: Optional[str] = None
    # Display name for this phone number table row in the Leadping API.
    name: Optional[str] = None
    # E.164 phone number exposed by this phone number table row.
    number: Optional[str] = None
    # Ownership classification for this phone number, such as Leadping-owned or customer-owned.
    ownership: Optional[str] = None
    # Human-readable routing summary for this phone number.
    routing_summary: Optional[str] = None
    # Indicates whether SMS messaging is ready for this business or phone number.
    sms_ready: Optional[bool] = None
    # 10DLC campaign status associated with this sender or SMS event.
    ten_dlc_campaign_status: Optional[str] = None
    # Type classification used to route and interpret this phone number table row in the Leadping API.
    type: Optional[str] = None
    # Indicates whether voice calling is ready for this business or phone number.
    voice_ready: Optional[bool] = None
    # Warmup state for this phone number.
    warmup: Optional[PhoneNumberWarmup] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberTableRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberTableRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberTableRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_warmup import PhoneNumberWarmup

        from .phone_number_warmup import PhoneNumberWarmup

        fields: dict[str, Callable[[Any], None]] = {
            "business": lambda n : setattr(self, 'business', n.get_str_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "ownership": lambda n : setattr(self, 'ownership', n.get_str_value()),
            "routingSummary": lambda n : setattr(self, 'routing_summary', n.get_str_value()),
            "smsReady": lambda n : setattr(self, 'sms_ready', n.get_bool_value()),
            "tenDlcCampaignStatus": lambda n : setattr(self, 'ten_dlc_campaign_status', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "voiceReady": lambda n : setattr(self, 'voice_ready', n.get_bool_value()),
            "warmup": lambda n : setattr(self, 'warmup', n.get_object_value(PhoneNumberWarmup)),
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
        writer.write_str_value("business", self.business)
        writer.write_str_value("businessId", self.business_id)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_str_value("location", self.location)
        writer.write_str_value("name", self.name)
        writer.write_str_value("number", self.number)
        writer.write_str_value("ownership", self.ownership)
        writer.write_str_value("routingSummary", self.routing_summary)
        writer.write_bool_value("smsReady", self.sms_ready)
        writer.write_str_value("tenDlcCampaignStatus", self.ten_dlc_campaign_status)
        writer.write_str_value("type", self.type)
        writer.write_bool_value("voiceReady", self.voice_ready)
        writer.write_object_value("warmup", self.warmup)
        writer.write_additional_data_value(self.additional_data)
    

