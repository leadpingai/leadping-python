from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_device_preferences import MobileDevicePreferences
    from .user_identity import UserIdentity
    from .user_response_billing_plan import UserResponse_billingPlan
    from .user_response_billing_state import UserResponse_billingState
    from .user_response_compliance import UserResponse_compliance
    from .user_response_current_organization import UserResponse_currentOrganization
    from .user_response_notification_preferences import UserResponse_notificationPreferences
    from .user_response_subscription_status import UserResponse_subscriptionStatus

@dataclass
class UserResponse(AdditionalDataHolder, Parsable):
    """
    Describes user data returned by Leadping.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifies the Leadping subscription plan that determines organization features, allowances, and billing behavior.
    billing_plan: Optional[UserResponse_billingPlan] = None
    # Customer-safe billing state for the user's currently selected organization.
    billing_state: Optional[UserResponse_billingState] = None
    # Compliance for this user.
    compliance: Optional[UserResponse_compliance] = None
    # UTC timestamp when the resource was created.
    created_at: Optional[datetime.datetime] = None
    # Current organization for this user.
    current_organization: Optional[UserResponse_currentOrganization] = None
    # The email address associated with this user.
    email: Optional[str] = None
    # First name for this user.
    first_name: Optional[str] = None
    # Stable unique identifier of the resource.
    id: Optional[str] = None
    # The identities included with this user.
    identities: Optional[list[UserIdentity]] = None
    # The date and time when this user last completed the Leadping sign-in flow.
    last_logged_in_at: Optional[datetime.datetime] = None
    # Last name of the Leadping user.
    last_name: Optional[str] = None
    # The Leadping mobile device preferences for this user.
    mobile_device_preferences: Optional[list[MobileDevicePreferences]] = None
    # UTC timestamp when the resource was last modified, or null when it has not been updated.
    modified_at: Optional[datetime.datetime] = None
    # Human-readable display name of the resource.
    name: Optional[str] = None
    # Notification preferences for this user.
    notification_preferences: Optional[UserResponse_notificationPreferences] = None
    # UTC timestamp for personal data deleted at on this user.
    personal_data_deleted_at: Optional[datetime.datetime] = None
    # The human-readable personal data deletion reason explaining this user.
    personal_data_deletion_reason: Optional[str] = None
    # UTC timestamp for personal data deletion requested at on this user.
    personal_data_deletion_requested_at: Optional[datetime.datetime] = None
    # The current personal data deletion status for this user.
    personal_data_deletion_status: Optional[str] = None
    # The phone number associated with this user.
    phone: Optional[str] = None
    # The roles included with this user.
    roles: Optional[list[str]] = None
    # Describes an organization's billing subscription lifecycle, including trial, active, delinquent, canceled, and expired states.
    subscription_status: Optional[UserResponse_subscriptionStatus] = None
    # IANA time zone identifier used when displaying dates and times for this user.
    time_zone_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_device_preferences import MobileDevicePreferences
        from .user_identity import UserIdentity
        from .user_response_billing_plan import UserResponse_billingPlan
        from .user_response_billing_state import UserResponse_billingState
        from .user_response_compliance import UserResponse_compliance
        from .user_response_current_organization import UserResponse_currentOrganization
        from .user_response_notification_preferences import UserResponse_notificationPreferences
        from .user_response_subscription_status import UserResponse_subscriptionStatus

        from .mobile_device_preferences import MobileDevicePreferences
        from .user_identity import UserIdentity
        from .user_response_billing_plan import UserResponse_billingPlan
        from .user_response_billing_state import UserResponse_billingState
        from .user_response_compliance import UserResponse_compliance
        from .user_response_current_organization import UserResponse_currentOrganization
        from .user_response_notification_preferences import UserResponse_notificationPreferences
        from .user_response_subscription_status import UserResponse_subscriptionStatus

        fields: dict[str, Callable[[Any], None]] = {
            "billingPlan": lambda n : setattr(self, 'billing_plan', n.get_enum_value(UserResponse_billingPlan)),
            "billingState": lambda n : setattr(self, 'billing_state', n.get_object_value(UserResponse_billingState)),
            "compliance": lambda n : setattr(self, 'compliance', n.get_object_value(UserResponse_compliance)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "currentOrganization": lambda n : setattr(self, 'current_organization', n.get_object_value(UserResponse_currentOrganization)),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "identities": lambda n : setattr(self, 'identities', n.get_collection_of_object_values(UserIdentity)),
            "lastLoggedInAt": lambda n : setattr(self, 'last_logged_in_at', n.get_datetime_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "mobileDevicePreferences": lambda n : setattr(self, 'mobile_device_preferences', n.get_collection_of_object_values(MobileDevicePreferences)),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "notificationPreferences": lambda n : setattr(self, 'notification_preferences', n.get_object_value(UserResponse_notificationPreferences)),
            "personalDataDeletedAt": lambda n : setattr(self, 'personal_data_deleted_at', n.get_datetime_value()),
            "personalDataDeletionReason": lambda n : setattr(self, 'personal_data_deletion_reason', n.get_str_value()),
            "personalDataDeletionRequestedAt": lambda n : setattr(self, 'personal_data_deletion_requested_at', n.get_datetime_value()),
            "personalDataDeletionStatus": lambda n : setattr(self, 'personal_data_deletion_status', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_primitive_values(str)),
            "subscriptionStatus": lambda n : setattr(self, 'subscription_status', n.get_enum_value(UserResponse_subscriptionStatus)),
            "timeZoneId": lambda n : setattr(self, 'time_zone_id', n.get_str_value()),
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
        writer.write_enum_value("billingPlan", self.billing_plan)
        writer.write_object_value("billingState", self.billing_state)
        writer.write_object_value("compliance", self.compliance)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_object_value("currentOrganization", self.current_organization)
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_object_values("identities", self.identities)
        writer.write_datetime_value("lastLoggedInAt", self.last_logged_in_at)
        writer.write_str_value("lastName", self.last_name)
        writer.write_collection_of_object_values("mobileDevicePreferences", self.mobile_device_preferences)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_object_value("notificationPreferences", self.notification_preferences)
        writer.write_datetime_value("personalDataDeletedAt", self.personal_data_deleted_at)
        writer.write_str_value("personalDataDeletionReason", self.personal_data_deletion_reason)
        writer.write_datetime_value("personalDataDeletionRequestedAt", self.personal_data_deletion_requested_at)
        writer.write_str_value("personalDataDeletionStatus", self.personal_data_deletion_status)
        writer.write_str_value("phone", self.phone)
        writer.write_collection_of_primitive_values("roles", self.roles)
        writer.write_enum_value("subscriptionStatus", self.subscription_status)
        writer.write_str_value("timeZoneId", self.time_zone_id)
        writer.write_additional_data_value(self.additional_data)
    

