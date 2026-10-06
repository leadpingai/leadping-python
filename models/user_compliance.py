from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .leadping_consent_certificate import LeadpingConsentCertificate

@dataclass
class UserCompliance(AdditionalDataHolder, Parsable):
    """
    Describes user compliance data used in Leadping API requests and responses.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether the user accepted BAA for this user compliance.
    accepted_baa: Optional[bool] = None
    # Whether the user accepted email for this user compliance.
    accepted_email: Optional[bool] = None
    # Whether the user accepted SMS for this user compliance.
    accepted_sms: Optional[bool] = None
    # Whether the user accepted terms for this user compliance.
    accepted_terms: Optional[bool] = None
    # Whether the user accepted subscription for this user compliance.
    accepted_to_subscription: Optional[bool] = None
    # The Leadping Consent certificates included with this user compliance.
    consent_certificates: Optional[list[LeadpingConsentCertificate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserCompliance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserCompliance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserCompliance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .leadping_consent_certificate import LeadpingConsentCertificate

        from .leadping_consent_certificate import LeadpingConsentCertificate

        fields: dict[str, Callable[[Any], None]] = {
            "acceptedBaa": lambda n : setattr(self, 'accepted_baa', n.get_bool_value()),
            "acceptedEmail": lambda n : setattr(self, 'accepted_email', n.get_bool_value()),
            "acceptedSms": lambda n : setattr(self, 'accepted_sms', n.get_bool_value()),
            "acceptedTerms": lambda n : setattr(self, 'accepted_terms', n.get_bool_value()),
            "acceptedToSubscription": lambda n : setattr(self, 'accepted_to_subscription', n.get_bool_value()),
            "consentCertificates": lambda n : setattr(self, 'consent_certificates', n.get_collection_of_object_values(LeadpingConsentCertificate)),
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
        writer.write_bool_value("acceptedBaa", self.accepted_baa)
        writer.write_bool_value("acceptedEmail", self.accepted_email)
        writer.write_bool_value("acceptedSms", self.accepted_sms)
        writer.write_bool_value("acceptedTerms", self.accepted_terms)
        writer.write_bool_value("acceptedToSubscription", self.accepted_to_subscription)
        writer.write_collection_of_object_values("consentCertificates", self.consent_certificates)
        writer.write_additional_data_value(self.additional_data)
    

