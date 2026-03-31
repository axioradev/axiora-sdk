# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date, datetime

import httpx

from ...types import (
    company_list_params,
    company_search_params,
    company_retrieve_params,
    company_get_forecasts_params,
    company_retrieve_peers_params,
    company_retrieve_growth_params,
    company_retrieve_ratios_params,
    company_retrieve_sections_params,
    company_list_shareholdings_params,
    company_list_voting_results_params,
    company_retrieve_financials_params,
    company_get_board_composition_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .buybacks import (
    BuybacksResource,
    AsyncBuybacksResource,
    BuybacksResourceWithRawResponse,
    AsyncBuybacksResourceWithRawResponse,
    BuybacksResourceWithStreamingResponse,
    AsyncBuybacksResourceWithStreamingResponse,
)
from .earnings import (
    EarningsResource,
    AsyncEarningsResource,
    EarningsResourceWithRawResponse,
    AsyncEarningsResourceWithRawResponse,
    EarningsResourceWithStreamingResponse,
    AsyncEarningsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .relationships import (
    RelationshipsResource,
    AsyncRelationshipsResource,
    RelationshipsResourceWithRawResponse,
    AsyncRelationshipsResourceWithRawResponse,
    RelationshipsResourceWithStreamingResponse,
    AsyncRelationshipsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .ownership.ownership import (
    OwnershipResource,
    AsyncOwnershipResource,
    OwnershipResourceWithRawResponse,
    AsyncOwnershipResourceWithRawResponse,
    OwnershipResourceWithStreamingResponse,
    AsyncOwnershipResourceWithStreamingResponse,
)
from ...types.list_response_company import ListResponseCompany
from ...types.list_response_section import ListResponseSection
from ...types.list_response_financial import ListResponseFinancial
from ...types.company_retrieve_response import CompanyRetrieveResponse
from ...types.list_response_shareholding import ListResponseShareholding
from ...types.list_response_voting_result import ListResponseVotingResult
from ...types.company_get_forecasts_response import CompanyGetForecastsResponse
from ...types.company_retrieve_peers_response import CompanyRetrievePeersResponse
from ...types.company_retrieve_growth_response import CompanyRetrieveGrowthResponse
from ...types.company_retrieve_health_response import CompanyRetrieveHealthResponse
from ...types.company_retrieve_ratios_response import CompanyRetrieveRatiosResponse
from ...types.company_retrieve_identifiers_response import CompanyRetrieveIdentifiersResponse
from ...types.company_get_board_composition_response import CompanyGetBoardCompositionResponse
from ...types.company_get_capital_allocation_response import CompanyGetCapitalAllocationResponse

__all__ = ["CompaniesResource", "AsyncCompaniesResource"]


class CompaniesResource(SyncAPIResource):
    @cached_property
    def buybacks(self) -> BuybacksResource:
        return BuybacksResource(self._client)

    @cached_property
    def ownership(self) -> OwnershipResource:
        return OwnershipResource(self._client)

    @cached_property
    def earnings(self) -> EarningsResource:
        return EarningsResource(self._client)

    @cached_property
    def relationships(self) -> RelationshipsResource:
        return RelationshipsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return CompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return CompaniesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        code: str,
        *,
        expand: Optional[str] | Omit = omit,
        peer_limit: int | Omit = omit,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveResponse:
        """
        Get Company

        Args:
          expand: Comma-separated sub-resources to include: financials, ratios, growth, peers,
              segments, translations, health_score. Use 'all' for everything.

          peer_limit: Max peers to return (default 10)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "peer_limit": peer_limit,
                        "years": years,
                    },
                    company_retrieve_params.CompanyRetrieveParams,
                ),
            ),
            cast_to=CompanyRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        name: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        sector: Optional[str] | Omit = omit,
        securities_code: Optional[str] | Omit = omit,
        since: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseCompany:
        """
        List Companies

        Args:
          cursor: Opaque cursor for keyset pagination

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          since: Return companies updated after this timestamp (ISO 8601). Use the sync_token
              from a previous response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/companies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "sector": sector,
                        "securities_code": securities_code,
                        "since": since,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            cast_to=ListResponseCompany,
        )

    def get_board_composition(
        self,
        code: str,
        *,
        fiscal_year: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyGetBoardCompositionResponse:
        """
        Get board composition and officer list for a company.

        Returns directors, auditors, and executive officers with outside/independent
        status, gender breakdown, and shares held.

        Args:
          fiscal_year: Fiscal year. Defaults to latest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/board", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"fiscal_year": fiscal_year}, company_get_board_composition_params.CompanyGetBoardCompositionParams
                ),
            ),
            cast_to=CompanyGetBoardCompositionResponse,
        )

    def get_capital_allocation(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyGetCapitalAllocationResponse:
        """
        Get capital allocation classification for a company.

        Args:
          code: Securities or EDINET code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/capital-allocation", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyGetCapitalAllocationResponse,
        )

    def get_forecasts(
        self,
        code: str,
        *,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyGetForecastsResponse:
        """
        Get management earnings forecasts (業績予想) for a company.

        Extracted from 決算短信 XBRL — the forward guidance management provides
        alongside their earnings release. Only returns snapshots that contain at least
        one forecast field.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/forecasts", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"years": years}, company_get_forecasts_params.CompanyGetForecastsParams),
            ),
            cast_to=CompanyGetForecastsResponse,
        )

    def list_shareholdings(
        self,
        code: str,
        *,
        cursor: Optional[str] | Omit = omit,
        date_from: Union[str, date, None] | Omit = omit,
        date_to: Union[str, date, None] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        report_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseShareholding:
        """
        Get large shareholding reports filed about this company (as issuer).

        Returns reports from investors who hold ≥5% of the company's shares. Shows
        combined totals by default (holder_index=0 rows).

        Args:
          code: Securities code (e.g. '7203') or EDINET code (e.g. 'E02144') of the issuer
              (target company)

          cursor: Opaque cursor for keyset pagination

          date_from: Filter: base date on or after (YYYY-MM-DD)

          date_to: Filter: base date on or before (YYYY-MM-DD)

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          report_type: Filter by report type: 'initial', 'amendment', or 'correction'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/shareholdings", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "date_from": date_from,
                        "date_to": date_to,
                        "limit": limit,
                        "offset": offset,
                        "report_type": report_type,
                    },
                    company_list_shareholdings_params.CompanyListShareholdingsParams,
                ),
            ),
            cast_to=ListResponseShareholding,
        )

    def list_voting_results(
        self,
        code: str,
        *,
        cursor: Optional[str] | Omit = omit,
        fiscal_year: Optional[int] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseVotingResult:
        """
        Get AGM voting results for a company.

        Returns per-proposal voting data including votes for/against/abstain, approval
        percentages, and outcomes. Director elections include per-candidate breakdowns.

        Args:
          code: EDINET code (e.g. 'E02144') or securities code (e.g. '7203')

          cursor: Opaque cursor for keyset pagination

          fiscal_year: Filter by fiscal year

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/voting", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "fiscal_year": fiscal_year,
                        "limit": limit,
                        "offset": offset,
                    },
                    company_list_voting_results_params.CompanyListVotingResultsParams,
                ),
            ),
            cast_to=ListResponseVotingResult,
        )

    def retrieve_financials(
        self,
        code: str,
        *,
        doc_type: str | Omit = omit,
        fields: Optional[str] | Omit = omit,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseFinancial:
        """
        Get Financials

        Args:
          doc_type: Filing type: 120 (annual), 130 (semi-annual), 140 (quarterly)

          fields: Comma-separated field names

          years: Number of fiscal years

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/financials", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "doc_type": doc_type,
                        "fields": fields,
                        "years": years,
                    },
                    company_retrieve_financials_params.CompanyRetrieveFinancialsParams,
                ),
            ),
            cast_to=ListResponseFinancial,
        )

    def retrieve_growth(
        self,
        code: str,
        *,
        split_adjusted: bool | Omit = omit,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveGrowthResponse:
        """
        Year-over-year growth rates and multi-year CAGRs.

        Args:
          split_adjusted: Adjust EPS for detected stock splits before computing growth. Set to false for
              raw unadjusted values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/growth", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "split_adjusted": split_adjusted,
                        "years": years,
                    },
                    company_retrieve_growth_params.CompanyRetrieveGrowthParams,
                ),
            ),
            cast_to=CompanyRetrieveGrowthResponse,
        )

    def retrieve_health(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveHealthResponse:
        """
        Get the health/credit score (0-100) for a company.

        Returns a transparent score with component breakdown, flags, and industry
        adjustment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/health", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRetrieveHealthResponse,
        )

    def retrieve_identifiers(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveIdentifiersResponse:
        """
        Get cross-reference identifiers (ISIN, LEI, Bloomberg ticker, etc.) for a
        company.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/identifiers", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRetrieveIdentifiersResponse,
        )

    def retrieve_peers(
        self,
        code: str,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrievePeersResponse:
        """
        Find peer companies (same sector, similar revenue size).

        Returns companies in the same sector, ordered by closest revenue to the target
        company.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/peers", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, company_retrieve_peers_params.CompanyRetrievePeersParams),
            ),
            cast_to=CompanyRetrievePeersResponse,
        )

    def retrieve_ratios(
        self,
        code: str,
        *,
        split_adjusted: bool | Omit = omit,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveRatiosResponse:
        """
        Computed financial ratios for a company over time.

        Args:
          split_adjusted: Adjust per-share values (EPS, BPS, DPS) for detected stock splits so the
              time-series is comparable. Set to false for raw unadjusted values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/ratios", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "split_adjusted": split_adjusted,
                        "years": years,
                    },
                    company_retrieve_ratios_params.CompanyRetrieveRatiosParams,
                ),
            ),
            cast_to=CompanyRetrieveRatiosResponse,
        )

    def retrieve_sections(
        self,
        code: str,
        *,
        fiscal_year: Optional[int] | Omit = omit,
        section: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseSection:
        """
        Get text sections from a company's annual filing.

        Returns the full Japanese text of each section, with English translations where
        available. No truncation.

        Args:
          fiscal_year: Fiscal year. Defaults to latest.

          section: Filter by section key. One of: mda, risk_factors, business_overview, strategy,
              sustainability, research_and_development, dividend_policy, governance,
              company_history, employees, critical_contracts, capital_expenditures,
              accounting_policy, segment_info, financial_instruments, officers,
              outside_directors, remuneration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/sections", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fiscal_year": fiscal_year,
                        "section": section,
                    },
                    company_retrieve_sections_params.CompanyRetrieveSectionsParams,
                ),
            ),
            cast_to=ListResponseSection,
        )

    def search(
        self,
        *,
        q: str,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseCompany:
        """
        Search companies by name, securities code, or EDINET code.

        Returns results ranked by match quality: exact code matches first, then prefix
        matches, then substring matches.

        Args:
          q: Search query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/companies/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                    },
                    company_search_params.CompanySearchParams,
                ),
            ),
            cast_to=ListResponseCompany,
        )


class AsyncCompaniesResource(AsyncAPIResource):
    @cached_property
    def buybacks(self) -> AsyncBuybacksResource:
        return AsyncBuybacksResource(self._client)

    @cached_property
    def ownership(self) -> AsyncOwnershipResource:
        return AsyncOwnershipResource(self._client)

    @cached_property
    def earnings(self) -> AsyncEarningsResource:
        return AsyncEarningsResource(self._client)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResource:
        return AsyncRelationshipsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncCompaniesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        code: str,
        *,
        expand: Optional[str] | Omit = omit,
        peer_limit: int | Omit = omit,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveResponse:
        """
        Get Company

        Args:
          expand: Comma-separated sub-resources to include: financials, ratios, growth, peers,
              segments, translations, health_score. Use 'all' for everything.

          peer_limit: Max peers to return (default 10)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expand": expand,
                        "peer_limit": peer_limit,
                        "years": years,
                    },
                    company_retrieve_params.CompanyRetrieveParams,
                ),
            ),
            cast_to=CompanyRetrieveResponse,
        )

    async def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        name: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        sector: Optional[str] | Omit = omit,
        securities_code: Optional[str] | Omit = omit,
        since: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseCompany:
        """
        List Companies

        Args:
          cursor: Opaque cursor for keyset pagination

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          since: Return companies updated after this timestamp (ISO 8601). Use the sync_token
              from a previous response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/companies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "sector": sector,
                        "securities_code": securities_code,
                        "since": since,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            cast_to=ListResponseCompany,
        )

    async def get_board_composition(
        self,
        code: str,
        *,
        fiscal_year: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyGetBoardCompositionResponse:
        """
        Get board composition and officer list for a company.

        Returns directors, auditors, and executive officers with outside/independent
        status, gender breakdown, and shares held.

        Args:
          fiscal_year: Fiscal year. Defaults to latest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/board", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"fiscal_year": fiscal_year}, company_get_board_composition_params.CompanyGetBoardCompositionParams
                ),
            ),
            cast_to=CompanyGetBoardCompositionResponse,
        )

    async def get_capital_allocation(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyGetCapitalAllocationResponse:
        """
        Get capital allocation classification for a company.

        Args:
          code: Securities or EDINET code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/capital-allocation", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyGetCapitalAllocationResponse,
        )

    async def get_forecasts(
        self,
        code: str,
        *,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyGetForecastsResponse:
        """
        Get management earnings forecasts (業績予想) for a company.

        Extracted from 決算短信 XBRL — the forward guidance management provides
        alongside their earnings release. Only returns snapshots that contain at least
        one forecast field.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/forecasts", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"years": years}, company_get_forecasts_params.CompanyGetForecastsParams
                ),
            ),
            cast_to=CompanyGetForecastsResponse,
        )

    async def list_shareholdings(
        self,
        code: str,
        *,
        cursor: Optional[str] | Omit = omit,
        date_from: Union[str, date, None] | Omit = omit,
        date_to: Union[str, date, None] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        report_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseShareholding:
        """
        Get large shareholding reports filed about this company (as issuer).

        Returns reports from investors who hold ≥5% of the company's shares. Shows
        combined totals by default (holder_index=0 rows).

        Args:
          code: Securities code (e.g. '7203') or EDINET code (e.g. 'E02144') of the issuer
              (target company)

          cursor: Opaque cursor for keyset pagination

          date_from: Filter: base date on or after (YYYY-MM-DD)

          date_to: Filter: base date on or before (YYYY-MM-DD)

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          report_type: Filter by report type: 'initial', 'amendment', or 'correction'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/shareholdings", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "date_from": date_from,
                        "date_to": date_to,
                        "limit": limit,
                        "offset": offset,
                        "report_type": report_type,
                    },
                    company_list_shareholdings_params.CompanyListShareholdingsParams,
                ),
            ),
            cast_to=ListResponseShareholding,
        )

    async def list_voting_results(
        self,
        code: str,
        *,
        cursor: Optional[str] | Omit = omit,
        fiscal_year: Optional[int] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseVotingResult:
        """
        Get AGM voting results for a company.

        Returns per-proposal voting data including votes for/against/abstain, approval
        percentages, and outcomes. Director elections include per-candidate breakdowns.

        Args:
          code: EDINET code (e.g. 'E02144') or securities code (e.g. '7203')

          cursor: Opaque cursor for keyset pagination

          fiscal_year: Filter by fiscal year

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/voting", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "fiscal_year": fiscal_year,
                        "limit": limit,
                        "offset": offset,
                    },
                    company_list_voting_results_params.CompanyListVotingResultsParams,
                ),
            ),
            cast_to=ListResponseVotingResult,
        )

    async def retrieve_financials(
        self,
        code: str,
        *,
        doc_type: str | Omit = omit,
        fields: Optional[str] | Omit = omit,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseFinancial:
        """
        Get Financials

        Args:
          doc_type: Filing type: 120 (annual), 130 (semi-annual), 140 (quarterly)

          fields: Comma-separated field names

          years: Number of fiscal years

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/financials", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "doc_type": doc_type,
                        "fields": fields,
                        "years": years,
                    },
                    company_retrieve_financials_params.CompanyRetrieveFinancialsParams,
                ),
            ),
            cast_to=ListResponseFinancial,
        )

    async def retrieve_growth(
        self,
        code: str,
        *,
        split_adjusted: bool | Omit = omit,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveGrowthResponse:
        """
        Year-over-year growth rates and multi-year CAGRs.

        Args:
          split_adjusted: Adjust EPS for detected stock splits before computing growth. Set to false for
              raw unadjusted values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/growth", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "split_adjusted": split_adjusted,
                        "years": years,
                    },
                    company_retrieve_growth_params.CompanyRetrieveGrowthParams,
                ),
            ),
            cast_to=CompanyRetrieveGrowthResponse,
        )

    async def retrieve_health(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveHealthResponse:
        """
        Get the health/credit score (0-100) for a company.

        Returns a transparent score with component breakdown, flags, and industry
        adjustment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/health", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRetrieveHealthResponse,
        )

    async def retrieve_identifiers(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveIdentifiersResponse:
        """
        Get cross-reference identifiers (ISIN, LEI, Bloomberg ticker, etc.) for a
        company.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/identifiers", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRetrieveIdentifiersResponse,
        )

    async def retrieve_peers(
        self,
        code: str,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrievePeersResponse:
        """
        Find peer companies (same sector, similar revenue size).

        Returns companies in the same sector, ordered by closest revenue to the target
        company.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/peers", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit}, company_retrieve_peers_params.CompanyRetrievePeersParams
                ),
            ),
            cast_to=CompanyRetrievePeersResponse,
        )

    async def retrieve_ratios(
        self,
        code: str,
        *,
        split_adjusted: bool | Omit = omit,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveRatiosResponse:
        """
        Computed financial ratios for a company over time.

        Args:
          split_adjusted: Adjust per-share values (EPS, BPS, DPS) for detected stock splits so the
              time-series is comparable. Set to false for raw unadjusted values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/ratios", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "split_adjusted": split_adjusted,
                        "years": years,
                    },
                    company_retrieve_ratios_params.CompanyRetrieveRatiosParams,
                ),
            ),
            cast_to=CompanyRetrieveRatiosResponse,
        )

    async def retrieve_sections(
        self,
        code: str,
        *,
        fiscal_year: Optional[int] | Omit = omit,
        section: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseSection:
        """
        Get text sections from a company's annual filing.

        Returns the full Japanese text of each section, with English translations where
        available. No truncation.

        Args:
          fiscal_year: Fiscal year. Defaults to latest.

          section: Filter by section key. One of: mda, risk_factors, business_overview, strategy,
              sustainability, research_and_development, dividend_policy, governance,
              company_history, employees, critical_contracts, capital_expenditures,
              accounting_policy, segment_info, financial_instruments, officers,
              outside_directors, remuneration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/sections", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fiscal_year": fiscal_year,
                        "section": section,
                    },
                    company_retrieve_sections_params.CompanyRetrieveSectionsParams,
                ),
            ),
            cast_to=ListResponseSection,
        )

    async def search(
        self,
        *,
        q: str,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseCompany:
        """
        Search companies by name, securities code, or EDINET code.

        Returns results ranked by match quality: exact code matches first, then prefix
        matches, then substring matches.

        Args:
          q: Search query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/companies/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                    },
                    company_search_params.CompanySearchParams,
                ),
            ),
            cast_to=ListResponseCompany,
        )


class CompaniesResourceWithRawResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.retrieve = to_raw_response_wrapper(
            companies.retrieve,
        )
        self.list = to_raw_response_wrapper(
            companies.list,
        )
        self.get_board_composition = to_raw_response_wrapper(
            companies.get_board_composition,
        )
        self.get_capital_allocation = to_raw_response_wrapper(
            companies.get_capital_allocation,
        )
        self.get_forecasts = to_raw_response_wrapper(
            companies.get_forecasts,
        )
        self.list_shareholdings = to_raw_response_wrapper(
            companies.list_shareholdings,
        )
        self.list_voting_results = to_raw_response_wrapper(
            companies.list_voting_results,
        )
        self.retrieve_financials = to_raw_response_wrapper(
            companies.retrieve_financials,
        )
        self.retrieve_growth = to_raw_response_wrapper(
            companies.retrieve_growth,
        )
        self.retrieve_health = to_raw_response_wrapper(
            companies.retrieve_health,
        )
        self.retrieve_identifiers = to_raw_response_wrapper(
            companies.retrieve_identifiers,
        )
        self.retrieve_peers = to_raw_response_wrapper(
            companies.retrieve_peers,
        )
        self.retrieve_ratios = to_raw_response_wrapper(
            companies.retrieve_ratios,
        )
        self.retrieve_sections = to_raw_response_wrapper(
            companies.retrieve_sections,
        )
        self.search = to_raw_response_wrapper(
            companies.search,
        )

    @cached_property
    def buybacks(self) -> BuybacksResourceWithRawResponse:
        return BuybacksResourceWithRawResponse(self._companies.buybacks)

    @cached_property
    def ownership(self) -> OwnershipResourceWithRawResponse:
        return OwnershipResourceWithRawResponse(self._companies.ownership)

    @cached_property
    def earnings(self) -> EarningsResourceWithRawResponse:
        return EarningsResourceWithRawResponse(self._companies.earnings)

    @cached_property
    def relationships(self) -> RelationshipsResourceWithRawResponse:
        return RelationshipsResourceWithRawResponse(self._companies.relationships)


class AsyncCompaniesResourceWithRawResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.retrieve = async_to_raw_response_wrapper(
            companies.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            companies.list,
        )
        self.get_board_composition = async_to_raw_response_wrapper(
            companies.get_board_composition,
        )
        self.get_capital_allocation = async_to_raw_response_wrapper(
            companies.get_capital_allocation,
        )
        self.get_forecasts = async_to_raw_response_wrapper(
            companies.get_forecasts,
        )
        self.list_shareholdings = async_to_raw_response_wrapper(
            companies.list_shareholdings,
        )
        self.list_voting_results = async_to_raw_response_wrapper(
            companies.list_voting_results,
        )
        self.retrieve_financials = async_to_raw_response_wrapper(
            companies.retrieve_financials,
        )
        self.retrieve_growth = async_to_raw_response_wrapper(
            companies.retrieve_growth,
        )
        self.retrieve_health = async_to_raw_response_wrapper(
            companies.retrieve_health,
        )
        self.retrieve_identifiers = async_to_raw_response_wrapper(
            companies.retrieve_identifiers,
        )
        self.retrieve_peers = async_to_raw_response_wrapper(
            companies.retrieve_peers,
        )
        self.retrieve_ratios = async_to_raw_response_wrapper(
            companies.retrieve_ratios,
        )
        self.retrieve_sections = async_to_raw_response_wrapper(
            companies.retrieve_sections,
        )
        self.search = async_to_raw_response_wrapper(
            companies.search,
        )

    @cached_property
    def buybacks(self) -> AsyncBuybacksResourceWithRawResponse:
        return AsyncBuybacksResourceWithRawResponse(self._companies.buybacks)

    @cached_property
    def ownership(self) -> AsyncOwnershipResourceWithRawResponse:
        return AsyncOwnershipResourceWithRawResponse(self._companies.ownership)

    @cached_property
    def earnings(self) -> AsyncEarningsResourceWithRawResponse:
        return AsyncEarningsResourceWithRawResponse(self._companies.earnings)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResourceWithRawResponse:
        return AsyncRelationshipsResourceWithRawResponse(self._companies.relationships)


class CompaniesResourceWithStreamingResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.retrieve = to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            companies.list,
        )
        self.get_board_composition = to_streamed_response_wrapper(
            companies.get_board_composition,
        )
        self.get_capital_allocation = to_streamed_response_wrapper(
            companies.get_capital_allocation,
        )
        self.get_forecasts = to_streamed_response_wrapper(
            companies.get_forecasts,
        )
        self.list_shareholdings = to_streamed_response_wrapper(
            companies.list_shareholdings,
        )
        self.list_voting_results = to_streamed_response_wrapper(
            companies.list_voting_results,
        )
        self.retrieve_financials = to_streamed_response_wrapper(
            companies.retrieve_financials,
        )
        self.retrieve_growth = to_streamed_response_wrapper(
            companies.retrieve_growth,
        )
        self.retrieve_health = to_streamed_response_wrapper(
            companies.retrieve_health,
        )
        self.retrieve_identifiers = to_streamed_response_wrapper(
            companies.retrieve_identifiers,
        )
        self.retrieve_peers = to_streamed_response_wrapper(
            companies.retrieve_peers,
        )
        self.retrieve_ratios = to_streamed_response_wrapper(
            companies.retrieve_ratios,
        )
        self.retrieve_sections = to_streamed_response_wrapper(
            companies.retrieve_sections,
        )
        self.search = to_streamed_response_wrapper(
            companies.search,
        )

    @cached_property
    def buybacks(self) -> BuybacksResourceWithStreamingResponse:
        return BuybacksResourceWithStreamingResponse(self._companies.buybacks)

    @cached_property
    def ownership(self) -> OwnershipResourceWithStreamingResponse:
        return OwnershipResourceWithStreamingResponse(self._companies.ownership)

    @cached_property
    def earnings(self) -> EarningsResourceWithStreamingResponse:
        return EarningsResourceWithStreamingResponse(self._companies.earnings)

    @cached_property
    def relationships(self) -> RelationshipsResourceWithStreamingResponse:
        return RelationshipsResourceWithStreamingResponse(self._companies.relationships)


class AsyncCompaniesResourceWithStreamingResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.retrieve = async_to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            companies.list,
        )
        self.get_board_composition = async_to_streamed_response_wrapper(
            companies.get_board_composition,
        )
        self.get_capital_allocation = async_to_streamed_response_wrapper(
            companies.get_capital_allocation,
        )
        self.get_forecasts = async_to_streamed_response_wrapper(
            companies.get_forecasts,
        )
        self.list_shareholdings = async_to_streamed_response_wrapper(
            companies.list_shareholdings,
        )
        self.list_voting_results = async_to_streamed_response_wrapper(
            companies.list_voting_results,
        )
        self.retrieve_financials = async_to_streamed_response_wrapper(
            companies.retrieve_financials,
        )
        self.retrieve_growth = async_to_streamed_response_wrapper(
            companies.retrieve_growth,
        )
        self.retrieve_health = async_to_streamed_response_wrapper(
            companies.retrieve_health,
        )
        self.retrieve_identifiers = async_to_streamed_response_wrapper(
            companies.retrieve_identifiers,
        )
        self.retrieve_peers = async_to_streamed_response_wrapper(
            companies.retrieve_peers,
        )
        self.retrieve_ratios = async_to_streamed_response_wrapper(
            companies.retrieve_ratios,
        )
        self.retrieve_sections = async_to_streamed_response_wrapper(
            companies.retrieve_sections,
        )
        self.search = async_to_streamed_response_wrapper(
            companies.search,
        )

    @cached_property
    def buybacks(self) -> AsyncBuybacksResourceWithStreamingResponse:
        return AsyncBuybacksResourceWithStreamingResponse(self._companies.buybacks)

    @cached_property
    def ownership(self) -> AsyncOwnershipResourceWithStreamingResponse:
        return AsyncOwnershipResourceWithStreamingResponse(self._companies.ownership)

    @cached_property
    def earnings(self) -> AsyncEarningsResourceWithStreamingResponse:
        return AsyncEarningsResourceWithStreamingResponse(self._companies.earnings)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResourceWithStreamingResponse:
        return AsyncRelationshipsResourceWithStreamingResponse(self._companies.relationships)
