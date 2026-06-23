from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .internal_phone_number_status import InternalPhoneNumberStatus
    from .phone_number_billing_attribution import PhoneNumberBillingAttribution
    from .phone_number_capabilities import PhoneNumberCapabilities
    from .phone_number_event_record import PhoneNumberEventRecord
    from .phone_number_inventory_state import PhoneNumberInventoryState
    from .phone_number_response_admin_enablement_override import PhoneNumberResponse_adminEnablementOverride
    from .phone_number_response_business import PhoneNumberResponse_business
    from .phone_number_response_call_warmup_stage import PhoneNumberResponse_callWarmupStage
    from .phone_number_response_call_warmup_state import PhoneNumberResponse_callWarmupState
    from .phone_number_response_health_status import PhoneNumberResponse_healthStatus
    from .phone_number_response_location import PhoneNumberResponse_location
    from .phone_number_response_user import PhoneNumberResponse_user
    from .phone_number_response_warmup_state import PhoneNumberResponse_warmupState
    from .phone_number_routing_metadata import PhoneNumberRoutingMetadata
    from .phone_number_ten_dlc_association import PhoneNumberTenDlcAssociation

@dataclass
class PhoneNumberResponse(AdditionalDataHolder, Parsable):
    """
    API response containing phone number data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The adminEnablementOverride property
    admin_enablement_override: Optional[PhoneNumberResponse_adminEnablementOverride] = None
    # The billing value for this phone number.
    billing: Optional[PhoneNumberBillingAttribution] = None
    # The business value for this phone number.
    business: Optional[PhoneNumberResponse_business] = None
    # Whether controlled internal voice call warmup is enabled for this phone number.
    call_warmup_enabled: Optional[bool] = None
    # The human-readable voice call warmup health reason for this phone number.
    call_warmup_health_reason: Optional[str] = None
    # The next voice call warmup action time for this phone number.
    call_warmup_next_action_at: Optional[datetime.datetime] = None
    # The human-readable voice call warmup pause reason for this phone number.
    call_warmup_pause_reason: Optional[str] = None
    # Defines the supported voice call warmup stages for a Leadping-managed phone number.
    call_warmup_stage: Optional[PhoneNumberResponse_callWarmupStage] = None
    # Defines the supported health states for controlled internal voice call warmup.
    call_warmup_state: Optional[PhoneNumberResponse_callWarmupState] = None
    # The campaign ID associated with this phone number.
    campaign_id: Optional[str] = None
    # The capabilities value for this phone number.
    capabilities: Optional[PhoneNumberCapabilities] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # Whether this phone number is enabled.
    enabled: Optional[bool] = None
    # The events included with this phone number.
    events: Optional[list[PhoneNumberEventRecord]] = None
    # The human-readable health reason explaining this phone number.
    health_reason: Optional[str] = None
    # Defines the supported SMS Warmup Health State values.
    health_status: Optional[PhoneNumberResponse_healthStatus] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # The current inventory state for this phone number.
    inventory_state: Optional[PhoneNumberInventoryState] = None
    # Whether this phone number is approved test destination.
    is_approved_test_destination: Optional[bool] = None
    # Whether this phone number is default.
    is_default: Optional[bool] = None
    # Whether this phone number is internal pool.
    is_internal_pool: Optional[bool] = None
    # Whether this phone number is messaging program approved.
    is_messaging_program_approved: Optional[bool] = None
    # Whether this phone number is preferred.
    is_preferred: Optional[bool] = None
    # Whether this phone number is Leadping owned.
    leadping_owned: Optional[bool] = None
    # The location value for this phone number.
    location: Optional[PhoneNumberResponse_location] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # The display name for the entity.
    name: Optional[str] = None
    # The number value for this phone number.
    number: Optional[str] = None
    # The provider value for this phone number.
    provider: Optional[str] = None
    # The provider error value for this phone number.
    provider_error: Optional[str] = None
    # The provider order ID associated with this phone number.
    provider_order_id: Optional[str] = None
    # The current provider order status for this phone number.
    provider_order_status: Optional[str] = None
    # The provider phone number ID associated with this phone number.
    provider_phone_number_id: Optional[str] = None
    # The providerReleaseHoldStartsAt property
    provider_release_hold_starts_at: Optional[datetime.datetime] = None
    # The providerReleaseReason property
    provider_release_reason: Optional[str] = None
    # The providerReleaseRequestedAt property
    provider_release_requested_at: Optional[datetime.datetime] = None
    # The providerReleaseRequestedByName property
    provider_release_requested_by_name: Optional[str] = None
    # The providerReleaseRequestedByUserId property
    provider_release_requested_by_user_id: Optional[str] = None
    # The providerReleaseScheduledAt property
    provider_release_scheduled_at: Optional[datetime.datetime] = None
    # The providerReleaseUnassignAtHoldStart property
    provider_release_unassign_at_hold_start: Optional[bool] = None
    # The date and time for the provider released at value on this phone number.
    provider_released_at: Optional[datetime.datetime] = None
    # The current provider status for this phone number.
    provider_status: Optional[str] = None
    # The date and time for the provider synced at value on this phone number.
    provider_synced_at: Optional[datetime.datetime] = None
    # The routing value for this phone number.
    routing: Optional[PhoneNumberRoutingMetadata] = None
    # The source ID associated with this phone number.
    source_id: Optional[str] = None
    # The current status for this phone number.
    status: Optional[InternalPhoneNumberStatus] = None
    # The team ID associated with this phone number.
    team_id: Optional[str] = None
    # The 10DLC value for this phone number.
    ten_dlc: Optional[PhoneNumberTenDlcAssociation] = None
    # The user value for this phone number.
    user: Optional[PhoneNumberResponse_user] = None
    # Whether warmup is enabled for this phone number.
    warmup_enabled: Optional[bool] = None
    # The warmup health score metric for this phone number.
    warmup_health_score: Optional[int] = None
    # The date and time for the warmup next action at value on this phone number.
    warmup_next_action_at: Optional[datetime.datetime] = None
    # The human-readable warmup pause reason explaining this phone number.
    warmup_pause_reason: Optional[str] = None
    # The warmup progress percent metric for this phone number.
    warmup_progress_percent: Optional[int] = None
    # Defines the supported SMS Warmup Health State values.
    warmup_state: Optional[PhoneNumberResponse_warmupState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .internal_phone_number_status import InternalPhoneNumberStatus
        from .phone_number_billing_attribution import PhoneNumberBillingAttribution
        from .phone_number_capabilities import PhoneNumberCapabilities
        from .phone_number_event_record import PhoneNumberEventRecord
        from .phone_number_inventory_state import PhoneNumberInventoryState
        from .phone_number_response_admin_enablement_override import PhoneNumberResponse_adminEnablementOverride
        from .phone_number_response_business import PhoneNumberResponse_business
        from .phone_number_response_call_warmup_stage import PhoneNumberResponse_callWarmupStage
        from .phone_number_response_call_warmup_state import PhoneNumberResponse_callWarmupState
        from .phone_number_response_health_status import PhoneNumberResponse_healthStatus
        from .phone_number_response_location import PhoneNumberResponse_location
        from .phone_number_response_user import PhoneNumberResponse_user
        from .phone_number_response_warmup_state import PhoneNumberResponse_warmupState
        from .phone_number_routing_metadata import PhoneNumberRoutingMetadata
        from .phone_number_ten_dlc_association import PhoneNumberTenDlcAssociation

        from .internal_phone_number_status import InternalPhoneNumberStatus
        from .phone_number_billing_attribution import PhoneNumberBillingAttribution
        from .phone_number_capabilities import PhoneNumberCapabilities
        from .phone_number_event_record import PhoneNumberEventRecord
        from .phone_number_inventory_state import PhoneNumberInventoryState
        from .phone_number_response_admin_enablement_override import PhoneNumberResponse_adminEnablementOverride
        from .phone_number_response_business import PhoneNumberResponse_business
        from .phone_number_response_call_warmup_stage import PhoneNumberResponse_callWarmupStage
        from .phone_number_response_call_warmup_state import PhoneNumberResponse_callWarmupState
        from .phone_number_response_health_status import PhoneNumberResponse_healthStatus
        from .phone_number_response_location import PhoneNumberResponse_location
        from .phone_number_response_user import PhoneNumberResponse_user
        from .phone_number_response_warmup_state import PhoneNumberResponse_warmupState
        from .phone_number_routing_metadata import PhoneNumberRoutingMetadata
        from .phone_number_ten_dlc_association import PhoneNumberTenDlcAssociation

        fields: dict[str, Callable[[Any], None]] = {
            "adminEnablementOverride": lambda n : setattr(self, 'admin_enablement_override', n.get_object_value(PhoneNumberResponse_adminEnablementOverride)),
            "billing": lambda n : setattr(self, 'billing', n.get_object_value(PhoneNumberBillingAttribution)),
            "business": lambda n : setattr(self, 'business', n.get_object_value(PhoneNumberResponse_business)),
            "callWarmupEnabled": lambda n : setattr(self, 'call_warmup_enabled', n.get_bool_value()),
            "callWarmupHealthReason": lambda n : setattr(self, 'call_warmup_health_reason', n.get_str_value()),
            "callWarmupNextActionAt": lambda n : setattr(self, 'call_warmup_next_action_at', n.get_datetime_value()),
            "callWarmupPauseReason": lambda n : setattr(self, 'call_warmup_pause_reason', n.get_str_value()),
            "callWarmupStage": lambda n : setattr(self, 'call_warmup_stage', n.get_enum_value(PhoneNumberResponse_callWarmupStage)),
            "callWarmupState": lambda n : setattr(self, 'call_warmup_state', n.get_enum_value(PhoneNumberResponse_callWarmupState)),
            "campaignId": lambda n : setattr(self, 'campaign_id', n.get_str_value()),
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_object_value(PhoneNumberCapabilities)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(PhoneNumberEventRecord)),
            "healthReason": lambda n : setattr(self, 'health_reason', n.get_str_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(PhoneNumberResponse_healthStatus)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "inventoryState": lambda n : setattr(self, 'inventory_state', n.get_enum_value(PhoneNumberInventoryState)),
            "isApprovedTestDestination": lambda n : setattr(self, 'is_approved_test_destination', n.get_bool_value()),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "isInternalPool": lambda n : setattr(self, 'is_internal_pool', n.get_bool_value()),
            "isMessagingProgramApproved": lambda n : setattr(self, 'is_messaging_program_approved', n.get_bool_value()),
            "isPreferred": lambda n : setattr(self, 'is_preferred', n.get_bool_value()),
            "leadpingOwned": lambda n : setattr(self, 'leadping_owned', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(PhoneNumberResponse_location)),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
            "providerError": lambda n : setattr(self, 'provider_error', n.get_str_value()),
            "providerOrderId": lambda n : setattr(self, 'provider_order_id', n.get_str_value()),
            "providerOrderStatus": lambda n : setattr(self, 'provider_order_status', n.get_str_value()),
            "providerPhoneNumberId": lambda n : setattr(self, 'provider_phone_number_id', n.get_str_value()),
            "providerReleaseHoldStartsAt": lambda n : setattr(self, 'provider_release_hold_starts_at', n.get_datetime_value()),
            "providerReleaseReason": lambda n : setattr(self, 'provider_release_reason', n.get_str_value()),
            "providerReleaseRequestedAt": lambda n : setattr(self, 'provider_release_requested_at', n.get_datetime_value()),
            "providerReleaseRequestedByName": lambda n : setattr(self, 'provider_release_requested_by_name', n.get_str_value()),
            "providerReleaseRequestedByUserId": lambda n : setattr(self, 'provider_release_requested_by_user_id', n.get_str_value()),
            "providerReleaseScheduledAt": lambda n : setattr(self, 'provider_release_scheduled_at', n.get_datetime_value()),
            "providerReleaseUnassignAtHoldStart": lambda n : setattr(self, 'provider_release_unassign_at_hold_start', n.get_bool_value()),
            "providerReleasedAt": lambda n : setattr(self, 'provider_released_at', n.get_datetime_value()),
            "providerStatus": lambda n : setattr(self, 'provider_status', n.get_str_value()),
            "providerSyncedAt": lambda n : setattr(self, 'provider_synced_at', n.get_datetime_value()),
            "routing": lambda n : setattr(self, 'routing', n.get_object_value(PhoneNumberRoutingMetadata)),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(InternalPhoneNumberStatus)),
            "teamId": lambda n : setattr(self, 'team_id', n.get_str_value()),
            "tenDlc": lambda n : setattr(self, 'ten_dlc', n.get_object_value(PhoneNumberTenDlcAssociation)),
            "user": lambda n : setattr(self, 'user', n.get_object_value(PhoneNumberResponse_user)),
            "warmupEnabled": lambda n : setattr(self, 'warmup_enabled', n.get_bool_value()),
            "warmupHealthScore": lambda n : setattr(self, 'warmup_health_score', n.get_int_value()),
            "warmupNextActionAt": lambda n : setattr(self, 'warmup_next_action_at', n.get_datetime_value()),
            "warmupPauseReason": lambda n : setattr(self, 'warmup_pause_reason', n.get_str_value()),
            "warmupProgressPercent": lambda n : setattr(self, 'warmup_progress_percent', n.get_int_value()),
            "warmupState": lambda n : setattr(self, 'warmup_state', n.get_enum_value(PhoneNumberResponse_warmupState)),
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
        writer.write_object_value("billing", self.billing)
        writer.write_object_value("business", self.business)
        writer.write_bool_value("callWarmupEnabled", self.call_warmup_enabled)
        writer.write_str_value("callWarmupHealthReason", self.call_warmup_health_reason)
        writer.write_datetime_value("callWarmupNextActionAt", self.call_warmup_next_action_at)
        writer.write_str_value("callWarmupPauseReason", self.call_warmup_pause_reason)
        writer.write_enum_value("callWarmupStage", self.call_warmup_stage)
        writer.write_enum_value("callWarmupState", self.call_warmup_state)
        writer.write_str_value("campaignId", self.campaign_id)
        writer.write_object_value("capabilities", self.capabilities)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_str_value("healthReason", self.health_reason)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("id", self.id)
        writer.write_enum_value("inventoryState", self.inventory_state)
        writer.write_bool_value("isApprovedTestDestination", self.is_approved_test_destination)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("isInternalPool", self.is_internal_pool)
        writer.write_bool_value("isMessagingProgramApproved", self.is_messaging_program_approved)
        writer.write_bool_value("isPreferred", self.is_preferred)
        writer.write_bool_value("leadpingOwned", self.leadping_owned)
        writer.write_object_value("location", self.location)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_str_value("number", self.number)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("providerError", self.provider_error)
        writer.write_str_value("providerOrderId", self.provider_order_id)
        writer.write_str_value("providerOrderStatus", self.provider_order_status)
        writer.write_str_value("providerPhoneNumberId", self.provider_phone_number_id)
        writer.write_datetime_value("providerReleaseHoldStartsAt", self.provider_release_hold_starts_at)
        writer.write_str_value("providerReleaseReason", self.provider_release_reason)
        writer.write_datetime_value("providerReleaseRequestedAt", self.provider_release_requested_at)
        writer.write_str_value("providerReleaseRequestedByName", self.provider_release_requested_by_name)
        writer.write_str_value("providerReleaseRequestedByUserId", self.provider_release_requested_by_user_id)
        writer.write_datetime_value("providerReleaseScheduledAt", self.provider_release_scheduled_at)
        writer.write_bool_value("providerReleaseUnassignAtHoldStart", self.provider_release_unassign_at_hold_start)
        writer.write_datetime_value("providerReleasedAt", self.provider_released_at)
        writer.write_str_value("providerStatus", self.provider_status)
        writer.write_datetime_value("providerSyncedAt", self.provider_synced_at)
        writer.write_object_value("routing", self.routing)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("teamId", self.team_id)
        writer.write_object_value("tenDlc", self.ten_dlc)
        writer.write_object_value("user", self.user)
        writer.write_bool_value("warmupEnabled", self.warmup_enabled)
        writer.write_int_value("warmupHealthScore", self.warmup_health_score)
        writer.write_datetime_value("warmupNextActionAt", self.warmup_next_action_at)
        writer.write_str_value("warmupPauseReason", self.warmup_pause_reason)
        writer.write_int_value("warmupProgressPercent", self.warmup_progress_percent)
        writer.write_enum_value("warmupState", self.warmup_state)
        writer.write_additional_data_value(self.additional_data)
    

