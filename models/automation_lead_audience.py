from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AutomationLeadAudience(AdditionalDataHolder, Parsable):
    """
    Active leads in the current organization, optionally limited to one assignee, as of the selection time.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The assignedToUserId property
    assigned_to_user_id: Optional[str] = None
    # The count property
    count: Optional[int] = None
    # The includeDemo property
    include_demo: Optional[bool] = None
    # The organizationId property
    organization_id: Optional[str] = None
    # The selectedAt property
    selected_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationLeadAudience:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationLeadAudience
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationLeadAudience()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "assignedToUserId": lambda n : setattr(self, 'assigned_to_user_id', n.get_str_value()),
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "includeDemo": lambda n : setattr(self, 'include_demo', n.get_bool_value()),
            "organizationId": lambda n : setattr(self, 'organization_id', n.get_str_value()),
            "selectedAt": lambda n : setattr(self, 'selected_at', n.get_datetime_value()),
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
        writer.write_str_value("assignedToUserId", self.assigned_to_user_id)
        writer.write_int_value("count", self.count)
        writer.write_bool_value("includeDemo", self.include_demo)
        writer.write_str_value("organizationId", self.organization_id)
        writer.write_datetime_value("selectedAt", self.selected_at)
        writer.write_additional_data_value(self.additional_data)
    

