# Health

Types:

```python
from axiora.types import HealthCheckResponse, HealthCheckDeepResponse
```

Methods:

- <code title="get /v1/health">client.health.<a href="./src/axiora/resources/health.py">check</a>() -> <a href="./src/axiora/types/health_check_response.py">HealthCheckResponse</a></code>
- <code title="get /v1/health/deep">client.health.<a href="./src/axiora/resources/health.py">check_deep</a>() -> <a href="./src/axiora/types/health_check_deep_response.py">HealthCheckDeepResponse</a></code>

# Freshness

Types:

```python
from axiora.types import Meta, FreshnessRetrieveResponse
```

Methods:

- <code title="get /v1/freshness">client.freshness.<a href="./src/axiora/resources/freshness.py">retrieve</a>() -> <a href="./src/axiora/types/freshness_retrieve_response.py">FreshnessRetrieveResponse</a></code>

# Companies

Types:

```python
from axiora.types import (
    Company,
    Financial,
    Growth,
    GrowthMetrics,
    HealthScore,
    ListResponse,
    Peer,
    Ratio,
    CompanyRetrieveResponse,
    CompanyRetrieveFinancialsResponse,
    CompanyRetrieveGrowthResponse,
    CompanyRetrieveHealthResponse,
    CompanyRetrievePeersResponse,
    CompanyRetrieveRatiosResponse,
)
```

Methods:

- <code title="get /v1/companies/{code}">client.companies.<a href="./src/axiora/resources/companies.py">retrieve</a>(code, \*\*<a href="src/axiora/types/company_retrieve_params.py">params</a>) -> <a href="./src/axiora/types/company_retrieve_response.py">CompanyRetrieveResponse</a></code>
- <code title="get /v1/companies">client.companies.<a href="./src/axiora/resources/companies.py">list</a>(\*\*<a href="src/axiora/types/company_list_params.py">params</a>) -> <a href="./src/axiora/types/list_response.py">ListResponse</a></code>
- <code title="get /v1/companies/{code}/financials">client.companies.<a href="./src/axiora/resources/companies.py">retrieve_financials</a>(code, \*\*<a href="src/axiora/types/company_retrieve_financials_params.py">params</a>) -> <a href="./src/axiora/types/company_retrieve_financials_response.py">CompanyRetrieveFinancialsResponse</a></code>
- <code title="get /v1/companies/{code}/growth">client.companies.<a href="./src/axiora/resources/companies.py">retrieve_growth</a>(code, \*\*<a href="src/axiora/types/company_retrieve_growth_params.py">params</a>) -> <a href="./src/axiora/types/company_retrieve_growth_response.py">CompanyRetrieveGrowthResponse</a></code>
- <code title="get /v1/companies/{code}/health">client.companies.<a href="./src/axiora/resources/companies.py">retrieve_health</a>(code) -> <a href="./src/axiora/types/company_retrieve_health_response.py">CompanyRetrieveHealthResponse</a></code>
- <code title="get /v1/companies/{code}/peers">client.companies.<a href="./src/axiora/resources/companies.py">retrieve_peers</a>(code, \*\*<a href="src/axiora/types/company_retrieve_peers_params.py">params</a>) -> <a href="./src/axiora/types/company_retrieve_peers_response.py">CompanyRetrievePeersResponse</a></code>
- <code title="get /v1/companies/{code}/ratios">client.companies.<a href="./src/axiora/resources/companies.py">retrieve_ratios</a>(code, \*\*<a href="src/axiora/types/company_retrieve_ratios_params.py">params</a>) -> <a href="./src/axiora/types/company_retrieve_ratios_response.py">CompanyRetrieveRatiosResponse</a></code>
- <code title="get /v1/companies/search">client.companies.<a href="./src/axiora/resources/companies.py">search</a>(\*\*<a href="src/axiora/types/company_search_params.py">params</a>) -> <a href="./src/axiora/types/list_response.py">ListResponse</a></code>

# Filings

Types:

```python
from axiora.types import (
    Filing,
    Translation,
    FilingRetrieveResponse,
    FilingListResponse,
    FilingCalendarResponse,
    FilingRetrieveTranslationsResponse,
)
```

Methods:

- <code title="get /v1/filings/{doc_id}">client.filings.<a href="./src/axiora/resources/filings.py">retrieve</a>(doc_id) -> <a href="./src/axiora/types/filing_retrieve_response.py">FilingRetrieveResponse</a></code>
- <code title="get /v1/filings">client.filings.<a href="./src/axiora/resources/filings.py">list</a>(\*\*<a href="src/axiora/types/filing_list_params.py">params</a>) -> <a href="./src/axiora/types/filing_list_response.py">FilingListResponse</a></code>
- <code title="get /v1/filings/calendar">client.filings.<a href="./src/axiora/resources/filings.py">calendar</a>(\*\*<a href="src/axiora/types/filing_calendar_params.py">params</a>) -> <a href="./src/axiora/types/filing_calendar_response.py">FilingCalendarResponse</a></code>
- <code title="get /v1/filings/{doc_id}/translations">client.filings.<a href="./src/axiora/resources/filings.py">retrieve_translations</a>(doc_id, \*\*<a href="src/axiora/types/filing_retrieve_translations_params.py">params</a>) -> <a href="./src/axiora/types/filing_retrieve_translations_response.py">FilingRetrieveTranslationsResponse</a></code>

# Translations

Types:

```python
from axiora.types import TranslationSearchResponse
```

Methods:

