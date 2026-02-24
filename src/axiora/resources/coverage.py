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
from ..types.coverage_retrieve_response import CoverageRetrieveResponse

__all__ = ["CoverageResource", "AsyncCoverageResource"]


class CoverageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CoverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#accessing-raw-response-data-eg-headers
        """
        return CoverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CoverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#with_streaming_response
        """
        return CoverageResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CoverageRetrieveResponse:
        """
        Data coverage statistics — metric availability, freshness, totals.

        Shows what percentage of companies have non-null values for each financial
        metric. Use this to assess data completeness and trust.
        """
        return self._get(
            "/v1/coverage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CoverageRetrieveResponse,
        )


class AsyncCoverageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCoverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCoverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCoverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#with_streaming_response
        """
        return AsyncCoverageResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CoverageRetrieveResponse:
        """
        Data coverage statistics — metric availability, freshness, totals.

        Shows what percentage of companies have non-null values for each financial
        metric. Use this to assess data completeness and trust.
        """
        return await self._get(
            "/v1/coverage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CoverageRetrieveResponse,
        )


class CoverageResourceWithRawResponse:
    def __init__(self, coverage: CoverageResource) -> None:
        self._coverage = coverage

        self.retrieve = to_raw_response_wrapper(
            coverage.retrieve,
        )


class AsyncCoverageResourceWithRawResponse:
    def __init__(self, coverage: AsyncCoverageResource) -> None:
        self._coverage = coverage

        self.retrieve = async_to_raw_response_wrapper(
            coverage.retrieve,
        )


class CoverageResourceWithStreamingResponse:
    def __init__(self, coverage: CoverageResource) -> None:
        self._coverage = coverage

        self.retrieve = to_streamed_response_wrapper(
            coverage.retrieve,
        )


class AsyncCoverageResourceWithStreamingResponse:
    def __init__(self, coverage: AsyncCoverageResource) -> None:
        self._coverage = coverage

        self.retrieve = async_to_streamed_response_wrapper(
            coverage.retrieve,
        )
