from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .internal_phone_number_status import InternalPhoneNumberStatus
    from .phone_number_inventory_state import PhoneNumberInventoryState
    from .phone_number_provider_lifecycle_state import PhoneNumberProviderLifecycleState
    from .phone_number_table_row_admin_enablement_override import PhoneNumberTableRow_adminEnablementOverride
    from .phone_number_table_row_call_warmup_stage import PhoneNumberTableRow_callWarmupStage
    from .phone_number_table_row_call_warmup_state import PhoneNumberTableRow_callWarmupState
    from .phone_number_table_row_health_status import PhoneNumberTableRow_healthStatus
    from .phone_number_table_row_warmup_state import PhoneNumberTableRow_warmupState

@dataclass
class PhoneNumberTableRow(AdditionalDataHolder, Parsable):
    """
    List item schema for Leadping API phone number table row results shown in searchable tables.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Admin override that can enable or disable this record independently of normal status checks.
    admin_enablement_override: Optional[PhoneNumberTableRow_adminEnablementOverride] = None
    # Billing attribution used to reconcile this phone number with subscription billing.
    billing_attribution: Optional[str] = None
    # Business summary connected to this phone number table row.
    business: Optional[str] = None
    # Unique Leadping business identifier connected to this phone number table row.
    business_id: Optional[str] = None
    # Indicates whether controlled voice call warmup is enabled for this phone number.
    call_warmup_enabled: Optional[bool] = None
    # Defines the supported voice call warmup stages for a Leadping-managed phone number.
    call_warmup_stage: Optional[PhoneNumberTableRow_callWarmupStage] = None
    # Defines the supported health states for controlled internal voice call warmup.
    call_warmup_state: Optional[PhoneNumberTableRow_callWarmupState] = None
    # SMS and voice capabilities available on this phone number.
    capabilities: Optional[str] = None
    # Indicates whether this phone number table row is active and available in the Leadping API.
    enabled: Optional[bool] = None
    # Defines the supported SMS Warmup Health State values.
    health_status: Optional[PhoneNumberTableRow_healthStatus] = None
    # Unique Leadping identifier for this phone number table row.
    id: Optional[str] = None
    # Indicates whether this record is restricted to internal Leadping testing.
    internal_test_only: Optional[bool] = None
    # Leadping inventory state for this phone number.
    inventory_state: Optional[PhoneNumberInventoryState] = None
    # Indicates whether this phone number is approved for the configured messaging program.
    is_messaging_program_approved: Optional[bool] = None
    # Geographic location metadata for the phone number, lead, or lookup result.
    location: Optional[str] = None
    # Display name for this phone number table row in the Leadping API.
    name: Optional[str] = None
    # E.164 phone number exposed by this phone number table row.
    number: Optional[str] = None
    # Ownership classification for this phone number, such as Leadping-owned or customer-owned.
    ownership: Optional[str] = None
    # Provider lifecycle state used to determine phone number readiness.
    provider_lifecycle_state: Optional[PhoneNumberProviderLifecycleState] = None
    # Reconciliation status comparing Leadping data with provider data.
    provider_reconciliation_status: Optional[str] = None
    # Provider lifecycle or delivery status for this phone number table row.
    provider_status: Optional[str] = None
    # Human-readable routing summary for this phone number.
    routing_summary: Optional[str] = None
    # Indicates whether SMS messaging is ready for this business or phone number.
    sms_ready: Optional[bool] = None
    # Current lifecycle status for this phone number table row in the Leadping API.
    status: Optional[InternalPhoneNumberStatus] = None
    # 10DLC campaign identifier associated with this sender or SMS event.
    ten_dlc_campaign_id: Optional[str] = None
    # 10DLC campaign status associated with this sender or SMS event.
    ten_dlc_campaign_status: Optional[str] = None
    # Type classification used to route and interpret this phone number table row in the Leadping API.
    type: Optional[str] = None
    # User summary connected to this phone number table row.
    user: Optional[str] = None
    # Indicates whether voice calling is ready for this business or phone number.
    voice_ready: Optional[bool] = None
    # Numeric sender warmup health score used by Leadping to assess deliverability readiness.
    warmup_health_score: Optional[int] = None
    # Indicates whether this phone number should only be used for warmup traffic.
    warmup_only: Optional[bool] = None
    # Percent complete for the SMS sender warmup plan.
    warmup_progress_percent: Optional[int] = None
    # Defines the supported SMS Warmup Health State values.
    warmup_state: Optional[PhoneNumberTableRow_warmupState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberTableRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberTableRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberTableRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .internal_phone_number_status import InternalPhoneNumberStatus
        from .phone_number_inventory_state import PhoneNumberInventoryState
        from .phone_number_provider_lifecycle_state import PhoneNumberProviderLifecycleState
        from .phone_number_table_row_admin_enablement_override import PhoneNumberTableRow_adminEnablementOverride
        from .phone_number_table_row_call_warmup_stage import PhoneNumberTableRow_callWarmupStage
        from .phone_number_table_row_call_warmup_state import PhoneNumberTableRow_callWarmupState
        from .phone_number_table_row_health_status import PhoneNumberTableRow_healthStatus
        from .phone_number_table_row_warmup_state import PhoneNumberTableRow_warmupState

        from .internal_phone_number_status import InternalPhoneNumberStatus
        from .phone_number_inventory_state import PhoneNumberInventoryState
        from .phone_number_provider_lifecycle_state import PhoneNumberProviderLifecycleState
        from .phone_number_table_row_admin_enablement_override import PhoneNumberTableRow_adminEnablementOverride
        from .phone_number_table_row_call_warmup_stage import PhoneNumberTableRow_callWarmupStage
        from .phone_number_table_row_call_warmup_state import PhoneNumberTableRow_callWarmupState
        from .phone_number_table_row_health_status import PhoneNumberTableRow_healthStatus
        from .phone_number_table_row_warmup_state import PhoneNumberTableRow_warmupState

        fields: dict[str, Callable[[Any], None]] = {
            "adminEnablementOverride": lambda n : setattr(self, 'admin_enablement_override', n.get_object_value(PhoneNumberTableRow_adminEnablementOverride)),
            "billingAttribution": lambda n : setattr(self, 'billing_attribution', n.get_str_value()),
            "business": lambda n : setattr(self, 'business', n.get_str_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "callWarmupEnabled": lambda n : setattr(self, 'call_warmup_enabled', n.get_bool_value()),
            "callWarmupStage": lambda n : setattr(self, 'call_warmup_stage', n.get_enum_value(PhoneNumberTableRow_callWarmupStage)),
            "callWarmupState": lambda n : setattr(self, 'call_warmup_state', n.get_enum_value(PhoneNumberTableRow_callWarmupState)),
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(PhoneNumberTableRow_healthStatus)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "internalTestOnly": lambda n : setattr(self, 'internal_test_only', n.get_bool_value()),
            "inventoryState": lambda n : setattr(self, 'inventory_state', n.get_enum_value(PhoneNumberInventoryState)),
            "isMessagingProgramApproved": lambda n : setattr(self, 'is_messaging_program_approved', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "ownership": lambda n : setattr(self, 'ownership', n.get_str_value()),
            "providerLifecycleState": lambda n : setattr(self, 'provider_lifecycle_state', n.get_enum_value(PhoneNumberProviderLifecycleState)),
            "providerReconciliationStatus": lambda n : setattr(self, 'provider_reconciliation_status', n.get_str_value()),
            "providerStatus": lambda n : setattr(self, 'provider_status', n.get_str_value()),
            "routingSummary": lambda n : setattr(self, 'routing_summary', n.get_str_value()),
            "smsReady": lambda n : setattr(self, 'sms_ready', n.get_bool_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(InternalPhoneNumberStatus)),
            "tenDlcCampaignId": lambda n : setattr(self, 'ten_dlc_campaign_id', n.get_str_value()),
            "tenDlcCampaignStatus": lambda n : setattr(self, 'ten_dlc_campaign_status', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_str_value()),
            "voiceReady": lambda n : setattr(self, 'voice_ready', n.get_bool_value()),
            "warmupHealthScore": lambda n : setattr(self, 'warmup_health_score', n.get_int_value()),
            "warmupOnly": lambda n : setattr(self, 'warmup_only', n.get_bool_value()),
            "warmupProgressPercent": lambda n : setattr(self, 'warmup_progress_percent', n.get_int_value()),
            "warmupState": lambda n : setattr(self, 'warmup_state', n.get_enum_value(PhoneNumberTableRow_warmupState)),
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
        writer.write_object_value("adminEnablementOverride", self.admin_enablement_override)
        writer.write_str_value("billingAttribution", self.billing_attribution)
        writer.write_str_value("business", self.business)
        writer.write_str_value("businessId", self.business_id)
        writer.write_bool_value("callWarmupEnabled", self.call_warmup_enabled)
        writer.write_enum_value("callWarmupStage", self.call_warmup_stage)
        writer.write_enum_value("callWarmupState", self.call_warmup_state)
        writer.write_str_value("capabilities", self.capabilities)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("internalTestOnly", self.internal_test_only)
        writer.write_enum_value("inventoryState", self.inventory_state)
        writer.write_bool_value("isMessagingProgramApproved", self.is_messaging_program_approved)
        writer.write_str_value("location", self.location)
        writer.write_str_value("name", self.name)
        writer.write_str_value("number", self.number)
        writer.write_str_value("ownership", self.ownership)
        writer.write_enum_value("providerLifecycleState", self.provider_lifecycle_state)
        writer.write_str_value("providerReconciliationStatus", self.provider_reconciliation_status)
        writer.write_str_value("providerStatus", self.provider_status)
        writer.write_str_value("routingSummary", self.routing_summary)
        writer.write_bool_value("smsReady", self.sms_ready)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("tenDlcCampaignId", self.ten_dlc_campaign_id)
        writer.write_str_value("tenDlcCampaignStatus", self.ten_dlc_campaign_status)
        writer.write_str_value("type", self.type)
        writer.write_str_value("user", self.user)
        writer.write_bool_value("voiceReady", self.voice_ready)
        writer.write_int_value("warmupHealthScore", self.warmup_health_score)
        writer.write_bool_value("warmupOnly", self.warmup_only)
        writer.write_int_value("warmupProgressPercent", self.warmup_progress_percent)
        writer.write_enum_value("warmupState", self.warmup_state)
        writer.write_additional_data_value(self.additional_data)
    

