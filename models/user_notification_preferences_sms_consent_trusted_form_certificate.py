from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .trusted_form_certificate import TrustedFormCertificate

from .trusted_form_certificate import TrustedFormCertificate

@dataclass
class UserNotificationPreferences_smsConsentTrustedFormCertificate(TrustedFormCertificate, Parsable):
    """
    The TrustedForm certificate captured for the user's most recent SMS opt-in.
    """
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserNotificationPreferences_smsConsentTrustedFormCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserNotificationPreferences_smsConsentTrustedFormCertificate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserNotificationPreferences_smsConsentTrustedFormCertificate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .trusted_form_certificate import TrustedFormCertificate

        from .trusted_form_certificate import TrustedFormCertificate

        fields: dict[str, Callable[[Any], None]] = {
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

