from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .push_installation_request_metadata import PushInstallationRequest_metadata

@dataclass
class PushInstallationRequest(AdditionalDataHolder, Parsable):
    """
    Describes a mobile push installation. Identity and Azure tags are derived by the API.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The application build number reported by the client.
    app_build: Optional[str] = None
    # The application bundle identifier or package name.
    app_identifier: Optional[str] = None
    # The human-readable application name reported by the client.
    app_name: Optional[str] = None
    # The semantic application version reported by the client.
    app_version: Optional[str] = None
    # The device model reported by the client.
    device_model: Optional[str] = None
    # The mobile operating-system platform reported by the device.
    device_platform: Optional[str] = None
    # The mobile operating-system version reported by the device.
    device_version: Optional[str] = None
    # The stable installation identifier assigned by the mobile client.
    installation_id: Optional[str] = None
    # Optional client metadata stored with the push installation.
    metadata: Optional[PushInstallationRequest_metadata] = None
    # The Azure Notification Hubs platform name, such as apns or fcmv1.
    platform: Optional[str] = None
    # The provider-issued push token or channel used to deliver notifications.
    push_channel: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PushInstallationRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PushInstallationRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PushInstallationRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .push_installation_request_metadata import PushInstallationRequest_metadata

        from .push_installation_request_metadata import PushInstallationRequest_metadata

        fields: dict[str, Callable[[Any], None]] = {
            "appBuild": lambda n : setattr(self, 'app_build', n.get_str_value()),
            "appIdentifier": lambda n : setattr(self, 'app_identifier', n.get_str_value()),
            "appName": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "appVersion": lambda n : setattr(self, 'app_version', n.get_str_value()),
            "deviceModel": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "devicePlatform": lambda n : setattr(self, 'device_platform', n.get_str_value()),
            "deviceVersion": lambda n : setattr(self, 'device_version', n.get_str_value()),
            "installationId": lambda n : setattr(self, 'installation_id', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(PushInstallationRequest_metadata)),
            "platform": lambda n : setattr(self, 'platform', n.get_str_value()),
            "pushChannel": lambda n : setattr(self, 'push_channel', n.get_str_value()),
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
        writer.write_str_value("appBuild", self.app_build)
        writer.write_str_value("appIdentifier", self.app_identifier)
        writer.write_str_value("appName", self.app_name)
        writer.write_str_value("appVersion", self.app_version)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_str_value("devicePlatform", self.device_platform)
        writer.write_str_value("deviceVersion", self.device_version)
        writer.write_str_value("installationId", self.installation_id)
        writer.write_object_value("metadata", self.metadata)
        writer.write_str_value("platform", self.platform)
        writer.write_str_value("pushChannel", self.push_channel)
        writer.write_additional_data_value(self.additional_data)
    

