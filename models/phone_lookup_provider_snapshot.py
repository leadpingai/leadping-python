from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PhoneLookupProviderSnapshot(AdditionalDataHolder, Parsable):
    """
    Lossless provider snapshot retained with a phone identity for replay, audits, and fields added by providers later.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The lookupType property
    lookup_type: Optional[str] = None
    # The provider property
    provider: Optional[str] = None
    # The rawRecordJson property
    raw_record_json: Optional[str] = None
    # The retrievedAt property
    retrieved_at: Optional[datetime.datetime] = None
    # The schemaVersion property
    schema_version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneLookupProviderSnapshot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneLookupProviderSnapshot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneLookupProviderSnapshot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "lookupType": lambda n : setattr(self, 'lookup_type', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
            "rawRecordJson": lambda n : setattr(self, 'raw_record_json', n.get_str_value()),
            "retrievedAt": lambda n : setattr(self, 'retrieved_at', n.get_datetime_value()),
            "schemaVersion": lambda n : setattr(self, 'schema_version', n.get_int_value()),
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
        writer.write_str_value("lookupType", self.lookup_type)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("rawRecordJson", self.raw_record_json)
        writer.write_datetime_value("retrievedAt", self.retrieved_at)
        writer.write_int_value("schemaVersion", self.schema_version)
        writer.write_additional_data_value(self.additional_data)
    

