# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import sector_retrieve_stats_params
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
from ..types.sector_list_response import SectorListResponse
from ..types.sector_retrieve_stats_response import SectorRetrieveStatsResponse

__all__ = ["SectorsResource", "AsyncSectorsResource"]


class SectorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#accessing-raw-response-data-eg-headers
        """
        return SectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#with_streaming_response
        """
        return SectorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SectorListResponse:
        """List all sectors with company counts."""
        return self._get(
            "/v1/sectors",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SectorListResponse,
        )

    def retrieve_stats(
        self,
        sector_name: str,
        *,
        fiscal_year: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SectorRetrieveStatsResponse:
        """
        Aggregate financial statistics for a sector.

        Returns median, average, min, max for key metrics across all companies in the
        sector.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sector_name:
            raise ValueError(f"Expected a non-empty value for `sector_name` but received {sector_name!r}")
        return self._get(
            f"/v1/sectors/{sector_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"fiscal_year": fiscal_year}, sector_retrieve_stats_params.SectorRetrieveStatsParams
                ),
            ),
            cast_to=SectorRetrieveStatsResponse,
        )


class AsyncSectorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#with_streaming_response
        """
        return AsyncSectorsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SectorListResponse:
        """List all sectors with company counts."""
        return await self._get(
            "/v1/sectors",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SectorListResponse,
        )

    async def retrieve_stats(
        self,
        sector_name: str,
        *,
        fiscal_year: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SectorRetrieveStatsResponse:
        """
        Aggregate financial statistics for a sector.

        Returns median, average, min, max for key metrics across all companies in the
        sector.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sector_name:
            raise ValueError(f"Expected a non-empty value for `sector_name` but received {sector_name!r}")
        return await self._get(
            f"/v1/sectors/{sector_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"fiscal_year": fiscal_year}, sector_retrieve_stats_params.SectorRetrieveStatsParams
                ),
            ),
            cast_to=SectorRetrieveStatsResponse,
        )


class SectorsResourceWithRawResponse:
    def __init__(self, sectors: SectorsResource) -> None:
        self._sectors = sectors

        self.list = to_raw_response_wrapper(
            sectors.list,
        )
        self.retrieve_stats = to_raw_response_wrapper(
            sectors.retrieve_stats,
        )


class AsyncSectorsResourceWithRawResponse:
    def __init__(self, sectors: AsyncSectorsResource) -> None:
        self._sectors = sectors

        self.list = async_to_raw_response_wrapper(
            sectors.list,
        )
        self.retrieve_stats = async_to_raw_response_wrapper(
            sectors.retrieve_stats,
        )


class SectorsResourceWithStreamingResponse:
    def __init__(self, sectors: SectorsResource) -> None:
        self._sectors = sectors

        self.list = to_streamed_response_wrapper(
            sectors.list,
        )
        self.retrieve_stats = to_streamed_response_wrapper(
            sectors.retrieve_stats,
        )


class AsyncSectorsResourceWithStreamingResponse:
    def __init__(self, sectors: AsyncSectorsResource) -> None:
        self._sectors = sectors

        self.list = async_to_streamed_response_wrapper(
            sectors.list,
        )
        self.retrieve_stats = async_to_streamed_response_wrapper(
            sectors.retrieve_stats,
        )
