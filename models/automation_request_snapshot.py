from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_action import AutomationAction
    from .automation_condition_group import AutomationConditionGroup
    from .automation_trigger import AutomationTrigger

@dataclass
class AutomationRequestSnapshot(AdditionalDataHolder, Parsable):
    """
    API DTO containing automation request snapshot data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The actions included with this automation request snapshot.
    actions: Optional[list[AutomationAction]] = None
    # The business ID associated with this automation request snapshot.
    business_id: Optional[str] = None
    # The condition groups included with this automation request snapshot.
    condition_groups: Optional[list[AutomationConditionGroup]] = None
    # The created by user ID associated with this automation request snapshot.
    created_by_user_id: Optional[str] = None
    # The human-readable description of this automation request snapshot.
    description: Optional[str] = None
    # Whether this automation request snapshot is enabled.
    enabled: Optional[bool] = None
    # The unique ID for this automation request snapshot.
    id: Optional[str] = None
    # Whether this automation request snapshot is system managed.
    is_system_managed: Optional[bool] = None
    # The management level value for this automation request snapshot.
    management_level: Optional[str] = None
    # The human-readable name shown for this automation request snapshot.
    name: Optional[str] = None
    # The scope value for this automation request snapshot.
    scope: Optional[str] = None
    # The triggers included with this automation request snapshot.
    triggers: Optional[list[AutomationTrigger]] = None
    # The visibility value for this automation request snapshot.
    visibility: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationRequestSnapshot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationRequestSnapshot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationRequestSnapshot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automation_action import AutomationAction
        from .automation_condition_group import AutomationConditionGroup
        from .automation_trigger import AutomationTrigger

        from .automation_action import AutomationAction
        from .automation_condition_group import AutomationConditionGroup
        from .automation_trigger import AutomationTrigger

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(AutomationAction)),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "conditionGroups": lambda n : setattr(self, 'condition_groups', n.get_collection_of_object_values(AutomationConditionGroup)),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isSystemManaged": lambda n : setattr(self, 'is_system_managed', n.get_bool_value()),
            "managementLevel": lambda n : setattr(self, 'management_level', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "triggers": lambda n : setattr(self, 'triggers', n.get_collection_of_object_values(AutomationTrigger)),
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
        writer.write_str_value("businessId", self.business_id)
        writer.write_collection_of_object_values("conditionGroups", self.condition_groups)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isSystemManaged", self.is_system_managed)
        writer.write_str_value("managementLevel", self.management_level)
        writer.write_str_value("name", self.name)
        writer.write_str_value("scope", self.scope)
        writer.write_collection_of_object_values("triggers", self.triggers)
        writer.write_str_value("visibility", self.visibility)
        writer.write_additional_data_value(self.additional_data)
    

