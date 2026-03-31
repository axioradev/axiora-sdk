# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date

import httpx

from ..types import (
    ownership_list_movers_params,
    ownership_list_signals_params,
    ownership_list_cross_holdings_params,
    ownership_list_activist_campaigns_params,
    ownership_list_unwinding_scoreboard_params,
)
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
from ..types.ownership_list_movers_response import OwnershipListMoversResponse
from ..types.ownership_list_signals_response import OwnershipListSignalsResponse
from ..types.ownership_list_cross_holdings_response import OwnershipListCrossHoldingsResponse
from ..types.ownership_get_probability_table_response import OwnershipGetProbabilityTableResponse
from ..types.ownership_list_activist_campaigns_response import OwnershipListActivistCampaignsResponse
from ..types.ownership_list_unwinding_scoreboard_response import OwnershipListUnwindingScoreboardResponse

__all__ = ["OwnershipResource", "AsyncOwnershipResource"]


class OwnershipResource(SyncAPIResource):
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

    def get_probability_table(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnershipGetProbabilityTableResponse:
        """
        Get the full conditional completion table for ownership trajectories.

        Shows P(reaching threshold | current stake range, streak, purpose) computed from
        all historical trajectories. Uses pre-computed table when available.
        """
        return self._get(
            "/v1/ownership/probability-table",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OwnershipGetProbabilityTableResponse,
        )

    def list_activist_campaigns(
        self,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnershipListActivistCampaignsResponse:
        """
        Get active and recent activist campaigns.

        Returns filers with activist purpose or escalation signals, ranked by most
        recent activity.

        Args:
          limit: Max results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/ownership/activist-campaigns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit}, ownership_list_activist_campaigns_params.OwnershipListActivistCampaignsParams
                ),
            ),
            cast_to=OwnershipListActivistCampaignsResponse,
        )

    def list_cross_holdings(
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
    ) -> OwnershipListCrossHoldingsResponse:
        """
        Get all detected cross-holding pairs.

        Returns pairs where Company A holds >=5% of Company B and vice versa, sorted by
        combined holding ratio (largest first).

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
            "/v1/ownership/cross-holdings",
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
                    ownership_list_cross_holdings_params.OwnershipListCrossHoldingsParams,
                ),
            ),
            cast_to=OwnershipListCrossHoldingsResponse,
        )

    def list_movers(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        days: int | Omit = omit,
        limit: int | Omit = omit,
        min_delta_pct: Optional[float] | Omit = omit,
        offset: int | Omit = omit,
        trajectory_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnershipListMoversResponse:
        """
        Get market-wide biggest ownership moves in the last N days.

        Returns filers with the largest accumulations or exits.

        Args:
          cursor: Opaque cursor for keyset pagination

          days: Look back period in days

          limit: Results per page

          min_delta_pct: Minimum absolute delta percentage

          offset: Results to skip (ignored when cursor is set)

          trajectory_type: Filter: 'accumulating' or 'exiting'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/ownership/movers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "days": days,
                        "limit": limit,
                        "min_delta_pct": min_delta_pct,
                        "offset": offset,
                        "trajectory_type": trajectory_type,
                    },
                    ownership_list_movers_params.OwnershipListMoversParams,
                ),
            ),
            cast_to=OwnershipListMoversResponse,
        )

    def list_signals(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        date_from: Union[str, date, None] | Omit = omit,
        date_to: Union[str, date, None] | Omit = omit,
        filer_code: Optional[str] | Omit = omit,
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
        Get market-wide ownership signals.

        Returns detected signals ordered by date (newest first). By default excludes
        trivial signals (tier 3: new_position, exit_below_5pct). Pass
        include_trivial=true or filter by specific signal_type to see all.

        Args:
          cursor: Opaque cursor for keyset pagination

          date_from: Filter: detected_date on or after

          date_to: Filter: detected_date on or before

          filer_code: Filter by filer EDINET code (e.g. 'E03606' for SBI Holdings)

          include_trivial: Include tier 3 (trivial) signals like new_position and exit_below_5pct. Default
              returns only tier 1 (actionable) and tier 2 (informational).

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          signal_type: Filter: accumulation_streak, large_step_up, large_step_down, exit_below_5pct,
              activist_escalation, new_position, pace_acceleration, purpose_drift,
              coordinated_accumulation, systematic_exit

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/ownership/signals",
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
                        "filer_code": filer_code,
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

    def list_unwinding_scoreboard(
        self,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnershipListUnwindingScoreboardResponse:
        """
        Get cross-holdings that are being unwound.

        Returns cross-holding pairs where at least one side shows declining ownership,
        ranked by fastest decline.

        Args:
          limit: Max results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/ownership/unwinding-scoreboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit}, ownership_list_unwinding_scoreboard_params.OwnershipListUnwindingScoreboardParams
                ),
            ),
            cast_to=OwnershipListUnwindingScoreboardResponse,
        )