- <code title="get /v1/translations/search">client.translations.<a href="./src/axiora/resources/translations.py">search</a>(\*\*<a href="src/axiora/types/translation_search_params.py">params</a>) -> <a href="./src/axiora/types/translation_search_response.py">TranslationSearchResponse</a></code>

# Screen

Types:

```python
from axiora.types import ScreenRetrieveResponse
```

Methods:

- <code title="get /v1/screen">client.screen.<a href="./src/axiora/resources/screen.py">retrieve</a>(\*\*<a href="src/axiora/types/screen_retrieve_params.py">params</a>) -> <a href="./src/axiora/types/screen_retrieve_response.py">ScreenRetrieveResponse</a></code>

# Rankings

Types:

```python
from axiora.types import RankingRetrieveResponse
```

Methods:

- <code title="get /v1/rankings/{metric}">client.rankings.<a href="./src/axiora/resources/rankings.py">retrieve</a>(metric, \*\*<a href="src/axiora/types/ranking_retrieve_params.py">params</a>) -> <a href="./src/axiora/types/ranking_retrieve_response.py">RankingRetrieveResponse</a></code>

# Sectors

Types:

```python
from axiora.types import SectorListResponse, SectorRetrieveStatsResponse
```

Methods:

- <code title="get /v1/sectors">client.sectors.<a href="./src/axiora/resources/sectors.py">list</a>() -> <a href="./src/axiora/types/sector_list_response.py">SectorListResponse</a></code>
- <code title="get /v1/sectors/{sector_name}">client.sectors.<a href="./src/axiora/resources/sectors.py">retrieve_stats</a>(sector_name, \*\*<a href="src/axiora/types/sector_retrieve_stats_params.py">params</a>) -> <a href="./src/axiora/types/sector_retrieve_stats_response.py">SectorRetrieveStatsResponse</a></code>

# Compare

Types:

```python
from axiora.types import CompareRetrieveResponse
```

Methods:

- <code title="get /v1/compare">client.compare.<a href="./src/axiora/resources/compare.py">retrieve</a>(\*\*<a href="src/axiora/types/compare_retrieve_params.py">params</a>) -> <a href="./src/axiora/types/compare_retrieve_response.py">CompareRetrieveResponse</a></code>

# Timeseries

Types:

```python
from axiora.types import TimeseryRetrieveResponse
```

Methods:

- <code title="get /v1/timeseries">client.timeseries.<a href="./src/axiora/resources/timeseries.py">retrieve</a>(\*\*<a href="src/axiora/types/timesery_retrieve_params.py">params</a>) -> <a href="./src/axiora/types/timesery_retrieve_response.py">TimeseryRetrieveResponse</a></code>

# Bulk

Types:

```python
from axiora.types import BulkExportFinancialsJsonResponse
```

Methods:

- <code title="get /v1/bulk/financials.csv">client.bulk.<a href="./src/axiora/resources/bulk.py">export_financials_csv</a>(\*\*<a href="src/axiora/types/bulk_export_financials_csv_params.py">params</a>) -> None</code>
- <code title="get /v1/bulk/financials.json">client.bulk.<a href="./src/axiora/resources/bulk.py">export_financials_json</a>(\*\*<a href="src/axiora/types/bulk_export_financials_json_params.py">params</a>) -> <a href="./src/axiora/types/bulk_export_financials_json_response.py">BulkExportFinancialsJsonResponse</a></code>

# Webhooks

Types:

```python
from axiora.types import DeletedOut, WebhookCreateResponse, WebhookListResponse
```

Methods:

- <code title="post /v1/webhooks">client.webhooks.<a href="./src/axiora/resources/webhooks.py">create</a>(\*\*<a href="src/axiora/types/webhook_create_params.py">params</a>) -> <a href="./src/axiora/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /v1/webhooks">client.webhooks.<a href="./src/axiora/resources/webhooks.py">list</a>() -> <a href="./src/axiora/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /v1/webhooks/{webhook_id}">client.webhooks.<a href="./src/axiora/resources/webhooks.py">delete</a>(webhook_id) -> <a href="./src/axiora/types/deleted_out.py">DeletedOut</a></code>

# Usage

Types:

```python
from axiora.types import UsageRetrieveResponse
```

Methods:

- <code title="get /v1/usage">client.usage.<a href="./src/axiora/resources/usage.py">retrieve</a>() -> <a href="./src/axiora/types/usage_retrieve_response.py">UsageRetrieveResponse</a></code>

# Keys

Types:

```python
from axiora.types import KeyResponse, KeyCreateResponse, KeyListResponse
```

Methods:

- <code title="post /v1/keys">client.keys.<a href="./src/axiora/resources/keys.py">create</a>(\*\*<a href="src/axiora/types/key_create_params.py">params</a>) -> <a href="./src/axiora/types/key_create_response.py">KeyCreateResponse</a></code>
- <code title="get /v1/keys">client.keys.<a href="./src/axiora/resources/keys.py">list</a>() -> <a href="./src/axiora/types/key_list_response.py">KeyListResponse</a></code>
- <code title="delete /v1/keys/{key_id}">client.keys.<a href="./src/axiora/resources/keys.py">delete</a>(key_id) -> <a href="./src/axiora/types/deleted_out.py">DeletedOut</a></code>

# Coverage

Types:

```python
from axiora.types import CoverageRetrieveResponse
```

Methods:

- <code title="get /v1/coverage">client.coverage.<a href="./src/axiora/resources/coverage.py">retrieve</a>() -> <a href="./src/axiora/types/coverage_retrieve_response.py">CoverageRetrieveResponse</a></code>
