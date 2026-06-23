from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_request_activation import BusinessRequest_activation
    from .business_request_address import BusinessRequest_address
    from .business_request_admin_enablement_override import BusinessRequest_adminEnablementOverride
    from .business_request_billing_plan import BusinessRequest_billingPlan
    from .business_request_compliance_policy import BusinessRequest_compliancePolicy
    from .business_request_ein_document import BusinessRequest_einDocument
    from .business_request_setup_step import BusinessRequest_setupStep
    from .business_request_status import BusinessRequest_status
    from .business_request_stripe_info import BusinessRequest_stripeInfo
    from .business_request_subscription_status import BusinessRequest_subscriptionStatus
    from .id_name_value import IdNameValue

@dataclass
class BusinessRequest(AdditionalDataHolder, Parsable):
    """
    Request payload for business.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The activation value for this business.
    activation: Optional[BusinessRequest_activation] = None
    # The postal address associated with this business.
    address: Optional[BusinessRequest_address] = None
    # The adminEnablementOverride property
    admin_enablement_override: Optional[BusinessRequest_adminEnablementOverride] = None
    # Whether auto refill is enabled for this business wallet.
    auto_refill_enabled: Optional[bool] = None
    # Defines the supported Billing Plan values.
    billing_plan: Optional[BusinessRequest_billingPlan] = None
    # The compliance policy value for this business.
    compliance_policy: Optional[BusinessRequest_compliancePolicy] = None
    # The human-readable description of this business.
    description: Optional[str] = None
    # The EIN value for this business.
    ein: Optional[str] = None
    # The EIN document value for this business.
    ein_document: Optional[BusinessRequest_einDocument] = None
    # The enabled property
    enabled: Optional[bool] = None
    # The unique identifier for the entity, when updating an existing entity.
    id: Optional[str] = None
    # Whether this business is younger than90.
    is_younger_than90: Optional[bool] = None
    # The display name for the entity.
    name: Optional[str] = None
    # The phone number associated with this business.
    phone: Optional[str] = None
    # The phones included with this business.
    phones: Optional[list[IdNameValue]] = None
    # The secondary name value for this business.
    secondary_name: Optional[str] = None
    # Defines the supported Business Setup Step values.
    setup_step: Optional[BusinessRequest_setupStep] = None
    # Defines the supported Business Status values.
    status: Optional[BusinessRequest_status] = None
    # Stripe billing state owned by this business.
    stripe_info: Optional[BusinessRequest_stripeInfo] = None
    # Defines the supported Subscription Status values.
    subscription_status: Optional[BusinessRequest_subscriptionStatus] = None
    # The vertical value for this business.
    vertical: Optional[str] = None
    # The website URL associated with this business.
    website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .business_request_activation import BusinessRequest_activation
        from .business_request_address import BusinessRequest_address
        from .business_request_admin_enablement_override import BusinessRequest_adminEnablementOverride
        from .business_request_billing_plan import BusinessRequest_billingPlan
        from .business_request_compliance_policy import BusinessRequest_compliancePolicy
        from .business_request_ein_document import BusinessRequest_einDocument
        from .business_request_setup_step import BusinessRequest_setupStep
        from .business_request_status import BusinessRequest_status
        from .business_request_stripe_info import BusinessRequest_stripeInfo
        from .business_request_subscription_status import BusinessRequest_subscriptionStatus
        from .id_name_value import IdNameValue

        from .business_request_activation import BusinessRequest_activation
        from .business_request_address import BusinessRequest_address
        from .business_request_admin_enablement_override import BusinessRequest_adminEnablementOverride
        from .business_request_billing_plan import BusinessRequest_billingPlan
        from .business_request_compliance_policy import BusinessRequest_compliancePolicy
        from .business_request_ein_document import BusinessRequest_einDocument
        from .business_request_setup_step import BusinessRequest_setupStep
        from .business_request_status import BusinessRequest_status
        from .business_request_stripe_info import BusinessRequest_stripeInfo
        from .business_request_subscription_status import BusinessRequest_subscriptionStatus
        from .id_name_value import IdNameValue

        fields: dict[str, Callable[[Any], None]] = {
            "activation": lambda n : setattr(self, 'activation', n.get_object_value(BusinessRequest_activation)),
            "address": lambda n : setattr(self, 'address', n.get_object_value(BusinessRequest_address)),
            "adminEnablementOverride": lambda n : setattr(self, 'admin_enablement_override', n.get_object_value(BusinessRequest_adminEnablementOverride)),
            "autoRefillEnabled": lambda n : setattr(self, 'auto_refill_enabled', n.get_bool_value()),
            "billingPlan": lambda n : setattr(self, 'billing_plan', n.get_enum_value(BusinessRequest_billingPlan)),
            "compliancePolicy": lambda n : setattr(self, 'compliance_policy', n.get_object_value(BusinessRequest_compliancePolicy)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "ein": lambda n : setattr(self, 'ein', n.get_str_value()),
            "einDocument": lambda n : setattr(self, 'ein_document', n.get_object_value(BusinessRequest_einDocument)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isYoungerThan90": lambda n : setattr(self, 'is_younger_than90', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(IdNameValue)),
            "secondaryName": lambda n : setattr(self, 'secondary_name', n.get_str_value()),
            "setupStep": lambda n : setattr(self, 'setup_step', n.get_enum_value(BusinessRequest_setupStep)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(BusinessRequest_status)),
            "stripeInfo": lambda n : setattr(self, 'stripe_info', n.get_object_value(BusinessRequest_stripeInfo)),
            "subscriptionStatus": lambda n : setattr(self, 'subscription_status', n.get_enum_value(BusinessRequest_subscriptionStatus)),
            "vertical": lambda n : setattr(self, 'vertical', n.get_str_value()),
            "website": lambda n : setattr(self, 'website', n.get_str_value()),
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
        writer.write_object_value("activation", self.activation)
        writer.write_object_value("address", self.address)
        writer.write_object_value("adminEnablementOverride", self.admin_enablement_override)
        writer.write_bool_value("autoRefillEnabled", self.auto_refill_enabled)
        writer.write_enum_value("billingPlan", self.billing_plan)
        writer.write_object_value("compliancePolicy", self.compliance_policy)
        writer.write_str_value("description", self.description)
        writer.write_str_value("ein", self.ein)
        writer.write_object_value("einDocument", self.ein_document)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isYoungerThan90", self.is_younger_than90)
        writer.write_str_value("name", self.name)
        writer.write_str_value("phone", self.phone)
        writer.write_collection_of_object_values("phones", self.phones)
        writer.write_str_value("secondaryName", self.secondary_name)
        writer.write_enum_value("setupStep", self.setup_step)
        writer.write_enum_value("status", self.status)
        writer.write_object_value("stripeInfo", self.stripe_info)
        writer.write_enum_value("subscriptionStatus", self.subscription_status)
        writer.write_str_value("vertical", self.vertical)
        writer.write_str_value("website", self.website)
        writer.write_additional_data_value(self.additional_data)
    

