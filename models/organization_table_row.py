from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .organization_table_row_activation_status import OrganizationTableRow_activationStatus
    from .organization_table_row_billing_plan import OrganizationTableRow_billingPlan
    from .organization_table_row_organization import OrganizationTableRow_organization
    from .organization_table_row_setup_step import OrganizationTableRow_setupStep
    from .organization_table_row_status import OrganizationTableRow_status
    from .organization_table_row_subscription_status import OrganizationTableRow_subscriptionStatus
    from .organization_table_row_ten_dlc_status import OrganizationTableRow_tenDlcStatus
    from .organization_table_row_website_status import OrganizationTableRow_websiteStatus

@dataclass
class OrganizationTableRow(AdditionalDataHolder, Parsable):
    """
    API DTO containing organization data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The account balance value for this organization.
    account_balance: Optional[float] = None
    # Defines the supported Customer Activation Status values.
    activation_status: Optional[OrganizationTableRow_activationStatus] = None
    # The date and time this organization API key expires, or null when it has no expiration.
    api_key_expires_at: Optional[datetime.datetime] = None
    # The date and time this organization API key was first used.
    api_key_first_used_at: Optional[datetime.datetime] = None
    # The date and time this organization API key was issued.
    api_key_issued_at: Optional[datetime.datetime] = None
    # The date and time this organization API key was last used.
    api_key_last_used_at: Optional[datetime.datetime] = None
    # WorkOS permission slugs granted to this organization API key.
    api_key_permissions: Optional[list[str]] = None
    # The masked API key preview owned by this organization.
    api_key_preview: Optional[str] = None
    # The total number of tracked uses for this organization API key.
    api_key_total_uses: Optional[int] = None
    # Defines the supported Billing Plan values.
    billing_plan: Optional[OrganizationTableRow_billingPlan] = None
    # Whether this organization is enabled.
    enabled: Optional[bool] = None
    # The unique ID for this organization.
    id: Optional[str] = None
    # The industry value for this organization.
    industry: Optional[str] = None
    # Date and time when this Leadping organization table row was last subscription event.
    last_subscription_event_at: Optional[datetime.datetime] = None
    # The date and time for the modified at value on this organization.
    modified_at: Optional[datetime.datetime] = None
    # The human-readable name shown for this organization.
    name: Optional[str] = None
    # Whether needs admin review applies to this organization.
    needs_admin_review: Optional[bool] = None
    # The ID and name for this organization.
    organization: Optional[OrganizationTableRow_organization] = None
    # Date and time when this Leadping organization table row was payment failed.
    payment_failed_at: Optional[datetime.datetime] = None
    # The phone number associated with this organization.
    phone: Optional[str] = None
    # Defines the supported Organization Setup Step values.
    setup_step: Optional[OrganizationTableRow_setupStep] = None
    # Defines the supported Organization Status values.
    status: Optional[OrganizationTableRow_status] = None
    # Date and time when this Leadping organization table row was subscription cancel.
    subscription_cancel_at: Optional[datetime.datetime] = None
    # Defines the supported Subscription Status values.
    subscription_status: Optional[OrganizationTableRow_subscriptionStatus] = None
    # Defines the supported 10DLC Application Status values.
    ten_dlc_status: Optional[OrganizationTableRow_tenDlcStatus] = None
    # The user count for this organization.
    user_count: Optional[int] = None
    # The website URL associated with this organization.
    website: Optional[str] = None
    # Defines the supported Website Lifecycle Status values.
    website_status: Optional[OrganizationTableRow_websiteStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationTableRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationTableRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationTableRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .organization_table_row_activation_status import OrganizationTableRow_activationStatus
        from .organization_table_row_billing_plan import OrganizationTableRow_billingPlan
        from .organization_table_row_organization import OrganizationTableRow_organization
        from .organization_table_row_setup_step import OrganizationTableRow_setupStep
        from .organization_table_row_status import OrganizationTableRow_status
        from .organization_table_row_subscription_status import OrganizationTableRow_subscriptionStatus
        from .organization_table_row_ten_dlc_status import OrganizationTableRow_tenDlcStatus
        from .organization_table_row_website_status import OrganizationTableRow_websiteStatus

        from .organization_table_row_activation_status import OrganizationTableRow_activationStatus
        from .organization_table_row_billing_plan import OrganizationTableRow_billingPlan
        from .organization_table_row_organization import OrganizationTableRow_organization
        from .organization_table_row_setup_step import OrganizationTableRow_setupStep
        from .organization_table_row_status import OrganizationTableRow_status
        from .organization_table_row_subscription_status import OrganizationTableRow_subscriptionStatus
        from .organization_table_row_ten_dlc_status import OrganizationTableRow_tenDlcStatus
        from .organization_table_row_website_status import OrganizationTableRow_websiteStatus

        fields: dict[str, Callable[[Any], None]] = {
            "accountBalance": lambda n : setattr(self, 'account_balance', n.get_float_value()),
            "activationStatus": lambda n : setattr(self, 'activation_status', n.get_enum_value(OrganizationTableRow_activationStatus)),
            "apiKeyExpiresAt": lambda n : setattr(self, 'api_key_expires_at', n.get_datetime_value()),
            "apiKeyFirstUsedAt": lambda n : setattr(self, 'api_key_first_used_at', n.get_datetime_value()),
            "apiKeyIssuedAt": lambda n : setattr(self, 'api_key_issued_at', n.get_datetime_value()),
            "apiKeyLastUsedAt": lambda n : setattr(self, 'api_key_last_used_at', n.get_datetime_value()),
            "apiKeyPermissions": lambda n : setattr(self, 'api_key_permissions', n.get_collection_of_primitive_values(str)),
            "apiKeyPreview": lambda n : setattr(self, 'api_key_preview', n.get_str_value()),
            "apiKeyTotalUses": lambda n : setattr(self, 'api_key_total_uses', n.get_int_value()),
            "billingPlan": lambda n : setattr(self, 'billing_plan', n.get_enum_value(OrganizationTableRow_billingPlan)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_str_value()),
            "lastSubscriptionEventAt": lambda n : setattr(self, 'last_subscription_event_at', n.get_datetime_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "needsAdminReview": lambda n : setattr(self, 'needs_admin_review', n.get_bool_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_object_value(OrganizationTableRow_organization)),
            "paymentFailedAt": lambda n : setattr(self, 'payment_failed_at', n.get_datetime_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "setupStep": lambda n : setattr(self, 'setup_step', n.get_enum_value(OrganizationTableRow_setupStep)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(OrganizationTableRow_status)),
            "subscriptionCancelAt": lambda n : setattr(self, 'subscription_cancel_at', n.get_datetime_value()),
            "subscriptionStatus": lambda n : setattr(self, 'subscription_status', n.get_enum_value(OrganizationTableRow_subscriptionStatus)),
            "tenDlcStatus": lambda n : setattr(self, 'ten_dlc_status', n.get_enum_value(OrganizationTableRow_tenDlcStatus)),
            "userCount": lambda n : setattr(self, 'user_count', n.get_int_value()),
            "website": lambda n : setattr(self, 'website', n.get_str_value()),
            "websiteStatus": lambda n : setattr(self, 'website_status', n.get_enum_value(OrganizationTableRow_websiteStatus)),
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
        writer.write_float_value("accountBalance", self.account_balance)
        writer.write_enum_value("activationStatus", self.activation_status)
        writer.write_datetime_value("apiKeyExpiresAt", self.api_key_expires_at)
        writer.write_datetime_value("apiKeyFirstUsedAt", self.api_key_first_used_at)
        writer.write_datetime_value("apiKeyIssuedAt", self.api_key_issued_at)
        writer.write_datetime_value("apiKeyLastUsedAt", self.api_key_last_used_at)
        writer.write_collection_of_primitive_values("apiKeyPermissions", self.api_key_permissions)
        writer.write_str_value("apiKeyPreview", self.api_key_preview)
        writer.write_int_value("apiKeyTotalUses", self.api_key_total_uses)
        writer.write_enum_value("billingPlan", self.billing_plan)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_str_value("industry", self.industry)
        writer.write_datetime_value("lastSubscriptionEventAt", self.last_subscription_event_at)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_bool_value("needsAdminReview", self.needs_admin_review)
        writer.write_object_value("organization", self.organization)
        writer.write_datetime_value("paymentFailedAt", self.payment_failed_at)
        writer.write_str_value("phone", self.phone)
        writer.write_enum_value("setupStep", self.setup_step)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("subscriptionCancelAt", self.subscription_cancel_at)
        writer.write_enum_value("subscriptionStatus", self.subscription_status)
        writer.write_enum_value("tenDlcStatus", self.ten_dlc_status)
        writer.write_int_value("userCount", self.user_count)
        writer.write_str_value("website", self.website)
        writer.write_enum_value("websiteStatus", self.website_status)
        writer.write_additional_data_value(self.additional_data)
    

