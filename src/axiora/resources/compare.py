# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import compare_retrieve_params
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
from ..types.compare_retrieve_response import CompareRetrieveResponse

__all__ = ["CompareResource", "AsyncCompareResource"]


class CompareResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompareResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return CompareResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompareResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return CompareResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        codes: str,
        fiscal_year: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompareRetrieveResponse:
        """
        Side-by-side financial comparison of multiple companies.

        Returns financials and computed ratios for each company, aligned by fiscal year
        for easy comparison.

        Args:
          codes: Comma-separated EDINET or securities codes (max 10)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/compare",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "codes": codes,
                        "fiscal_year": fiscal_year,
                    },
                    compare_retrieve_params.CompareRetrieveParams,
                ),
            ),
            cast_to=CompareRetrieveResponse,
        )


class AsyncCompareResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompareResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCompareResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompareResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncCompareResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        codes: str,
        fiscal_year: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompareRetrieveResponse:
        """
        Side-by-side financial comparison of multiple companies.

        Returns financials and computed ratios for each company, aligned by fiscal year
        for easy comparison.

        Args:
          codes: Comma-separated EDINET or securities codes (max 10)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/compare",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "codes": codes,
                        "fiscal_year": fiscal_year,
                    },
                    compare_retrieve_params.CompareRetrieveParams,
                ),
            ),
            cast_to=CompareRetrieveResponse,
        )


class CompareResourceWithRawResponse:
    def __init__(self, compare: CompareResource) -> None:
        self._compare = compare

        self.retrieve = to_raw_response_wrapper(
            compare.retrieve,
        )


class AsyncCompareResourceWithRawResponse:
    def __init__(self, compare: AsyncCompareResource) -> None:
        self._compare = compare

        self.retrieve = async_to_raw_response_wrapper(
            compare.retrieve,
        )


class CompareResourceWithStreamingResponse:
    def __init__(self, compare: CompareResource) -> None:
        self._compare = compare

        self.retrieve = to_streamed_response_wrapper(
            compare.retrieve,
        )


class AsyncCompareResourceWithStreamingResponse:
    def __init__(self, compare: AsyncCompareResource) -> None:
        self._compare = compare

        self.retrieve = async_to_streamed_response_wrapper(
            compare.retrieve,
        )
