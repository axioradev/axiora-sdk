# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import buyback_list_latest_params, buyback_list_accelerations_params
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
from ..types.buyback_list_latest_response import BuybackListLatestResponse
from ..types.buyback_list_accelerations_response import BuybackListAccelerationsResponse

__all__ = ["BuybacksResource", "AsyncBuybacksResource"]


class BuybacksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BuybacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return BuybacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BuybacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return BuybacksResourceWithStreamingResponse(self)

    def list_accelerations(
        self,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuybackListAccelerationsResponse:
        """
        Get market-wide buyback acceleration events.

        Returns companies where buyback execution pace increased significantly (>=10pp
        completion in a single reporting period).

        Args:
          limit: Max results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/buybacks/accelerations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit}, buyback_list_accelerations_params.BuybackListAccelerationsParams
                ),
            ),
            cast_to=BuybackListAccelerationsResponse,
        )

    def list_latest(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sector: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuybackListLatestResponse:
        """
        Get the latest buyback reports across all companies.

        Returns the most recent share buyback status filings, ordered newest first. Use
        this to monitor buyback activity across the market or within a specific sector.

        Args:
          cursor: Opaque cursor for keyset pagination

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          sector: Filter by sector (e.g. '情報・通信業')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/buybacks/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "offset": offset,
                        "sector": sector,
                    },
                    buyback_list_latest_params.BuybackListLatestParams,
                ),
            ),
            cast_to=BuybackListLatestResponse,
        )


class AsyncBuybacksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBuybacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBuybacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBuybacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncBuybacksResourceWithStreamingResponse(self)

    async def list_accelerations(
        self,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuybackListAccelerationsResponse:
        """
        Get market-wide buyback acceleration events.

        Returns companies where buyback execution pace increased significantly (>=10pp
        completion in a single reporting period).

        Args:
          limit: Max results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/buybacks/accelerations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit}, buyback_list_accelerations_params.BuybackListAccelerationsParams
                ),
            ),
            cast_to=BuybackListAccelerationsResponse,
        )

    async def list_latest(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sector: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuybackListLatestResponse:
        """
        Get the latest buyback reports across all companies.

        Returns the most recent share buyback status filings, ordered newest first. Use
        this to monitor buyback activity across the market or within a specific sector.

        Args:
          cursor: Opaque cursor for keyset pagination

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          sector: Filter by sector (e.g. '情報・通信業')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/buybacks/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "offset": offset,
                        "sector": sector,
                    },
                    buyback_list_latest_params.BuybackListLatestParams,
                ),
            ),
            cast_to=BuybackListLatestResponse,
        )


class BuybacksResourceWithRawResponse:
    def __init__(self, buybacks: BuybacksResource) -> None:
        self._buybacks = buybacks

        self.list_accelerations = to_raw_response_wrapper(
            buybacks.list_accelerations,
        )
        self.list_latest = to_raw_response_wrapper(
            buybacks.list_latest,
        )


class AsyncBuybacksResourceWithRawResponse:
    def __init__(self, buybacks: AsyncBuybacksResource) -> None:
        self._buybacks = buybacks

        self.list_accelerations = async_to_raw_response_wrapper(
            buybacks.list_accelerations,
        )
        self.list_latest = async_to_raw_response_wrapper(
            buybacks.list_latest,
        )


class BuybacksResourceWithStreamingResponse:
    def __init__(self, buybacks: BuybacksResource) -> None:
        self._buybacks = buybacks

        self.list_accelerations = to_streamed_response_wrapper(
            buybacks.list_accelerations,
        )
        self.list_latest = to_streamed_response_wrapper(
            buybacks.list_latest,
        )


class AsyncBuybacksResourceWithStreamingResponse:
    def __init__(self, buybacks: AsyncBuybacksResource) -> None:
        self._buybacks = buybacks

        self.list_accelerations = async_to_streamed_response_wrapper(
            buybacks.list_accelerations,
        )
        self.list_latest = async_to_streamed_response_wrapper(
            buybacks.list_latest,
        )
