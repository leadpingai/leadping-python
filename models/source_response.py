from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .source_response_admin_enablement_override import SourceResponse_adminEnablementOverride
    from .source_response_business import SourceResponse_business
    from .source_response_created_by_user import SourceResponse_createdByUser
    from .source_response_modified_by_user import SourceResponse_modifiedByUser
    from .source_response_user import SourceResponse_user
    from .tag_summary import TagSummary

@dataclass
class SourceResponse(AdditionalDataHolder, Parsable):
    """
    Response schema for the Leadping API lead source response returned to authenticated clients.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Admin override that can enable or disable this record independently of normal status checks.
    admin_enablement_override: Optional[SourceResponse_adminEnablementOverride] = None
    # Product allowlist used to accept or route leads from this source.
    allowed_products: Optional[list[str]] = None
    # State or region allowlist used to accept leads from this source.
    allowed_states: Optional[list[str]] = None
    # UTC timestamp when Leadping issued the source API key.
    api_key_issued_at: Optional[datetime.datetime] = None
    # Masked preview of the source API key for display without exposing the secret.
    api_key_preview: Optional[str] = None
    # Business summary connected to this lead source response.
    business: Optional[SourceResponse_business] = None
    # Indicates whether the business or sender passed compliance review.
    compliance_approved: Optional[bool] = None
    # Compliance notes captured for admin review.
    compliance_notes: Optional[str] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # User summary for the person who created this lead source response.
    created_by_user: Optional[SourceResponse_createdByUser] = None
    # Tag IDs automatically assigned to leads created by this source.
    default_tag_ids: Optional[list[str]] = None
    # Default tag summaries automatically applied to leads from this source.
    default_tags: Optional[list[TagSummary]] = None
    # Human-readable description that explains this lead source response to API users.
    description: Optional[str] = None
    # Indicates whether this lead source response is active and available in the Leadping API.
    enabled: Optional[bool] = None
    # UTC timestamp when this source first delivered a lead to Leadping.
    first_lead_received_at: Optional[datetime.datetime] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # UTC timestamp when this source most recently delivered a lead to Leadping.
    last_lead_received_at: Optional[datetime.datetime] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # User summary for the person who last modified this lead source response.
    modified_by_user: Optional[SourceResponse_modifiedByUser] = None
    # The display name for the entity.
    name: Optional[str] = None
    # Indicates whether leads from this source must include a TrustedForm certificate for consent proof.
    requires_trusted_form: Optional[bool] = None
    # User summary connected to this lead source response.
    user: Optional[SourceResponse_user] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SourceResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SourceResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SourceResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .source_response_admin_enablement_override import SourceResponse_adminEnablementOverride
        from .source_response_business import SourceResponse_business
        from .source_response_created_by_user import SourceResponse_createdByUser
        from .source_response_modified_by_user import SourceResponse_modifiedByUser
        from .source_response_user import SourceResponse_user
        from .tag_summary import TagSummary

        from .source_response_admin_enablement_override import SourceResponse_adminEnablementOverride
        from .source_response_business import SourceResponse_business
        from .source_response_created_by_user import SourceResponse_createdByUser
        from .source_response_modified_by_user import SourceResponse_modifiedByUser
        from .source_response_user import SourceResponse_user
        from .tag_summary import TagSummary

        fields: dict[str, Callable[[Any], None]] = {
            "adminEnablementOverride": lambda n : setattr(self, 'admin_enablement_override', n.get_object_value(SourceResponse_adminEnablementOverride)),
            "allowedProducts": lambda n : setattr(self, 'allowed_products', n.get_collection_of_primitive_values(str)),
            "allowedStates": lambda n : setattr(self, 'allowed_states', n.get_collection_of_primitive_values(str)),
            "apiKeyIssuedAt": lambda n : setattr(self, 'api_key_issued_at', n.get_datetime_value()),
            "apiKeyPreview": lambda n : setattr(self, 'api_key_preview', n.get_str_value()),
            "business": lambda n : setattr(self, 'business', n.get_object_value(SourceResponse_business)),
            "complianceApproved": lambda n : setattr(self, 'compliance_approved', n.get_bool_value()),
            "complianceNotes": lambda n : setattr(self, 'compliance_notes', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "createdByUser": lambda n : setattr(self, 'created_by_user', n.get_object_value(SourceResponse_createdByUser)),
            "defaultTagIds": lambda n : setattr(self, 'default_tag_ids', n.get_collection_of_primitive_values(str)),
            "defaultTags": lambda n : setattr(self, 'default_tags', n.get_collection_of_object_values(TagSummary)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "firstLeadReceivedAt": lambda n : setattr(self, 'first_lead_received_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lastLeadReceivedAt": lambda n : setattr(self, 'last_lead_received_at', n.get_datetime_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "modifiedByUser": lambda n : setattr(self, 'modified_by_user', n.get_object_value(SourceResponse_modifiedByUser)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "requiresTrustedForm": lambda n : setattr(self, 'requires_trusted_form', n.get_bool_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(SourceResponse_user)),
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
        writer.write_datetime_value("apiKeyIssuedAt", self.api_key_issued_at)
        writer.write_str_value("apiKeyPreview", self.api_key_preview)
        writer.write_object_value("business", self.business)
        writer.write_bool_value("complianceApproved", self.compliance_approved)
        writer.write_str_value("complianceNotes", self.compliance_notes)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_object_value("createdByUser", self.created_by_user)
        writer.write_collection_of_primitive_values("defaultTagIds", self.default_tag_ids)
        writer.write_collection_of_object_values("defaultTags", self.default_tags)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_datetime_value("firstLeadReceivedAt", self.first_lead_received_at)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("lastLeadReceivedAt", self.last_lead_received_at)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_object_value("modifiedByUser", self.modified_by_user)
        writer.write_str_value("name", self.name)
        writer.write_bool_value("requiresTrustedForm", self.requires_trusted_form)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    

