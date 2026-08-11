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
    Represents customer automation health data exposed by Leadping analytics.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Collection of failing automations included with this Leadping customer automation health.
    failing_automations: Optional[list[CustomerFailingAutomation]] = None
    # Last failure associated with this Leadping customer automation health.
    last_failure: Optional[CustomerAutomationHealth_lastFailure] = None
    
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
            "failingAutomations": lambda n : setattr(self, 'failing_automations', n.get_collection_of_object_values(CustomerFailingAutomation)),
            "lastFailure": lambda n : setattr(self, 'last_failure', n.get_object_value(CustomerAutomationHealth_lastFailure)),
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
        writer.write_collection_of_object_values("failingAutomations", self.failing_automations)
        writer.write_object_value("lastFailure", self.last_failure)
        writer.write_additional_data_value(self.additional_data)
    

