from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ten_dlc_registration_status import TenDlcRegistrationStatus

@dataclass
class TenDlcApplicationDraft(AdditionalDataHolder, Parsable):
    """
    Describes 10DLC application draft data used in Leadping API requests and responses.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether campaign content is age gated.
    age_gated: Optional[bool] = None
    # Whether the campaign subscription renews automatically.
    auto_renewal: Optional[bool] = None
    # Legal entity type registered with Telnyx.
    brand_entity_type: Optional[str] = None
    # Defines the provider lifecycle for an individual 10DLC brand or campaign.
    brand_status: Optional[TenDlcRegistrationStatus] = None
    # Individual representative email required for public-company verification.
    business_contact_email: Optional[str] = None
    # Defines the provider lifecycle for an individual 10DLC brand or campaign.
    campaign_status: Optional[TenDlcRegistrationStatus] = None
    # Legal business city.
    city: Optional[str] = None
    # Company name for this 10DLC application draft.
    company_name: Optional[str] = None
    # The compliance warnings included with this 10DLC application draft.
    compliance_warnings: Optional[list[str]] = None
    # Contact email for this 10DLC application draft.
    contact_email: Optional[str] = None
    # Contact name for this 10DLC application draft.
    contact_name: Optional[str] = None
    # Contact phone for this 10DLC application draft.
    contact_phone: Optional[str] = None
    # ISO two-letter country of registration.
    country: Optional[str] = None
    # Whether messages concern direct lending or loan arrangements.
    direct_lending: Optional[bool] = None
    # Customer-facing brand or DBA name.
    display_name: Optional[str] = None
    # EIN for this 10DLC application draft.
    ein: Optional[str] = None
    # Whether campaign messages contain links.
    embedded_link: Optional[bool] = None
    # Representative embedded link submitted for review.
    embedded_link_sample: Optional[str] = None
    # Whether campaign messages contain phone numbers.
    embedded_phone: Optional[bool] = None
    # Expected monthly volume for this 10DLC application draft.
    expected_monthly_volume: Optional[int] = None
    # Comma-separated help keywords.
    help_keywords: Optional[str] = None
    # Help response with customer-care information.
    help_message: Optional[str] = None
    # The Telnyx brand vertical for this 10DLC application draft. The JSON name is retained for backward compatibility.
    industry: Optional[str] = None
    # Whether the brand resells services to other businesses.
    is_reseller: Optional[bool] = None
    # UTC timestamp for last submitted at on this 10DLC application draft.
    last_submitted_at: Optional[datetime.datetime] = None
    # The message examples included with this 10DLC application draft.
    message_examples: Optional[list[str]] = None
    # The missing fields included with this 10DLC application draft.
    missing_fields: Optional[list[str]] = None
    # Whether the campaign uses a number pool.
    number_pool: Optional[bool] = None
    # Opt in language for this 10DLC application draft.
    opt_in_language: Optional[str] = None
    # Comma-separated opt-in keywords.
    optin_keywords: Optional[str] = None
    # Opt-in confirmation response.
    optin_message: Optional[str] = None
    # Comma-separated opt-out keywords.
    optout_keywords: Optional[str] = None
    # Opt-out confirmation response.
    optout_message: Optional[str] = None
    # Legal business postal code.
    postal_code: Optional[str] = None
    # Public privacy-policy URL that explains how messaging recipient data is handled.
    privacy_policy_url: Optional[str] = None
    # The human-readable rejection reason explaining this 10DLC application draft.
    rejection_reason: Optional[str] = None
    # Legal business state or region.
    state: Optional[str] = None
    # Public-company stock exchange.
    stock_exchange: Optional[str] = None
    # Public-company stock ticker.
    stock_symbol: Optional[str] = None
    # Legal business street address.
    street: Optional[str] = None
    # Selected sub-use cases for a mixed campaign.
    sub_use_cases: Optional[list[str]] = None
    # Whether the program responds to help keywords.
    subscriber_help: Optional[bool] = None
    # Whether subscribers opt in before messaging.
    subscriber_optin: Optional[bool] = None
    # Whether the program supports opt-out keywords.
    subscriber_optout: Optional[bool] = None
    # Acceptance of the carrier campaign terms.
    terms_and_conditions: Optional[bool] = None
    # Public terms-of-service URL governing the messaging program.
    terms_url: Optional[str] = None
    # Whether TrustedForm required applies to this 10DLC application draft.
    trusted_form_required: Optional[bool] = None
    # UTC timestamp for updated at on this 10DLC application draft.
    updated_at: Optional[datetime.datetime] = None
    # Use case for this 10DLC application draft.
    use_case: Optional[str] = None
    # Use case description for this 10DLC application draft.
    use_case_description: Optional[str] = None
    # Version for this 10DLC application draft.
    version: Optional[int] = None
    # Public business website URL submitted to carriers during brand review.
    website_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenDlcApplicationDraft:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenDlcApplicationDraft
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenDlcApplicationDraft()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ten_dlc_registration_status import TenDlcRegistrationStatus

        from .ten_dlc_registration_status import TenDlcRegistrationStatus

        fields: dict[str, Callable[[Any], None]] = {
            "ageGated": lambda n : setattr(self, 'age_gated', n.get_bool_value()),
            "autoRenewal": lambda n : setattr(self, 'auto_renewal', n.get_bool_value()),
            "brandEntityType": lambda n : setattr(self, 'brand_entity_type', n.get_str_value()),
            "brandStatus": lambda n : setattr(self, 'brand_status', n.get_enum_value(TenDlcRegistrationStatus)),
            "businessContactEmail": lambda n : setattr(self, 'business_contact_email', n.get_str_value()),
            "campaignStatus": lambda n : setattr(self, 'campaign_status', n.get_enum_value(TenDlcRegistrationStatus)),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "complianceWarnings": lambda n : setattr(self, 'compliance_warnings', n.get_collection_of_primitive_values(str)),
            "contactEmail": lambda n : setattr(self, 'contact_email', n.get_str_value()),
            "contactName": lambda n : setattr(self, 'contact_name', n.get_str_value()),
            "contactPhone": lambda n : setattr(self, 'contact_phone', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "directLending": lambda n : setattr(self, 'direct_lending', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "ein": lambda n : setattr(self, 'ein', n.get_str_value()),
            "embeddedLink": lambda n : setattr(self, 'embedded_link', n.get_bool_value()),
            "embeddedLinkSample": lambda n : setattr(self, 'embedded_link_sample', n.get_str_value()),
            "embeddedPhone": lambda n : setattr(self, 'embedded_phone', n.get_bool_value()),
            "expectedMonthlyVolume": lambda n : setattr(self, 'expected_monthly_volume', n.get_int_value()),
            "helpKeywords": lambda n : setattr(self, 'help_keywords', n.get_str_value()),
            "helpMessage": lambda n : setattr(self, 'help_message', n.get_str_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_str_value()),
            "isReseller": lambda n : setattr(self, 'is_reseller', n.get_bool_value()),
            "lastSubmittedAt": lambda n : setattr(self, 'last_submitted_at', n.get_datetime_value()),
            "messageExamples": lambda n : setattr(self, 'message_examples', n.get_collection_of_primitive_values(str)),
            "missingFields": lambda n : setattr(self, 'missing_fields', n.get_collection_of_primitive_values(str)),
            "numberPool": lambda n : setattr(self, 'number_pool', n.get_bool_value()),
            "optInLanguage": lambda n : setattr(self, 'opt_in_language', n.get_str_value()),
            "optinKeywords": lambda n : setattr(self, 'optin_keywords', n.get_str_value()),
            "optinMessage": lambda n : setattr(self, 'optin_message', n.get_str_value()),
            "optoutKeywords": lambda n : setattr(self, 'optout_keywords', n.get_str_value()),
            "optoutMessage": lambda n : setattr(self, 'optout_message', n.get_str_value()),
            "postalCode": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "privacyPolicyUrl": lambda n : setattr(self, 'privacy_policy_url', n.get_str_value()),
            "rejectionReason": lambda n : setattr(self, 'rejection_reason', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "stockExchange": lambda n : setattr(self, 'stock_exchange', n.get_str_value()),
            "stockSymbol": lambda n : setattr(self, 'stock_symbol', n.get_str_value()),
            "street": lambda n : setattr(self, 'street', n.get_str_value()),
            "subUseCases": lambda n : setattr(self, 'sub_use_cases', n.get_collection_of_primitive_values(str)),
            "subscriberHelp": lambda n : setattr(self, 'subscriber_help', n.get_bool_value()),
            "subscriberOptin": lambda n : setattr(self, 'subscriber_optin', n.get_bool_value()),
            "subscriberOptout": lambda n : setattr(self, 'subscriber_optout', n.get_bool_value()),
            "termsAndConditions": lambda n : setattr(self, 'terms_and_conditions', n.get_bool_value()),
            "termsUrl": lambda n : setattr(self, 'terms_url', n.get_str_value()),
            "trustedFormRequired": lambda n : setattr(self, 'trusted_form_required', n.get_bool_value()),
            "updatedAt": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
            "useCase": lambda n : setattr(self, 'use_case', n.get_str_value()),
            "useCaseDescription": lambda n : setattr(self, 'use_case_description', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "websiteUrl": lambda n : setattr(self, 'website_url', n.get_str_value()),
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
        writer.write_bool_value("ageGated", self.age_gated)
        writer.write_bool_value("autoRenewal", self.auto_renewal)
        writer.write_str_value("brandEntityType", self.brand_entity_type)
        writer.write_enum_value("brandStatus", self.brand_status)
        writer.write_str_value("businessContactEmail", self.business_contact_email)
        writer.write_enum_value("campaignStatus", self.campaign_status)
        writer.write_str_value("city", self.city)
        writer.write_str_value("companyName", self.company_name)
        writer.write_collection_of_primitive_values("complianceWarnings", self.compliance_warnings)
        writer.write_str_value("contactEmail", self.contact_email)
        writer.write_str_value("contactName", self.contact_name)
        writer.write_str_value("contactPhone", self.contact_phone)
        writer.write_str_value("country", self.country)
        writer.write_bool_value("directLending", self.direct_lending)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("ein", self.ein)
        writer.write_bool_value("embeddedLink", self.embedded_link)
        writer.write_str_value("embeddedLinkSample", self.embedded_link_sample)
        writer.write_bool_value("embeddedPhone", self.embedded_phone)
        writer.write_int_value("expectedMonthlyVolume", self.expected_monthly_volume)
        writer.write_str_value("helpKeywords", self.help_keywords)
        writer.write_str_value("helpMessage", self.help_message)
        writer.write_str_value("industry", self.industry)
        writer.write_bool_value("isReseller", self.is_reseller)
        writer.write_datetime_value("lastSubmittedAt", self.last_submitted_at)
        writer.write_collection_of_primitive_values("messageExamples", self.message_examples)
        writer.write_collection_of_primitive_values("missingFields", self.missing_fields)
        writer.write_bool_value("numberPool", self.number_pool)
        writer.write_str_value("optInLanguage", self.opt_in_language)
        writer.write_str_value("optinKeywords", self.optin_keywords)
        writer.write_str_value("optinMessage", self.optin_message)
        writer.write_str_value("optoutKeywords", self.optout_keywords)
        writer.write_str_value("optoutMessage", self.optout_message)
        writer.write_str_value("postalCode", self.postal_code)
        writer.write_str_value("privacyPolicyUrl", self.privacy_policy_url)
        writer.write_str_value("rejectionReason", self.rejection_reason)
        writer.write_str_value("state", self.state)
        writer.write_str_value("stockExchange", self.stock_exchange)
        writer.write_str_value("stockSymbol", self.stock_symbol)
        writer.write_str_value("street", self.street)
        writer.write_collection_of_primitive_values("subUseCases", self.sub_use_cases)
        writer.write_bool_value("subscriberHelp", self.subscriber_help)
        writer.write_bool_value("subscriberOptin", self.subscriber_optin)
        writer.write_bool_value("subscriberOptout", self.subscriber_optout)
        writer.write_bool_value("termsAndConditions", self.terms_and_conditions)
        writer.write_str_value("termsUrl", self.terms_url)
        writer.write_bool_value("trustedFormRequired", self.trusted_form_required)
        writer.write_datetime_value("updatedAt", self.updated_at)
        writer.write_str_value("useCase", self.use_case)
        writer.write_str_value("useCaseDescription", self.use_case_description)
        writer.write_int_value("version", self.version)
        writer.write_str_value("websiteUrl", self.website_url)
        writer.write_additional_data_value(self.additional_data)
    

