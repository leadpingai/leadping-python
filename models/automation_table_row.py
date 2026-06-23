from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_table_row_admin_enablement_override import AutomationTableRow_adminEnablementOverride
    from .automation_table_row_business import AutomationTableRow_business
    from .automation_table_row_user import AutomationTableRow_user

@dataclass
class AutomationTableRow(AdditionalDataHolder, Parsable):
    """
    API DTO containing automation data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The action summary value for this automation.
    action_summary: Optional[str] = None
    # The admin force enablement override on this automation.
    admin_enablement_override: Optional[AutomationTableRow_adminEnablementOverride] = None
    # The business value for this automation.
    business: Optional[AutomationTableRow_business] = None
    # The business ID associated with this automation.
    business_id: Optional[str] = None
    # The condition summary value for this automation.
    condition_summary: Optional[str] = None
    # The created by user ID associated with this automation.
    created_by_user_id: Optional[str] = None
    # The human-readable description of this automation.
    description: Optional[str] = None
    # Whether this automation is enabled.
    enabled: Optional[bool] = None
    # The health summary value for this automation.
    health_summary: Optional[str] = None
    # The unique ID for this automation.
    id: Optional[str] = None
    # Whether this automation is system managed.
    is_system_managed: Optional[bool] = None
    # The date and time for the last run at value on this automation.
    last_run_at: Optional[datetime.datetime] = None
    # The date and time for the last run error value on this automation.
    last_run_error: Optional[str] = None
    # The current last run status for this automation.
    last_run_status: Optional[str] = None
    # The management level value for this automation.
    management_level: Optional[str] = None
    # The date and time this automation was last modified.
    modified_at: Optional[datetime.datetime] = None
    # The human-readable name shown for this automation.
    name: Optional[str] = None
    # The rule sentence value for this automation.
    rule_sentence: Optional[str] = None
    # The scope value for this automation.
    scope: Optional[str] = None
    # The trigger summary value for this automation.
    trigger_summary: Optional[str] = None
    # The primary trigger type label for this automation.
    trigger_type: Optional[str] = None
    # The user value for this automation.
    user: Optional[AutomationTableRow_user] = None
    # The visibility value for this automation.
    visibility: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationTableRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationTableRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationTableRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automation_table_row_admin_enablement_override import AutomationTableRow_adminEnablementOverride
        from .automation_table_row_business import AutomationTableRow_business
        from .automation_table_row_user import AutomationTableRow_user

        from .automation_table_row_admin_enablement_override import AutomationTableRow_adminEnablementOverride
        from .automation_table_row_business import AutomationTableRow_business
        from .automation_table_row_user import AutomationTableRow_user

        fields: dict[str, Callable[[Any], None]] = {
            "actionSummary": lambda n : setattr(self, 'action_summary', n.get_str_value()),
            "adminEnablementOverride": lambda n : setattr(self, 'admin_enablement_override', n.get_object_value(AutomationTableRow_adminEnablementOverride)),
            "business": lambda n : setattr(self, 'business', n.get_object_value(AutomationTableRow_business)),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "conditionSummary": lambda n : setattr(self, 'condition_summary', n.get_str_value()),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "healthSummary": lambda n : setattr(self, 'health_summary', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isSystemManaged": lambda n : setattr(self, 'is_system_managed', n.get_bool_value()),
            "lastRunAt": lambda n : setattr(self, 'last_run_at', n.get_datetime_value()),
            "lastRunError": lambda n : setattr(self, 'last_run_error', n.get_str_value()),
            "lastRunStatus": lambda n : setattr(self, 'last_run_status', n.get_str_value()),
            "managementLevel": lambda n : setattr(self, 'management_level', n.get_str_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "ruleSentence": lambda n : setattr(self, 'rule_sentence', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "triggerSummary": lambda n : setattr(self, 'trigger_summary', n.get_str_value()),
            "triggerType": lambda n : setattr(self, 'trigger_type', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(AutomationTableRow_user)),
            "visibility": lambda n : setattr(self, 'visibility', n.get_str_value()),
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
        writer.write_str_value("actionSummary", self.action_summary)
        writer.write_object_value("adminEnablementOverride", self.admin_enablement_override)
        writer.write_object_value("business", self.business)
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("conditionSummary", self.condition_summary)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("healthSummary", self.health_summary)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isSystemManaged", self.is_system_managed)
        writer.write_datetime_value("lastRunAt", self.last_run_at)
        writer.write_str_value("lastRunError", self.last_run_error)
        writer.write_str_value("lastRunStatus", self.last_run_status)
        writer.write_str_value("managementLevel", self.management_level)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_str_value("ruleSentence", self.rule_sentence)
        writer.write_str_value("scope", self.scope)
        writer.write_str_value("triggerSummary", self.trigger_summary)
        writer.write_str_value("triggerType", self.trigger_type)
        writer.write_object_value("user", self.user)
        writer.write_str_value("visibility", self.visibility)
        writer.write_additional_data_value(self.additional_data)
    

