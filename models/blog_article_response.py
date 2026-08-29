from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BlogArticleResponse(AdditionalDataHolder, Parsable):
    """
    Represents a blog article response.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Gets or sets the author name.
    author_name: Optional[str] = None
    # Gets or sets the category.
    category: Optional[str] = None
    # Gets or sets the content.
    content: Optional[str] = None
    # Gets or sets the cover image URL.
    cover_image_url: Optional[str] = None
    # Gets or sets the created at.
    created_at: Optional[datetime.datetime] = None
    # Gets or sets the excerpt.
    excerpt: Optional[str] = None
    # Gets or sets the ID.
    id: Optional[str] = None
    # Gets or sets the is featured.
    is_featured: Optional[bool] = None
    # Gets or sets the is published.
    is_published: Optional[bool] = None
    # Gets or sets the modified at.
    modified_at: Optional[datetime.datetime] = None
    # Gets or sets the published at.
    published_at: Optional[datetime.datetime] = None
    # Gets or sets the slug.
    slug: Optional[str] = None
    # Gets or sets the title.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BlogArticleResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BlogArticleResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BlogArticleResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "authorName": lambda n : setattr(self, 'author_name', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "coverImageUrl": lambda n : setattr(self, 'cover_image_url', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "excerpt": lambda n : setattr(self, 'excerpt', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isFeatured": lambda n : setattr(self, 'is_featured', n.get_bool_value()),
            "isPublished": lambda n : setattr(self, 'is_published', n.get_bool_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "publishedAt": lambda n : setattr(self, 'published_at', n.get_datetime_value()),
            "slug": lambda n : setattr(self, 'slug', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("authorName", self.author_name)
        writer.write_str_value("category", self.category)
        writer.write_str_value("content", self.content)
        writer.write_str_value("coverImageUrl", self.cover_image_url)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("excerpt", self.excerpt)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isFeatured", self.is_featured)
        writer.write_bool_value("isPublished", self.is_published)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_datetime_value("publishedAt", self.published_at)
        writer.write_str_value("slug", self.slug)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

