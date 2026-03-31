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
    BoardMember,
    CapitalAllocation,
    Company,
    Financial,
    Growth,
    GrowthMetrics,
    HealthScore,
    ListResponseCompany,
    ListResponseFinancial,
    ListResponseSection,
    ListResponseShareholding,
    ListResponseVotingResult,
    Peer,
    Ratio,
    CompanyRetrieveResponse,
    CompanyGetBoardCompositionResponse,
    CompanyGetCapitalAllocationResponse,
    CompanyGetForecastsResponse,
    CompanyRetrieveGrowthResponse,
    CompanyRetrieveHealthResponse,
    CompanyRetrieveIdentifiersResponse,
    CompanyRetrievePeersResponse,
    CompanyRetrieveRatiosResponse,
)
```

Methods:

- <code title="get /v1/companies/{code}">client.companies.<a href="./src/axiora/resources/companies/companies.py">retrieve</a>(code, \*\*<a href="src/axiora/types/company_retrieve_params.py">params</a>) -> <a href="./src/axiora/types/company_retrieve_response.py">CompanyRetrieveResponse</a></code>
- <code title="get /v1/companies">client.companies.<a href="./src/axiora/resources/companies/companies.py">list</a>(\*\*<a href="src/axiora/types/company_list_params.py">params</a>) -> <a href="./src/axiora/types/list_response_company.py">ListResponseCompany</a></code>
- <code title="get /v1/companies/{code}/board">client.companies.<a href="./src/axiora/resources/companies/companies.py">get_board_composition</a>(code, \*\*<a href="src/axiora/types/company_get_board_composition_params.py">params</a>) -> <a href="./src/axiora/types/company_get_board_composition_response.py">CompanyGetBoardCompositionResponse</a></code>
- <code title="get /v1/companies/{code}/capital-allocation">client.companies.<a href="./src/axiora/resources/companies/companies.py">get_capital_allocation</a>(code) -> <a href="./src/axiora/types/company_get_capital_allocation_response.py">CompanyGetCapitalAllocationResponse</a></code>
- <code title="get /v1/companies/{code}/forecasts">client.companies.<a href="./src/axiora/resources/companies/companies.py">get_forecasts</a>(code, \*\*<a href="src/axiora/types/company_get_forecasts_params.py">params</a>) -> <a href="./src/axiora/types/company_get_forecasts_response.py">CompanyGetForecastsResponse</a></code>
- <code title="get /v1/companies/{code}/shareholdings">client.companies.<a href="./src/axiora/resources/companies/companies.py">list_shareholdings</a>(code, \*\*<a href="src/axiora/types/company_list_shareholdings_params.py">params</a>) -> <a href="./src/axiora/types/list_response_shareholding.py">ListResponseShareholding</a></code>
- <code title="get /v1/companies/{code}/voting">client.companies.<a href="./src/axiora/resources/companies/companies.py">list_voting_results</a>(code, \*\*<a href="src/axiora/types/company_list_voting_results_params.py">params</a>) -> <a href="./src/axiora/types/list_response_voting_result.py">ListResponseVotingResult</a></code>
- <code title="get /v1/companies/{code}/financials">client.companies.<a href="./src/axiora/resources/companies/companies.py">retrieve_financials</a>(code, \*\*<a href="src/axiora/types/company_retrieve_financials_params.py">params</a>) -> <a href="./src/axiora/types/list_response_financial.py">ListResponseFinancial</a></code>
- <code title="get /v1/companies/{code}/growth">client.companies.<a href="./src/axiora/resources/companies/companies.py">retrieve_growth</a>(code, \*\*<a href="src/axiora/types/company_retrieve_growth_params.py">params</a>) -> <a href="./src/axiora/types/company_retrieve_growth_response.py">CompanyRetrieveGrowthResponse</a></code>
- <code title="get /v1/companies/{code}/health">client.companies.<a href="./src/axiora/resources/companies/companies.py">retrieve_health</a>(code) -> <a href="./src/axiora/types/company_retrieve_health_response.py">CompanyRetrieveHealthResponse</a></code>
- <code title="get /v1/companies/{code}/identifiers">client.companies.<a href="./src/axiora/resources/companies/companies.py">retrieve_identifiers</a>(code) -> <a href="./src/axiora/types/company_retrieve_identifiers_response.py">CompanyRetrieveIdentifiersResponse</a></code>
- <code title="get /v1/companies/{code}/peers">client.companies.<a href="./src/axiora/resources/companies/companies.py">retrieve_peers</a>(code, \*\*<a href="src/axiora/types/company_retrieve_peers_params.py">params</a>) -> <a href="./src/axiora/types/company_retrieve_peers_response.py">CompanyRetrievePeersResponse</a></code>
- <code title="get /v1/companies/{code}/ratios">client.companies.<a href="./src/axiora/resources/companies/companies.py">retrieve_ratios</a>(code, \*\*<a href="src/axiora/types/company_retrieve_ratios_params.py">params</a>) -> <a href="./src/axiora/types/company_retrieve_ratios_response.py">CompanyRetrieveRatiosResponse</a></code>
- <code title="get /v1/companies/{code}/sections">client.companies.<a href="./src/axiora/resources/companies/companies.py">retrieve_sections</a>(code, \*\*<a href="src/axiora/types/company_retrieve_sections_params.py">params</a>) -> <a href="./src/axiora/types/list_response_section.py">ListResponseSection</a></code>
- <code title="get /v1/companies/search">client.companies.<a href="./src/axiora/resources/companies/companies.py">search</a>(\*\*<a href="src/axiora/types/company_search_params.py">params</a>) -> <a href="./src/axiora/types/list_response_company.py">ListResponseCompany</a></code>

## Buybacks

Types:

```python
from axiora.types.companies import BuybackListResponse, BuybackGetAnalysisResponse
```

Methods:

- <code title="get /v1/companies/{code}/buybacks">client.companies.buybacks.<a href="./src/axiora/resources/companies/buybacks.py">list</a>(code, \*\*<a href="src/axiora/types/companies/buyback_list_params.py">params</a>) -> <a href="./src/axiora/types/companies/buyback_list_response.py">BuybackListResponse</a></code>
- <code title="get /v1/companies/{code}/buybacks/analysis">client.companies.buybacks.<a href="./src/axiora/resources/companies/buybacks.py">get_analysis</a>(code) -> <a href="./src/axiora/types/companies/buyback_get_analysis_response.py">BuybackGetAnalysisResponse</a></code>

## Ownership

Types:

```python
from axiora.types.companies import (
    OwnershipGetChartResponse,
    OwnershipGetNetworkResponse,
    OwnershipListSignalsResponse,
)
```

Methods:

- <code title="get /v1/companies/{code}/ownership/chart">client.companies.ownership.<a href="./src/axiora/resources/companies/ownership/ownership.py">get_chart</a>(code) -> <a href="./src/axiora/types/companies/ownership_get_chart_response.py">OwnershipGetChartResponse</a></code>
- <code title="get /v1/companies/{code}/ownership/network">client.companies.ownership.<a href="./src/axiora/resources/companies/ownership/ownership.py">get_network</a>(code) -> <a href="./src/axiora/types/companies/ownership_get_network_response.py">OwnershipGetNetworkResponse</a></code>
- <code title="get /v1/companies/{code}/ownership/signals">client.companies.ownership.<a href="./src/axiora/resources/companies/ownership/ownership.py">list_signals</a>(code, \*\*<a href="src/axiora/types/companies/ownership_list_signals_params.py">params</a>) -> <a href="./src/axiora/types/companies/ownership_list_signals_response.py">OwnershipListSignalsResponse</a></code>

### Trajectories

Types:

```python
from axiora.types.companies.ownership import (
    TrajectoryListResponse,
    TrajectoryGetFilerTrajectoryResponse,
    TrajectoryGetProbabilitiesResponse,
)
```

Methods:

- <code title="get /v1/companies/{code}/ownership/trajectories">client.companies.ownership.trajectories.<a href="./src/axiora/resources/companies/ownership/trajectories.py">list</a>(code, \*\*<a href="src/axiora/types/companies/ownership/trajectory_list_params.py">params</a>) -> <a href="./src/axiora/types/companies/ownership/trajectory_list_response.py">TrajectoryListResponse</a></code>
- <code title="get /v1/companies/{code}/ownership/trajectories/{filer_code}">client.companies.ownership.trajectories.<a href="./src/axiora/resources/companies/ownership/trajectories.py">get_filer_trajectory</a>(filer_code, \*, code) -> <a href="./src/axiora/types/companies/ownership/trajectory_get_filer_trajectory_response.py">TrajectoryGetFilerTrajectoryResponse</a></code>
- <code title="get /v1/companies/{code}/ownership/trajectories/{filer_code}/probabilities">client.companies.ownership.trajectories.<a href="./src/axiora/resources/companies/ownership/trajectories.py">get_probabilities</a>(filer_code, \*, code) -> <a href="./src/axiora/types/companies/ownership/trajectory_get_probabilities_response.py">TrajectoryGetProbabilitiesResponse</a></code>

## Earnings

Types:

```python
from axiora.types.companies import (
    EarningGetEarningsResponse,
    EarningGetSignalsResponse,
    EarningGetSurpriseResponse,
)
```

Methods:

- <code title="get /v1/companies/{code}/earnings">client.companies.earnings.<a href="./src/axiora/resources/companies/earnings.py">get_earnings</a>(code, \*\*<a href="src/axiora/types/companies/earning_get_earnings_params.py">params</a>) -> <a href="./src/axiora/types/companies/earning_get_earnings_response.py">EarningGetEarningsResponse</a></code>
- <code title="get /v1/companies/{code}/earnings/signals">client.companies.earnings.<a href="./src/axiora/resources/companies/earnings.py">get_signals</a>(code, \*\*<a href="src/axiora/types/companies/earning_get_signals_params.py">params</a>) -> <a href="./src/axiora/types/companies/earning_get_signals_response.py">EarningGetSignalsResponse</a></code>
- <code title="get /v1/companies/{code}/earnings/surprise">client.companies.earnings.<a href="./src/axiora/resources/companies/earnings.py">get_surprise</a>(code) -> <a href="./src/axiora/types/companies/earning_get_surprise_response.py">EarningGetSurpriseResponse</a></code>

## Relationships

Types:

```python
from axiora.types.companies import (
    RelationshipGetRelationshipsResponse,
    RelationshipListInterlocksResponse,
)
```

Methods:

- <code title="get /v1/companies/{code}/relationships">client.companies.relationships.<a href="./src/axiora/resources/companies/relationships.py">get_relationships</a>(code, \*\*<a href="src/axiora/types/companies/relationship_get_relationships_params.py">params</a>) -> <a href="./src/axiora/types/companies/relationship_get_relationships_response.py">RelationshipGetRelationshipsResponse</a></code>
- <code title="get /v1/companies/{code}/relationships/interlocks">client.companies.relationships.<a href="./src/axiora/resources/companies/relationships.py">list_interlocks</a>(code, \*\*<a href="src/axiora/types/companies/relationship_list_interlocks_params.py">params</a>) -> <a href="./src/axiora/types/companies/relationship_list_interlocks_response.py">RelationshipListInterlocksResponse</a></code>

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
- <code title="get /v1/filings/{doc_id}/sections">client.filings.<a href="./src/axiora/resources/filings.py">retrieve_sections</a>(doc_id, \*\*<a href="src/axiora/types/filing_retrieve_sections_params.py">params</a>) -> <a href="./src/axiora/types/list_response_section.py">ListResponseSection</a></code>
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
- <code title="get /v1/bulk/ownership_signals.parquet">client.bulk.<a href="./src/axiora/resources/bulk.py">export_ownership_signals</a>() -> BinaryAPIResponse</code>
- <code title="get /v1/bulk/ownership_trajectories.parquet">client.bulk.<a href="./src/axiora/resources/bulk.py">export_ownership_trajectories</a>() -> BinaryAPIResponse</code>

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

# Batch

Methods:

- <code title="post /v1/batch/financials">client.batch.<a href="./src/axiora/resources/batch.py">fetch_financials</a>(\*\*<a href="src/axiora/types/batch_fetch_financials_params.py">params</a>) -> <a href="./src/axiora/types/list_response_financial.py">ListResponseFinancial</a></code>

# Waitlist

Types:

```python
from axiora.types import WaitlistJoinResponse
```

Methods:

- <code title="post /v1/waitlist">client.waitlist.<a href="./src/axiora/resources/waitlist.py">join</a>(\*\*<a href="src/axiora/types/waitlist_join_params.py">params</a>) -> <a href="./src/axiora/types/waitlist_join_response.py">WaitlistJoinResponse</a></code>

# Sections

Types:

```python
from axiora.types import SectionListAvailableResponse
```

Methods:

- <code title="get /v1/sections/available">client.sections.<a href="./src/axiora/resources/sections.py">list_available</a>() -> <a href="./src/axiora/types/section_list_available_response.py">SectionListAvailableResponse</a></code>

# Buybacks

Types:

```python
from axiora.types import BuybackListAccelerationsResponse, BuybackListLatestResponse
```

Methods:

- <code title="get /v1/buybacks/accelerations">client.buybacks.<a href="./src/axiora/resources/buybacks.py">list_accelerations</a>(\*\*<a href="src/axiora/types/buyback_list_accelerations_params.py">params</a>) -> <a href="./src/axiora/types/buyback_list_accelerations_response.py">BuybackListAccelerationsResponse</a></code>
- <code title="get /v1/buybacks/latest">client.buybacks.<a href="./src/axiora/resources/buybacks.py">list_latest</a>(\*\*<a href="src/axiora/types/buyback_list_latest_params.py">params</a>) -> <a href="./src/axiora/types/buyback_list_latest_response.py">BuybackListLatestResponse</a></code>

# Shareholdings

Methods:

- <code title="get /v1/shareholdings/latest">client.shareholdings.<a href="./src/axiora/resources/shareholdings.py">list_latest</a>(\*\*<a href="src/axiora/types/shareholding_list_latest_params.py">params</a>) -> <a href="./src/axiora/types/list_response_shareholding.py">ListResponseShareholding</a></code>

# Ownership

Types:

```python
from axiora.types import (
    OwnershipGetProbabilityTableResponse,
    OwnershipListActivistCampaignsResponse,
    OwnershipListCrossHoldingsResponse,
    OwnershipListMoversResponse,
    OwnershipListSignalsResponse,
    OwnershipListUnwindingScoreboardResponse,
)
```

Methods:

- <code title="get /v1/ownership/probability-table">client.ownership.<a href="./src/axiora/resources/ownership.py">get_probability_table</a>() -> <a href="./src/axiora/types/ownership_get_probability_table_response.py">OwnershipGetProbabilityTableResponse</a></code>
- <code title="get /v1/ownership/activist-campaigns">client.ownership.<a href="./src/axiora/resources/ownership.py">list_activist_campaigns</a>(\*\*<a href="src/axiora/types/ownership_list_activist_campaigns_params.py">params</a>) -> <a href="./src/axiora/types/ownership_list_activist_campaigns_response.py">OwnershipListActivistCampaignsResponse</a></code>
- <code title="get /v1/ownership/cross-holdings">client.ownership.<a href="./src/axiora/resources/ownership.py">list_cross_holdings</a>(\*\*<a href="src/axiora/types/ownership_list_cross_holdings_params.py">params</a>) -> <a href="./src/axiora/types/ownership_list_cross_holdings_response.py">OwnershipListCrossHoldingsResponse</a></code>
- <code title="get /v1/ownership/movers">client.ownership.<a href="./src/axiora/resources/ownership.py">list_movers</a>(\*\*<a href="src/axiora/types/ownership_list_movers_params.py">params</a>) -> <a href="./src/axiora/types/ownership_list_movers_response.py">OwnershipListMoversResponse</a></code>
- <code title="get /v1/ownership/signals">client.ownership.<a href="./src/axiora/resources/ownership.py">list_signals</a>(\*\*<a href="src/axiora/types/ownership_list_signals_params.py">params</a>) -> <a href="./src/axiora/types/ownership_list_signals_response.py">OwnershipListSignalsResponse</a></code>
- <code title="get /v1/ownership/unwinding-scoreboard">client.ownership.<a href="./src/axiora/resources/ownership.py">list_unwinding_scoreboard</a>(\*\*<a href="src/axiora/types/ownership_list_unwinding_scoreboard_params.py">params</a>) -> <a href="./src/axiora/types/ownership_list_unwinding_scoreboard_response.py">OwnershipListUnwindingScoreboardResponse</a></code>

# CapitalAllocation

Types:

```python
from axiora.types import CapitalAllocationListRankingResponse
```

Methods:

- <code title="get /v1/capital-allocation/ranking">client.capital_allocation.<a href="./src/axiora/resources/capital_allocation.py">list_ranking</a>(\*\*<a href="src/axiora/types/capital_allocation_list_ranking_params.py">params</a>) -> <a href="./src/axiora/types/capital_allocation_list_ranking_response.py">CapitalAllocationListRankingResponse</a></code>

# Voting

Methods:

- <code title="get /v1/voting/recent">client.voting.<a href="./src/axiora/resources/voting.py">list_recent</a>(\*\*<a href="src/axiora/types/voting_list_recent_params.py">params</a>) -> <a href="./src/axiora/types/list_response_voting_result.py">ListResponseVotingResult</a></code>

# Earnings

Types:

```python
from axiora.types import EarningListSignalsResponse, EarningRetrieveLatestResponse
```

Methods:

- <code title="get /v1/earnings/signals">client.earnings.<a href="./src/axiora/resources/earnings.py">list_signals</a>(\*\*<a href="src/axiora/types/earning_list_signals_params.py">params</a>) -> <a href="./src/axiora/types/earning_list_signals_response.py">EarningListSignalsResponse</a></code>
- <code title="get /v1/earnings/latest">client.earnings.<a href="./src/axiora/resources/earnings.py">retrieve_latest</a>(\*\*<a href="src/axiora/types/earning_retrieve_latest_params.py">params</a>) -> <a href="./src/axiora/types/earning_retrieve_latest_response.py">EarningRetrieveLatestResponse</a></code>

# Investors

Types:

```python
from axiora.types import InvestorRetrievePositionsResponse, InvestorSearchResponse
```

Methods:

- <code title="get /v1/investors/{code}/positions">client.investors.<a href="./src/axiora/resources/investors.py">retrieve_positions</a>(code, \*\*<a href="src/axiora/types/investor_retrieve_positions_params.py">params</a>) -> <a href="./src/axiora/types/investor_retrieve_positions_response.py">InvestorRetrievePositionsResponse</a></code>
- <code title="get /v1/investors/search">client.investors.<a href="./src/axiora/resources/investors.py">search</a>(\*\*<a href="src/axiora/types/investor_search_params.py">params</a>) -> <a href="./src/axiora/types/investor_search_response.py">InvestorSearchResponse</a></code>

# Watchlist

Types:

```python
from axiora.types import WatchlistListResponse, WatchlistAddResponse, WatchlistRemoveResponse
```

Methods:

- <code title="get /v1/watchlist">client.watchlist.<a href="./src/axiora/resources/watchlist.py">list</a>() -> <a href="./src/axiora/types/watchlist_list_response.py">WatchlistListResponse</a></code>
- <code title="post /v1/watchlist">client.watchlist.<a href="./src/axiora/resources/watchlist.py">add</a>(\*\*<a href="src/axiora/types/watchlist_add_params.py">params</a>) -> <a href="./src/axiora/types/watchlist_add_response.py">WatchlistAddResponse</a></code>
- <code title="delete /v1/watchlist/{item_id}">client.watchlist.<a href="./src/axiora/resources/watchlist.py">remove</a>(item_id) -> <a href="./src/axiora/types/watchlist_remove_response.py">WatchlistRemoveResponse</a></code>

# Relationships

Types:

```python
from axiora.types import RelationshipListInterlocksResponse
```

Methods:

- <code title="get /v1/relationships/interlocks">client.relationships.<a href="./src/axiora/resources/relationships.py">list_interlocks</a>(\*\*<a href="src/axiora/types/relationship_list_interlocks_params.py">params</a>) -> <a href="./src/axiora/types/relationship_list_interlocks_response.py">RelationshipListInterlocksResponse</a></code>

# WellKnown

Methods:

- <code title="get /.well-known/oauth-authorization-server">client.well_known.<a href="./src/axiora/resources/well_known/well_known.py">retrieve_authorization_server_metadata</a>() -> object</code>
- <code title="get /.well-known/oauth-protected-resource">client.well_known.<a href="./src/axiora/resources/well_known/well_known.py">retrieve_protected_resource_metadata</a>() -> object</code>

## Mcp

Methods:

- <code title="get /.well-known/mcp/server-card.json">client.well_known.mcp.<a href="./src/axiora/resources/well_known/mcp.py">retrieve_server_card</a>() -> object</code>

# OAuth

Methods:

- <code title="post /oauth/token">client.oauth.<a href="./src/axiora/resources/oauth/oauth.py">exchange_token</a>() -> object</code>

## Authorize

Types:

```python
from axiora.types.oauth import AuthorizeShowResponse
```

Methods:

- <code title="get /oauth/authorize">client.oauth.authorize.<a href="./src/axiora/resources/oauth/authorize.py">show</a>(\*\*<a href="src/axiora/types/oauth/authorize_show_params.py">params</a>) -> str</code>
- <code title="post /oauth/authorize">client.oauth.authorize.<a href="./src/axiora/resources/oauth/authorize.py">validate</a>(\*\*<a href="src/axiora/types/oauth/authorize_validate_params.py">params</a>) -> object</code>
