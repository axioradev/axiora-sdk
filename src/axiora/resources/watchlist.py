# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import watchlist_add_params
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
from ..types.watchlist_add_response import WatchlistAddResponse
from ..types.watchlist_list_response import WatchlistListResponse
from ..types.watchlist_remove_response import WatchlistRemoveResponse

__all__ = ["WatchlistResource", "AsyncWatchlistResource"]


class WatchlistResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WatchlistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return WatchlistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WatchlistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return WatchlistResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistListResponse:
        """List all watchlist items for the authenticated user."""
        return self._get(
            "/v1/watchlist",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistListResponse,
        )

    def add(
        self,
        *,
        entity_code: str,
        entity_type: str,
        entity_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistAddResponse:
        """
        Add a company or investor to the user's watchlist.

        Args:
          entity_code: Securities code or EDINET code

          entity_type: company or investor

          entity_name: Display name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/watchlist",
            body=maybe_transform(
                {
                    "entity_code": entity_code,
                    "entity_type": entity_type,
                    "entity_name": entity_name,
                },
                watchlist_add_params.WatchlistAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistAddResponse,
        )

    def remove(
        self,
        item_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistRemoveResponse:
        """
        Remove an item from the user's watchlist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            path_template("/v1/watchlist/{item_id}", item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistRemoveResponse,
        )


class AsyncWatchlistResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWatchlistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWatchlistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWatchlistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncWatchlistResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistListResponse:
        """List all watchlist items for the authenticated user."""
        return await self._get(
            "/v1/watchlist",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistListResponse,
        )

    async def add(
        self,
        *,
        entity_code: str,
        entity_type: str,
        entity_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistAddResponse:
        """
        Add a company or investor to the user's watchlist.

        Args:
          entity_code: Securities code or EDINET code

          entity_type: company or investor

          entity_name: Display name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/watchlist",
            body=await async_maybe_transform(
                {
                    "entity_code": entity_code,
                    "entity_type": entity_type,
                    "entity_name": entity_name,
                },
                watchlist_add_params.WatchlistAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistAddResponse,
        )

    async def remove(
        self,
        item_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistRemoveResponse:
        """
        Remove an item from the user's watchlist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            path_template("/v1/watchlist/{item_id}", item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistRemoveResponse,
        )


class WatchlistResourceWithRawResponse:
    def __init__(self, watchlist: WatchlistResource) -> None:
        self._watchlist = watchlist

        self.list = to_raw_response_wrapper(
            watchlist.list,
        )
        self.add = to_raw_response_wrapper(
            watchlist.add,
        )
        self.remove = to_raw_response_wrapper(
            watchlist.remove,
        )


class AsyncWatchlistResourceWithRawResponse:
    def __init__(self, watchlist: AsyncWatchlistResource) -> None:
        self._watchlist = watchlist

        self.list = async_to_raw_response_wrapper(
            watchlist.list,
        )
        self.add = async_to_raw_response_wrapper(
            watchlist.add,
        )
        self.remove = async_to_raw_response_wrapper(
            watchlist.remove,
        )


class WatchlistResourceWithStreamingResponse:
    def __init__(self, watchlist: WatchlistResource) -> None:
        self._watchlist = watchlist

        self.list = to_streamed_response_wrapper(
            watchlist.list,
        )
        self.add = to_streamed_response_wrapper(
            watchlist.add,
        )
        self.remove = to_streamed_response_wrapper(
            watchlist.remove,
        )


class AsyncWatchlistResourceWithStreamingResponse:
    def __init__(self, watchlist: AsyncWatchlistResource) -> None:
        self._watchlist = watchlist

        self.list = async_to_streamed_response_wrapper(
            watchlist.list,
        )
        self.add = async_to_streamed_response_wrapper(
            watchlist.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            watchlist.remove,
        )