class AsyncOwnershipResource(AsyncAPIResource):
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

    async def get_probability_table(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnershipGetProbabilityTableResponse:
        """
        Get the full conditional completion table for ownership trajectories.

        Shows P(reaching threshold | current stake range, streak, purpose) computed from
        all historical trajectories. Uses pre-computed table when available.
        """
        return await self._get(
            "/v1/ownership/probability-table",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OwnershipGetProbabilityTableResponse,
        )

    async def list_activist_campaigns(
        self,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnershipListActivistCampaignsResponse:
        """
        Get active and recent activist campaigns.

        Returns filers with activist purpose or escalation signals, ranked by most
        recent activity.

        Args:
          limit: Max results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/ownership/activist-campaigns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit}, ownership_list_activist_campaigns_params.OwnershipListActivistCampaignsParams
                ),
            ),
            cast_to=OwnershipListActivistCampaignsResponse,
        )

    async def list_cross_holdings(
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
    ) -> OwnershipListCrossHoldingsResponse:
        """
        Get all detected cross-holding pairs.

        Returns pairs where Company A holds >=5% of Company B and vice versa, sorted by
        combined holding ratio (largest first).

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
            "/v1/ownership/cross-holdings",
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
                    ownership_list_cross_holdings_params.OwnershipListCrossHoldingsParams,
                ),
            ),
            cast_to=OwnershipListCrossHoldingsResponse,
        )

    async def list_movers(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        days: int | Omit = omit,
        limit: int | Omit = omit,
        min_delta_pct: Optional[float] | Omit = omit,
        offset: int | Omit = omit,
        trajectory_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnershipListMoversResponse:
        """
        Get market-wide biggest ownership moves in the last N days.

        Returns filers with the largest accumulations or exits.

        Args:
          cursor: Opaque cursor for keyset pagination

          days: Look back period in days

          limit: Results per page

          min_delta_pct: Minimum absolute delta percentage

          offset: Results to skip (ignored when cursor is set)

          trajectory_type: Filter: 'accumulating' or 'exiting'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/ownership/movers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "days": days,
                        "limit": limit,
                        "min_delta_pct": min_delta_pct,
                        "offset": offset,
                        "trajectory_type": trajectory_type,
                    },
                    ownership_list_movers_params.OwnershipListMoversParams,
                ),
            ),
            cast_to=OwnershipListMoversResponse,
        )

    async def list_signals(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        date_from: Union[str, date, None] | Omit = omit,
        date_to: Union[str, date, None] | Omit = omit,
        filer_code: Optional[str] | Omit = omit,
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
        Get market-wide ownership signals.

        Returns detected signals ordered by date (newest first). By default excludes
        trivial signals (tier 3: new_position, exit_below_5pct). Pass
        include_trivial=true or filter by specific signal_type to see all.

        Args:
          cursor: Opaque cursor for keyset pagination

          date_from: Filter: detected_date on or after

          date_to: Filter: detected_date on or before

          filer_code: Filter by filer EDINET code (e.g. 'E03606' for SBI Holdings)

          include_trivial: Include tier 3 (trivial) signals like new_position and exit_below_5pct. Default
              returns only tier 1 (actionable) and tier 2 (informational).

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          signal_type: Filter: accumulation_streak, large_step_up, large_step_down, exit_below_5pct,
              activist_escalation, new_position, pace_acceleration, purpose_drift,
              coordinated_accumulation, systematic_exit

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/ownership/signals",
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
                        "filer_code": filer_code,
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

    async def list_unwinding_scoreboard(
        self,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnershipListUnwindingScoreboardResponse:
        """
        Get cross-holdings that are being unwound.

        Returns cross-holding pairs where at least one side shows declining ownership,
        ranked by fastest decline.

        Args:
          limit: Max results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/ownership/unwinding-scoreboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit}, ownership_list_unwinding_scoreboard_params.OwnershipListUnwindingScoreboardParams
                ),
            ),
            cast_to=OwnershipListUnwindingScoreboardResponse,
        )


