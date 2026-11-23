from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .automation_lead_audience import AutomationLeadAudience

@dataclass
class AutomationAudienceRequest(AdditionalDataHolder, Parsable):
    """
    Runs an automation for a server-resolved audience, omitting leads the user unchecked.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Active leads in the current organization, optionally limited to one assignee, as of the selection time.
    audience: Optional[AutomationLeadAudience] = None
    # The excludedLeadIds property
    excluded_lead_ids: Optional[list[str]] = None
    # The requestId property
    request_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationAudienceRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationAudienceRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationAudienceRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automation_lead_audience import AutomationLeadAudience

        from .automation_lead_audience import AutomationLeadAudience

        fields: dict[str, Callable[[Any], None]] = {
            "audience": lambda n : setattr(self, 'audience', n.get_object_value(AutomationLeadAudience)),
            "excludedLeadIds": lambda n : setattr(self, 'excluded_lead_ids', n.get_collection_of_primitive_values(str)),
            "requestId": lambda n : setattr(self, 'request_id', n.get_uuid_value()),
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
        writer.write_object_value("audience", self.audience)
        writer.write_collection_of_primitive_values("excludedLeadIds", self.excluded_lead_ids)
        writer.write_uuid_value("requestId", self.request_id)
        writer.write_additional_data_value(self.additional_data)
    

