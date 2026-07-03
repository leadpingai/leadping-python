from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.api_client_builder import enable_backing_store_for_serialization_writer_factory, register_default_deserializer, register_default_serializer
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.serialization import ParseNodeFactoryRegistry, SerializationWriterFactoryRegistry
from kiota_serialization_form.form_parse_node_factory import FormParseNodeFactory
from kiota_serialization_form.form_serialization_writer_factory import FormSerializationWriterFactory
from kiota_serialization_json.json_parse_node_factory import JsonParseNodeFactory
from kiota_serialization_json.json_serialization_writer_factory import JsonSerializationWriterFactory
from kiota_serialization_multipart.multipart_serialization_writer_factory import MultipartSerializationWriterFactory
from kiota_serialization_text.text_parse_node_factory import TextParseNodeFactory
from kiota_serialization_text.text_serialization_writer_factory import TextSerializationWriterFactory
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytics.analytics_request_builder import AnalyticsRequestBuilder
    from .automations.automations_request_builder import AutomationsRequestBuilder
    from .businesses.businesses_request_builder import BusinessesRequestBuilder
    from .contact.contact_request_builder import ContactRequestBuilder
    from .conversations.conversations_request_builder import ConversationsRequestBuilder
    from .dispositions.dispositions_request_builder import DispositionsRequestBuilder
    from .events.events_request_builder import EventsRequestBuilder
    from .feedback.feedback_request_builder import FeedbackRequestBuilder
    from .leads.leads_request_builder import LeadsRequestBuilder
    from .notifications.notifications_request_builder import NotificationsRequestBuilder
    from .outbound.outbound_request_builder import OutboundRequestBuilder
    from .payment_methods.payment_methods_request_builder import PaymentMethodsRequestBuilder
    from .phone_call.phone_call_request_builder import PhoneCallRequestBuilder
    from .phone_numbers.phone_numbers_request_builder import PhoneNumbersRequestBuilder
    from .reports.reports_request_builder import ReportsRequestBuilder
    from .sms.sms_request_builder import SmsRequestBuilder
    from .sources.sources_request_builder import SourcesRequestBuilder
    from .suppressions.suppressions_request_builder import SuppressionsRequestBuilder
    from .tags.tags_request_builder import TagsRequestBuilder
    from .telephony.telephony_request_builder import TelephonyRequestBuilder
    from .transactions.transactions_request_builder import TransactionsRequestBuilder
    from .usage.usage_request_builder import UsageRequestBuilder
    from .users.users_request_builder import UsersRequestBuilder
    from .wallets.wallets_request_builder import WalletsRequestBuilder

