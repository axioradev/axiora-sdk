# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import voting_list_recent_params
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
from ..types.list_response_voting_result import ListResponseVotingResult

__all__ = ["VotingResource", "AsyncVotingResource"]


class VotingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VotingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return VotingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VotingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return VotingResourceWithStreamingResponse(self)

    def list_recent(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        min_dissent_pct: Optional[float] | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseVotingResult:
        """
        Get recent AGM voting results across all companies.

        Returns the most recent voting data, ordered by AGM date descending. Use
        min_dissent_pct to find proposals with significant opposition.

        Args:
          cursor: Opaque cursor for keyset pagination

          limit: Results per page

          min_dissent_pct: Minimum dissent percentage to filter high-opposition proposals (e.g. 20.0)

          offset: Results to skip (ignored when cursor is set)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/voting/recent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "min_dissent_pct": min_dissent_pct,
                        "offset": offset,
                    },
                    voting_list_recent_params.VotingListRecentParams,
                ),
            ),
            cast_to=ListResponseVotingResult,
        )


class AsyncVotingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVotingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncVotingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVotingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncVotingResourceWithStreamingResponse(self)

    async def list_recent(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        min_dissent_pct: Optional[float] | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseVotingResult:
        """
        Get recent AGM voting results across all companies.

        Returns the most recent voting data, ordered by AGM date descending. Use
        min_dissent_pct to find proposals with significant opposition.

        Args:
          cursor: Opaque cursor for keyset pagination

          limit: Results per page

          min_dissent_pct: Minimum dissent percentage to filter high-opposition proposals (e.g. 20.0)

          offset: Results to skip (ignored when cursor is set)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/voting/recent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "min_dissent_pct": min_dissent_pct,
                        "offset": offset,
                    },
                    voting_list_recent_params.VotingListRecentParams,
                ),
            ),
            cast_to=ListResponseVotingResult,
        )


class VotingResourceWithRawResponse:
    def __init__(self, voting: VotingResource) -> None:
        self._voting = voting

        self.list_recent = to_raw_response_wrapper(
            voting.list_recent,
        )


class AsyncVotingResourceWithRawResponse:
    def __init__(self, voting: AsyncVotingResource) -> None:
        self._voting = voting

        self.list_recent = async_to_raw_response_wrapper(
            voting.list_recent,
        )


class VotingResourceWithStreamingResponse:
    def __init__(self, voting: VotingResource) -> None:
        self._voting = voting

        self.list_recent = to_streamed_response_wrapper(
            voting.list_recent,
        )


class AsyncVotingResourceWithStreamingResponse:
    def __init__(self, voting: AsyncVotingResource) -> None:
        self._voting = voting

        self.list_recent = async_to_streamed_response_wrapper(
            voting.list_recent,
        )