class OwnershipResourceWithRawResponse:
    def __init__(self, ownership: OwnershipResource) -> None:
        self._ownership = ownership

        self.get_probability_table = to_raw_response_wrapper(
            ownership.get_probability_table,
        )
        self.list_activist_campaigns = to_raw_response_wrapper(
            ownership.list_activist_campaigns,
        )
        self.list_cross_holdings = to_raw_response_wrapper(
            ownership.list_cross_holdings,
        )
        self.list_movers = to_raw_response_wrapper(
            ownership.list_movers,
        )
        self.list_signals = to_raw_response_wrapper(
            ownership.list_signals,
        )
        self.list_unwinding_scoreboard = to_raw_response_wrapper(
            ownership.list_unwinding_scoreboard,
        )


class AsyncOwnershipResourceWithRawResponse:
    def __init__(self, ownership: AsyncOwnershipResource) -> None:
        self._ownership = ownership

        self.get_probability_table = async_to_raw_response_wrapper(
            ownership.get_probability_table,
        )
        self.list_activist_campaigns = async_to_raw_response_wrapper(
            ownership.list_activist_campaigns,
        )
        self.list_cross_holdings = async_to_raw_response_wrapper(
            ownership.list_cross_holdings,
        )
        self.list_movers = async_to_raw_response_wrapper(
            ownership.list_movers,
        )
        self.list_signals = async_to_raw_response_wrapper(
            ownership.list_signals,
        )
        self.list_unwinding_scoreboard = async_to_raw_response_wrapper(
            ownership.list_unwinding_scoreboard,
        )


class OwnershipResourceWithStreamingResponse:
    def __init__(self, ownership: OwnershipResource) -> None:
        self._ownership = ownership

        self.get_probability_table = to_streamed_response_wrapper(
            ownership.get_probability_table,
        )
        self.list_activist_campaigns = to_streamed_response_wrapper(
            ownership.list_activist_campaigns,
        )
        self.list_cross_holdings = to_streamed_response_wrapper(
            ownership.list_cross_holdings,
        )
        self.list_movers = to_streamed_response_wrapper(
            ownership.list_movers,
        )
        self.list_signals = to_streamed_response_wrapper(
            ownership.list_signals,
        )
        self.list_unwinding_scoreboard = to_streamed_response_wrapper(
            ownership.list_unwinding_scoreboard,
        )


class AsyncOwnershipResourceWithStreamingResponse:
    def __init__(self, ownership: AsyncOwnershipResource) -> None:
        self._ownership = ownership

        self.get_probability_table = async_to_streamed_response_wrapper(
            ownership.get_probability_table,
        )
        self.list_activist_campaigns = async_to_streamed_response_wrapper(
            ownership.list_activist_campaigns,
        )
        self.list_cross_holdings = async_to_streamed_response_wrapper(
            ownership.list_cross_holdings,
        )
        self.list_movers = async_to_streamed_response_wrapper(
            ownership.list_movers,
        )
        self.list_signals = async_to_streamed_response_wrapper(
            ownership.list_signals,
        )
        self.list_unwinding_scoreboard = async_to_streamed_response_wrapper(
            ownership.list_unwinding_scoreboard,
        )
