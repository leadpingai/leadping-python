from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_invitation_status import BusinessInvitationStatus
    from .business_user_role import BusinessUserRole

@dataclass
class BusinessInvitationResponse(AdditionalDataHolder, Parsable):
    """
    API response containing business invitation data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date and time for the accepted at value on this business invitation.
    accepted_at: Optional[datetime.datetime] = None
    # The business ID associated with this business invitation.
    business_id: Optional[str] = None
    # The business name value for this business invitation.
    business_name: Optional[str] = None
    # The date and time for the created at value on this business invitation.
    created_at: Optional[datetime.datetime] = None
    # The email address associated with this business invitation.
    email: Optional[str] = None
    # The date and time for the expires at value on this business invitation.
    expires_at: Optional[datetime.datetime] = None
    # The unique ID for this business invitation.
    id: Optional[str] = None
    # The date and time this invitation's paid license was created.
    license_activated_at: Optional[datetime.datetime] = None
    # The billing status for the paid license created by this invitation.
    license_billing_status: Optional[str] = None
    # The date and time this invitation's paid license was released.
    license_released_at: Optional[datetime.datetime] = None
    # The renewal date used for proration of this license.
    license_renewal_date: Optional[datetime.datetime] = None
    # The date and time for the resent at value on this business invitation.
    resent_at: Optional[datetime.datetime] = None
    # The date and time for the revoked at value on this business invitation.
    revoked_at: Optional[datetime.datetime] = None
    # The role value for this business invitation.
    role: Optional[BusinessUserRole] = None
    # The safe message value for this business invitation.
    safe_message: Optional[str] = None
    # The human-readable send failure reason explaining this business invitation.
    send_failure_reason: Optional[str] = None
    # The date and time for the sent at value on this business invitation.
    sent_at: Optional[datetime.datetime] = None
    # The current status for this business invitation.
    status: Optional[BusinessInvitationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessInvitationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessInvitationResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessInvitationResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .business_invitation_status import BusinessInvitationStatus
        from .business_user_role import BusinessUserRole

        from .business_invitation_status import BusinessInvitationStatus
        from .business_user_role import BusinessUserRole

        fields: dict[str, Callable[[Any], None]] = {
            "acceptedAt": lambda n : setattr(self, 'accepted_at', n.get_datetime_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "businessName": lambda n : setattr(self, 'business_name', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "expiresAt": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "licenseActivatedAt": lambda n : setattr(self, 'license_activated_at', n.get_datetime_value()),
            "licenseBillingStatus": lambda n : setattr(self, 'license_billing_status', n.get_str_value()),
            "licenseReleasedAt": lambda n : setattr(self, 'license_released_at', n.get_datetime_value()),
            "licenseRenewalDate": lambda n : setattr(self, 'license_renewal_date', n.get_datetime_value()),
            "resentAt": lambda n : setattr(self, 'resent_at', n.get_datetime_value()),
            "revokedAt": lambda n : setattr(self, 'revoked_at', n.get_datetime_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(BusinessUserRole)),
            "safeMessage": lambda n : setattr(self, 'safe_message', n.get_str_value()),
            "sendFailureReason": lambda n : setattr(self, 'send_failure_reason', n.get_str_value()),
            "sentAt": lambda n : setattr(self, 'sent_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(BusinessInvitationStatus)),
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
        writer.write_datetime_value("acceptedAt", self.accepted_at)
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("businessName", self.business_name)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("email", self.email)
        writer.write_datetime_value("expiresAt", self.expires_at)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("licenseActivatedAt", self.license_activated_at)
        writer.write_str_value("licenseBillingStatus", self.license_billing_status)
        writer.write_datetime_value("licenseReleasedAt", self.license_released_at)
        writer.write_datetime_value("licenseRenewalDate", self.license_renewal_date)
        writer.write_datetime_value("resentAt", self.resent_at)
        writer.write_datetime_value("revokedAt", self.revoked_at)
        writer.write_enum_value("role", self.role)
        writer.write_str_value("safeMessage", self.safe_message)
        writer.write_str_value("sendFailureReason", self.send_failure_reason)
        writer.write_datetime_value("sentAt", self.sent_at)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

