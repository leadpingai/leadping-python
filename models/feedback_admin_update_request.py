from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .feedback_admin_update_request_status import FeedbackAdminUpdateRequest_status
    from .feedback_admin_update_request_type import FeedbackAdminUpdateRequest_type

@dataclass
class FeedbackAdminUpdateRequest(AdditionalDataHolder, Parsable):
    """
    Admin triage update request for product feedback.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The adminNote property
    admin_note: Optional[str] = None
    # The area property
    area: Optional[str] = None
    # The duplicateOfFeedbackItemId property
    duplicate_of_feedback_item_id: Optional[str] = None
    # The externalIssueUrl property
    external_issue_url: Optional[str] = None
    # Defines admin triage statuses for durable product feedback.
    status: Optional[FeedbackAdminUpdateRequest_status] = None
    # Defines the type of product feedback submitted from inside Leadping.
    type: Optional[FeedbackAdminUpdateRequest_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FeedbackAdminUpdateRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FeedbackAdminUpdateRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FeedbackAdminUpdateRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .feedback_admin_update_request_status import FeedbackAdminUpdateRequest_status
        from .feedback_admin_update_request_type import FeedbackAdminUpdateRequest_type

        from .feedback_admin_update_request_status import FeedbackAdminUpdateRequest_status
        from .feedback_admin_update_request_type import FeedbackAdminUpdateRequest_type

        fields: dict[str, Callable[[Any], None]] = {
            "adminNote": lambda n : setattr(self, 'admin_note', n.get_str_value()),
            "area": lambda n : setattr(self, 'area', n.get_str_value()),
            "duplicateOfFeedbackItemId": lambda n : setattr(self, 'duplicate_of_feedback_item_id', n.get_str_value()),
            "externalIssueUrl": lambda n : setattr(self, 'external_issue_url', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(FeedbackAdminUpdateRequest_status)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(FeedbackAdminUpdateRequest_type)),
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
        writer.write_str_value("adminNote", self.admin_note)
        writer.write_str_value("area", self.area)
        writer.write_str_value("duplicateOfFeedbackItemId", self.duplicate_of_feedback_item_id)
        writer.write_str_value("externalIssueUrl", self.external_issue_url)
        writer.write_enum_value("status", self.status)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

