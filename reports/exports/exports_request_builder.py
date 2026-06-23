from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_export_item_request_builder import WithExportItemRequestBuilder
    from .my.my_request_builder import MyRequestBuilder

class ExportsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /reports/exports
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ExportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/reports/exports", path_parameters)
    
    def by_export_id(self,export_id: str) -> WithExportItemRequestBuilder:
        """
        Gets an item from the leadping.reports.exports.item collection
        param export_id: Unique identifier of the item
        Returns: WithExportItemRequestBuilder
        """
        if export_id is None:
            raise TypeError("export_id cannot be null.")
        from .item.with_export_item_request_builder import WithExportItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["exportId"] = export_id
        return WithExportItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def my(self) -> MyRequestBuilder:
        """
        The my property
        """
        from .my.my_request_builder import MyRequestBuilder

        return MyRequestBuilder(self.request_adapter, self.path_parameters)
    

