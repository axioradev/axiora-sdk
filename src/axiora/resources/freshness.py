# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.freshness_retrieve_response import FreshnessRetrieveResponse

__all__ = ["FreshnessResource", "AsyncFreshnessResource"]


class FreshnessResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FreshnessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return FreshnessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FreshnessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return FreshnessResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FreshnessRetrieveResponse:
        """Return data freshness metrics. Public endpoint, no auth required."""
        return self._get(
            "/v1/freshness",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FreshnessRetrieveResponse,
        )


class AsyncFreshnessResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFreshnessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFreshnessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFreshnessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncFreshnessResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FreshnessRetrieveResponse:
        """Return data freshness metrics. Public endpoint, no auth required."""
        return await self._get(
            "/v1/freshness",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FreshnessRetrieveResponse,
        )


class FreshnessResourceWithRawResponse:
    def __init__(self, freshness: FreshnessResource) -> None:
        self._freshness = freshness

        self.retrieve = to_raw_response_wrapper(
            freshness.retrieve,
        )


class AsyncFreshnessResourceWithRawResponse:
    def __init__(self, freshness: AsyncFreshnessResource) -> None:
        self._freshness = freshness

        self.retrieve = async_to_raw_response_wrapper(
            freshness.retrieve,
        )


class FreshnessResourceWithStreamingResponse:
    def __init__(self, freshness: FreshnessResource) -> None:
        self._freshness = freshness

        self.retrieve = to_streamed_response_wrapper(
            freshness.retrieve,
        )


class AsyncFreshnessResourceWithStreamingResponse:
    def __init__(self, freshness: AsyncFreshnessResource) -> None:
        self._freshness = freshness

        self.retrieve = async_to_streamed_response_wrapper(
            freshness.retrieve,
        )
