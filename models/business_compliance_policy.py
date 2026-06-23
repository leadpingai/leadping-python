from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BusinessCompliancePolicy(AdditionalDataHolder, Parsable):
    """
    API DTO containing business compliance policy data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The allowed products included with this business compliance policy.
    allowed_products: Optional[list[str]] = None
    # The allowed states included with this business compliance policy.
    allowed_states: Optional[list[str]] = None
    # Whether this business compliance policy is enabled.
    enabled: Optional[bool] = None
    # Whether this business compliance policy requires agent license state.
    require_agent_license_state: Optional[bool] = None
    # Whether this business compliance policy requires lead state.
    require_lead_state: Optional[bool] = None
    # Whether this business compliance policy requires product.
    require_product: Optional[bool] = None
    # Whether this business compliance policy requires source compliance approval.
    require_source_compliance_approval: Optional[bool] = None
    # Whether this business compliance policy requires TrustedForm for automations.
    require_trusted_form_for_automations: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessCompliancePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessCompliancePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowedProducts": lambda n : setattr(self, 'allowed_products', n.get_collection_of_primitive_values(str)),
            "allowedStates": lambda n : setattr(self, 'allowed_states', n.get_collection_of_primitive_values(str)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "requireAgentLicenseState": lambda n : setattr(self, 'require_agent_license_state', n.get_bool_value()),
            "requireLeadState": lambda n : setattr(self, 'require_lead_state', n.get_bool_value()),
            "requireProduct": lambda n : setattr(self, 'require_product', n.get_bool_value()),
            "requireSourceComplianceApproval": lambda n : setattr(self, 'require_source_compliance_approval', n.get_bool_value()),
            "requireTrustedFormForAutomations": lambda n : setattr(self, 'require_trusted_form_for_automations', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("allowedProducts", self.allowed_products)
        writer.write_collection_of_primitive_values("allowedStates", self.allowed_states)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_bool_value("requireAgentLicenseState", self.require_agent_license_state)
        writer.write_bool_value("requireLeadState", self.require_lead_state)
        writer.write_bool_value("requireProduct", self.require_product)
        writer.write_bool_value("requireSourceComplianceApproval", self.require_source_compliance_approval)
        writer.write_bool_value("requireTrustedFormForAutomations", self.require_trusted_form_for_automations)
        writer.write_additional_data_value(self.additional_data)
    

