from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .feedback_status import FeedbackStatus
    from .feedback_type import FeedbackType

@dataclass
class FeedbackResponse(AdditionalDataHolder, Parsable):
    """
    Response schema for the Leadping API feedback item response returned to authenticated clients.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether the submitter permits Leadping support to contact them about the feedback.
    allow_contact: Optional[bool] = None
    # Product area or app section connected to this feedback item response.
    area: Optional[str] = None
    # Business ID connected to the feedback item, when the feedback came from a business workspace.
    business_id: Optional[str] = None
    # Client application version that submitted this feedback item response.
    client_version: Optional[str] = None
    # UTC timestamp when this feedback item response was created.
    created_at: Optional[datetime.datetime] = None
    # Unique Leadping identifier for this feedback item response.
    id: Optional[str] = None
    # Message text supplied by the user or returned by the Leadping API for this feedback item response.
    message: Optional[str] = None
    # Application route where this feedback item response originated or should direct the user.
    route: Optional[str] = None
    # Current lifecycle status for this feedback item response in the Leadping API.
    status: Optional[FeedbackStatus] = None
    # Type classification used to route and interpret this feedback item response in the Leadping API.
    type: Optional[FeedbackType] = None
    # User ID for the person who submitted the feedback.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FeedbackResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FeedbackResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FeedbackResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .feedback_status import FeedbackStatus
        from .feedback_type import FeedbackType

        from .feedback_status import FeedbackStatus
        from .feedback_type import FeedbackType

        fields: dict[str, Callable[[Any], None]] = {
            "allowContact": lambda n : setattr(self, 'allow_contact', n.get_bool_value()),
            "area": lambda n : setattr(self, 'area', n.get_str_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "clientVersion": lambda n : setattr(self, 'client_version', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "route": lambda n : setattr(self, 'route', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(FeedbackStatus)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(FeedbackType)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_bool_value("allowContact", self.allow_contact)
        writer.write_str_value("area", self.area)
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("clientVersion", self.client_version)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("id", self.id)
        writer.write_str_value("message", self.message)
        writer.write_str_value("route", self.route)
        writer.write_enum_value("status", self.status)
        writer.write_enum_value("type", self.type)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

