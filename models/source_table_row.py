from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .source_table_row_admin_enablement_override import SourceTableRow_adminEnablementOverride
    from .source_table_row_business import SourceTableRow_business
    from .source_table_row_created_by_user import SourceTableRow_createdByUser
    from .source_table_row_modified_by_user import SourceTableRow_modifiedByUser
    from .source_table_row_user import SourceTableRow_user
    from .tag_summary import TagSummary

@dataclass
class SourceTableRow(AdditionalDataHolder, Parsable):
    """
    API DTO containing source data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The admin force enablement override on this source.
    admin_enablement_override: Optional[SourceTableRow_adminEnablementOverride] = None
    # The allowed products included with this source.
    allowed_products: Optional[list[str]] = None
    # The allowed states included with this source.
    allowed_states: Optional[list[str]] = None
    # The date and time when the API key was issued.
    api_key_issued_at: Optional[datetime.datetime] = None
    # The date and time this source API key was last used.
    api_key_last_used_at: Optional[datetime.datetime] = None
    # The API key preview value for this source.
    api_key_preview: Optional[str] = None
    # The total number of tracked uses for this source API key.
    api_key_total_uses: Optional[int] = None
    # The business value for this source.
    business: Optional[SourceTableRow_business] = None
    # The business ID associated with this source.
    business_id: Optional[str] = None
    # Whether this source is compliance approved.
    compliance_approved: Optional[bool] = None
    # The date and time for the created at value on this source.
    created_at: Optional[datetime.datetime] = None
    # The user that created this source.
    created_by_user: Optional[SourceTableRow_createdByUser] = None
    # Tag ids applied automatically to leads created from this source.
    default_tag_ids: Optional[list[str]] = None
    # Tags applied automatically to leads created from this source.
    default_tags: Optional[list[TagSummary]] = None
    # The human-readable description of this source.
    description: Optional[str] = None
    # Whether this source is enabled.
    enabled: Optional[bool] = None
    # The date and time when this source first accepted a lead.
    first_lead_received_at: Optional[datetime.datetime] = None
    # The unique ID for this source.
    id: Optional[str] = None
    # The date and time when this source most recently accepted a lead.
    last_lead_received_at: Optional[datetime.datetime] = None
    # The date and time for the modified at value on this source.
    modified_at: Optional[datetime.datetime] = None
    # The user that most recently modified this source.
    modified_by_user: Optional[SourceTableRow_modifiedByUser] = None
    # The human-readable name shown for this source.
    name: Optional[str] = None
    # Whether this source requires TrustedForm.
    requires_trusted_form: Optional[bool] = None
    # The user value for this source.
    user: Optional[SourceTableRow_user] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SourceTableRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SourceTableRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SourceTableRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .source_table_row_admin_enablement_override import SourceTableRow_adminEnablementOverride
        from .source_table_row_business import SourceTableRow_business
        from .source_table_row_created_by_user import SourceTableRow_createdByUser
        from .source_table_row_modified_by_user import SourceTableRow_modifiedByUser
        from .source_table_row_user import SourceTableRow_user
        from .tag_summary import TagSummary

        from .source_table_row_admin_enablement_override import SourceTableRow_adminEnablementOverride
        from .source_table_row_business import SourceTableRow_business
        from .source_table_row_created_by_user import SourceTableRow_createdByUser
        from .source_table_row_modified_by_user import SourceTableRow_modifiedByUser
        from .source_table_row_user import SourceTableRow_user
        from .tag_summary import TagSummary

        fields: dict[str, Callable[[Any], None]] = {
            "adminEnablementOverride": lambda n : setattr(self, 'admin_enablement_override', n.get_object_value(SourceTableRow_adminEnablementOverride)),
            "allowedProducts": lambda n : setattr(self, 'allowed_products', n.get_collection_of_primitive_values(str)),
            "allowedStates": lambda n : setattr(self, 'allowed_states', n.get_collection_of_primitive_values(str)),
            "apiKeyIssuedAt": lambda n : setattr(self, 'api_key_issued_at', n.get_datetime_value()),
            "apiKeyLastUsedAt": lambda n : setattr(self, 'api_key_last_used_at', n.get_datetime_value()),
            "apiKeyPreview": lambda n : setattr(self, 'api_key_preview', n.get_str_value()),
            "apiKeyTotalUses": lambda n : setattr(self, 'api_key_total_uses', n.get_int_value()),
            "business": lambda n : setattr(self, 'business', n.get_object_value(SourceTableRow_business)),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "complianceApproved": lambda n : setattr(self, 'compliance_approved', n.get_bool_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "createdByUser": lambda n : setattr(self, 'created_by_user', n.get_object_value(SourceTableRow_createdByUser)),
            "defaultTagIds": lambda n : setattr(self, 'default_tag_ids', n.get_collection_of_primitive_values(str)),
            "defaultTags": lambda n : setattr(self, 'default_tags', n.get_collection_of_object_values(TagSummary)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "firstLeadReceivedAt": lambda n : setattr(self, 'first_lead_received_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lastLeadReceivedAt": lambda n : setattr(self, 'last_lead_received_at', n.get_datetime_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "modifiedByUser": lambda n : setattr(self, 'modified_by_user', n.get_object_value(SourceTableRow_modifiedByUser)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "requiresTrustedForm": lambda n : setattr(self, 'requires_trusted_form', n.get_bool_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(SourceTableRow_user)),
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
        writer.write_datetime_value("apiKeyLastUsedAt", self.api_key_last_used_at)
        writer.write_str_value("apiKeyPreview", self.api_key_preview)
        writer.write_int_value("apiKeyTotalUses", self.api_key_total_uses)
        writer.write_object_value("business", self.business)
        writer.write_str_value("businessId", self.business_id)
        writer.write_bool_value("complianceApproved", self.compliance_approved)
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
    

