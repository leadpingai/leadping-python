from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_request_admin_enablement_override import PhoneNumberRequest_adminEnablementOverride

@dataclass
class PhoneNumberRequest(AdditionalDataHolder, Parsable):
    """
    Request payload for phone number.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The adminEnablementOverride property
    admin_enablement_override: Optional[PhoneNumberRequest_adminEnablementOverride] = None
    # The business ID associated with this phone number.
    business_id: Optional[str] = None
    # Whether this phone number is enabled.
    enabled: Optional[bool] = None
    # The unique identifier for the entity, when updating an existing entity.
    id: Optional[str] = None
    # The display name for the entity.
    name: Optional[str] = None
    # The number value for this phone number.
    number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_request_admin_enablement_override import PhoneNumberRequest_adminEnablementOverride

        from .phone_number_request_admin_enablement_override import PhoneNumberRequest_adminEnablementOverride

        fields: dict[str, Callable[[Any], None]] = {
            "adminEnablementOverride": lambda n : setattr(self, 'admin_enablement_override', n.get_object_value(PhoneNumberRequest_adminEnablementOverride)),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
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
        writer.write_str_value("businessId", self.business_id)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("number", self.number)
        writer.write_additional_data_value(self.additional_data)
    

