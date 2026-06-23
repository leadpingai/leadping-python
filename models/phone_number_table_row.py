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
    from .phone_number_table_row_health_status import PhoneNumberTableRow_healthStatus
    from .phone_number_table_row_warmup_state import PhoneNumberTableRow_warmupState

@dataclass
class PhoneNumberTableRow(AdditionalDataHolder, Parsable):
    """
    API DTO containing phone number data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The admin force enablement override on this phone number.
    admin_enablement_override: Optional[PhoneNumberTableRow_adminEnablementOverride] = None
    # The billing attribution value for this phone number.
    billing_attribution: Optional[str] = None
    # The business value for this phone number.
    business: Optional[str] = None
    # The capabilities value for this phone number.
    capabilities: Optional[str] = None
    # Whether this phone number is enabled.
    enabled: Optional[bool] = None
    # Defines the supported SMS Warmup Health State values.
    health_status: Optional[PhoneNumberTableRow_healthStatus] = None
    # The unique ID for this phone number.
    id: Optional[str] = None
    # Whether internal test only applies to this phone number.
    internal_test_only: Optional[bool] = None
    # The current inventory state for this phone number.
    inventory_state: Optional[PhoneNumberInventoryState] = None
    # Whether this phone number is messaging program approved.
    is_messaging_program_approved: Optional[bool] = None
    # The location value for this phone number.
    location: Optional[str] = None
    # The human-readable name shown for this phone number.
    name: Optional[str] = None
    # The number value for this phone number.
    number: Optional[str] = None
    # The ownership value for this phone number.
    ownership: Optional[str] = None
    # The current provider lifecycle state for this phone number.
    provider_lifecycle_state: Optional[PhoneNumberProviderLifecycleState] = None
    # The current provider reconciliation status for this phone number.
    provider_reconciliation_status: Optional[str] = None
    # The current provider status for this phone number.
    provider_status: Optional[str] = None
    # The routing summary value for this phone number.
    routing_summary: Optional[str] = None
    # Whether this phone number is SMS ready.
    sms_ready: Optional[bool] = None
    # The current status for this phone number.
    status: Optional[InternalPhoneNumberStatus] = None
    # The 10DLC campaign ID associated with this phone number.
    ten_dlc_campaign_id: Optional[str] = None
    # The current 10DLC campaign status for this phone number.
    ten_dlc_campaign_status: Optional[str] = None
    # The type classification for this phone number.
    type: Optional[str] = None
    # The user value for this phone number.
    user: Optional[str] = None
    # Whether this phone number is voice ready.
    voice_ready: Optional[bool] = None
    # The warmup health score metric for this phone number.
    warmup_health_score: Optional[int] = None
    # Whether warmup only applies to this phone number.
    warmup_only: Optional[bool] = None
    # The warmup progress percent metric for this phone number.
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
        from .phone_number_table_row_health_status import PhoneNumberTableRow_healthStatus
        from .phone_number_table_row_warmup_state import PhoneNumberTableRow_warmupState

        from .internal_phone_number_status import InternalPhoneNumberStatus
        from .phone_number_inventory_state import PhoneNumberInventoryState
        from .phone_number_provider_lifecycle_state import PhoneNumberProviderLifecycleState
        from .phone_number_table_row_admin_enablement_override import PhoneNumberTableRow_adminEnablementOverride
        from .phone_number_table_row_health_status import PhoneNumberTableRow_healthStatus
        from .phone_number_table_row_warmup_state import PhoneNumberTableRow_warmupState

        fields: dict[str, Callable[[Any], None]] = {
            "adminEnablementOverride": lambda n : setattr(self, 'admin_enablement_override', n.get_object_value(PhoneNumberTableRow_adminEnablementOverride)),
            "billingAttribution": lambda n : setattr(self, 'billing_attribution', n.get_str_value()),
            "business": lambda n : setattr(self, 'business', n.get_str_value()),
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
    