class LeadpingOpenApiClient(BaseRequestBuilder):
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
    def __init__(self,request_adapter: RequestAdapter) -> None:
        """
        Instantiates a new LeadpingOpenApiClient and sets the default values.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if request_adapter is None:
            raise TypeError("request_adapter cannot be null.")
        super().__init__(request_adapter, "{+baseurl}", None)
        register_default_serializer(JsonSerializationWriterFactory)
        register_default_serializer(TextSerializationWriterFactory)
        register_default_serializer(FormSerializationWriterFactory)
        register_default_serializer(MultipartSerializationWriterFactory)
        register_default_deserializer(JsonParseNodeFactory)
        register_default_deserializer(TextParseNodeFactory)
        register_default_deserializer(FormParseNodeFactory)
        if not self.request_adapter.base_url:
            self.request_adapter.base_url = "https://api.leadping.ai"
        self.path_parameters["base_url"] = self.request_adapter.base_url
    
    @property
    def analytics(self) -> AnalyticsRequestBuilder:
        """
        The analytics property
        """
        from .analytics.analytics_request_builder import AnalyticsRequestBuilder

        return AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def automations(self) -> AutomationsRequestBuilder:
        """
        The automations property
        """
        from .automations.automations_request_builder import AutomationsRequestBuilder

        return AutomationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def businesses(self) -> BusinessesRequestBuilder:
        """
        The businesses property
        """
        from .businesses.businesses_request_builder import BusinessesRequestBuilder

        return BusinessesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contact(self) -> ContactRequestBuilder:
        """
        The contact property
        """
        from .contact.contact_request_builder import ContactRequestBuilder

        return ContactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conversations(self) -> ConversationsRequestBuilder:
        """
        The conversations property
        """
        from .conversations.conversations_request_builder import ConversationsRequestBuilder

        return ConversationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dispositions(self) -> DispositionsRequestBuilder:
        """
        The dispositions property
        """
        from .dispositions.dispositions_request_builder import DispositionsRequestBuilder

        return DispositionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def events(self) -> EventsRequestBuilder:
        """
        The events property
        """
        from .events.events_request_builder import EventsRequestBuilder

        return EventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def feedback(self) -> FeedbackRequestBuilder:
        """
        The feedback property
        """
        from .feedback.feedback_request_builder import FeedbackRequestBuilder

        return FeedbackRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def leads(self) -> LeadsRequestBuilder:
        """
        The leads property
        """
        from .leads.leads_request_builder import LeadsRequestBuilder

        return LeadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notifications(self) -> NotificationsRequestBuilder:
        """
        The notifications property
        """
        from .notifications.notifications_request_builder import NotificationsRequestBuilder

        return NotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def outbound(self) -> OutboundRequestBuilder:
        """
        The outbound property
        """
        from .outbound.outbound_request_builder import OutboundRequestBuilder

        return OutboundRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payment_methods(self) -> PaymentMethodsRequestBuilder:
        """
        The paymentMethods property
        """
        from .payment_methods.payment_methods_request_builder import PaymentMethodsRequestBuilder

        return PaymentMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def phone_call(self) -> PhoneCallRequestBuilder:
        """
        The phoneCall property
        """
        from .phone_call.phone_call_request_builder import PhoneCallRequestBuilder

        return PhoneCallRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def phone_numbers(self) -> PhoneNumbersRequestBuilder:
        """
        The phoneNumbers property
        """
        from .phone_numbers.phone_numbers_request_builder import PhoneNumbersRequestBuilder

        return PhoneNumbersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reports(self) -> ReportsRequestBuilder:
        """
        The reports property
        """
        from .reports.reports_request_builder import ReportsRequestBuilder

        return ReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sms(self) -> SmsRequestBuilder:
        """
        The sms property
        """
        from .sms.sms_request_builder import SmsRequestBuilder

        return SmsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sources(self) -> SourcesRequestBuilder:
        """
        The sources property
        """
        from .sources.sources_request_builder import SourcesRequestBuilder

        return SourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def suppressions(self) -> SuppressionsRequestBuilder:
        """
        The suppressions property
        """
        from .suppressions.suppressions_request_builder import SuppressionsRequestBuilder

        return SuppressionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tags(self) -> TagsRequestBuilder:
        """
        The tags property
        """
        from .tags.tags_request_builder import TagsRequestBuilder

        return TagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def telephony(self) -> TelephonyRequestBuilder:
        """
        The telephony property
        """
        from .telephony.telephony_request_builder import TelephonyRequestBuilder

        return TelephonyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transactions(self) -> TransactionsRequestBuilder:
        """
        The transactions property
        """
        from .transactions.transactions_request_builder import TransactionsRequestBuilder

        return TransactionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def usage(self) -> UsageRequestBuilder:
        """
        The usage property
        """
        from .usage.usage_request_builder import UsageRequestBuilder

        return UsageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> UsersRequestBuilder:
        """
        The users property
        """
        from .users.users_request_builder import UsersRequestBuilder

        return UsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wallets(self) -> WalletsRequestBuilder:
        """
        The wallets property
        """
        from .wallets.wallets_request_builder import WalletsRequestBuilder

        return WalletsRequestBuilder(self.request_adapter, self.path_parameters)
    

