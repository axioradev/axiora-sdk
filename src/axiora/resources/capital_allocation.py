# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import capital_allocation_list_ranking_params
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
from ..types.capital_allocation_list_ranking_response import CapitalAllocationListRankingResponse

__all__ = ["CapitalAllocationResource", "AsyncCapitalAllocationResource"]


class CapitalAllocationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CapitalAllocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return CapitalAllocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CapitalAllocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return CapitalAllocationResourceWithStreamingResponse(self)

    def list_ranking(
        self,
        *,
        classification: Optional[str] | Omit = omit,
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
    ) -> CapitalAllocationListRankingResponse:
        """
        Get capital allocation ranking across companies.

        Sorted by return ratio (highest returners first by default).

        Args:
          classification: Filter: Returner, Hoarder, Reinvestor, Mixed

          cursor: Opaque cursor for keyset pagination

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          sector: Filter by sector

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/capital-allocation/ranking",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "classification": classification,
                        "cursor": cursor,
                        "limit": limit,
                        "offset": offset,
                        "sector": sector,
                    },
                    capital_allocation_list_ranking_params.CapitalAllocationListRankingParams,
                ),
            ),
            cast_to=CapitalAllocationListRankingResponse,
        )


class AsyncCapitalAllocationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCapitalAllocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCapitalAllocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCapitalAllocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncCapitalAllocationResourceWithStreamingResponse(self)

    async def list_ranking(
        self,
        *,
        classification: Optional[str] | Omit = omit,
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
    ) -> CapitalAllocationListRankingResponse:
        """
        Get capital allocation ranking across companies.

        Sorted by return ratio (highest returners first by default).

        Args:
          classification: Filter: Returner, Hoarder, Reinvestor, Mixed

          cursor: Opaque cursor for keyset pagination

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          sector: Filter by sector

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/capital-allocation/ranking",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "classification": classification,
                        "cursor": cursor,
                        "limit": limit,
                        "offset": offset,
                        "sector": sector,
                    },
                    capital_allocation_list_ranking_params.CapitalAllocationListRankingParams,
                ),
            ),
            cast_to=CapitalAllocationListRankingResponse,
        )


class CapitalAllocationResourceWithRawResponse:
    def __init__(self, capital_allocation: CapitalAllocationResource) -> None:
        self._capital_allocation = capital_allocation

        self.list_ranking = to_raw_response_wrapper(
            capital_allocation.list_ranking,
        )


class AsyncCapitalAllocationResourceWithRawResponse:
    def __init__(self, capital_allocation: AsyncCapitalAllocationResource) -> None:
        self._capital_allocation = capital_allocation

        self.list_ranking = async_to_raw_response_wrapper(
            capital_allocation.list_ranking,
        )


class CapitalAllocationResourceWithStreamingResponse:
    def __init__(self, capital_allocation: CapitalAllocationResource) -> None:
        self._capital_allocation = capital_allocation

        self.list_ranking = to_streamed_response_wrapper(
            capital_allocation.list_ranking,
        )


class AsyncCapitalAllocationResourceWithStreamingResponse:
    def __init__(self, capital_allocation: AsyncCapitalAllocationResource) -> None:
        self._capital_allocation = capital_allocation

        self.list_ranking = async_to_streamed_response_wrapper(
            capital_allocation.list_ranking,
        )
