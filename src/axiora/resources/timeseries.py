# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import timesery_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.timesery_retrieve_response import TimeseryRetrieveResponse

__all__ = ["TimeseriesResource", "AsyncTimeseriesResource"]


class TimeseriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TimeseriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return TimeseriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimeseriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return TimeseriesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        codes: str,
        metric: str | Omit = omit,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseryRetrieveResponse:
        """
        Time-series data for a single metric across one or more companies.

        Returns data in a chart-friendly format: one array per company, each element
        being {fiscal_year, value}.

        Args:
          codes: Comma-separated EDINET or securities codes (max 5)

          metric: Financial metric to chart

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "codes": codes,
                        "metric": metric,
                        "years": years,
                    },
                    timesery_retrieve_params.TimeseryRetrieveParams,
                ),
            ),
            cast_to=TimeseryRetrieveResponse,
        )


class AsyncTimeseriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTimeseriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTimeseriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimeseriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncTimeseriesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        codes: str,
        metric: str | Omit = omit,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseryRetrieveResponse:
        """
        Time-series data for a single metric across one or more companies.

        Returns data in a chart-friendly format: one array per company, each element
        being {fiscal_year, value}.

        Args:
          codes: Comma-separated EDINET or securities codes (max 5)

          metric: Financial metric to chart

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "codes": codes,
                        "metric": metric,
                        "years": years,
                    },
                    timesery_retrieve_params.TimeseryRetrieveParams,
                ),
            ),
            cast_to=TimeseryRetrieveResponse,
        )


class TimeseriesResourceWithRawResponse:
    def __init__(self, timeseries: TimeseriesResource) -> None:
        self._timeseries = timeseries

        self.retrieve = to_raw_response_wrapper(
            timeseries.retrieve,
        )


class AsyncTimeseriesResourceWithRawResponse:
    def __init__(self, timeseries: AsyncTimeseriesResource) -> None:
        self._timeseries = timeseries

        self.retrieve = async_to_raw_response_wrapper(
            timeseries.retrieve,
        )


class TimeseriesResourceWithStreamingResponse:
    def __init__(self, timeseries: TimeseriesResource) -> None:
        self._timeseries = timeseries

        self.retrieve = to_streamed_response_wrapper(
            timeseries.retrieve,
        )


class AsyncTimeseriesResourceWithStreamingResponse:
    def __init__(self, timeseries: AsyncTimeseriesResource) -> None:
        self._timeseries = timeseries

        self.retrieve = async_to_streamed_response_wrapper(
            timeseries.retrieve,
        )
