from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_request_address import BusinessRequest_address
    from .business_request_billing_address import BusinessRequest_billingAddress
    from .business_request_compliance_policy import BusinessRequest_compliancePolicy
    from .business_request_ein_document import BusinessRequest_einDocument
    from .business_request_status import BusinessRequest_status
    from .id_name_value import IdNameValue

@dataclass
class BusinessRequest(AdditionalDataHolder, Parsable):
    """
    Request schema for the Leadping API business profile request, including the fields clients can send.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Postal address for the business, lead, or contact represented by this business profile request.
    address: Optional[BusinessRequest_address] = None
    # Indicates whether automatic wallet refill is enabled for the business.
    auto_refill_enabled: Optional[bool] = None
    # Postal address used for invoices, receipts, and payment processor billing records.
    billing_address: Optional[BusinessRequest_billingAddress] = None
    # Name used for invoices, receipts, and payment processor billing records.
    billing_name: Optional[str] = None
    # Compliance policy configuration for the business.
    compliance_policy: Optional[BusinessRequest_compliancePolicy] = None
    # Human-readable description that explains this business profile request to API users.
    description: Optional[str] = None
    # Employer Identification Number used for business and 10DLC verification.
    ein: Optional[str] = None
    # Uploaded EIN document reference used for business verification.
    ein_document: Optional[BusinessRequest_einDocument] = None
    # Indicates whether this business profile request is active and available in the Leadping API.
    enabled: Optional[bool] = None
    # The unique identifier for the entity, when updating an existing entity.
    id: Optional[str] = None
    # Indicates whether the business serves customers younger than 90, for compliance and underwriting context.
    is_younger_than90: Optional[bool] = None
    # The display name for the entity.
    name: Optional[str] = None
    # Phone details for the lead, user, or business represented by this business profile request.
    phone: Optional[str] = None
    # Phone numbers assigned to this business.
    phones: Optional[list[IdNameValue]] = None
    # Alternate business name or DBA shown in Leadping.
    secondary_name: Optional[str] = None
    # Defines the supported Business Status values.
    status: Optional[BusinessRequest_status] = None
    # Industry vertical used for lead routing, compliance review, and reporting.
    vertical: Optional[str] = None
    # Business website URL used for compliance, brand review, and lead attribution.
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
        from .business_request_address import BusinessRequest_address
        from .business_request_billing_address import BusinessRequest_billingAddress
        from .business_request_compliance_policy import BusinessRequest_compliancePolicy
        from .business_request_ein_document import BusinessRequest_einDocument
        from .business_request_status import BusinessRequest_status
        from .id_name_value import IdNameValue

        from .business_request_address import BusinessRequest_address
        from .business_request_billing_address import BusinessRequest_billingAddress
        from .business_request_compliance_policy import BusinessRequest_compliancePolicy
        from .business_request_ein_document import BusinessRequest_einDocument
        from .business_request_status import BusinessRequest_status
        from .id_name_value import IdNameValue

        fields: dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(BusinessRequest_address)),
            "autoRefillEnabled": lambda n : setattr(self, 'auto_refill_enabled', n.get_bool_value()),
            "billingAddress": lambda n : setattr(self, 'billing_address', n.get_object_value(BusinessRequest_billingAddress)),
            "billingName": lambda n : setattr(self, 'billing_name', n.get_str_value()),
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
            "status": lambda n : setattr(self, 'status', n.get_enum_value(BusinessRequest_status)),
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
        writer.write_object_value("address", self.address)
        writer.write_bool_value("autoRefillEnabled", self.auto_refill_enabled)
        writer.write_object_value("billingAddress", self.billing_address)
        writer.write_str_value("billingName", self.billing_name)
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
        writer.write_enum_value("status", self.status)
        writer.write_str_value("vertical", self.vertical)
        writer.write_str_value("website", self.website)
        writer.write_additional_data_value(self.additional_data)
    

