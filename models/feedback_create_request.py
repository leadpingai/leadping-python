from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .feedback_create_request_type import FeedbackCreateRequest_type

@dataclass
class FeedbackCreateRequest(AdditionalDataHolder, Parsable):
    """
    User-facing request for product feedback capture.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The allowContact property
    allow_contact: Optional[bool] = None
    # The area property
    area: Optional[str] = None
    # The clientVersion property
    client_version: Optional[str] = None
    # The message property
    message: Optional[str] = None
    # The route property
    route: Optional[str] = None
    # Defines the type of product feedback submitted from inside Leadping.
    type: Optional[FeedbackCreateRequest_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FeedbackCreateRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FeedbackCreateRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FeedbackCreateRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .feedback_create_request_type import FeedbackCreateRequest_type

        from .feedback_create_request_type import FeedbackCreateRequest_type

        fields: dict[str, Callable[[Any], None]] = {
            "allowContact": lambda n : setattr(self, 'allow_contact', n.get_bool_value()),
            "area": lambda n : setattr(self, 'area', n.get_str_value()),
            "clientVersion": lambda n : setattr(self, 'client_version', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "route": lambda n : setattr(self, 'route', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(FeedbackCreateRequest_type)),
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
        writer.write_bool_value("allowContact", self.allow_contact)
        writer.write_str_value("area", self.area)
        writer.write_str_value("clientVersion", self.client_version)
        writer.write_str_value("message", self.message)
        writer.write_str_value("route", self.route)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

