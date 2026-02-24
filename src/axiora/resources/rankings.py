# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import ranking_retrieve_params
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
from ..types.ranking_retrieve_response import RankingRetrieveResponse

__all__ = ["RankingsResource", "AsyncRankingsResource"]


class RankingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RankingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#accessing-raw-response-data-eg-headers
        """
        return RankingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RankingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#with_streaming_response
        """
        return RankingsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        metric: str,
        *,
        fiscal_year: Optional[int] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: str | Omit = omit,
        sector: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RankingRetrieveResponse:
        """
        Rank companies by a financial metric.

        Returns top N companies sorted by the chosen metric, with the metric value and
        basic company info.

        Args:
          sector: Filter by sector

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric:
            raise ValueError(f"Expected a non-empty value for `metric` but received {metric!r}")
        return self._get(
            f"/v1/rankings/{metric}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fiscal_year": fiscal_year,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "sector": sector,
                    },
                    ranking_retrieve_params.RankingRetrieveParams,
                ),
            ),
            cast_to=RankingRetrieveResponse,
        )


class AsyncRankingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRankingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRankingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRankingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#with_streaming_response
        """
        return AsyncRankingsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        metric: str,
        *,
        fiscal_year: Optional[int] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: str | Omit = omit,
        sector: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RankingRetrieveResponse:
        """
        Rank companies by a financial metric.

        Returns top N companies sorted by the chosen metric, with the metric value and
        basic company info.

        Args:
          sector: Filter by sector

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric:
            raise ValueError(f"Expected a non-empty value for `metric` but received {metric!r}")
        return await self._get(
            f"/v1/rankings/{metric}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fiscal_year": fiscal_year,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "sector": sector,
                    },
                    ranking_retrieve_params.RankingRetrieveParams,
                ),
            ),
            cast_to=RankingRetrieveResponse,
        )


class RankingsResourceWithRawResponse:
    def __init__(self, rankings: RankingsResource) -> None:
        self._rankings = rankings

        self.retrieve = to_raw_response_wrapper(
            rankings.retrieve,
        )


class AsyncRankingsResourceWithRawResponse:
    def __init__(self, rankings: AsyncRankingsResource) -> None:
        self._rankings = rankings

        self.retrieve = async_to_raw_response_wrapper(
            rankings.retrieve,
        )


class RankingsResourceWithStreamingResponse:
    def __init__(self, rankings: RankingsResource) -> None:
        self._rankings = rankings

        self.retrieve = to_streamed_response_wrapper(
            rankings.retrieve,
        )


class AsyncRankingsResourceWithStreamingResponse:
    def __init__(self, rankings: AsyncRankingsResource) -> None:
        self._rankings = rankings

        self.retrieve = async_to_streamed_response_wrapper(
            rankings.retrieve,
        )
