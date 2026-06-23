from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .announcements.announcements_request_builder import AnnouncementsRequestBuilder
    from .item.notifications_item_request_builder import NotificationsItemRequestBuilder
    from .mark_all_read.mark_all_read_request_builder import MarkAllReadRequestBuilder
    from .me.me_request_builder import MeRequestBuilder
    from .unread_count.unread_count_request_builder import UnreadCountRequestBuilder

class NotificationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /notifications
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new NotificationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/notifications", path_parameters)
    
    def by_id(self,id: str) -> NotificationsItemRequestBuilder:
        """
        Gets an item from the leadping.notifications.item collection
        param id: The ID of the notification to mark as read.
        Returns: NotificationsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.notifications_item_request_builder import NotificationsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return NotificationsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def announcements(self) -> AnnouncementsRequestBuilder:
        """
        The announcements property
        """
        from .announcements.announcements_request_builder import AnnouncementsRequestBuilder

        return AnnouncementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mark_all_read(self) -> MarkAllReadRequestBuilder:
        """
        The markAllRead property
        """
        from .mark_all_read.mark_all_read_request_builder import MarkAllReadRequestBuilder

        return MarkAllReadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def me(self) -> MeRequestBuilder:
        """
        The me property
        """
        from .me.me_request_builder import MeRequestBuilder

        return MeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unread_count(self) -> UnreadCountRequestBuilder:
        """
        The unreadCount property
        """
        from .unread_count.unread_count_request_builder import UnreadCountRequestBuilder

        return UnreadCountRequestBuilder(self.request_adapter, self.path_parameters)
    

