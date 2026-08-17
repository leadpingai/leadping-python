# AGENTS.md

This file is the operating guide for coding agents working in the public Leadping Python SDK repository. Follow it together with `CONTRIBUTING.md`, `SECURITY.md`, and the project’s packaging configuration.

## Repository purpose

This repository contains the official asynchronous Python client for the Leadping API. Microsoft Kiota generates the client from Leadping’s OpenAPI contract. Applications provide authentication, credential storage, retry behavior, transport configuration, and logging policy.

Authoritative public resources:

- API contract: <https://leadping.ai/docs/openapi.json>
- API documentation: <https://leadping.ai/docs/api-reference>
- Authentication discovery: <https://leadping.ai/auth.md>
- Security reporting: `SECURITY.md`

## Understand the change before editing

Endpoint paths, schemas, optionality, and response behavior belong in the upstream API/OpenAPI contract. Generated request builders, models, serializers, parsers, and `leadping_open_api_client.py` should be regenerated from the corrected contract. Documentation, examples, packaging metadata, workflows, and contributor files are maintained here.

If correct OpenAPI produces invalid Python, identify the Kiota generator issue and keep any temporary workaround narrow and documented. Avoid unrelated regeneration, reformatting, or dependency churn.

## Python conventions

- Preserve asynchronous request methods, type annotations, package exports, and the Python compatibility declared by project metadata.
- Follow existing snake_case module naming and Kiota parse, serialization, and error-mapping conventions.
- Do not add a parallel HTTP or model-serialization layer.
- Treat exported names and constructor behavior as compatibility-sensitive.
- Avoid import-time I/O, hidden global state, and implicit event-loop management in library code.

## Authentication and examples

Send Leadping credentials as `Authorization: Bearer <credential>`. Never commit or log real user tokens, WorkOS agent assertions or refresh tokens, organization API keys, or source keys. Examples must use nonfunctional values, load secrets outside source control, and use `await` correctly. Do not imply that the SDK stores or refreshes credentials.

## Validation

For Python or packaging changes, run in an isolated environment:

```bash
python -m pip install -e .
python -m compileall .
```

Run the repository’s relevant test suite when tests are present. Do not include virtual environments, wheels, source distributions, caches, or unrelated generated files in the diff. Documentation-only changes normally need link, spelling, and example review.

Before handing off, inspect `git diff`, explain OpenAPI or Kiota changes, update documentation when usage changes, and report checks run and checks omitted.

## Releases and security

Do not change package versions, build or upload distributions, create tags, or alter publishing workflows unless explicitly authorized. Follow `SECURITY.md` for private vulnerability reporting.
