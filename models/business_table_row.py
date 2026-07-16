from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_table_row_activation_status import BusinessTableRow_activationStatus
    from .business_table_row_billing_plan import BusinessTableRow_billingPlan
    from .business_table_row_setup_step import BusinessTableRow_setupStep
    from .business_table_row_status import BusinessTableRow_status
    from .business_table_row_subscription_status import BusinessTableRow_subscriptionStatus
    from .business_table_row_ten_dlc_status import BusinessTableRow_tenDlcStatus
    from .business_table_row_website_status import BusinessTableRow_websiteStatus

@dataclass
class BusinessTableRow(AdditionalDataHolder, Parsable):
    """
    API DTO containing business data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Defines the supported Customer Activation Status values.
    activation_status: Optional[BusinessTableRow_activationStatus] = None
    # The date and time this business API key expires, or null when it has no expiration.
    api_key_expires_at: Optional[datetime.datetime] = None
    # The date and time this business API key was first used.
    api_key_first_used_at: Optional[datetime.datetime] = None
    # The date and time this business API key was issued.
    api_key_issued_at: Optional[datetime.datetime] = None
    # The date and time this business API key was last used.
    api_key_last_used_at: Optional[datetime.datetime] = None
    # The masked API key preview owned by this business.
    api_key_preview: Optional[str] = None
    # The total number of tracked uses for this business API key.
    api_key_total_uses: Optional[int] = None
    # Defines the supported Billing Plan values.
    billing_plan: Optional[BusinessTableRow_billingPlan] = None
    # The business ID that owns this row when the row represents a child business resource.
    business_id: Optional[str] = None
    # The business name that owns this row when the row represents a child business resource.
    business_name: Optional[str] = None
    # Whether this business is enabled.
    enabled: Optional[bool] = None
    # The unique ID for this business.
    id: Optional[str] = None
    # The industry value for this business.
    industry: Optional[str] = None
    # Date and time when this Leadping business table row was last subscription event.
    last_subscription_event_at: Optional[datetime.datetime] = None
    # The date and time for the modified at value on this business.
    modified_at: Optional[datetime.datetime] = None
    # The human-readable name shown for this business.
    name: Optional[str] = None
    # Whether needs admin review applies to this business.
    needs_admin_review: Optional[bool] = None
    # Date and time when this Leadping business table row was payment failed.
    payment_failed_at: Optional[datetime.datetime] = None
    # The phone number associated with this business.
    phone: Optional[str] = None
    # Defines the supported Business Setup Step values.
    setup_step: Optional[BusinessTableRow_setupStep] = None
    # Defines the supported Business Status values.
    status: Optional[BusinessTableRow_status] = None
    # Date and time when this Leadping business table row was subscription cancel.
    subscription_cancel_at: Optional[datetime.datetime] = None
    # Defines the supported Subscription Status values.
    subscription_status: Optional[BusinessTableRow_subscriptionStatus] = None
    # Defines the supported 10DLC Application Status values.
    ten_dlc_status: Optional[BusinessTableRow_tenDlcStatus] = None
    # The user count for this business.
    user_count: Optional[int] = None
    # The user ID value for this business.
    user_id: Optional[str] = None
    # The user name value for this business.
    user_name: Optional[str] = None
    # The website URL associated with this business.
    website: Optional[str] = None
    # Defines the supported Website Lifecycle Status values.
    website_status: Optional[BusinessTableRow_websiteStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessTableRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessTableRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessTableRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .business_table_row_activation_status import BusinessTableRow_activationStatus
        from .business_table_row_billing_plan import BusinessTableRow_billingPlan
        from .business_table_row_setup_step import BusinessTableRow_setupStep
        from .business_table_row_status import BusinessTableRow_status
        from .business_table_row_subscription_status import BusinessTableRow_subscriptionStatus
        from .business_table_row_ten_dlc_status import BusinessTableRow_tenDlcStatus
        from .business_table_row_website_status import BusinessTableRow_websiteStatus

        from .business_table_row_activation_status import BusinessTableRow_activationStatus
        from .business_table_row_billing_plan import BusinessTableRow_billingPlan
        from .business_table_row_setup_step import BusinessTableRow_setupStep
        from .business_table_row_status import BusinessTableRow_status
        from .business_table_row_subscription_status import BusinessTableRow_subscriptionStatus
        from .business_table_row_ten_dlc_status import BusinessTableRow_tenDlcStatus
        from .business_table_row_website_status import BusinessTableRow_websiteStatus

        fields: dict[str, Callable[[Any], None]] = {
            "activationStatus": lambda n : setattr(self, 'activation_status', n.get_enum_value(BusinessTableRow_activationStatus)),
            "apiKeyExpiresAt": lambda n : setattr(self, 'api_key_expires_at', n.get_datetime_value()),
            "apiKeyFirstUsedAt": lambda n : setattr(self, 'api_key_first_used_at', n.get_datetime_value()),
            "apiKeyIssuedAt": lambda n : setattr(self, 'api_key_issued_at', n.get_datetime_value()),
            "apiKeyLastUsedAt": lambda n : setattr(self, 'api_key_last_used_at', n.get_datetime_value()),
            "apiKeyPreview": lambda n : setattr(self, 'api_key_preview', n.get_str_value()),
            "apiKeyTotalUses": lambda n : setattr(self, 'api_key_total_uses', n.get_int_value()),
            "billingPlan": lambda n : setattr(self, 'billing_plan', n.get_enum_value(BusinessTableRow_billingPlan)),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "businessName": lambda n : setattr(self, 'business_name', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_str_value()),
            "lastSubscriptionEventAt": lambda n : setattr(self, 'last_subscription_event_at', n.get_datetime_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "needsAdminReview": lambda n : setattr(self, 'needs_admin_review', n.get_bool_value()),
            "paymentFailedAt": lambda n : setattr(self, 'payment_failed_at', n.get_datetime_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "setupStep": lambda n : setattr(self, 'setup_step', n.get_enum_value(BusinessTableRow_setupStep)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(BusinessTableRow_status)),
            "subscriptionCancelAt": lambda n : setattr(self, 'subscription_cancel_at', n.get_datetime_value()),
            "subscriptionStatus": lambda n : setattr(self, 'subscription_status', n.get_enum_value(BusinessTableRow_subscriptionStatus)),
            "tenDlcStatus": lambda n : setattr(self, 'ten_dlc_status', n.get_enum_value(BusinessTableRow_tenDlcStatus)),
            "userCount": lambda n : setattr(self, 'user_count', n.get_int_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "website": lambda n : setattr(self, 'website', n.get_str_value()),
            "websiteStatus": lambda n : setattr(self, 'website_status', n.get_enum_value(BusinessTableRow_websiteStatus)),
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
        writer.write_enum_value("activationStatus", self.activation_status)
        writer.write_datetime_value("apiKeyExpiresAt", self.api_key_expires_at)
        writer.write_datetime_value("apiKeyFirstUsedAt", self.api_key_first_used_at)
        writer.write_datetime_value("apiKeyIssuedAt", self.api_key_issued_at)
        writer.write_datetime_value("apiKeyLastUsedAt", self.api_key_last_used_at)
        writer.write_str_value("apiKeyPreview", self.api_key_preview)
        writer.write_int_value("apiKeyTotalUses", self.api_key_total_uses)
        writer.write_enum_value("billingPlan", self.billing_plan)
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("businessName", self.business_name)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_str_value("industry", self.industry)
        writer.write_datetime_value("lastSubscriptionEventAt", self.last_subscription_event_at)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_bool_value("needsAdminReview", self.needs_admin_review)
        writer.write_datetime_value("paymentFailedAt", self.payment_failed_at)
        writer.write_str_value("phone", self.phone)
        writer.write_enum_value("setupStep", self.setup_step)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("subscriptionCancelAt", self.subscription_cancel_at)
        writer.write_enum_value("subscriptionStatus", self.subscription_status)
        writer.write_enum_value("tenDlcStatus", self.ten_dlc_status)
        writer.write_int_value("userCount", self.user_count)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("website", self.website)
        writer.write_enum_value("websiteStatus", self.website_status)
        writer.write_additional_data_value(self.additional_data)
    

