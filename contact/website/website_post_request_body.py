from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WebsitePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The CompanyWebsite property
    company_website: Optional[str] = None
    # The Email property
    email: Optional[str] = None
    # The Message property
    message: Optional[str] = None
    # The Name property
    name: Optional[str] = None
    # The Phone property
    phone: Optional[str] = None
    # The ReturnUrl property
    return_url: Optional[str] = None
    # The SmsConsent property
    sms_consent: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebsitePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebsitePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebsitePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "CompanyWebsite": lambda n : setattr(self, 'company_website', n.get_str_value()),
            "Email": lambda n : setattr(self, 'email', n.get_str_value()),
            "Message": lambda n : setattr(self, 'message', n.get_str_value()),
            "Name": lambda n : setattr(self, 'name', n.get_str_value()),
            "Phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "ReturnUrl": lambda n : setattr(self, 'return_url', n.get_str_value()),
            "SmsConsent": lambda n : setattr(self, 'sms_consent', n.get_bool_value()),
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
        writer.write_str_value("CompanyWebsite", self.company_website)
        writer.write_str_value("Email", self.email)
        writer.write_str_value("Message", self.message)
        writer.write_str_value("Name", self.name)
        writer.write_str_value("Phone", self.phone)
        writer.write_str_value("ReturnUrl", self.return_url)
        writer.write_bool_value("SmsConsent", self.sms_consent)
        writer.write_additional_data_value(self.additional_data)
    

