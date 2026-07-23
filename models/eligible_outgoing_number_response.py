from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .eligible_outgoing_number_response_health_status import EligibleOutgoingNumberResponse_healthStatus
    from .outgoing_number_selection_reason import OutgoingNumberSelectionReason

@dataclass
class EligibleOutgoingNumberResponse(AdditionalDataHolder, Parsable):
    """
    Response schema for the Leadping API eligible outgoing phone number returned to authenticated clients.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Messaging campaign identifier associated with this eligible outgoing phone number.
    campaign_id: Optional[str] = None
    # Indicates whether Leadping can send outbound messages using this eligible outgoing phone number.
    can_send: Optional[bool] = None
    # Human-readable phone number shown in Leadping UI and API responses.
    display_number: Optional[str] = None
    # Short label describing the health state for display in dashboards.
    health_label: Optional[str] = None
    # Defines the supported SMS readiness health assessments.
    health_status: Optional[EligibleOutgoingNumberResponse_healthStatus] = None
    # Warning text that explains a potential health or readiness issue.
    health_warning: Optional[str] = None
    # Indicates whether this eligible outgoing phone number was selected for the requested operation.
    is_selected: Optional[bool] = None
    # Short display label for this eligible outgoing phone number, formatted for charts, filters, or list views.
    label: Optional[str] = None
    # E.164 phone number exposed by this eligible outgoing phone number.
    number: Optional[str] = None
    # Leadping phone number ID connected to this eligible outgoing phone number.
    phone_number_id: Optional[str] = None
    # Human-readable label for the reason code on this eligible outgoing phone number.
    reason_label: Optional[str] = None
    # Reason Leadping selected this outbound sender number.
    selection_reason: Optional[OutgoingNumberSelectionReason] = None
    # Lead source ID used to determine this phone number's outbound eligibility.
    source_id: Optional[str] = None
    # Team ID used to determine this phone number's outbound eligibility.
    team_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EligibleOutgoingNumberResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EligibleOutgoingNumberResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EligibleOutgoingNumberResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .eligible_outgoing_number_response_health_status import EligibleOutgoingNumberResponse_healthStatus
        from .outgoing_number_selection_reason import OutgoingNumberSelectionReason

        from .eligible_outgoing_number_response_health_status import EligibleOutgoingNumberResponse_healthStatus
        from .outgoing_number_selection_reason import OutgoingNumberSelectionReason

        fields: dict[str, Callable[[Any], None]] = {
            "campaignId": lambda n : setattr(self, 'campaign_id', n.get_str_value()),
            "canSend": lambda n : setattr(self, 'can_send', n.get_bool_value()),
            "displayNumber": lambda n : setattr(self, 'display_number', n.get_str_value()),
            "healthLabel": lambda n : setattr(self, 'health_label', n.get_str_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(EligibleOutgoingNumberResponse_healthStatus)),
            "healthWarning": lambda n : setattr(self, 'health_warning', n.get_str_value()),
            "isSelected": lambda n : setattr(self, 'is_selected', n.get_bool_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "phoneNumberId": lambda n : setattr(self, 'phone_number_id', n.get_str_value()),
            "reasonLabel": lambda n : setattr(self, 'reason_label', n.get_str_value()),
            "selectionReason": lambda n : setattr(self, 'selection_reason', n.get_enum_value(OutgoingNumberSelectionReason)),
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
        writer.write_bool_value("canSend", self.can_send)
        writer.write_str_value("displayNumber", self.display_number)
        writer.write_str_value("healthLabel", self.health_label)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("healthWarning", self.health_warning)
        writer.write_bool_value("isSelected", self.is_selected)
        writer.write_str_value("label", self.label)
        writer.write_str_value("number", self.number)
        writer.write_str_value("phoneNumberId", self.phone_number_id)
        writer.write_str_value("reasonLabel", self.reason_label)
        writer.write_enum_value("selectionReason", self.selection_reason)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_str_value("teamId", self.team_id)
        writer.write_additional_data_value(self.additional_data)
    

