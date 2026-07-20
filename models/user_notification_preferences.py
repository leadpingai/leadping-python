from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_notification_preferences_sms_consent_trusted_form_certificate import UserNotificationPreferences_smsConsentTrustedFormCertificate

@dataclass
class UserNotificationPreferences(AdditionalDataHolder, Parsable):
    """
    API DTO containing user notification preferences data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether automation failed email functionality is enabled for this Leadping user notification preferences.
    automation_failed_email_enabled: Optional[bool] = None
    # Whether automation failed notifications are enabled for this user notification preferences.
    automation_failed_enabled: Optional[bool] = None
    # Indicates whether automation failed SMS functionality is enabled for this Leadping user notification preferences.
    automation_failed_sms_enabled: Optional[bool] = None
    # Whether billing email is enabled for this user notification preferences.
    billing_email_enabled: Optional[bool] = None
    # Whether billing SMS is enabled for this user notification preferences.
    billing_sms_enabled: Optional[bool] = None
    # Indicates whether low wallet balance email functionality is enabled for this Leadping user notification preferences.
    low_wallet_balance_email_enabled: Optional[bool] = None
    # Whether low wallet balance notifications are enabled for this user notification preferences.
    low_wallet_balance_enabled: Optional[bool] = None
    # Indicates whether low wallet balance SMS functionality is enabled for this Leadping user notification preferences.
    low_wallet_balance_sms_enabled: Optional[bool] = None
    # Indicates whether missed call email functionality is enabled for this Leadping user notification preferences.
    missed_call_email_enabled: Optional[bool] = None
    # Whether missed call notifications are enabled for this user notification preferences.
    missed_call_enabled: Optional[bool] = None
    # Indicates whether missed call SMS functionality is enabled for this Leadping user notification preferences.
    missed_call_sms_enabled: Optional[bool] = None
    # Whether new lead email is enabled for this user notification preferences.
    new_lead_email_enabled: Optional[bool] = None
    # Whether new lead notifications are enabled for this user notification preferences.
    new_lead_enabled: Optional[bool] = None
    # Whether new lead SMS is enabled for this user notification preferences.
    new_lead_sms_enabled: Optional[bool] = None
    # Whether payment failed notifications are enabled for this user notification preferences.
    payment_failed_enabled: Optional[bool] = None
    # Indicates whether payment failed SMS functionality is enabled for this Leadping user notification preferences.
    payment_failed_sms_enabled: Optional[bool] = None
    # Whether the user has consented to receive Leadping account notification SMS messages.
    sms_consent_opted_in: Optional[bool] = None
    # The TrustedForm certificate captured for the user's most recent SMS opt-in.
    sms_consent_trusted_form_certificate: Optional[UserNotificationPreferences_smsConsentTrustedFormCertificate] = None
    # When the user's Leadping notification SMS consent was last changed.
    sms_consent_updated_at: Optional[datetime.datetime] = None
    # Indicates whether subscription renewing email functionality is enabled for this Leadping user notification preferences.
    subscription_renewing_email_enabled: Optional[bool] = None
    # Whether subscription renewing notifications are enabled for this user notification preferences.
    subscription_renewing_enabled: Optional[bool] = None
    # Indicates whether subscription renewing SMS functionality is enabled for this Leadping user notification preferences.
    subscription_renewing_sms_enabled: Optional[bool] = None
    # Whether 10DLC status notifications are enabled for this user notification preferences.
    ten_dlc_status_enabled: Optional[bool] = None
    # Indicates whether unread SMS email functionality is enabled for this Leadping user notification preferences.
    unread_sms_email_enabled: Optional[bool] = None
    # Whether unread SMS notifications are enabled for this user notification preferences.
    unread_sms_enabled: Optional[bool] = None
    # Indicates whether unread SMS SMS functionality is enabled for this Leadping user notification preferences.
    unread_sms_sms_enabled: Optional[bool] = None
    # Whether usage limit hit notifications are enabled for this user notification preferences.
    usage_limit_hit_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserNotificationPreferences:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserNotificationPreferences
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserNotificationPreferences()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .user_notification_preferences_sms_consent_trusted_form_certificate import UserNotificationPreferences_smsConsentTrustedFormCertificate

        from .user_notification_preferences_sms_consent_trusted_form_certificate import UserNotificationPreferences_smsConsentTrustedFormCertificate

        fields: dict[str, Callable[[Any], None]] = {
            "automationFailedEmailEnabled": lambda n : setattr(self, 'automation_failed_email_enabled', n.get_bool_value()),
            "automationFailedEnabled": lambda n : setattr(self, 'automation_failed_enabled', n.get_bool_value()),
            "automationFailedSmsEnabled": lambda n : setattr(self, 'automation_failed_sms_enabled', n.get_bool_value()),
            "billingEmailEnabled": lambda n : setattr(self, 'billing_email_enabled', n.get_bool_value()),
            "billingSmsEnabled": lambda n : setattr(self, 'billing_sms_enabled', n.get_bool_value()),
            "lowWalletBalanceEmailEnabled": lambda n : setattr(self, 'low_wallet_balance_email_enabled', n.get_bool_value()),
            "lowWalletBalanceEnabled": lambda n : setattr(self, 'low_wallet_balance_enabled', n.get_bool_value()),
            "lowWalletBalanceSmsEnabled": lambda n : setattr(self, 'low_wallet_balance_sms_enabled', n.get_bool_value()),
            "missedCallEmailEnabled": lambda n : setattr(self, 'missed_call_email_enabled', n.get_bool_value()),
            "missedCallEnabled": lambda n : setattr(self, 'missed_call_enabled', n.get_bool_value()),
            "missedCallSmsEnabled": lambda n : setattr(self, 'missed_call_sms_enabled', n.get_bool_value()),
            "newLeadEmailEnabled": lambda n : setattr(self, 'new_lead_email_enabled', n.get_bool_value()),
            "newLeadEnabled": lambda n : setattr(self, 'new_lead_enabled', n.get_bool_value()),
            "newLeadSmsEnabled": lambda n : setattr(self, 'new_lead_sms_enabled', n.get_bool_value()),
            "paymentFailedEnabled": lambda n : setattr(self, 'payment_failed_enabled', n.get_bool_value()),
            "paymentFailedSmsEnabled": lambda n : setattr(self, 'payment_failed_sms_enabled', n.get_bool_value()),
            "smsConsentOptedIn": lambda n : setattr(self, 'sms_consent_opted_in', n.get_bool_value()),
            "smsConsentTrustedFormCertificate": lambda n : setattr(self, 'sms_consent_trusted_form_certificate', n.get_object_value(UserNotificationPreferences_smsConsentTrustedFormCertificate)),
            "smsConsentUpdatedAt": lambda n : setattr(self, 'sms_consent_updated_at', n.get_datetime_value()),
            "subscriptionRenewingEmailEnabled": lambda n : setattr(self, 'subscription_renewing_email_enabled', n.get_bool_value()),
            "subscriptionRenewingEnabled": lambda n : setattr(self, 'subscription_renewing_enabled', n.get_bool_value()),
            "subscriptionRenewingSmsEnabled": lambda n : setattr(self, 'subscription_renewing_sms_enabled', n.get_bool_value()),
            "tenDlcStatusEnabled": lambda n : setattr(self, 'ten_dlc_status_enabled', n.get_bool_value()),
            "unreadSmsEmailEnabled": lambda n : setattr(self, 'unread_sms_email_enabled', n.get_bool_value()),
            "unreadSmsEnabled": lambda n : setattr(self, 'unread_sms_enabled', n.get_bool_value()),
            "unreadSmsSmsEnabled": lambda n : setattr(self, 'unread_sms_sms_enabled', n.get_bool_value()),
            "usageLimitHitEnabled": lambda n : setattr(self, 'usage_limit_hit_enabled', n.get_bool_value()),
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
        writer.write_bool_value("automationFailedEmailEnabled", self.automation_failed_email_enabled)
        writer.write_bool_value("automationFailedEnabled", self.automation_failed_enabled)
        writer.write_bool_value("automationFailedSmsEnabled", self.automation_failed_sms_enabled)
        writer.write_bool_value("billingEmailEnabled", self.billing_email_enabled)
        writer.write_bool_value("billingSmsEnabled", self.billing_sms_enabled)
        writer.write_bool_value("lowWalletBalanceEmailEnabled", self.low_wallet_balance_email_enabled)
        writer.write_bool_value("lowWalletBalanceEnabled", self.low_wallet_balance_enabled)
        writer.write_bool_value("lowWalletBalanceSmsEnabled", self.low_wallet_balance_sms_enabled)
        writer.write_bool_value("missedCallEmailEnabled", self.missed_call_email_enabled)
        writer.write_bool_value("missedCallEnabled", self.missed_call_enabled)
        writer.write_bool_value("missedCallSmsEnabled", self.missed_call_sms_enabled)
        writer.write_bool_value("newLeadEmailEnabled", self.new_lead_email_enabled)
        writer.write_bool_value("newLeadEnabled", self.new_lead_enabled)
        writer.write_bool_value("newLeadSmsEnabled", self.new_lead_sms_enabled)
        writer.write_bool_value("paymentFailedEnabled", self.payment_failed_enabled)
        writer.write_bool_value("paymentFailedSmsEnabled", self.payment_failed_sms_enabled)
        writer.write_bool_value("smsConsentOptedIn", self.sms_consent_opted_in)
        writer.write_object_value("smsConsentTrustedFormCertificate", self.sms_consent_trusted_form_certificate)
        writer.write_datetime_value("smsConsentUpdatedAt", self.sms_consent_updated_at)
        writer.write_bool_value("subscriptionRenewingEmailEnabled", self.subscription_renewing_email_enabled)
        writer.write_bool_value("subscriptionRenewingEnabled", self.subscription_renewing_enabled)
        writer.write_bool_value("subscriptionRenewingSmsEnabled", self.subscription_renewing_sms_enabled)
        writer.write_bool_value("tenDlcStatusEnabled", self.ten_dlc_status_enabled)
        writer.write_bool_value("unreadSmsEmailEnabled", self.unread_sms_email_enabled)
        writer.write_bool_value("unreadSmsEnabled", self.unread_sms_enabled)
        writer.write_bool_value("unreadSmsSmsEnabled", self.unread_sms_sms_enabled)
        writer.write_bool_value("usageLimitHitEnabled", self.usage_limit_hit_enabled)
        writer.write_additional_data_value(self.additional_data)
    

