# Leadping Python SDK

Typed Python client for the Leadping API, generated from `leadpingai/openapi` with Kiota.

## Install

```bash
pip install leadping
```

Use a Kiota request adapter, such as:

```bash
pip install microsoft-kiota-http
```

## Use

```python
from leadping import LeadpingOpenApiClient

adapter = create_leadping_request_adapter()
adapter.base_url = "https://api.leadping.ai"

client = LeadpingOpenApiClient(adapter)
me = await client.users.me.get()
```

`create_leadping_request_adapter` should return a Kiota request adapter configured with your Leadping authentication.

## Notes

- Generated code comes from `leadpingai/openapi`; update the OpenAPI spec instead of hand-editing generated files.
- Package name: `leadping`
- License: see `LICENSE`
