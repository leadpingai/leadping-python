from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_identity_lookup_action import PhoneIdentityLookupAction
    from .phone_identity_response_lookup import PhoneIdentityResponse_lookup
    from .phone_identity_response_provider_enrichment import PhoneIdentityResponse_providerEnrichment

@dataclass
class PhoneIdentityResponse(AdditionalDataHolder, Parsable):
    """
    Describes Leadping's canonical identity for a phone number, including normalization, carrier, line type, reputation, and lookup history.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # UTC timestamp when the resource was created.
    created_at: Optional[datetime.datetime] = None
    # Stable unique identifier of the resource.
    id: Optional[str] = None
    # The most recent time lookup data was enriched.
    last_enriched_at: Optional[datetime.datetime] = None
    # Provider lookup and enrichment data for the number.
    lookup: Optional[PhoneIdentityResponse_lookup] = None
    # Lookup, enrichment, and reputation actions performed for this identity.
    lookup_actions: Optional[list[PhoneIdentityLookupAction]] = None
    # UTC timestamp when the resource was last modified, or null when it has not been updated.
    modified_at: Optional[datetime.datetime] = None
    # Human-readable display name of the resource.
    name: Optional[str] = None
    # The canonical E.164 phone number.
    number: Optional[str] = None
    # Lossless provider response retained for administrative diagnostics.
    provider_enrichment: Optional[PhoneIdentityResponse_providerEnrichment] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneIdentityResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneIdentityResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneIdentityResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_identity_lookup_action import PhoneIdentityLookupAction
        from .phone_identity_response_lookup import PhoneIdentityResponse_lookup
        from .phone_identity_response_provider_enrichment import PhoneIdentityResponse_providerEnrichment

        from .phone_identity_lookup_action import PhoneIdentityLookupAction
        from .phone_identity_response_lookup import PhoneIdentityResponse_lookup
        from .phone_identity_response_provider_enrichment import PhoneIdentityResponse_providerEnrichment

        fields: dict[str, Callable[[Any], None]] = {
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lastEnrichedAt": lambda n : setattr(self, 'last_enriched_at', n.get_datetime_value()),
            "lookup": lambda n : setattr(self, 'lookup', n.get_object_value(PhoneIdentityResponse_lookup)),
            "lookupActions": lambda n : setattr(self, 'lookup_actions', n.get_collection_of_object_values(PhoneIdentityLookupAction)),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "providerEnrichment": lambda n : setattr(self, 'provider_enrichment', n.get_object_value(PhoneIdentityResponse_providerEnrichment)),
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
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("lastEnrichedAt", self.last_enriched_at)
        writer.write_object_value("lookup", self.lookup)
        writer.write_collection_of_object_values("lookupActions", self.lookup_actions)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_str_value("number", self.number)
        writer.write_object_value("providerEnrichment", self.provider_enrichment)
        writer.write_additional_data_value(self.additional_data)
    

