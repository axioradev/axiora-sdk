# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.companies import buyback_list_params
from ...types.companies.buyback_list_response import BuybackListResponse
from ...types.companies.buyback_get_analysis_response import BuybackGetAnalysisResponse

__all__ = ["BuybacksResource", "AsyncBuybacksResource"]


class BuybacksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BuybacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return BuybacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BuybacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return BuybacksResourceWithStreamingResponse(self)

    def list(
        self,
        code: str,
        *,
        cursor: Optional[str] | Omit = omit,
        date_from: Union[str, date, None] | Omit = omit,
        date_to: Union[str, date, None] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuybackListResponse:
        """
        Get share buyback reports for a company.

        Returns monthly buyback status filings from EDINET (doc type 220), ordered
        newest first. Each record shows authorized limits, shares acquired in the month,
        cumulative progress, and treasury share holdings.

        Args:
          code: EDINET code (e.g. 'E02497') or securities code (e.g. '8001')

          cursor: Opaque cursor for keyset pagination

          date_from: Filter: reporting period ends on or after this date (YYYY-MM-DD)

          date_to: Filter: reporting period ends on or before this date (YYYY-MM-DD)

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/buybacks", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "date_from": date_from,
                        "date_to": date_to,
                        "limit": limit,
                        "offset": offset,
                    },
                    buyback_list_params.BuybackListParams,
                ),
            ),
            cast_to=BuybackListResponse,
        )

    def get_analysis(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuybackGetAnalysisResponse:
        """
        Get buyback execution analysis for a company.

        Returns per-program completion rates, pace metrics, and acceleration data.

        Args:
          code: EDINET code or securities code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/buybacks/analysis", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuybackGetAnalysisResponse,
        )


class AsyncBuybacksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBuybacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBuybacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBuybacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncBuybacksResourceWithStreamingResponse(self)

    async def list(
        self,
        code: str,
        *,
        cursor: Optional[str] | Omit = omit,
        date_from: Union[str, date, None] | Omit = omit,
        date_to: Union[str, date, None] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuybackListResponse:
        """
        Get share buyback reports for a company.

        Returns monthly buyback status filings from EDINET (doc type 220), ordered
        newest first. Each record shows authorized limits, shares acquired in the month,
        cumulative progress, and treasury share holdings.

        Args:
          code: EDINET code (e.g. 'E02497') or securities code (e.g. '8001')

          cursor: Opaque cursor for keyset pagination

          date_from: Filter: reporting period ends on or after this date (YYYY-MM-DD)

          date_to: Filter: reporting period ends on or before this date (YYYY-MM-DD)

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/buybacks", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "date_from": date_from,
                        "date_to": date_to,
                        "limit": limit,
                        "offset": offset,
                    },
                    buyback_list_params.BuybackListParams,
                ),
            ),
            cast_to=BuybackListResponse,
        )

    async def get_analysis(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuybackGetAnalysisResponse:
        """
        Get buyback execution analysis for a company.

        Returns per-program completion rates, pace metrics, and acceleration data.

        Args:
          code: EDINET code or securities code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/buybacks/analysis", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuybackGetAnalysisResponse,
        )


class BuybacksResourceWithRawResponse:
    def __init__(self, buybacks: BuybacksResource) -> None:
        self._buybacks = buybacks

        self.list = to_raw_response_wrapper(
            buybacks.list,
        )
        self.get_analysis = to_raw_response_wrapper(
            buybacks.get_analysis,
        )


class AsyncBuybacksResourceWithRawResponse:
    def __init__(self, buybacks: AsyncBuybacksResource) -> None:
        self._buybacks = buybacks

        self.list = async_to_raw_response_wrapper(
            buybacks.list,
        )
        self.get_analysis = async_to_raw_response_wrapper(
            buybacks.get_analysis,
        )


class BuybacksResourceWithStreamingResponse:
    def __init__(self, buybacks: BuybacksResource) -> None:
        self._buybacks = buybacks

        self.list = to_streamed_response_wrapper(
            buybacks.list,
        )
        self.get_analysis = to_streamed_response_wrapper(
            buybacks.get_analysis,
        )


class AsyncBuybacksResourceWithStreamingResponse:
    def __init__(self, buybacks: AsyncBuybacksResource) -> None:
        self._buybacks = buybacks

        self.list = async_to_streamed_response_wrapper(
            buybacks.list,
        )
        self.get_analysis = async_to_streamed_response_wrapper(
            buybacks.get_analysis,
        )
