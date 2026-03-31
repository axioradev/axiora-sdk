# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.companies import earning_get_signals_params, earning_get_earnings_params
from ...types.companies.earning_get_signals_response import EarningGetSignalsResponse
from ...types.companies.earning_get_earnings_response import EarningGetEarningsResponse
from ...types.companies.earning_get_surprise_response import EarningGetSurpriseResponse

__all__ = ["EarningsResource", "AsyncEarningsResource"]


class EarningsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EarningsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return EarningsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EarningsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return EarningsResourceWithStreamingResponse(self)

    def get_earnings(
        self,
        code: str,
        *,
        period_type: Optional[str] | Omit = omit,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EarningGetEarningsResponse:
        """
        Get earnings snapshots from 決算短信 for a company.

        Returns actuals, balance sheet, cash flows, and ratios for each period. Data
        arrives weeks before EDINET annual reports.

        Args:
          period_type: Filter: FY, Q1, Q2, Q3

          years: Number of fiscal years

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/earnings", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "period_type": period_type,
                        "years": years,
                    },
                    earning_get_earnings_params.EarningGetEarningsParams,
                ),
            ),
            cast_to=EarningGetEarningsResponse,
        )

    def get_signals(
        self,
        code: str,
        *,
        limit: int | Omit = omit,
        signal_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EarningGetSignalsResponse:
        """
        Get earnings signals for a company (beats, misses, revisions, records).

        Args:
          signal_type: Filter: earnings_beat, earnings_miss, forecast_revision_up,
              forecast_revision_down, record_revenue, margin_expansion, margin_contraction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/earnings/signals", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "signal_type": signal_type,
                    },
                    earning_get_signals_params.EarningGetSignalsParams,
                ),
            ),
            cast_to=EarningGetSignalsResponse,
        )

    def get_surprise(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EarningGetSurpriseResponse:
        """
        Compare actual earnings against prior management forecasts.

        For each earnings snapshot, finds the most recent prior snapshot that contained
        a forecast, then computes the surprise (beat/miss) percentage.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/earnings/surprise", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EarningGetSurpriseResponse,
        )


class AsyncEarningsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEarningsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEarningsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEarningsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncEarningsResourceWithStreamingResponse(self)

    async def get_earnings(
        self,
        code: str,
        *,
        period_type: Optional[str] | Omit = omit,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EarningGetEarningsResponse:
        """
        Get earnings snapshots from 決算短信 for a company.

        Returns actuals, balance sheet, cash flows, and ratios for each period. Data
        arrives weeks before EDINET annual reports.

        Args:
          period_type: Filter: FY, Q1, Q2, Q3

          years: Number of fiscal years

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/earnings", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "period_type": period_type,
                        "years": years,
                    },
                    earning_get_earnings_params.EarningGetEarningsParams,
                ),
            ),
            cast_to=EarningGetEarningsResponse,
        )

    async def get_signals(
        self,
        code: str,
        *,
        limit: int | Omit = omit,
        signal_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EarningGetSignalsResponse:
        """
        Get earnings signals for a company (beats, misses, revisions, records).

        Args:
          signal_type: Filter: earnings_beat, earnings_miss, forecast_revision_up,
              forecast_revision_down, record_revenue, margin_expansion, margin_contraction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/earnings/signals", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "signal_type": signal_type,
                    },
                    earning_get_signals_params.EarningGetSignalsParams,
                ),
            ),
            cast_to=EarningGetSignalsResponse,
        )

    async def get_surprise(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EarningGetSurpriseResponse:
        """
        Compare actual earnings against prior management forecasts.

        For each earnings snapshot, finds the most recent prior snapshot that contained
        a forecast, then computes the surprise (beat/miss) percentage.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/earnings/surprise", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EarningGetSurpriseResponse,
        )


class EarningsResourceWithRawResponse:
    def __init__(self, earnings: EarningsResource) -> None:
        self._earnings = earnings

        self.get_earnings = to_raw_response_wrapper(
            earnings.get_earnings,
        )
        self.get_signals = to_raw_response_wrapper(
            earnings.get_signals,
        )
        self.get_surprise = to_raw_response_wrapper(
            earnings.get_surprise,
        )


class AsyncEarningsResourceWithRawResponse:
    def __init__(self, earnings: AsyncEarningsResource) -> None:
        self._earnings = earnings

        self.get_earnings = async_to_raw_response_wrapper(
            earnings.get_earnings,
        )
        self.get_signals = async_to_raw_response_wrapper(
            earnings.get_signals,
        )
        self.get_surprise = async_to_raw_response_wrapper(
            earnings.get_surprise,
        )


class EarningsResourceWithStreamingResponse:
    def __init__(self, earnings: EarningsResource) -> None:
        self._earnings = earnings

        self.get_earnings = to_streamed_response_wrapper(
            earnings.get_earnings,
        )
        self.get_signals = to_streamed_response_wrapper(
            earnings.get_signals,
        )
        self.get_surprise = to_streamed_response_wrapper(
            earnings.get_surprise,
        )


class AsyncEarningsResourceWithStreamingResponse:
    def __init__(self, earnings: AsyncEarningsResource) -> None:
        self._earnings = earnings

        self.get_earnings = async_to_streamed_response_wrapper(
            earnings.get_earnings,
        )
        self.get_signals = async_to_streamed_response_wrapper(
            earnings.get_signals,
        )
        self.get_surprise = async_to_streamed_response_wrapper(
            earnings.get_surprise,
        )
