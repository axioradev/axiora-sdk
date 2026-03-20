# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import (
    company_list_params,
    company_search_params,
    company_retrieve_params,
    company_retrieve_peers_params,
    company_retrieve_growth_params,
    company_retrieve_ratios_params,
    company_retrieve_sections_params,
    company_retrieve_financials_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.list_response import ListResponse
from ..types.company_retrieve_response import CompanyRetrieveResponse
from ..types.company_retrieve_peers_response import CompanyRetrievePeersResponse
from ..types.company_retrieve_growth_response import CompanyRetrieveGrowthResponse
from ..types.company_retrieve_health_response import CompanyRetrieveHealthResponse
from ..types.company_retrieve_ratios_response import CompanyRetrieveRatiosResponse
from ..types.company_retrieve_sections_response import CompanyRetrieveSectionsResponse
from ..types.company_retrieve_financials_response import CompanyRetrieveFinancialsResponse
from ..types.company_retrieve_identifiers_response import CompanyRetrieveIdentifiersResponse

__all__ = ["CompaniesResource", "AsyncCompaniesResource"]


class CompaniesResource(SyncAPIResource):
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
    ) -> ListResponse:
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
            cast_to=ListResponse,
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
    ) -> CompanyRetrieveFinancialsResponse:
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
            cast_to=CompanyRetrieveFinancialsResponse,
        )

    def retrieve_growth(
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
    ) -> CompanyRetrieveGrowthResponse:
        """
        Year-over-year growth rates and multi-year CAGRs.

        Args:
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
                query=maybe_transform({"years": years}, company_retrieve_growth_params.CompanyRetrieveGrowthParams),
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
                query=maybe_transform({"years": years}, company_retrieve_ratios_params.CompanyRetrieveRatiosParams),
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
    ) -> CompanyRetrieveSectionsResponse:
        """
        Get text sections from a company's annual filing.

        Returns the full Japanese text of each section, with English translations where
        available. No truncation.

        Args:
          fiscal_year: Fiscal year. Defaults to latest.

          section: Filter by section key. One of: mda, risk_factors, business_overview, strategy,
              sustainability, research_and_development, dividend_policy, governance,
              company_history, employees, critical_contracts, capital_expenditures,
              accounting_policy, segment_info, financial_instruments.

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
            cast_to=CompanyRetrieveSectionsResponse,
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
    ) -> ListResponse:
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
            cast_to=ListResponse,
        )


class AsyncCompaniesResource(AsyncAPIResource):
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
    ) -> ListResponse:
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
            cast_to=ListResponse,
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
    ) -> CompanyRetrieveFinancialsResponse:
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
            cast_to=CompanyRetrieveFinancialsResponse,
        )

    async def retrieve_growth(
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
    ) -> CompanyRetrieveGrowthResponse:
        """
        Year-over-year growth rates and multi-year CAGRs.

        Args:
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
                    {"years": years}, company_retrieve_growth_params.CompanyRetrieveGrowthParams
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
                    {"years": years}, company_retrieve_ratios_params.CompanyRetrieveRatiosParams
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
    ) -> CompanyRetrieveSectionsResponse:
        """
        Get text sections from a company's annual filing.

        Returns the full Japanese text of each section, with English translations where
        available. No truncation.

        Args:
          fiscal_year: Fiscal year. Defaults to latest.

          section: Filter by section key. One of: mda, risk_factors, business_overview, strategy,
              sustainability, research_and_development, dividend_policy, governance,
              company_history, employees, critical_contracts, capital_expenditures,
              accounting_policy, segment_info, financial_instruments.

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
            cast_to=CompanyRetrieveSectionsResponse,
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
    ) -> ListResponse:
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
            cast_to=ListResponse,
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


class AsyncCompaniesResourceWithRawResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.retrieve = async_to_raw_response_wrapper(
            companies.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            companies.list,
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


class CompaniesResourceWithStreamingResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.retrieve = to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            companies.list,
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


class AsyncCompaniesResourceWithStreamingResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.retrieve = async_to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            companies.list,
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
