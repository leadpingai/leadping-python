from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_response_activation import BusinessResponse_activation
    from .business_response_address import BusinessResponse_address
    from .business_response_billing_address import BusinessResponse_billingAddress
    from .business_response_billing_plan import BusinessResponse_billingPlan
    from .business_response_billing_state import BusinessResponse_billingState
    from .business_response_compliance_policy import BusinessResponse_compliancePolicy
    from .business_response_ein_document import BusinessResponse_einDocument
    from .business_response_setup_status import BusinessResponse_setupStatus
    from .business_response_setup_step import BusinessResponse_setupStep
    from .business_response_site import BusinessResponse_site
    from .business_response_status import BusinessResponse_status
    from .business_response_subscription_status import BusinessResponse_subscriptionStatus
    from .business_response_user import BusinessResponse_user
    from .id_name_value import IdNameValue

@dataclass
class BusinessResponse(AdditionalDataHolder, Parsable):
    """
    Response schema for the Leadping API business profile response returned to authenticated clients.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Current wallet balance available to the business.
    account_balance: Optional[float] = None
    # Business activation state covering site, billing, compliance, and telephony readiness.
    activation: Optional[BusinessResponse_activation] = None
    # Postal address for the business, lead, or contact represented by this business profile response.
    address: Optional[BusinessResponse_address] = None
    # Indicates whether automatic wallet refill is enabled for the business.
    auto_refill_enabled: Optional[bool] = None
    # Postal address used for invoices, receipts, and payment processor billing records.
    billing_address: Optional[BusinessResponse_billingAddress] = None
    # Name used for invoices, receipts, and payment processor billing records.
    billing_name: Optional[str] = None
    # Defines the supported Billing Plan values.
    billing_plan: Optional[BusinessResponse_billingPlan] = None
    # Customer-safe billing state for this business.
    billing_state: Optional[BusinessResponse_billingState] = None
    # Compliance policy configuration for the business.
    compliance_policy: Optional[BusinessResponse_compliancePolicy] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # Human-readable description that explains this business profile response to API users.
    description: Optional[str] = None
    # Domain name connected to the business website or activation workflow.
    domain: Optional[str] = None
    # Employer Identification Number used for business and 10DLC verification.
    ein: Optional[str] = None
    # Uploaded EIN document reference used for business verification.
    ein_document: Optional[BusinessResponse_einDocument] = None
    # Indicates whether this business profile response is active and available in the Leadping API.
    enabled: Optional[bool] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # The display name for the entity.
    name: Optional[str] = None
    # Phone details for the lead, user, or business represented by this business profile response.
    phone: Optional[str] = None
    # Phone numbers assigned to this business.
    phones: Optional[list[IdNameValue]] = None
    # Alternate business name or DBA shown in Leadping.
    secondary_name: Optional[str] = None
    # Defines the supported User Setup Status values.
    setup_status: Optional[BusinessResponse_setupStatus] = None
    # Defines the supported Business Setup Step values.
    setup_step: Optional[BusinessResponse_setupStep] = None
    # Leadping website record connected to this business.
    site: Optional[BusinessResponse_site] = None
    # Defines the supported Business Status values.
    status: Optional[BusinessResponse_status] = None
    # Defines the supported Subscription Status values.
    subscription_status: Optional[BusinessResponse_subscriptionStatus] = None
    # User summary connected to this business profile response.
    user: Optional[BusinessResponse_user] = None
    # Industry vertical used for lead routing, compliance review, and reporting.
    vertical: Optional[str] = None
    # Business website URL used for compliance, brand review, and lead attribution.
    website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .business_response_activation import BusinessResponse_activation
        from .business_response_address import BusinessResponse_address
        from .business_response_billing_address import BusinessResponse_billingAddress
        from .business_response_billing_plan import BusinessResponse_billingPlan
        from .business_response_billing_state import BusinessResponse_billingState
        from .business_response_compliance_policy import BusinessResponse_compliancePolicy
        from .business_response_ein_document import BusinessResponse_einDocument
        from .business_response_setup_status import BusinessResponse_setupStatus
        from .business_response_setup_step import BusinessResponse_setupStep
        from .business_response_site import BusinessResponse_site
        from .business_response_status import BusinessResponse_status
        from .business_response_subscription_status import BusinessResponse_subscriptionStatus
        from .business_response_user import BusinessResponse_user
        from .id_name_value import IdNameValue

        from .business_response_activation import BusinessResponse_activation
        from .business_response_address import BusinessResponse_address
        from .business_response_billing_address import BusinessResponse_billingAddress
        from .business_response_billing_plan import BusinessResponse_billingPlan
        from .business_response_billing_state import BusinessResponse_billingState
        from .business_response_compliance_policy import BusinessResponse_compliancePolicy
        from .business_response_ein_document import BusinessResponse_einDocument
        from .business_response_setup_status import BusinessResponse_setupStatus
        from .business_response_setup_step import BusinessResponse_setupStep
        from .business_response_site import BusinessResponse_site
        from .business_response_status import BusinessResponse_status
        from .business_response_subscription_status import BusinessResponse_subscriptionStatus
        from .business_response_user import BusinessResponse_user
        from .id_name_value import IdNameValue

        fields: dict[str, Callable[[Any], None]] = {
            "accountBalance": lambda n : setattr(self, 'account_balance', n.get_float_value()),
            "activation": lambda n : setattr(self, 'activation', n.get_object_value(BusinessResponse_activation)),
            "address": lambda n : setattr(self, 'address', n.get_object_value(BusinessResponse_address)),
            "autoRefillEnabled": lambda n : setattr(self, 'auto_refill_enabled', n.get_bool_value()),
            "billingAddress": lambda n : setattr(self, 'billing_address', n.get_object_value(BusinessResponse_billingAddress)),
            "billingName": lambda n : setattr(self, 'billing_name', n.get_str_value()),
            "billingPlan": lambda n : setattr(self, 'billing_plan', n.get_enum_value(BusinessResponse_billingPlan)),
            "billingState": lambda n : setattr(self, 'billing_state', n.get_object_value(BusinessResponse_billingState)),
            "compliancePolicy": lambda n : setattr(self, 'compliance_policy', n.get_object_value(BusinessResponse_compliancePolicy)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "ein": lambda n : setattr(self, 'ein', n.get_str_value()),
            "einDocument": lambda n : setattr(self, 'ein_document', n.get_object_value(BusinessResponse_einDocument)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(IdNameValue)),
            "secondaryName": lambda n : setattr(self, 'secondary_name', n.get_str_value()),
            "setupStatus": lambda n : setattr(self, 'setup_status', n.get_enum_value(BusinessResponse_setupStatus)),
            "setupStep": lambda n : setattr(self, 'setup_step', n.get_enum_value(BusinessResponse_setupStep)),
            "site": lambda n : setattr(self, 'site', n.get_object_value(BusinessResponse_site)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(BusinessResponse_status)),
            "subscriptionStatus": lambda n : setattr(self, 'subscription_status', n.get_enum_value(BusinessResponse_subscriptionStatus)),
            "user": lambda n : setattr(self, 'user', n.get_object_value(BusinessResponse_user)),
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
        writer.write_float_value("accountBalance", self.account_balance)
        writer.write_object_value("activation", self.activation)
        writer.write_object_value("address", self.address)
        writer.write_bool_value("autoRefillEnabled", self.auto_refill_enabled)
        writer.write_object_value("billingAddress", self.billing_address)
        writer.write_str_value("billingName", self.billing_name)
        writer.write_enum_value("billingPlan", self.billing_plan)
        writer.write_object_value("billingState", self.billing_state)
        writer.write_object_value("compliancePolicy", self.compliance_policy)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("description", self.description)
        writer.write_str_value("domain", self.domain)
        writer.write_str_value("ein", self.ein)
        writer.write_object_value("einDocument", self.ein_document)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_str_value("phone", self.phone)
        writer.write_collection_of_object_values("phones", self.phones)
        writer.write_str_value("secondaryName", self.secondary_name)
        writer.write_enum_value("setupStatus", self.setup_status)
        writer.write_enum_value("setupStep", self.setup_step)
        writer.write_object_value("site", self.site)
        writer.write_enum_value("status", self.status)
        writer.write_enum_value("subscriptionStatus", self.subscription_status)
        writer.write_object_value("user", self.user)
        writer.write_str_value("vertical", self.vertical)
        writer.write_str_value("website", self.website)
        writer.write_additional_data_value(self.additional_data)
    

