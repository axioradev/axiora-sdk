# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import waitlist_join_params
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

__all__ = ["WaitlistResource", "AsyncWaitlistResource"]


class WaitlistResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WaitlistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return WaitlistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WaitlistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return WaitlistResourceWithStreamingResponse(self)

    def join(
        self,
        *,
        tier: str,
        email: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Join Waitlist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/waitlist",
            body=maybe_transform(
                {
                    "tier": tier,
                    "email": email,
                },
                waitlist_join_params.WaitlistJoinParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncWaitlistResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWaitlistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWaitlistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWaitlistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncWaitlistResourceWithStreamingResponse(self)

    async def join(
        self,
        *,
        tier: str,
        email: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Join Waitlist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/waitlist",
            body=await async_maybe_transform(
                {
                    "tier": tier,
                    "email": email,
                },
                waitlist_join_params.WaitlistJoinParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class WaitlistResourceWithRawResponse:
    def __init__(self, waitlist: WaitlistResource) -> None:
        self._waitlist = waitlist

        self.join = to_raw_response_wrapper(
            waitlist.join,
        )


class AsyncWaitlistResourceWithRawResponse:
    def __init__(self, waitlist: AsyncWaitlistResource) -> None:
        self._waitlist = waitlist

        self.join = async_to_raw_response_wrapper(
            waitlist.join,
        )


class WaitlistResourceWithStreamingResponse:
    def __init__(self, waitlist: WaitlistResource) -> None:
        self._waitlist = waitlist

        self.join = to_streamed_response_wrapper(
            waitlist.join,
        )


class AsyncWaitlistResourceWithStreamingResponse:
    def __init__(self, waitlist: AsyncWaitlistResource) -> None:
        self._waitlist = waitlist

        self.join = async_to_streamed_response_wrapper(
            waitlist.join,
        )
