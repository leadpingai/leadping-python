from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_user_role import BusinessUserRole
    from .id_name_pair import IdNamePair

@dataclass
class BusinessUserResponse(AdditionalDataHolder, Parsable):
    """
    API response containing business user data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The business value for this business user.
    business: Optional[IdNamePair] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # The created by user ID associated with this business user.
    created_by_user_id: Optional[str] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # The date and time for the last used at value on this business user.
    last_used_at: Optional[datetime.datetime] = None
    # The billing status for this user's business license.
    license_billing_status: Optional[str] = None
    # The renewal date used for this user's license proration.
    license_renewal_date: Optional[datetime.datetime] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # The display name for the entity.
    name: Optional[str] = None
    # The date and time for the removed at value on this business user.
    removed_at: Optional[datetime.datetime] = None
    # The removed by user ID associated with this business user.
    removed_by_user_id: Optional[str] = None
    # The role value for this business user.
    role: Optional[BusinessUserRole] = None
    # The user value for this business user.
    user: Optional[IdNamePair] = None
    # The user email value for this business user.
    user_email: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessUserResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessUserResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessUserResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .business_user_role import BusinessUserRole
        from .id_name_pair import IdNamePair

        from .business_user_role import BusinessUserRole
        from .id_name_pair import IdNamePair

        fields: dict[str, Callable[[Any], None]] = {
            "business": lambda n : setattr(self, 'business', n.get_object_value(IdNamePair)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lastUsedAt": lambda n : setattr(self, 'last_used_at', n.get_datetime_value()),
            "licenseBillingStatus": lambda n : setattr(self, 'license_billing_status', n.get_str_value()),
            "licenseRenewalDate": lambda n : setattr(self, 'license_renewal_date', n.get_datetime_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "removedAt": lambda n : setattr(self, 'removed_at', n.get_datetime_value()),
            "removedByUserId": lambda n : setattr(self, 'removed_by_user_id', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(BusinessUserRole)),
            "user": lambda n : setattr(self, 'user', n.get_object_value(IdNamePair)),
            "userEmail": lambda n : setattr(self, 'user_email', n.get_str_value()),
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
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("lastUsedAt", self.last_used_at)
        writer.write_str_value("licenseBillingStatus", self.license_billing_status)
        writer.write_datetime_value("licenseRenewalDate", self.license_renewal_date)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_datetime_value("removedAt", self.removed_at)
        writer.write_str_value("removedByUserId", self.removed_by_user_id)
        writer.write_enum_value("role", self.role)
        writer.write_object_value("user", self.user)
        writer.write_str_value("userEmail", self.user_email)
        writer.write_additional_data_value(self.additional_data)
    

