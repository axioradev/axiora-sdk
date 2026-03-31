# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .trajectories import (
    TrajectoriesResource,
    AsyncTrajectoriesResource,
    TrajectoriesResourceWithRawResponse,
    AsyncTrajectoriesResourceWithRawResponse,
    TrajectoriesResourceWithStreamingResponse,
    AsyncTrajectoriesResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.companies import ownership_list_signals_params
from ....types.companies.ownership_get_chart_response import OwnershipGetChartResponse
from ....types.companies.ownership_get_network_response import OwnershipGetNetworkResponse
from ....types.companies.ownership_list_signals_response import OwnershipListSignalsResponse

__all__ = ["OwnershipResource", "AsyncOwnershipResource"]


class OwnershipResource(SyncAPIResource):
    @cached_property
    def trajectories(self) -> TrajectoriesResource:
        return TrajectoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> OwnershipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return OwnershipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OwnershipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return OwnershipResourceWithStreamingResponse(self)

    def get_chart(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnershipGetChartResponse:
        """
        Chart-ready ownership timeline for a company.

        Returns one series per filer with all points sorted by date. Merges trajectory
        data (entity-grouped) with raw shareholding filings for filers not covered by
        trajectories. Max 15 series.

        Args:
          code: Securities code (e.g. '7203') or EDINET code (e.g. 'E02144')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/ownership/chart", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OwnershipGetChartResponse,
        )

    def get_network(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnershipGetNetworkResponse:
        """
        Get cross-holding relationships for a specific company.

        Returns all cross-holding pairs involving this company.

        Args:
          code: Securities or EDINET code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/ownership/network", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OwnershipGetNetworkResponse,
        )

    def list_signals(
        self,
        code: str,
        *,
        cursor: Optional[str] | Omit = omit,
        include_trivial: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        signal_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnershipListSignalsResponse:
        """
        Get ownership signals for a specific company.

        By default excludes trivial signals (tier 3: new_position, exit_below_5pct).

        Args:
          code: Securities or EDINET code of the issuer

          cursor: Opaque cursor for keyset pagination

          include_trivial: Include tier 3 (trivial) signals

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          signal_type: Filter by signal type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/ownership/signals", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_trivial": include_trivial,
                        "limit": limit,
                        "offset": offset,
                        "signal_type": signal_type,
                    },
                    ownership_list_signals_params.OwnershipListSignalsParams,
                ),
            ),
            cast_to=OwnershipListSignalsResponse,
        )


class AsyncOwnershipResource(AsyncAPIResource):
    @cached_property
    def trajectories(self) -> AsyncTrajectoriesResource:
        return AsyncTrajectoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOwnershipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOwnershipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOwnershipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncOwnershipResourceWithStreamingResponse(self)

    async def get_chart(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnershipGetChartResponse:
        """
        Chart-ready ownership timeline for a company.

        Returns one series per filer with all points sorted by date. Merges trajectory
        data (entity-grouped) with raw shareholding filings for filers not covered by
        trajectories. Max 15 series.

        Args:
          code: Securities code (e.g. '7203') or EDINET code (e.g. 'E02144')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/ownership/chart", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OwnershipGetChartResponse,
        )

    async def get_network(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnershipGetNetworkResponse:
        """
        Get cross-holding relationships for a specific company.

        Returns all cross-holding pairs involving this company.

        Args:
          code: Securities or EDINET code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/ownership/network", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OwnershipGetNetworkResponse,
        )

    async def list_signals(
        self,
        code: str,
        *,
        cursor: Optional[str] | Omit = omit,
        include_trivial: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        signal_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnershipListSignalsResponse:
        """
        Get ownership signals for a specific company.

        By default excludes trivial signals (tier 3: new_position, exit_below_5pct).

        Args:
          code: Securities or EDINET code of the issuer

          cursor: Opaque cursor for keyset pagination

          include_trivial: Include tier 3 (trivial) signals

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          signal_type: Filter by signal type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/ownership/signals", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "include_trivial": include_trivial,
                        "limit": limit,
                        "offset": offset,
                        "signal_type": signal_type,
                    },
                    ownership_list_signals_params.OwnershipListSignalsParams,
                ),
            ),
            cast_to=OwnershipListSignalsResponse,
        )


class OwnershipResourceWithRawResponse:
    def __init__(self, ownership: OwnershipResource) -> None:
        self._ownership = ownership

        self.get_chart = to_raw_response_wrapper(
            ownership.get_chart,
        )
        self.get_network = to_raw_response_wrapper(
            ownership.get_network,
        )
        self.list_signals = to_raw_response_wrapper(
            ownership.list_signals,
        )

    @cached_property
    def trajectories(self) -> TrajectoriesResourceWithRawResponse:
        return TrajectoriesResourceWithRawResponse(self._ownership.trajectories)


class AsyncOwnershipResourceWithRawResponse:
    def __init__(self, ownership: AsyncOwnershipResource) -> None:
        self._ownership = ownership

        self.get_chart = async_to_raw_response_wrapper(
            ownership.get_chart,
        )
        self.get_network = async_to_raw_response_wrapper(
            ownership.get_network,
        )
        self.list_signals = async_to_raw_response_wrapper(
            ownership.list_signals,
        )

    @cached_property
    def trajectories(self) -> AsyncTrajectoriesResourceWithRawResponse:
        return AsyncTrajectoriesResourceWithRawResponse(self._ownership.trajectories)


class OwnershipResourceWithStreamingResponse:
    def __init__(self, ownership: OwnershipResource) -> None:
        self._ownership = ownership

        self.get_chart = to_streamed_response_wrapper(
            ownership.get_chart,
        )
        self.get_network = to_streamed_response_wrapper(
            ownership.get_network,
        )
        self.list_signals = to_streamed_response_wrapper(
            ownership.list_signals,
        )

    @cached_property
    def trajectories(self) -> TrajectoriesResourceWithStreamingResponse:
        return TrajectoriesResourceWithStreamingResponse(self._ownership.trajectories)


class AsyncOwnershipResourceWithStreamingResponse:
    def __init__(self, ownership: AsyncOwnershipResource) -> None:
        self._ownership = ownership

        self.get_chart = async_to_streamed_response_wrapper(
            ownership.get_chart,
        )
        self.get_network = async_to_streamed_response_wrapper(
            ownership.get_network,
        )
        self.list_signals = async_to_streamed_response_wrapper(
            ownership.list_signals,
        )

    @cached_property
    def trajectories(self) -> AsyncTrajectoriesResourceWithStreamingResponse:
        return AsyncTrajectoriesResourceWithStreamingResponse(self._ownership.trajectories)
