from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conversation_response import ConversationResponse

@dataclass
class ConversationPage(AdditionalDataHolder, Parsable):
    """
    A page of inbox conversations with optional action counts and refresh timing.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The continuationToken property
    continuation_token: Optional[str] = None
    # The items property
    items: Optional[list[ConversationResponse]] = None
    # Visible unanswered conversations, capped at ReplyCountDisplayLimit + 1. Included on request.
    needs_reply_count: Optional[int] = None
    # The pageSize property
    page_size: Optional[int] = None
    # Time remaining until a scheduled action or contact window could change this page, measured on the server.
    refresh_after: Optional[str] = None
    # The totalCount property
    total_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConversationPage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConversationPage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConversationPage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conversation_response import ConversationResponse

        from .conversation_response import ConversationResponse

        fields: dict[str, Callable[[Any], None]] = {
            "continuationToken": lambda n : setattr(self, 'continuation_token', n.get_str_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(ConversationResponse)),
            "needsReplyCount": lambda n : setattr(self, 'needs_reply_count', n.get_int_value()),
            "pageSize": lambda n : setattr(self, 'page_size', n.get_int_value()),
            "refreshAfter": lambda n : setattr(self, 'refresh_after', n.get_str_value()),
            "totalCount": lambda n : setattr(self, 'total_count', n.get_int_value()),
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
        writer.write_str_value("continuationToken", self.continuation_token)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_int_value("needsReplyCount", self.needs_reply_count)
        writer.write_int_value("pageSize", self.page_size)
        writer.write_str_value("refreshAfter", self.refresh_after)
        writer.write_int_value("totalCount", self.total_count)
        writer.write_additional_data_value(self.additional_data)
    

