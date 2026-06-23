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
    API response containing eligible outgoing number data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The campaign ID associated with this eligible outgoing number.
    campaign_id: Optional[str] = None
    # Whether the caller can send this eligible outgoing number.
    can_send: Optional[bool] = None
    # The display number value for this eligible outgoing number.
    display_number: Optional[str] = None
    # The health label value for this eligible outgoing number.
    health_label: Optional[str] = None
    # Defines the supported SMS Warmup Health State values.
    health_status: Optional[EligibleOutgoingNumberResponse_healthStatus] = None
    # The health warning value for this eligible outgoing number.
    health_warning: Optional[str] = None
    # Whether this eligible outgoing number is selected.
    is_selected: Optional[bool] = None
    # The human-readable label shown for this eligible outgoing number.
    label: Optional[str] = None
    # The number value for this eligible outgoing number.
    number: Optional[str] = None
    # The phone number ID associated with this eligible outgoing number.
    phone_number_id: Optional[str] = None
    # The reason label value for this eligible outgoing number.
    reason_label: Optional[str] = None
    # The human-readable selection reason explaining this eligible outgoing number.
    selection_reason: Optional[OutgoingNumberSelectionReason] = None
    # The source ID associated with this eligible outgoing number.
    source_id: Optional[str] = None
    # The team ID associated with this eligible outgoing number.
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
    

