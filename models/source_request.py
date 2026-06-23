from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .source_request_admin_enablement_override import SourceRequest_adminEnablementOverride

@dataclass
class SourceRequest(AdditionalDataHolder, Parsable):
    """
    Request payload for source.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The adminEnablementOverride property
    admin_enablement_override: Optional[SourceRequest_adminEnablementOverride] = None
    # The allowed products included with this source.
    allowed_products: Optional[list[str]] = None
    # The allowed states included with this source.
    allowed_states: Optional[list[str]] = None
    # The business ID associated with this source.
    business_id: Optional[str] = None
    # Whether this source is compliance approved.
    compliance_approved: Optional[bool] = None
    # The compliance notes value for this source.
    compliance_notes: Optional[str] = None
    # Tag ids applied automatically to leads created from this source.
    default_tag_ids: Optional[list[str]] = None
    # Tag names applied automatically to leads created from this source, creating missing tags when allowed by the caller.
    default_tag_names: Optional[list[str]] = None
    # The human-readable description of this source.
    description: Optional[str] = None
    # Whether this source is enabled.
    enabled: Optional[bool] = None
    # The unique identifier for the entity, when updating an existing entity.
    id: Optional[str] = None
    # The display name for the entity.
    name: Optional[str] = None
    # Whether regenerate API key applies to this source.
    regenerate_api_key: Optional[bool] = None
    # Whether this source requires TrustedForm.
    requires_trusted_form: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SourceRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SourceRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SourceRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .source_request_admin_enablement_override import SourceRequest_adminEnablementOverride

        from .source_request_admin_enablement_override import SourceRequest_adminEnablementOverride

        fields: dict[str, Callable[[Any], None]] = {
            "adminEnablementOverride": lambda n : setattr(self, 'admin_enablement_override', n.get_object_value(SourceRequest_adminEnablementOverride)),
            "allowedProducts": lambda n : setattr(self, 'allowed_products', n.get_collection_of_primitive_values(str)),
            "allowedStates": lambda n : setattr(self, 'allowed_states', n.get_collection_of_primitive_values(str)),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "complianceApproved": lambda n : setattr(self, 'compliance_approved', n.get_bool_value()),
            "complianceNotes": lambda n : setattr(self, 'compliance_notes', n.get_str_value()),
            "defaultTagIds": lambda n : setattr(self, 'default_tag_ids', n.get_collection_of_primitive_values(str)),
            "defaultTagNames": lambda n : setattr(self, 'default_tag_names', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "regenerateApiKey": lambda n : setattr(self, 'regenerate_api_key', n.get_bool_value()),
            "requiresTrustedForm": lambda n : setattr(self, 'requires_trusted_form', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("allowedProducts", self.allowed_products)
        writer.write_collection_of_primitive_values("allowedStates", self.allowed_states)
        writer.write_str_value("businessId", self.business_id)
        writer.write_bool_value("complianceApproved", self.compliance_approved)
        writer.write_str_value("complianceNotes", self.compliance_notes)
        writer.write_collection_of_primitive_values("defaultTagIds", self.default_tag_ids)
        writer.write_collection_of_primitive_values("defaultTagNames", self.default_tag_names)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_bool_value("regenerateApiKey", self.regenerate_api_key)
        writer.write_bool_value("requiresTrustedForm", self.requires_trusted_form)
        writer.write_additional_data_value(self.additional_data)
    

