from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .id_name_value import IdNameValue
    from .organization_response_activation import OrganizationResponse_activation
    from .organization_response_address import OrganizationResponse_address
    from .organization_response_billing_address import OrganizationResponse_billingAddress
    from .organization_response_billing_plan import OrganizationResponse_billingPlan
    from .organization_response_billing_state import OrganizationResponse_billingState
    from .organization_response_compliance_policy import OrganizationResponse_compliancePolicy
    from .organization_response_ein_document import OrganizationResponse_einDocument
    from .organization_response_setup_status import OrganizationResponse_setupStatus
    from .organization_response_setup_step import OrganizationResponse_setupStep
    from .organization_response_site import OrganizationResponse_site
    from .organization_response_status import OrganizationResponse_status
    from .organization_response_subscription_status import OrganizationResponse_subscriptionStatus
    from .organization_response_user import OrganizationResponse_user

@dataclass
class OrganizationResponse(AdditionalDataHolder, Parsable):
    """
    Describes organization profile data returned by Leadping.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Organization activation state covering site, billing, compliance, and telephony readiness.
    activation: Optional[OrganizationResponse_activation] = None
    # Postal address for the organization, lead, or contact represented by this organization profile response.
    address: Optional[OrganizationResponse_address] = None
    # Indicates whether automatic wallet refill is enabled for the organization.
    auto_refill_enabled: Optional[bool] = None
    # Postal address used for invoices, receipts, and payment processor billing records.
    billing_address: Optional[OrganizationResponse_billingAddress] = None
    # Name used for invoices, receipts, and payment processor billing records.
    billing_name: Optional[str] = None
    # Defines the supported Billing Plan values.
    billing_plan: Optional[OrganizationResponse_billingPlan] = None
    # Customer-safe billing state for this organization.
    billing_state: Optional[OrganizationResponse_billingState] = None
    # Tax identifier printed on billing documents. This may differ from the organization verification EIN.
    billing_tax_id: Optional[str] = None
    # Compliance policy configuration for the organization.
    compliance_policy: Optional[OrganizationResponse_compliancePolicy] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # Human-readable description that explains this organization profile response to API users.
    description: Optional[str] = None
    # Domain name connected to the organization website or activation workflow.
    domain: Optional[str] = None
    # Employer Identification Number used for organization and 10DLC verification.
    ein: Optional[str] = None
    # Uploaded EIN document reference used for organization verification.
    ein_document: Optional[OrganizationResponse_einDocument] = None
    # Indicates whether this organization profile response is active and available in the Leadping API.
    enabled: Optional[bool] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # The display name for the entity.
    name: Optional[str] = None
    # Phone details for the lead, user, or organization represented by this organization profile response.
    phone: Optional[str] = None
    # Phone numbers assigned to this organization.
    phones: Optional[list[IdNameValue]] = None
    # Alternate organization name or DBA shown in Leadping.
    secondary_name: Optional[str] = None
    # Defines the supported User Setup Status values.
    setup_status: Optional[OrganizationResponse_setupStatus] = None
    # Defines the supported Organization Setup Step values.
    setup_step: Optional[OrganizationResponse_setupStep] = None
    # Leadping website record connected to this organization.
    site: Optional[OrganizationResponse_site] = None
    # Defines the supported Organization Status values.
    status: Optional[OrganizationResponse_status] = None
    # Defines the supported Subscription Status values.
    subscription_status: Optional[OrganizationResponse_subscriptionStatus] = None
    # User summary connected to this organization profile response.
    user: Optional[OrganizationResponse_user] = None
    # Industry vertical used for lead routing, compliance review, and reporting.
    vertical: Optional[str] = None
    # Organization website URL used for compliance, brand review, and lead attribution.
    website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .id_name_value import IdNameValue
        from .organization_response_activation import OrganizationResponse_activation
        from .organization_response_address import OrganizationResponse_address
        from .organization_response_billing_address import OrganizationResponse_billingAddress
        from .organization_response_billing_plan import OrganizationResponse_billingPlan
        from .organization_response_billing_state import OrganizationResponse_billingState
        from .organization_response_compliance_policy import OrganizationResponse_compliancePolicy
        from .organization_response_ein_document import OrganizationResponse_einDocument
        from .organization_response_setup_status import OrganizationResponse_setupStatus
        from .organization_response_setup_step import OrganizationResponse_setupStep
        from .organization_response_site import OrganizationResponse_site
        from .organization_response_status import OrganizationResponse_status
        from .organization_response_subscription_status import OrganizationResponse_subscriptionStatus
        from .organization_response_user import OrganizationResponse_user

        from .id_name_value import IdNameValue
        from .organization_response_activation import OrganizationResponse_activation
        from .organization_response_address import OrganizationResponse_address
        from .organization_response_billing_address import OrganizationResponse_billingAddress
        from .organization_response_billing_plan import OrganizationResponse_billingPlan
        from .organization_response_billing_state import OrganizationResponse_billingState
        from .organization_response_compliance_policy import OrganizationResponse_compliancePolicy
        from .organization_response_ein_document import OrganizationResponse_einDocument
        from .organization_response_setup_status import OrganizationResponse_setupStatus
        from .organization_response_setup_step import OrganizationResponse_setupStep
        from .organization_response_site import OrganizationResponse_site
        from .organization_response_status import OrganizationResponse_status
        from .organization_response_subscription_status import OrganizationResponse_subscriptionStatus
        from .organization_response_user import OrganizationResponse_user

        fields: dict[str, Callable[[Any], None]] = {
            "activation": lambda n : setattr(self, 'activation', n.get_object_value(OrganizationResponse_activation)),
            "address": lambda n : setattr(self, 'address', n.get_object_value(OrganizationResponse_address)),
            "autoRefillEnabled": lambda n : setattr(self, 'auto_refill_enabled', n.get_bool_value()),
            "billingAddress": lambda n : setattr(self, 'billing_address', n.get_object_value(OrganizationResponse_billingAddress)),
            "billingName": lambda n : setattr(self, 'billing_name', n.get_str_value()),
            "billingPlan": lambda n : setattr(self, 'billing_plan', n.get_enum_value(OrganizationResponse_billingPlan)),
            "billingState": lambda n : setattr(self, 'billing_state', n.get_object_value(OrganizationResponse_billingState)),
            "billingTaxId": lambda n : setattr(self, 'billing_tax_id', n.get_str_value()),
            "compliancePolicy": lambda n : setattr(self, 'compliance_policy', n.get_object_value(OrganizationResponse_compliancePolicy)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "ein": lambda n : setattr(self, 'ein', n.get_str_value()),
            "einDocument": lambda n : setattr(self, 'ein_document', n.get_object_value(OrganizationResponse_einDocument)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(IdNameValue)),
            "secondaryName": lambda n : setattr(self, 'secondary_name', n.get_str_value()),
            "setupStatus": lambda n : setattr(self, 'setup_status', n.get_enum_value(OrganizationResponse_setupStatus)),
            "setupStep": lambda n : setattr(self, 'setup_step', n.get_enum_value(OrganizationResponse_setupStep)),
            "site": lambda n : setattr(self, 'site', n.get_object_value(OrganizationResponse_site)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(OrganizationResponse_status)),
            "subscriptionStatus": lambda n : setattr(self, 'subscription_status', n.get_enum_value(OrganizationResponse_subscriptionStatus)),
            "user": lambda n : setattr(self, 'user', n.get_object_value(OrganizationResponse_user)),
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
        writer.write_bool_value("autoRefillEnabled", self.auto_refill_enabled)
        writer.write_object_value("billingAddress", self.billing_address)
        writer.write_str_value("billingName", self.billing_name)
        writer.write_enum_value("billingPlan", self.billing_plan)
        writer.write_object_value("billingState", self.billing_state)
        writer.write_str_value("billingTaxId", self.billing_tax_id)
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
    

