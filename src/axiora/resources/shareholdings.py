# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import shareholding_list_latest_params
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
from ..types.list_response_shareholding import ListResponseShareholding

__all__ = ["ShareholdingsResource", "AsyncShareholdingsResource"]


class ShareholdingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShareholdingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return ShareholdingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShareholdingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return ShareholdingsResourceWithStreamingResponse(self)

    def list_latest(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseShareholding:
        """
        Get the latest large shareholding reports across all companies.

        Returns per-holder rows ordered by base date (newest first).

        Args:
          cursor: Opaque cursor for keyset pagination

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/shareholdings/latest",
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
                    },
                    shareholding_list_latest_params.ShareholdingListLatestParams,
                ),
            ),
            cast_to=ListResponseShareholding,
        )


class AsyncShareholdingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShareholdingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncShareholdingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShareholdingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncShareholdingsResourceWithStreamingResponse(self)

    async def list_latest(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseShareholding:
        """
        Get the latest large shareholding reports across all companies.

        Returns per-holder rows ordered by base date (newest first).

        Args:
          cursor: Opaque cursor for keyset pagination

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/shareholdings/latest",
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
                    },
                    shareholding_list_latest_params.ShareholdingListLatestParams,
                ),
            ),
            cast_to=ListResponseShareholding,
        )


class ShareholdingsResourceWithRawResponse:
    def __init__(self, shareholdings: ShareholdingsResource) -> None:
        self._shareholdings = shareholdings

        self.list_latest = to_raw_response_wrapper(
            shareholdings.list_latest,
        )


class AsyncShareholdingsResourceWithRawResponse:
    def __init__(self, shareholdings: AsyncShareholdingsResource) -> None:
        self._shareholdings = shareholdings

        self.list_latest = async_to_raw_response_wrapper(
            shareholdings.list_latest,
        )


class ShareholdingsResourceWithStreamingResponse:
    def __init__(self, shareholdings: ShareholdingsResource) -> None:
        self._shareholdings = shareholdings

        self.list_latest = to_streamed_response_wrapper(
            shareholdings.list_latest,
        )


class AsyncShareholdingsResourceWithStreamingResponse:
    def __init__(self, shareholdings: AsyncShareholdingsResource) -> None:
        self._shareholdings = shareholdings

        self.list_latest = async_to_streamed_response_wrapper(
            shareholdings.list_latest,
        )
