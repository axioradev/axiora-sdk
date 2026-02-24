# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import screen_retrieve_params
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
from ..types.screen_retrieve_response import ScreenRetrieveResponse

__all__ = ["ScreenResource", "AsyncScreenResource"]


class ScreenResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScreenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#accessing-raw-response-data-eg-headers
        """
        return ScreenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScreenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#with_streaming_response
        """
        return ScreenResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        fiscal_year: Optional[int] | Omit = omit,
        limit: int | Omit = omit,
        net_income_max: Optional[int] | Omit = omit,
        net_income_min: Optional[int] | Omit = omit,
        offset: int | Omit = omit,
        operating_income_max: Optional[int] | Omit = omit,
        operating_income_min: Optional[int] | Omit = omit,
        revenue_max: Optional[int] | Omit = omit,
        revenue_min: Optional[int] | Omit = omit,
        roa_max: Optional[float] | Omit = omit,
        roa_min: Optional[float] | Omit = omit,
        roe_max: Optional[float] | Omit = omit,
        roe_min: Optional[float] | Omit = omit,
        sector: Optional[str] | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenRetrieveResponse:
        """
        Screen Companies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/screen",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fiscal_year": fiscal_year,
                        "limit": limit,
                        "net_income_max": net_income_max,
                        "net_income_min": net_income_min,
                        "offset": offset,
                        "operating_income_max": operating_income_max,
                        "operating_income_min": operating_income_min,
                        "revenue_max": revenue_max,
                        "revenue_min": revenue_min,
                        "roa_max": roa_max,
                        "roa_min": roa_min,
                        "roe_max": roe_max,
                        "roe_min": roe_min,
                        "sector": sector,
                        "sort": sort,
                    },
                    screen_retrieve_params.ScreenRetrieveParams,
                ),
            ),
            cast_to=ScreenRetrieveResponse,
        )


class AsyncScreenResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScreenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScreenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScreenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#with_streaming_response
        """
        return AsyncScreenResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        fiscal_year: Optional[int] | Omit = omit,
        limit: int | Omit = omit,
        net_income_max: Optional[int] | Omit = omit,
        net_income_min: Optional[int] | Omit = omit,
        offset: int | Omit = omit,
        operating_income_max: Optional[int] | Omit = omit,
        operating_income_min: Optional[int] | Omit = omit,
        revenue_max: Optional[int] | Omit = omit,
        revenue_min: Optional[int] | Omit = omit,
        roa_max: Optional[float] | Omit = omit,
        roa_min: Optional[float] | Omit = omit,
        roe_max: Optional[float] | Omit = omit,
        roe_min: Optional[float] | Omit = omit,
        sector: Optional[str] | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenRetrieveResponse:
        """
        Screen Companies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/screen",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fiscal_year": fiscal_year,
                        "limit": limit,
                        "net_income_max": net_income_max,
                        "net_income_min": net_income_min,
                        "offset": offset,
                        "operating_income_max": operating_income_max,
                        "operating_income_min": operating_income_min,
                        "revenue_max": revenue_max,
                        "revenue_min": revenue_min,
                        "roa_max": roa_max,
                        "roa_min": roa_min,
                        "roe_max": roe_max,
                        "roe_min": roe_min,
                        "sector": sector,
                        "sort": sort,
                    },
                    screen_retrieve_params.ScreenRetrieveParams,
                ),
            ),
            cast_to=ScreenRetrieveResponse,
        )


class ScreenResourceWithRawResponse:
    def __init__(self, screen: ScreenResource) -> None:
        self._screen = screen

        self.retrieve = to_raw_response_wrapper(
            screen.retrieve,
        )


class AsyncScreenResourceWithRawResponse:
    def __init__(self, screen: AsyncScreenResource) -> None:
        self._screen = screen

        self.retrieve = async_to_raw_response_wrapper(
            screen.retrieve,
        )


class ScreenResourceWithStreamingResponse:
    def __init__(self, screen: ScreenResource) -> None:
        self._screen = screen

        self.retrieve = to_streamed_response_wrapper(
            screen.retrieve,
        )


class AsyncScreenResourceWithStreamingResponse:
    def __init__(self, screen: AsyncScreenResource) -> None:
        self._screen = screen

        self.retrieve = async_to_streamed_response_wrapper(
            screen.retrieve,
        )
