from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .customer_automation_health_last_failure import CustomerAutomationHealth_lastFailure
    from .customer_failing_automation import CustomerFailingAutomation

@dataclass
class CustomerAutomationHealth(AdditionalDataHolder, Parsable):
    """
    Automation health associated with this Leadping customer analytics.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Total number of automation records represented by this Leadping customer automation health.
    automation_count: Optional[int] = None
    # Total number of enabled records represented by this Leadping customer automation health.
    enabled_count: Optional[int] = None
    # Number of executions represented by this Leadping customer automation health.
    executions: Optional[int] = None
    # Collection of failing automations included with this Leadping customer automation health.
    failing_automations: Optional[list[CustomerFailingAutomation]] = None
    # Total number of failure records represented by this Leadping customer automation health.
    failure_count: Optional[int] = None
    # Last failure associated with this Leadping customer automation health.
    last_failure: Optional[CustomerAutomationHealth_lastFailure] = None
    # Total number of success records represented by this Leadping customer automation health.
    success_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerAutomationHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerAutomationHealth
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerAutomationHealth()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .customer_automation_health_last_failure import CustomerAutomationHealth_lastFailure
        from .customer_failing_automation import CustomerFailingAutomation

        from .customer_automation_health_last_failure import CustomerAutomationHealth_lastFailure
        from .customer_failing_automation import CustomerFailingAutomation

        fields: dict[str, Callable[[Any], None]] = {
            "automationCount": lambda n : setattr(self, 'automation_count', n.get_int_value()),
            "enabledCount": lambda n : setattr(self, 'enabled_count', n.get_int_value()),
            "executions": lambda n : setattr(self, 'executions', n.get_int_value()),
            "failingAutomations": lambda n : setattr(self, 'failing_automations', n.get_collection_of_object_values(CustomerFailingAutomation)),
            "failureCount": lambda n : setattr(self, 'failure_count', n.get_int_value()),
            "lastFailure": lambda n : setattr(self, 'last_failure', n.get_object_value(CustomerAutomationHealth_lastFailure)),
            "successCount": lambda n : setattr(self, 'success_count', n.get_int_value()),
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
        writer.write_int_value("automationCount", self.automation_count)
        writer.write_int_value("enabledCount", self.enabled_count)
        writer.write_int_value("executions", self.executions)
        writer.write_collection_of_object_values("failingAutomations", self.failing_automations)
        writer.write_int_value("failureCount", self.failure_count)
        writer.write_object_value("lastFailure", self.last_failure)
        writer.write_int_value("successCount", self.success_count)
        writer.write_additional_data_value(self.additional_data)
    

