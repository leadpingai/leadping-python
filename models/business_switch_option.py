from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_switch_option_activation_status import BusinessSwitchOption_activationStatus
    from .business_switch_option_business_status import BusinessSwitchOption_businessStatus
    from .business_user_role import BusinessUserRole

@dataclass
class BusinessSwitchOption(AdditionalDataHolder, Parsable):
    """
    API DTO containing business switch option data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Defines the supported Customer Activation Status values.
    activation_status: Optional[BusinessSwitchOption_activationStatus] = None
    # The activation summary value for this business switch option.
    activation_summary: Optional[str] = None
    # Defines the supported Business Status values.
    business_status: Optional[BusinessSwitchOption_businessStatus] = None
    # Whether the business has a default billing payment method.
    has_payment_method: Optional[bool] = None
    # The unique ID for this business switch option.
    id: Optional[str] = None
    # Whether this business switch option is current.
    is_current: Optional[bool] = None
    # The date and time for the last used at value on this business switch option.
    last_used_at: Optional[datetime.datetime] = None
    # The human-readable name shown for this business switch option.
    name: Optional[str] = None
    # Whether needs admin review applies to this business switch option.
    needs_admin_review: Optional[bool] = None
    # Whether ready for customer traffic applies to this business switch option.
    ready_for_customer_traffic: Optional[bool] = None
    # The role value for this business switch option.
    role: Optional[BusinessUserRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessSwitchOption:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessSwitchOption
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessSwitchOption()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .business_switch_option_activation_status import BusinessSwitchOption_activationStatus
        from .business_switch_option_business_status import BusinessSwitchOption_businessStatus
        from .business_user_role import BusinessUserRole

        from .business_switch_option_activation_status import BusinessSwitchOption_activationStatus
        from .business_switch_option_business_status import BusinessSwitchOption_businessStatus
        from .business_user_role import BusinessUserRole

        fields: dict[str, Callable[[Any], None]] = {
            "activationStatus": lambda n : setattr(self, 'activation_status', n.get_enum_value(BusinessSwitchOption_activationStatus)),
            "activationSummary": lambda n : setattr(self, 'activation_summary', n.get_str_value()),
            "businessStatus": lambda n : setattr(self, 'business_status', n.get_enum_value(BusinessSwitchOption_businessStatus)),
            "hasPaymentMethod": lambda n : setattr(self, 'has_payment_method', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isCurrent": lambda n : setattr(self, 'is_current', n.get_bool_value()),
            "lastUsedAt": lambda n : setattr(self, 'last_used_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "needsAdminReview": lambda n : setattr(self, 'needs_admin_review', n.get_bool_value()),
            "readyForCustomerTraffic": lambda n : setattr(self, 'ready_for_customer_traffic', n.get_bool_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(BusinessUserRole)),
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
        writer.write_enum_value("businessStatus", self.business_status)
        writer.write_bool_value("hasPaymentMethod", self.has_payment_method)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isCurrent", self.is_current)
        writer.write_datetime_value("lastUsedAt", self.last_used_at)
        writer.write_str_value("name", self.name)
        writer.write_bool_value("needsAdminReview", self.needs_admin_review)
        writer.write_bool_value("readyForCustomerTraffic", self.ready_for_customer_traffic)
        writer.write_enum_value("role", self.role)
        writer.write_additional_data_value(self.additional_data)
    

