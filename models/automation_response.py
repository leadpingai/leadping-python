from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_action import AutomationAction
    from .automation_condition_group import AutomationConditionGroup
    from .automation_connection import AutomationConnection
    from .automation_response_organization import AutomationResponse_organization
    from .automation_response_user import AutomationResponse_user
    from .automation_run_record import AutomationRunRecord
    from .automation_trigger import AutomationTrigger

@dataclass
class AutomationResponse(AdditionalDataHolder, Parsable):
    """
    Describes automation configuration data returned by Leadping.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Automation actions configured or returned for this workflow.
    actions: Optional[list[AutomationAction]] = None
    # Grouped automation conditions used to decide whether this workflow should run.
    condition_groups: Optional[list[AutomationConditionGroup]] = None
    # Directed connections between nodes in this automation graph.
    connections: Optional[list[AutomationConnection]] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # User ID of the person who created this automation configuration response.
    created_by_user_id: Optional[str] = None
    # Human-readable description that explains this automation configuration response to API users.
    description: Optional[str] = None
    # Indicates whether this automation configuration response is active and available in the Leadping API.
    enabled: Optional[bool] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # Indicates whether Leadping manages this automation configuration response automatically instead of a user.
    is_system_managed: Optional[bool] = None
    # UTC timestamp when this automation last ran.
    last_run_at: Optional[datetime.datetime] = None
    # Status from the most recent automation run.
    last_run_status: Optional[str] = None
    # Management level that controls whether Leadping or the organization owns this automation setting.
    management_level: Optional[str] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # The display name for the entity.
    name: Optional[str] = None
    # Organization summary connected to this automation configuration response.
    organization: Optional[AutomationResponse_organization] = None
    # Organization ID that owns this automation.
    organization_id: Optional[str] = None
    # Recent automation runs returned for history and troubleshooting.
    recent_runs: Optional[list[AutomationRunRecord]] = None
    # Scope that limits where this automation configuration response applies in Leadping.
    scope: Optional[str] = None
    # Automation triggers that can start this workflow.
    triggers: Optional[list[AutomationTrigger]] = None
    # User summary connected to this automation configuration response.
    user: Optional[AutomationResponse_user] = None
    # Visibility level that controls who can see this automation configuration response.
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
        from .automation_connection import AutomationConnection
        from .automation_response_organization import AutomationResponse_organization
        from .automation_response_user import AutomationResponse_user
        from .automation_run_record import AutomationRunRecord
        from .automation_trigger import AutomationTrigger

        from .automation_action import AutomationAction
        from .automation_condition_group import AutomationConditionGroup
        from .automation_connection import AutomationConnection
        from .automation_response_organization import AutomationResponse_organization
        from .automation_response_user import AutomationResponse_user
        from .automation_run_record import AutomationRunRecord
        from .automation_trigger import AutomationTrigger

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(AutomationAction)),
            "conditionGroups": lambda n : setattr(self, 'condition_groups', n.get_collection_of_object_values(AutomationConditionGroup)),
            "connections": lambda n : setattr(self, 'connections', n.get_collection_of_object_values(AutomationConnection)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isSystemManaged": lambda n : setattr(self, 'is_system_managed', n.get_bool_value()),
            "lastRunAt": lambda n : setattr(self, 'last_run_at', n.get_datetime_value()),
            "lastRunStatus": lambda n : setattr(self, 'last_run_status', n.get_str_value()),
            "managementLevel": lambda n : setattr(self, 'management_level', n.get_str_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_object_value(AutomationResponse_organization)),
            "organizationId": lambda n : setattr(self, 'organization_id', n.get_str_value()),
            "recentRuns": lambda n : setattr(self, 'recent_runs', n.get_collection_of_object_values(AutomationRunRecord)),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "triggers": lambda n : setattr(self, 'triggers', n.get_collection_of_object_values(AutomationTrigger)),
            "user": lambda n : setattr(self, 'user', n.get_object_value(AutomationResponse_user)),
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
        writer.write_collection_of_object_values("conditionGroups", self.condition_groups)
        writer.write_collection_of_object_values("connections", self.connections)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isSystemManaged", self.is_system_managed)
        writer.write_datetime_value("lastRunAt", self.last_run_at)
        writer.write_str_value("lastRunStatus", self.last_run_status)
        writer.write_str_value("managementLevel", self.management_level)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_object_value("organization", self.organization)
        writer.write_str_value("organizationId", self.organization_id)
        writer.write_collection_of_object_values("recentRuns", self.recent_runs)
        writer.write_str_value("scope", self.scope)
        writer.write_collection_of_object_values("triggers", self.triggers)
        writer.write_object_value("user", self.user)
        writer.write_str_value("visibility", self.visibility)
        writer.write_additional_data_value(self.additional_data)
    

