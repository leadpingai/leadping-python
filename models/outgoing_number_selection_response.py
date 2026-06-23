from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .eligible_outgoing_number_response import EligibleOutgoingNumberResponse
    from .outgoing_number_selection_response_health_status import OutgoingNumberSelectionResponse_healthStatus
    from .outgoing_number_selection_response_selection_reason import OutgoingNumberSelectionResponse_selectionReason

@dataclass
class OutgoingNumberSelectionResponse(AdditionalDataHolder, Parsable):
    """
    API response containing outgoing number selection data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The campaign ID associated with this outgoing number selection.
    campaign_id: Optional[str] = None
    # Whether the caller can send this outgoing number selection.
    can_send: Optional[bool] = None
    # The display number value for this outgoing number selection.
    display_number: Optional[str] = None
    # The eligible numbers included with this outgoing number selection.
    eligible_numbers: Optional[list[EligibleOutgoingNumberResponse]] = None
    # The health label value for this outgoing number selection.
    health_label: Optional[str] = None
    # Defines the supported SMS Warmup Health State values.
    health_status: Optional[OutgoingNumberSelectionResponse_healthStatus] = None
    # The health warning value for this outgoing number selection.
    health_warning: Optional[str] = None
    # The number value for this outgoing number selection.
    number: Optional[str] = None
    # The phone number ID associated with this outgoing number selection.
    phone_number_id: Optional[str] = None
    # The reason label value for this outgoing number selection.
    reason_label: Optional[str] = None
    # Defines the supported Outgoing Number Selection Reason values.
    selection_reason: Optional[OutgoingNumberSelectionResponse_selectionReason] = None
    # The setup message value for this outgoing number selection.
    setup_message: Optional[str] = None
    # The source ID associated with this outgoing number selection.
    source_id: Optional[str] = None
    # Whether this outgoing number selection was manually overridden.
    was_manually_overridden: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OutgoingNumberSelectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutgoingNumberSelectionResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OutgoingNumberSelectionResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .eligible_outgoing_number_response import EligibleOutgoingNumberResponse
        from .outgoing_number_selection_response_health_status import OutgoingNumberSelectionResponse_healthStatus
        from .outgoing_number_selection_response_selection_reason import OutgoingNumberSelectionResponse_selectionReason

        from .eligible_outgoing_number_response import EligibleOutgoingNumberResponse
        from .outgoing_number_selection_response_health_status import OutgoingNumberSelectionResponse_healthStatus
        from .outgoing_number_selection_response_selection_reason import OutgoingNumberSelectionResponse_selectionReason

        fields: dict[str, Callable[[Any], None]] = {
            "campaignId": lambda n : setattr(self, 'campaign_id', n.get_str_value()),
            "canSend": lambda n : setattr(self, 'can_send', n.get_bool_value()),
            "displayNumber": lambda n : setattr(self, 'display_number', n.get_str_value()),
            "eligibleNumbers": lambda n : setattr(self, 'eligible_numbers', n.get_collection_of_object_values(EligibleOutgoingNumberResponse)),
            "healthLabel": lambda n : setattr(self, 'health_label', n.get_str_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(OutgoingNumberSelectionResponse_healthStatus)),
            "healthWarning": lambda n : setattr(self, 'health_warning', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "phoneNumberId": lambda n : setattr(self, 'phone_number_id', n.get_str_value()),
            "reasonLabel": lambda n : setattr(self, 'reason_label', n.get_str_value()),
            "selectionReason": lambda n : setattr(self, 'selection_reason', n.get_enum_value(OutgoingNumberSelectionResponse_selectionReason)),
            "setupMessage": lambda n : setattr(self, 'setup_message', n.get_str_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "wasManuallyOverridden": lambda n : setattr(self, 'was_manually_overridden', n.get_bool_value()),
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
        writer.write_collection_of_object_values("eligibleNumbers", self.eligible_numbers)
        writer.write_str_value("healthLabel", self.health_label)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("healthWarning", self.health_warning)
        writer.write_str_value("number", self.number)
        writer.write_str_value("phoneNumberId", self.phone_number_id)
        writer.write_str_value("reasonLabel", self.reason_label)
        writer.write_enum_value("selectionReason", self.selection_reason)
        writer.write_str_value("setupMessage", self.setup_message)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_bool_value("wasManuallyOverridden", self.was_manually_overridden)
        writer.write_additional_data_value(self.additional_data)
    

