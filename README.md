# Leadping Python SDK

Type-safe Python client for the Leadping API.

## Install

```bash
pip install leadping
```

The generated client uses a Kiota request adapter. Install the default HTTP adapter:

```bash
pip install microsoft-kiota-http
```

## Use

```python
from leadping import LeadpingOpenApiClient

adapter = create_leadping_request_adapter()
client = LeadpingOpenApiClient(adapter)

me = await client.users.me.get()
```

`create_leadping_request_adapter` is application code. Configure it to send one of:

- `Authorization: Bearer <token>`
- `X-Leadping-Api-Key: <key>`

The client defaults to `https://api.leadping.ai` when the adapter does not already have a base URL.

## Links

- [API reference](https://leadping.ai/docs/api-reference)
- [License](LICENSE)
