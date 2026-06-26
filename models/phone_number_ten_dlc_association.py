from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PhoneNumberTenDlcAssociation(AdditionalDataHolder, Parsable):
    """
    Public Leadping API schema for phone number 10DLC association data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Provider assignment status for linking the phone number to a 10DLC campaign.
    assignment_status: Optional[str] = None
    # 10DLC brand identifier associated with this phone number or campaign.
    brand_id: Optional[str] = None
    # Messaging campaign identifier associated with this phone number 10DLC association.
    campaign_id: Optional[str] = None
    # 10DLC campaign status reported by the messaging provider.
    campaign_status: Optional[str] = None
    # Human-readable reason explaining why this phone number 10DLC association failed.
    failure_reason: Optional[str] = None
    # Most recent provider event identifier processed for this phone number 10DLC association.
    last_provider_event_id: Optional[str] = None
    # Messaging profile identifier used for SMS routing with the provider.
    messaging_profile_id: Optional[str] = None
    # UTC timestamp when s ta tu su pd at e d occurred for this phone number 10DLC association.
    status_updated_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberTenDlcAssociation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberTenDlcAssociation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberTenDlcAssociation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "assignmentStatus": lambda n : setattr(self, 'assignment_status', n.get_str_value()),
            "brandId": lambda n : setattr(self, 'brand_id', n.get_str_value()),
            "campaignId": lambda n : setattr(self, 'campaign_id', n.get_str_value()),
            "campaignStatus": lambda n : setattr(self, 'campaign_status', n.get_str_value()),
            "failureReason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "lastProviderEventId": lambda n : setattr(self, 'last_provider_event_id', n.get_str_value()),
            "messagingProfileId": lambda n : setattr(self, 'messaging_profile_id', n.get_str_value()),
            "statusUpdatedAt": lambda n : setattr(self, 'status_updated_at', n.get_datetime_value()),
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
        writer.write_str_value("assignmentStatus", self.assignment_status)
        writer.write_str_value("brandId", self.brand_id)
        writer.write_str_value("campaignId", self.campaign_id)
        writer.write_str_value("campaignStatus", self.campaign_status)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_str_value("lastProviderEventId", self.last_provider_event_id)
        writer.write_str_value("messagingProfileId", self.messaging_profile_id)
        writer.write_datetime_value("statusUpdatedAt", self.status_updated_at)
        writer.write_additional_data_value(self.additional_data)
    

