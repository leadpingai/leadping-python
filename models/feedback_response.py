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

    # Internal admin note used to track feedback review or resolution.
    admin_note: Optional[str] = None
    # Indicates whether the submitter permits Leadping support to contact them about the feedback.
    allow_contact: Optional[bool] = None
    # Product area or app section connected to this feedback item response.
    area: Optional[str] = None
    # Business ID connected to the feedback item, when the feedback came from a business workspace.
    business_id: Optional[str] = None
    # Business name snapshot captured when the user submitted the feedback.
    business_name_snapshot: Optional[str] = None
    # Client application version that submitted this feedback item response.
    client_version: Optional[str] = None
    # UTC timestamp when this feedback item response was closed.
    closed_at: Optional[datetime.datetime] = None
    # User ID of the person who closed this item.
    closed_by_user_id: Optional[str] = None
    # UTC timestamp when this feedback item response was created.
    created_at: Optional[datetime.datetime] = None
    # Feedback item ID that this item duplicates, when applicable.
    duplicate_of_feedback_item_id: Optional[str] = None
    # Deployment environment where this feedback item response was captured or processed.
    environment: Optional[str] = None
    # External issue tracker URL linked to this feedback item.
    external_issue_url: Optional[str] = None
    # Unique Leadping identifier for this feedback item response.
    id: Optional[str] = None
    # Message text supplied by the user or returned by the Leadping API for this feedback item response.
    message: Optional[str] = None
    # UTC timestamp when an admin reviewed this feedback item response.
    reviewed_at: Optional[datetime.datetime] = None
    # User ID of the admin who reviewed this item.
    reviewed_by_user_id: Optional[str] = None
    # Application route where this feedback item response originated or should direct the user.
    route: Optional[str] = None
    # Leadping API server version that processed this feedback item response.
    server_version: Optional[str] = None
    # Current lifecycle status for this feedback item response in the Leadping API.
    status: Optional[FeedbackStatus] = None
    # Billing plan snapshot captured when the user submitted the feedback.
    subscription_plan_snapshot: Optional[str] = None
    # Type classification used to route and interpret this feedback item response in the Leadping API.
    type: Optional[FeedbackType] = None
    # Browser or client user agent captured when this feedback item response was submitted.
    user_agent: Optional[str] = None
    # User display name snapshot captured when the user submitted the feedback.
    user_display_name_snapshot: Optional[str] = None
    # User email snapshot captured when the user submitted the feedback.
    user_email_snapshot: Optional[str] = None
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
            "adminNote": lambda n : setattr(self, 'admin_note', n.get_str_value()),
            "allowContact": lambda n : setattr(self, 'allow_contact', n.get_bool_value()),
            "area": lambda n : setattr(self, 'area', n.get_str_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "businessNameSnapshot": lambda n : setattr(self, 'business_name_snapshot', n.get_str_value()),
            "clientVersion": lambda n : setattr(self, 'client_version', n.get_str_value()),
            "closedAt": lambda n : setattr(self, 'closed_at', n.get_datetime_value()),
            "closedByUserId": lambda n : setattr(self, 'closed_by_user_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "duplicateOfFeedbackItemId": lambda n : setattr(self, 'duplicate_of_feedback_item_id', n.get_str_value()),
            "environment": lambda n : setattr(self, 'environment', n.get_str_value()),
            "externalIssueUrl": lambda n : setattr(self, 'external_issue_url', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "reviewedAt": lambda n : setattr(self, 'reviewed_at', n.get_datetime_value()),
            "reviewedByUserId": lambda n : setattr(self, 'reviewed_by_user_id', n.get_str_value()),
            "route": lambda n : setattr(self, 'route', n.get_str_value()),
            "serverVersion": lambda n : setattr(self, 'server_version', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(FeedbackStatus)),
            "subscriptionPlanSnapshot": lambda n : setattr(self, 'subscription_plan_snapshot', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(FeedbackType)),
            "userAgent": lambda n : setattr(self, 'user_agent', n.get_str_value()),
            "userDisplayNameSnapshot": lambda n : setattr(self, 'user_display_name_snapshot', n.get_str_value()),
            "userEmailSnapshot": lambda n : setattr(self, 'user_email_snapshot', n.get_str_value()),
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
        writer.write_str_value("adminNote", self.admin_note)
        writer.write_bool_value("allowContact", self.allow_contact)
        writer.write_str_value("area", self.area)
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("businessNameSnapshot", self.business_name_snapshot)
        writer.write_str_value("clientVersion", self.client_version)
        writer.write_datetime_value("closedAt", self.closed_at)
        writer.write_str_value("closedByUserId", self.closed_by_user_id)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("duplicateOfFeedbackItemId", self.duplicate_of_feedback_item_id)
        writer.write_str_value("environment", self.environment)
        writer.write_str_value("externalIssueUrl", self.external_issue_url)
        writer.write_str_value("id", self.id)
        writer.write_str_value("message", self.message)
        writer.write_datetime_value("reviewedAt", self.reviewed_at)
        writer.write_str_value("reviewedByUserId", self.reviewed_by_user_id)
        writer.write_str_value("route", self.route)
        writer.write_str_value("serverVersion", self.server_version)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("subscriptionPlanSnapshot", self.subscription_plan_snapshot)
        writer.write_enum_value("type", self.type)
        writer.write_str_value("userAgent", self.user_agent)
        writer.write_str_value("userDisplayNameSnapshot", self.user_display_name_snapshot)
        writer.write_str_value("userEmailSnapshot", self.user_email_snapshot)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

