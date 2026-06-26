from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_device_preferences import MobileDevicePreferences
    from .user_request_billing_plan import UserRequest_billingPlan
    from .user_request_business import UserRequest_business
    from .user_request_compliance import UserRequest_compliance
    from .user_request_current_business import UserRequest_currentBusiness
    from .user_request_notification_preferences import UserRequest_notificationPreferences
    from .user_request_subscription_status import UserRequest_subscriptionStatus

@dataclass
class UserRequest(AdditionalDataHolder, Parsable):
    """
    Request schema for the Leadping API user profile request, including the fields clients can send.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Defines the supported Billing Plan values.
    billing_plan: Optional[UserRequest_billingPlan] = None
    # Business summary connected to this user profile request.
    business: Optional[UserRequest_business] = None
    # User compliance settings and attestations captured for Leadping account review.
    compliance: Optional[UserRequest_compliance] = None
    # Business currently selected for the user session or profile.
    current_business: Optional[UserRequest_currentBusiness] = None
    # Email address for the person represented by this user profile request.
    email: Optional[str] = None
    # First name of the lead, user, or contact represented by this user profile request.
    first_name: Optional[str] = None
    # The unique identifier for the entity, when updating an existing entity.
    id: Optional[str] = None
    # Last name of the lead, user, or contact represented by this user profile request.
    last_name: Optional[str] = None
    # Mobile notification preferences configured for the user.
    mobile_device_preferences: Optional[list[MobileDevicePreferences]] = None
    # The display name for the entity.
    name: Optional[str] = None
    # Notification preferences configured for the user.
    notification_preferences: Optional[UserRequest_notificationPreferences] = None
    # Phone details for the lead, user, or business represented by this user profile request.
    phone: Optional[str] = None
    # Defines the supported Subscription Status values.
    subscription_status: Optional[UserRequest_subscriptionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_device_preferences import MobileDevicePreferences
        from .user_request_billing_plan import UserRequest_billingPlan
        from .user_request_business import UserRequest_business
        from .user_request_compliance import UserRequest_compliance
        from .user_request_current_business import UserRequest_currentBusiness
        from .user_request_notification_preferences import UserRequest_notificationPreferences
        from .user_request_subscription_status import UserRequest_subscriptionStatus

        from .mobile_device_preferences import MobileDevicePreferences
        from .user_request_billing_plan import UserRequest_billingPlan
        from .user_request_business import UserRequest_business
        from .user_request_compliance import UserRequest_compliance
        from .user_request_current_business import UserRequest_currentBusiness
        from .user_request_notification_preferences import UserRequest_notificationPreferences
        from .user_request_subscription_status import UserRequest_subscriptionStatus

        fields: dict[str, Callable[[Any], None]] = {
            "billingPlan": lambda n : setattr(self, 'billing_plan', n.get_enum_value(UserRequest_billingPlan)),
            "business": lambda n : setattr(self, 'business', n.get_object_value(UserRequest_business)),
            "compliance": lambda n : setattr(self, 'compliance', n.get_object_value(UserRequest_compliance)),
            "currentBusiness": lambda n : setattr(self, 'current_business', n.get_object_value(UserRequest_currentBusiness)),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "mobileDevicePreferences": lambda n : setattr(self, 'mobile_device_preferences', n.get_collection_of_object_values(MobileDevicePreferences)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "notificationPreferences": lambda n : setattr(self, 'notification_preferences', n.get_object_value(UserRequest_notificationPreferences)),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "subscriptionStatus": lambda n : setattr(self, 'subscription_status', n.get_enum_value(UserRequest_subscriptionStatus)),
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
        writer.write_object_value("business", self.business)
        writer.write_object_value("compliance", self.compliance)
        writer.write_object_value("currentBusiness", self.current_business)
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("lastName", self.last_name)
        writer.write_collection_of_object_values("mobileDevicePreferences", self.mobile_device_preferences)
        writer.write_str_value("name", self.name)
        writer.write_object_value("notificationPreferences", self.notification_preferences)
        writer.write_str_value("phone", self.phone)
        writer.write_enum_value("subscriptionStatus", self.subscription_status)
        writer.write_additional_data_value(self.additional_data)
    

