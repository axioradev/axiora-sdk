# Axiora — Python SDK

[![PyPI](https://img.shields.io/pypi/v/axiora.svg)](https://pypi.org/project/axiora/)

**Provable financial intelligence for Japanese equities.**

The Axiora SDK gives Python access to ~4,000 listed Japanese companies and ~9,000 unlisted EDINET filers — financials, ownership networks, audit-stamped per-row classifications, subsidiary cross-validation, and live activist signals. Every figure traces to its source filing.

```sh
pip install axiora
```

## Get an API key

Request access at [axiora.dev](https://axiora.dev). Set it as an environment variable:

```sh
export AXIORA_API_KEY="ax_live_..."
```

## Quickstart

```python
from axiora import Axiora

client = Axiora()  # picks up AXIORA_API_KEY from env

# Who holds Toyota — with the audit bundle institutional users actually need.
rows = client.companies.list_shareholdings("7203", limit=10).data

for r in rows:
    print(
        f"{r.holder_name:<40} {r.holding_ratio_pct:>6.2f}%  "
        f"{r.holding_purpose_category:<22} "
        f"conf={r.purpose_confidence:.2f}  validated={r.purpose_validated}  "
        f"retro={r.purpose_retrospective_label}"
    )
```

Every row carries:
- `purpose_confidence` — calibrated probability of the at-filing classification
- `purpose_validated` — passed cross-checks against the filer's history
- `purpose_retrospective_label` — what later filings revealed (drift detection)
- `purpose_classifier_version` — opaque hash, lets you replay analysis if the model is retrained

## What you can do

```python
# Multi-year financials with derived ratios (ROA/ROE/margins computed in-band)
client.companies.retrieve_financials("7203", years=5)

# Growth — YoY rates per metric + 3y / 5y CAGR
client.companies.retrieve_growth("7203")

# Discovery: rank, screen, sector aggregates
client.rankings.retrieve("net_income", limit=20)
client.screen.retrieve(min_roe=15, min_revenue=100_000_000_000)
client.sectors.list()

# Earnings: actuals + management forecasts + market-wide surprise signals
client.companies.earnings.list("5423")
client.companies.get_forecasts("5423")
client.earnings.list_signals(limit=20)

# Governance: board composition + AGM voting outcomes
client.companies.get_board_composition("7203")
client.companies.list_voting_results("7036")

# Ownership intelligence
client.ownership.list_movers(days=90, limit=20)
client.ownership.list_activist_campaigns(limit=20)
client.companies.relationships.retrieve("7203")  # holders + holdings + interlocks + cross-holds
client.companies.subsidiaries.retrieve("7203")   # parent–subsidiary cross-validation

# Per-row provenance for any shareholding
client.shareholdings.audit("312750")
```

Full method index: [api.md](api.md). REST docs: [axiora.dev/docs](https://axiora.dev/docs).

## Async

```python
import asyncio
from axiora import AsyncAxiora

async def main():
    async with AsyncAxiora() as client:
        rows = (await client.companies.list_shareholdings("7203", limit=5)).data
        for r in rows:
            print(r.holder_name, r.holding_ratio_pct)

asyncio.run(main())
```

Functionality is identical to the sync client.

## Translation note

English filer / company / sector / business-description fields are populated by best-effort translation today. We don't yet guarantee them — treat the Japanese fields (`name_jp`, `sector`, `address_jp`, `business_description_jp`) as the contract and use the English variants as hints. A fine-tuned frontier-model translation pipeline ships in May 2026; after rollout, English fields will carry per-field source / model version / confidence stamps.

## Error handling

```python
from axiora import Axiora, APIStatusError, RateLimitError

client = Axiora()
try:
    client.companies.retrieve("7203")
except RateLimitError:
    ...   # 429 — back off
except APIStatusError as e:
    print(e.status_code, e.response)
```

| Status | Error                       |
|---|---|
| 400 | `BadRequestError`             |
| 401 | `AuthenticationError`         |
| 403 | `PermissionDeniedError`       |
| 404 | `NotFoundError`               |
| 422 | `UnprocessableEntityError`    |
| 429 | `RateLimitError`              |
| 5xx | `InternalServerError`         |
| —   | `APIConnectionError`          |

## Configuration

`max_retries` (default 2), `timeout` (default 60s), and `base_url` are configurable per-client and per-request:

```python
client = Axiora(max_retries=5, timeout=20.0)
client.with_options(timeout=5.0).companies.retrieve("7203")
```

For raw responses (headers etc.), prefix `with_raw_response`. For streaming, `with_streaming_response`. See the [Stainless conventions](https://www.stainless.com/docs/concepts/clients) for the full surface — every method supports both.

## Requirements

Python 3.9+. The async client uses `httpx` by default; `pip install axiora[aiohttp]` to switch backends.

## Versioning

[SemVer](https://semver.org). Breaking changes get noted in the [CHANGELOG](./CHANGELOG.md). Minor 0.x bumps may include backwards-incompatible static-type adjustments — if you pin runtime behaviour, pin the patch version.

```python
import axiora
print(axiora.__version__)
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). The SDK is generated by [Stainless](https://www.stainless.com/) from our OpenAPI spec — substantive changes ship via spec updates, not direct edits to generated files.

## License

Apache 2.0. See [LICENSE](./LICENSE).
