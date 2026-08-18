from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_lookup_caller_name import PhoneLookup_callerName
    from .phone_lookup_carrier import PhoneLookup_carrier
    from .phone_lookup_line_type import PhoneLookup_lineType
    from .phone_lookup_location import PhoneLookup_location
    from .phone_lookup_portability import PhoneLookup_portability

@dataclass
class PhoneLookup(AdditionalDataHolder, Parsable):
    """
    Public Leadping API schema for phone lookup result data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Caller-name data returned by the provider.
    caller_name: Optional[PhoneLookup_callerName] = None
    # Complete carrier metadata reported for this phone number.
    carrier: Optional[PhoneLookup_carrier] = None
    # UTC timestamp when the resource was created.
    created_at: Optional[datetime.datetime] = None
    # Fraud value returned by the provider, when available.
    fraud: Optional[str] = None
    # Stable unique identifier of the resource.
    id: Optional[str] = None
    # Indicates whether this phone lookup result passed validation.
    is_valid: Optional[bool] = None
    # Classifies the access technology or service type associated with a telephone number.
    line_type: Optional[PhoneLookup_lineType] = None
    # Geographic location metadata for the phone number, lead, or lookup result.
    location: Optional[PhoneLookup_location] = None
    # UTC timestamp when the resource was last modified, or null when it has not been updated.
    modified_at: Optional[datetime.datetime] = None
    # Provider-formatted national phone number.
    national_format: Optional[str] = None
    # E.164 phone number exposed by this phone lookup result.
    number: Optional[str] = None
    # Complete portability data returned by Telnyx.
    portability: Optional[PhoneLookup_portability] = None
    # Provider record discriminator.
    record_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneLookup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneLookup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneLookup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_lookup_caller_name import PhoneLookup_callerName
        from .phone_lookup_carrier import PhoneLookup_carrier
        from .phone_lookup_line_type import PhoneLookup_lineType
        from .phone_lookup_location import PhoneLookup_location
        from .phone_lookup_portability import PhoneLookup_portability

        from .phone_lookup_caller_name import PhoneLookup_callerName
        from .phone_lookup_carrier import PhoneLookup_carrier
        from .phone_lookup_line_type import PhoneLookup_lineType
        from .phone_lookup_location import PhoneLookup_location
        from .phone_lookup_portability import PhoneLookup_portability

        fields: dict[str, Callable[[Any], None]] = {
            "callerName": lambda n : setattr(self, 'caller_name', n.get_object_value(PhoneLookup_callerName)),
            "carrier": lambda n : setattr(self, 'carrier', n.get_object_value(PhoneLookup_carrier)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "fraud": lambda n : setattr(self, 'fraud', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isValid": lambda n : setattr(self, 'is_valid', n.get_bool_value()),
            "lineType": lambda n : setattr(self, 'line_type', n.get_enum_value(PhoneLookup_lineType)),
            "location": lambda n : setattr(self, 'location', n.get_object_value(PhoneLookup_location)),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "nationalFormat": lambda n : setattr(self, 'national_format', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "portability": lambda n : setattr(self, 'portability', n.get_object_value(PhoneLookup_portability)),
            "recordType": lambda n : setattr(self, 'record_type', n.get_str_value()),
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
        writer.write_object_value("callerName", self.caller_name)
        writer.write_object_value("carrier", self.carrier)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("fraud", self.fraud)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isValid", self.is_valid)
        writer.write_enum_value("lineType", self.line_type)
        writer.write_object_value("location", self.location)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("nationalFormat", self.national_format)
        writer.write_str_value("number", self.number)
        writer.write_object_value("portability", self.portability)
        writer.write_str_value("recordType", self.record_type)
        writer.write_additional_data_value(self.additional_data)
    

