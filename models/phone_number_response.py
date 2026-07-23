from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_readiness import PhoneNumberReadiness
    from .phone_number_response_business import PhoneNumberResponse_business
    from .phone_number_routing_metadata import PhoneNumberRoutingMetadata

@dataclass
class PhoneNumberResponse(AdditionalDataHolder, Parsable):
    """
    Response schema for the Leadping API phone number returned to authenticated clients.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Business summary connected to this phone number.
    business: Optional[PhoneNumberResponse_business] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # Indicates whether this phone number is active and available in the Leadping API.
    enabled: Optional[bool] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # Indicates whether Leadping provisions and manages this phone number.
    leadping_owned: Optional[bool] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # The display name for the entity.
    name: Optional[str] = None
    # E.164 phone number exposed by this phone number.
    number: Optional[str] = None
    # Identifier of the canonical phone identity for this number.
    phone_identity_id: Optional[str] = None
    # Routing metadata that connects this phone number to teams, campaigns, and sources.
    routing: Optional[PhoneNumberRoutingMetadata] = None
    # SMS and call warmup for this phone number.
    warmup: Optional[PhoneNumberReadiness] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_readiness import PhoneNumberReadiness
        from .phone_number_response_business import PhoneNumberResponse_business
        from .phone_number_routing_metadata import PhoneNumberRoutingMetadata

        from .phone_number_readiness import PhoneNumberReadiness
        from .phone_number_response_business import PhoneNumberResponse_business
        from .phone_number_routing_metadata import PhoneNumberRoutingMetadata

        fields: dict[str, Callable[[Any], None]] = {
            "business": lambda n : setattr(self, 'business', n.get_object_value(PhoneNumberResponse_business)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "leadpingOwned": lambda n : setattr(self, 'leadping_owned', n.get_bool_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "phoneIdentityId": lambda n : setattr(self, 'phone_identity_id', n.get_str_value()),
            "routing": lambda n : setattr(self, 'routing', n.get_object_value(PhoneNumberRoutingMetadata)),
            "warmup": lambda n : setattr(self, 'warmup', n.get_object_value(PhoneNumberReadiness)),
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
        writer.write_object_value("business", self.business)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("leadpingOwned", self.leadping_owned)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_str_value("number", self.number)
        writer.write_str_value("phoneIdentityId", self.phone_identity_id)
        writer.write_object_value("routing", self.routing)
        writer.write_object_value("warmup", self.warmup)
        writer.write_additional_data_value(self.additional_data)
    

