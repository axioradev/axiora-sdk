# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import earning_list_signals_params, earning_retrieve_latest_params
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
from ..types.earning_list_signals_response import EarningListSignalsResponse
from ..types.earning_retrieve_latest_response import EarningRetrieveLatestResponse

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

    def list_signals(
        self,
        *,
        limit: int | Omit = omit,
        signal_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EarningListSignalsResponse:
        """
        Get latest earnings signals across all companies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/earnings/signals",
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
                    earning_list_signals_params.EarningListSignalsParams,
                ),
            ),
            cast_to=EarningListSignalsResponse,
        )

    def retrieve_latest(
        self,
        *,
        limit: int | Omit = omit,
        period_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EarningRetrieveLatestResponse:
        """
        Get the most recent earnings releases across all companies.

        Useful for screening recent 決算短信 filings.

        Args:
          period_type: Filter: FY, Q1, Q2, Q3

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/earnings/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "period_type": period_type,
                    },
                    earning_retrieve_latest_params.EarningRetrieveLatestParams,
                ),
            ),
            cast_to=EarningRetrieveLatestResponse,
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

    async def list_signals(
        self,
        *,
        limit: int | Omit = omit,
        signal_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EarningListSignalsResponse:
        """
        Get latest earnings signals across all companies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/earnings/signals",
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
                    earning_list_signals_params.EarningListSignalsParams,
                ),
            ),
            cast_to=EarningListSignalsResponse,
        )

    async def retrieve_latest(
        self,
        *,
        limit: int | Omit = omit,
        period_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EarningRetrieveLatestResponse:
        """
        Get the most recent earnings releases across all companies.

        Useful for screening recent 決算短信 filings.

        Args:
          period_type: Filter: FY, Q1, Q2, Q3

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/earnings/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "period_type": period_type,
                    },
                    earning_retrieve_latest_params.EarningRetrieveLatestParams,
                ),
            ),
            cast_to=EarningRetrieveLatestResponse,
        )


class EarningsResourceWithRawResponse:
    def __init__(self, earnings: EarningsResource) -> None:
        self._earnings = earnings

        self.list_signals = to_raw_response_wrapper(
            earnings.list_signals,
        )
        self.retrieve_latest = to_raw_response_wrapper(
            earnings.retrieve_latest,
        )


class AsyncEarningsResourceWithRawResponse:
    def __init__(self, earnings: AsyncEarningsResource) -> None:
        self._earnings = earnings

        self.list_signals = async_to_raw_response_wrapper(
            earnings.list_signals,
        )
        self.retrieve_latest = async_to_raw_response_wrapper(
            earnings.retrieve_latest,
        )


class EarningsResourceWithStreamingResponse:
    def __init__(self, earnings: EarningsResource) -> None:
        self._earnings = earnings

        self.list_signals = to_streamed_response_wrapper(
            earnings.list_signals,
        )
        self.retrieve_latest = to_streamed_response_wrapper(
            earnings.retrieve_latest,
        )


class AsyncEarningsResourceWithStreamingResponse:
    def __init__(self, earnings: AsyncEarningsResource) -> None:
        self._earnings = earnings

        self.list_signals = async_to_streamed_response_wrapper(
            earnings.list_signals,
        )
        self.retrieve_latest = async_to_streamed_response_wrapper(
            earnings.retrieve_latest,
        )
