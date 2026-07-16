from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_data_export_file import UserDataExportFile
    from .user_data_export_statuses import UserDataExportStatuses

@dataclass
class UserDataExportResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Date and time when the user data export completed.
    completed_at: Optional[datetime.datetime] = None
    # Media type of the generated file or response content.
    content_type: Optional[str] = None
    # Total number of download records represented by this Leadping user data export.
    download_count: Optional[int] = None
    # Temporary URL for downloading the completed Leadping data export.
    download_url: Optional[str] = None
    # Date and time when the user data export expires.
    expires_at: Optional[datetime.datetime] = None
    # Date and time when the user data export failed.
    failed_at: Optional[datetime.datetime] = None
    # Human-readable file name associated with this Leadping user data export.
    file_name: Optional[str] = None
    # Collection of files included with this Leadping user data export.
    files: Optional[list[UserDataExportFile]] = None
    # Unique Leadping identifier for the user data export.
    id: Optional[str] = None
    # Total number of max download records represented by this Leadping user data export.
    max_download_count: Optional[int] = None
    # Human-readable message for this Leadping user data export.
    message: Optional[str] = None
    # Date and time when the user data export was requested.
    requested_at: Optional[datetime.datetime] = None
    # Date and time when the user data export started.
    started_at: Optional[datetime.datetime] = None
    # Current status for this Leadping user data export.
    status: Optional[UserDataExportStatuses] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserDataExportResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserDataExportResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserDataExportResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .user_data_export_file import UserDataExportFile
        from .user_data_export_statuses import UserDataExportStatuses

        from .user_data_export_file import UserDataExportFile
        from .user_data_export_statuses import UserDataExportStatuses

        fields: dict[str, Callable[[Any], None]] = {
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "downloadCount": lambda n : setattr(self, 'download_count', n.get_int_value()),
            "downloadUrl": lambda n : setattr(self, 'download_url', n.get_str_value()),
            "expiresAt": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "failedAt": lambda n : setattr(self, 'failed_at', n.get_datetime_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "files": lambda n : setattr(self, 'files', n.get_collection_of_object_values(UserDataExportFile)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "maxDownloadCount": lambda n : setattr(self, 'max_download_count', n.get_int_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "requestedAt": lambda n : setattr(self, 'requested_at', n.get_datetime_value()),
            "startedAt": lambda n : setattr(self, 'started_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(UserDataExportStatuses)),
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
        writer.write_datetime_value("completedAt", self.completed_at)
        writer.write_str_value("contentType", self.content_type)
        writer.write_int_value("downloadCount", self.download_count)
        writer.write_str_value("downloadUrl", self.download_url)
        writer.write_datetime_value("expiresAt", self.expires_at)
        writer.write_datetime_value("failedAt", self.failed_at)
        writer.write_str_value("fileName", self.file_name)
        writer.write_collection_of_object_values("files", self.files)
        writer.write_str_value("id", self.id)
        writer.write_int_value("maxDownloadCount", self.max_download_count)
        writer.write_str_value("message", self.message)
        writer.write_datetime_value("requestedAt", self.requested_at)
        writer.write_datetime_value("startedAt", self.started_at)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

