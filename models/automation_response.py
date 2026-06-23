from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_action import AutomationAction
    from .automation_condition_group import AutomationConditionGroup
    from .automation_response_admin_enablement_override import AutomationResponse_adminEnablementOverride
    from .automation_response_business import AutomationResponse_business
    from .automation_response_user import AutomationResponse_user
    from .automation_run_record import AutomationRunRecord
    from .automation_trigger import AutomationTrigger

@dataclass
class AutomationResponse(AdditionalDataHolder, Parsable):
    """
    API response containing automation data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The actions included with this automation.
    actions: Optional[list[AutomationAction]] = None
    # The adminEnablementOverride property
    admin_enablement_override: Optional[AutomationResponse_adminEnablementOverride] = None
    # The business value for this automation.
    business: Optional[AutomationResponse_business] = None
    # The business ID associated with this automation.
    business_id: Optional[str] = None
    # The condition groups included with this automation.
    condition_groups: Optional[list[AutomationConditionGroup]] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # The created by user ID associated with this automation.
    created_by_user_id: Optional[str] = None
    # The human-readable description of this automation.
    description: Optional[str] = None
    # Whether this automation is enabled.
    enabled: Optional[bool] = None
    # The unique identifier for the entity.
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
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # The display name for the entity.
    name: Optional[str] = None
    # The recent runs included with this automation.
    recent_runs: Optional[list[AutomationRunRecord]] = None
    # The scope value for this automation.
    scope: Optional[str] = None
    # The triggers included with this automation.
    triggers: Optional[list[AutomationTrigger]] = None
    # The user value for this automation.
    user: Optional[AutomationResponse_user] = None
    # The version value for this automation.
    version: Optional[int] = None
    # The visibility value for this automation.
    visibility: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automation_action import AutomationAction
        from .automation_condition_group import AutomationConditionGroup
        from .automation_response_admin_enablement_override import AutomationResponse_adminEnablementOverride
        from .automation_response_business import AutomationResponse_business
        from .automation_response_user import AutomationResponse_user
        from .automation_run_record import AutomationRunRecord
        from .automation_trigger import AutomationTrigger

        from .automation_action import AutomationAction
        from .automation_condition_group import AutomationConditionGroup
        from .automation_response_admin_enablement_override import AutomationResponse_adminEnablementOverride
        from .automation_response_business import AutomationResponse_business
        from .automation_response_user import AutomationResponse_user
        from .automation_run_record import AutomationRunRecord
        from .automation_trigger import AutomationTrigger

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(AutomationAction)),
            "adminEnablementOverride": lambda n : setattr(self, 'admin_enablement_override', n.get_object_value(AutomationResponse_adminEnablementOverride)),
            "business": lambda n : setattr(self, 'business', n.get_object_value(AutomationResponse_business)),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "conditionGroups": lambda n : setattr(self, 'condition_groups', n.get_collection_of_object_values(AutomationConditionGroup)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isSystemManaged": lambda n : setattr(self, 'is_system_managed', n.get_bool_value()),
            "lastRunAt": lambda n : setattr(self, 'last_run_at', n.get_datetime_value()),
            "lastRunError": lambda n : setattr(self, 'last_run_error', n.get_str_value()),
            "lastRunStatus": lambda n : setattr(self, 'last_run_status', n.get_str_value()),
            "managementLevel": lambda n : setattr(self, 'management_level', n.get_str_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "recentRuns": lambda n : setattr(self, 'recent_runs', n.get_collection_of_object_values(AutomationRunRecord)),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "triggers": lambda n : setattr(self, 'triggers', n.get_collection_of_object_values(AutomationTrigger)),
            "user": lambda n : setattr(self, 'user', n.get_object_value(AutomationResponse_user)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_collection_of_object_values("actions", self.actions)
        writer.write_object_value("adminEnablementOverride", self.admin_enablement_override)
        writer.write_object_value("business", self.business)
        writer.write_str_value("businessId", self.business_id)
        writer.write_collection_of_object_values("conditionGroups", self.condition_groups)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isSystemManaged", self.is_system_managed)
        writer.write_datetime_value("lastRunAt", self.last_run_at)
        writer.write_str_value("lastRunError", self.last_run_error)
        writer.write_str_value("lastRunStatus", self.last_run_status)
        writer.write_str_value("managementLevel", self.management_level)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("recentRuns", self.recent_runs)
        writer.write_str_value("scope", self.scope)
        writer.write_collection_of_object_values("triggers", self.triggers)
        writer.write_object_value("user", self.user)
        writer.write_int_value("version", self.version)
        writer.write_str_value("visibility", self.visibility)
        writer.write_additional_data_value(self.additional_data)
    

