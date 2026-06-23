from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .billing_plan import BillingPlan

@dataclass
class ChangeBillingPlanRequest(AdditionalDataHolder, Parsable):
    """
    Request payload for change billing plan.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The billing plan value for this billing plan.
    billing_plan: Optional[BillingPlan] = None
    # The user ID associated with this billing plan.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChangeBillingPlanRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChangeBillingPlanRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChangeBillingPlanRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .billing_plan import BillingPlan

        from .billing_plan import BillingPlan

        fields: dict[str, Callable[[Any], None]] = {
            "billingPlan": lambda n : setattr(self, 'billing_plan', n.get_enum_value(BillingPlan)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_enum_value("billingPlan", self.billing_plan)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

