from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .organization_member_role import OrganizationMemberRole
    from .organization_switch_option_activation_status import OrganizationSwitchOption_activationStatus
    from .organization_switch_option_organization_status import OrganizationSwitchOption_organizationStatus
    from .organization_switch_option_ten_dlc_status import OrganizationSwitchOption_tenDlcStatus

@dataclass
class OrganizationSwitchOption(AdditionalDataHolder, Parsable):
    """
    Describes organization switch option data used in Leadping API requests and responses.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Summarizes an organization's overall progress from initial Leadping onboarding through launch readiness.
    activation_status: Optional[OrganizationSwitchOption_activationStatus] = None
    # Activation summary for this organization switch option.
    activation_summary: Optional[str] = None
    # Whether the organization has a default billing payment method.
    has_payment_method: Optional[bool] = None
    # Unique Leadping identifier for this organization switch option.
    id: Optional[str] = None
    # Whether this organization switch option is current.
    is_current: Optional[bool] = None
    # UTC timestamp for last used at on this organization switch option.
    last_used_at: Optional[datetime.datetime] = None
    # The human-readable name shown for this organization switch option.
    name: Optional[str] = None
    # Whether needs admin review applies to this organization switch option.
    needs_admin_review: Optional[bool] = None
    # Describes an organization's account lifecycle and whether it can actively use Leadping services.
    organization_status: Optional[OrganizationSwitchOption_organizationStatus] = None
    # Whether ready for customer traffic applies to this organization switch option.
    ready_for_customer_traffic: Optional[bool] = None
    # Role for this organization switch option.
    role: Optional[OrganizationMemberRole] = None
    # Describes an organization's overall 10DLC registration lifecycle across brand and messaging campaign submission.
    ten_dlc_status: Optional[OrganizationSwitchOption_tenDlcStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationSwitchOption:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationSwitchOption
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationSwitchOption()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .organization_member_role import OrganizationMemberRole
        from .organization_switch_option_activation_status import OrganizationSwitchOption_activationStatus
        from .organization_switch_option_organization_status import OrganizationSwitchOption_organizationStatus
        from .organization_switch_option_ten_dlc_status import OrganizationSwitchOption_tenDlcStatus

        from .organization_member_role import OrganizationMemberRole
        from .organization_switch_option_activation_status import OrganizationSwitchOption_activationStatus
        from .organization_switch_option_organization_status import OrganizationSwitchOption_organizationStatus
        from .organization_switch_option_ten_dlc_status import OrganizationSwitchOption_tenDlcStatus

        fields: dict[str, Callable[[Any], None]] = {
            "activationStatus": lambda n : setattr(self, 'activation_status', n.get_enum_value(OrganizationSwitchOption_activationStatus)),
            "activationSummary": lambda n : setattr(self, 'activation_summary', n.get_str_value()),
            "hasPaymentMethod": lambda n : setattr(self, 'has_payment_method', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isCurrent": lambda n : setattr(self, 'is_current', n.get_bool_value()),
            "lastUsedAt": lambda n : setattr(self, 'last_used_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "needsAdminReview": lambda n : setattr(self, 'needs_admin_review', n.get_bool_value()),
            "organizationStatus": lambda n : setattr(self, 'organization_status', n.get_enum_value(OrganizationSwitchOption_organizationStatus)),
            "readyForCustomerTraffic": lambda n : setattr(self, 'ready_for_customer_traffic', n.get_bool_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(OrganizationMemberRole)),
            "tenDlcStatus": lambda n : setattr(self, 'ten_dlc_status', n.get_enum_value(OrganizationSwitchOption_tenDlcStatus)),
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
        writer.write_str_value("activationSummary", self.activation_summary)
        writer.write_bool_value("hasPaymentMethod", self.has_payment_method)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isCurrent", self.is_current)
        writer.write_datetime_value("lastUsedAt", self.last_used_at)
        writer.write_str_value("name", self.name)
        writer.write_bool_value("needsAdminReview", self.needs_admin_review)
        writer.write_enum_value("organizationStatus", self.organization_status)
        writer.write_bool_value("readyForCustomerTraffic", self.ready_for_customer_traffic)
        writer.write_enum_value("role", self.role)
        writer.write_enum_value("tenDlcStatus", self.ten_dlc_status)
        writer.write_additional_data_value(self.additional_data)
    

