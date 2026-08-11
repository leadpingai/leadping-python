[![](https://img.shields.io/pypi/v/leadping.svg?style=for-the-badge)](https://pypi.org/project/leadping/)
[![](https://img.shields.io/github/actions/workflow/status/leadpingai/leadping-python/publish.yml?style=for-the-badge)](https://github.com/leadpingai/leadping-python/actions/workflows/publish.yml)
[![](https://img.shields.io/pepy/dt/leadping?style=for-the-badge)](https://pypi.org/project/leadping/)
[![](https://img.shields.io/github/actions/workflow/status/leadpingai/leadping-python/codeql.yml?label=CodeQL&style=for-the-badge)](https://github.com/leadpingai/leadping-python/actions/workflows/codeql.yml)

# ![Leadping](https://leadping.ai/favicon.ico) Leadping Python SDK

The official, type-safe Python SDK for the Leadping API. Use it to integrate lead management, conversations, SMS and calling, automations, reporting, billing, and business settings into Python applications.

The package is generated from the [Leadping OpenAPI specification](https://leadping.ai/docs/openapi.json) with Microsoft Kiota. It contains asynchronous request builders and models; your application supplies the HTTP request adapter, credentials, retry policy, and credential storage.

## Installation

Install the SDK and Kiota's `httpx` request adapter:

```bash
python -m pip install leadping microsoft-kiota-http
```

## Authentication

Set `LEADPING_API_KEY` to a WorkOS organization API key (`sk_...`). The SDK sends it as `Authorization: Bearer <credential>`. User access tokens are also supported when acting for a signed-in user; `lp_src_...` keys are only for lead-ingestion endpoints. See [API authentication](https://leadping.ai/docs/api-authentication).

## Create a client

Kiota's API-key authentication provider can place the complete Bearer value in the `Authorization` header:

```python
import os

from kiota_abstractions.authentication.api_key_authentication_provider import (
    ApiKeyAuthenticationProvider,
    KeyLocation,
)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from leadping import LeadpingOpenApiClient

credential = os.environ["LEADPING_API_KEY"]
auth_provider = ApiKeyAuthenticationProvider(
    KeyLocation.Header,
    f"Bearer {credential}",
    "Authorization",
    ["api.leadping.ai"],
)

adapter = HttpxRequestAdapter(auth_provider)
client = LeadpingOpenApiClient(adapter)

lead = await client.leads.by_id("lead-id").get()
print(lead.id)
```

The client defaults to `https://api.leadping.ai`.

## Common operations

Request builders mirror the API path. Methods such as `by_id()` select a resource; terminal methods are asynchronous.

```python
# Requires a user access token.
current_user = await client.users.me.get()

# Retrieve organization resources by ID.
source = await client.sources.by_id("source-id").get()
lead = await client.leads.by_id("lead-id").get()
```

Create and update operations accept generated request classes from the `leadping` package.

## Resources

- [Leadping introduction](https://leadping.ai/docs/introduction)
- [API authentication](https://leadping.ai/docs/api-authentication)
- [API reference](https://leadping.ai/docs/api-reference)
- [OpenAPI specification](https://leadping.ai/docs/openapi.json)
- [PyPI package](https://pypi.org/project/leadping/)
- [License](LICENSE)
