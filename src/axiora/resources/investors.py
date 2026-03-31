# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import investor_search_params, investor_retrieve_positions_params
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
from ..types.investor_search_response import InvestorSearchResponse
from ..types.investor_retrieve_positions_response import InvestorRetrievePositionsResponse

__all__ = ["InvestorsResource", "AsyncInvestorsResource"]


class InvestorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvestorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return InvestorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvestorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return InvestorsResourceWithStreamingResponse(self)

    def retrieve_positions(
        self,
        code: str,
        *,
        limit: int | Omit = omit,
        trajectory_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvestorRetrievePositionsResponse:
        """
        Get all positions for an investor across all companies.

        Returns companies where this investor has filed large shareholding reports, with
        trajectory data (direction, velocity, holding %).

        Args:
          trajectory_type: Filter: accumulating, exiting, stable, new_position

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/investors/{code}/positions", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "trajectory_type": trajectory_type,
                    },
                    investor_retrieve_positions_params.InvestorRetrievePositionsParams,
                ),
            ),
            cast_to=InvestorRetrievePositionsResponse,
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
    ) -> InvestorSearchResponse:
        """
        Search investors by name or EDINET code.

        Searches across ownership trajectories and large shareholding filings. Matches
        Japanese filer names, English names in parentheses, and company names.

        Args:
          q: Search by investor name or EDINET code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/investors/search",
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
                    investor_search_params.InvestorSearchParams,
                ),
            ),
            cast_to=InvestorSearchResponse,
        )


class AsyncInvestorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvestorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncInvestorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvestorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncInvestorsResourceWithStreamingResponse(self)

    async def retrieve_positions(
        self,
        code: str,
        *,
        limit: int | Omit = omit,
        trajectory_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvestorRetrievePositionsResponse:
        """
        Get all positions for an investor across all companies.

        Returns companies where this investor has filed large shareholding reports, with
        trajectory data (direction, velocity, holding %).

        Args:
          trajectory_type: Filter: accumulating, exiting, stable, new_position

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/investors/{code}/positions", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "trajectory_type": trajectory_type,
                    },
                    investor_retrieve_positions_params.InvestorRetrievePositionsParams,
                ),
            ),
            cast_to=InvestorRetrievePositionsResponse,
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
    ) -> InvestorSearchResponse:
        """
        Search investors by name or EDINET code.

        Searches across ownership trajectories and large shareholding filings. Matches
        Japanese filer names, English names in parentheses, and company names.

        Args:
          q: Search by investor name or EDINET code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/investors/search",
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
                    investor_search_params.InvestorSearchParams,
                ),
            ),
            cast_to=InvestorSearchResponse,
        )


class InvestorsResourceWithRawResponse:
    def __init__(self, investors: InvestorsResource) -> None:
        self._investors = investors

        self.retrieve_positions = to_raw_response_wrapper(
            investors.retrieve_positions,
        )
        self.search = to_raw_response_wrapper(
            investors.search,
        )


class AsyncInvestorsResourceWithRawResponse:
    def __init__(self, investors: AsyncInvestorsResource) -> None:
        self._investors = investors

        self.retrieve_positions = async_to_raw_response_wrapper(
            investors.retrieve_positions,
        )
        self.search = async_to_raw_response_wrapper(
            investors.search,
        )


class InvestorsResourceWithStreamingResponse:
    def __init__(self, investors: InvestorsResource) -> None:
        self._investors = investors

        self.retrieve_positions = to_streamed_response_wrapper(
            investors.retrieve_positions,
        )
        self.search = to_streamed_response_wrapper(
            investors.search,
        )


class AsyncInvestorsResourceWithStreamingResponse:
    def __init__(self, investors: AsyncInvestorsResource) -> None:
        self._investors = investors

        self.retrieve_positions = async_to_streamed_response_wrapper(
            investors.retrieve_positions,
        )
        self.search = async_to_streamed_response_wrapper(
            investors.search,
        )
