# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date

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
from ...._base_client import make_request_options
from ....types.companies.ownership import trajectory_list_params
from ....types.companies.ownership.trajectory_list_response import TrajectoryListResponse
from ....types.companies.ownership.trajectory_get_probabilities_response import TrajectoryGetProbabilitiesResponse
from ....types.companies.ownership.trajectory_get_filer_trajectory_response import TrajectoryGetFilerTrajectoryResponse

__all__ = ["TrajectoriesResource", "AsyncTrajectoriesResource"]


class TrajectoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrajectoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return TrajectoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrajectoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return TrajectoriesResourceWithStreamingResponse(self)

    def list(
        self,
        code: str,
        *,
        cursor: Optional[str] | Omit = omit,
        date_from: Union[str, date, None] | Omit = omit,
        date_to: Union[str, date, None] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        trajectory_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrajectoryListResponse:
        """
        Get all filer trajectories for an issuer.

        Returns ownership trajectory data for each filer that holds >=5% of the company.

        Args:
          code: Securities code (e.g. '7203') or EDINET code (e.g. 'E02144')

          cursor: Opaque cursor for keyset pagination

          date_from: Filter: last_base_date on or after

          date_to: Filter: last_base_date on or before

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          trajectory_type: Filter: accumulating, exiting, stable, new_position

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/ownership/trajectories", code=code),
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
                        "trajectory_type": trajectory_type,
                    },
                    trajectory_list_params.TrajectoryListParams,
                ),
            ),
            cast_to=TrajectoryListResponse,
        )

    def get_filer_trajectory(
        self,
        filer_code: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrajectoryGetFilerTrajectoryResponse:
        """
        Get a single filer's trajectory for an issuer, with full point history.

        Args:
          code: Securities or EDINET code of the issuer

          filer_code: EDINET code of the filer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        if not filer_code:
            raise ValueError(f"Expected a non-empty value for `filer_code` but received {filer_code!r}")
        return self._get(
            path_template("/v1/companies/{code}/ownership/trajectories/{filer_code}", code=code, filer_code=filer_code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrajectoryGetFilerTrajectoryResponse,
        )

    def get_probabilities(
        self,
        filer_code: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrajectoryGetProbabilitiesResponse:
        """
        Get conditional probabilities for a specific active trajectory.

        Returns P(reaching 10%, 20%, 33%) and P(exit within 6 months) based on the
        filer's current stake, streak, and purpose compared to historical data. Uses
        CoxPH survival model when available, falls back to base rates.

        Args:
          code: Securities or EDINET code of the issuer

          filer_code: EDINET code of the filer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        if not filer_code:
            raise ValueError(f"Expected a non-empty value for `filer_code` but received {filer_code!r}")
        return self._get(
            path_template(
                "/v1/companies/{code}/ownership/trajectories/{filer_code}/probabilities",
                code=code,
                filer_code=filer_code,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrajectoryGetProbabilitiesResponse,
        )


class AsyncTrajectoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrajectoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTrajectoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrajectoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncTrajectoriesResourceWithStreamingResponse(self)

    async def list(
        self,
        code: str,
        *,
        cursor: Optional[str] | Omit = omit,
        date_from: Union[str, date, None] | Omit = omit,
        date_to: Union[str, date, None] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        trajectory_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrajectoryListResponse:
        """
        Get all filer trajectories for an issuer.

        Returns ownership trajectory data for each filer that holds >=5% of the company.

        Args:
          code: Securities code (e.g. '7203') or EDINET code (e.g. 'E02144')

          cursor: Opaque cursor for keyset pagination

          date_from: Filter: last_base_date on or after

          date_to: Filter: last_base_date on or before

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          trajectory_type: Filter: accumulating, exiting, stable, new_position

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/ownership/trajectories", code=code),
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
                        "trajectory_type": trajectory_type,
                    },
                    trajectory_list_params.TrajectoryListParams,
                ),
            ),
            cast_to=TrajectoryListResponse,
        )

    async def get_filer_trajectory(
        self,
        filer_code: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrajectoryGetFilerTrajectoryResponse:
        """
        Get a single filer's trajectory for an issuer, with full point history.

        Args:
          code: Securities or EDINET code of the issuer

          filer_code: EDINET code of the filer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        if not filer_code:
            raise ValueError(f"Expected a non-empty value for `filer_code` but received {filer_code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/ownership/trajectories/{filer_code}", code=code, filer_code=filer_code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrajectoryGetFilerTrajectoryResponse,
        )

    async def get_probabilities(
        self,
        filer_code: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrajectoryGetProbabilitiesResponse:
        """
        Get conditional probabilities for a specific active trajectory.

        Returns P(reaching 10%, 20%, 33%) and P(exit within 6 months) based on the
        filer's current stake, streak, and purpose compared to historical data. Uses
        CoxPH survival model when available, falls back to base rates.

        Args:
          code: Securities or EDINET code of the issuer

          filer_code: EDINET code of the filer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        if not filer_code:
            raise ValueError(f"Expected a non-empty value for `filer_code` but received {filer_code!r}")
        return await self._get(
            path_template(
                "/v1/companies/{code}/ownership/trajectories/{filer_code}/probabilities",
                code=code,
                filer_code=filer_code,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrajectoryGetProbabilitiesResponse,
        )


class TrajectoriesResourceWithRawResponse:
    def __init__(self, trajectories: TrajectoriesResource) -> None:
        self._trajectories = trajectories

        self.list = to_raw_response_wrapper(
            trajectories.list,
        )
        self.get_filer_trajectory = to_raw_response_wrapper(
            trajectories.get_filer_trajectory,
        )
        self.get_probabilities = to_raw_response_wrapper(
            trajectories.get_probabilities,
        )


class AsyncTrajectoriesResourceWithRawResponse:
    def __init__(self, trajectories: AsyncTrajectoriesResource) -> None:
        self._trajectories = trajectories

        self.list = async_to_raw_response_wrapper(
            trajectories.list,
        )
        self.get_filer_trajectory = async_to_raw_response_wrapper(
            trajectories.get_filer_trajectory,
        )
        self.get_probabilities = async_to_raw_response_wrapper(
            trajectories.get_probabilities,
        )


class TrajectoriesResourceWithStreamingResponse:
    def __init__(self, trajectories: TrajectoriesResource) -> None:
        self._trajectories = trajectories

        self.list = to_streamed_response_wrapper(
            trajectories.list,
        )
        self.get_filer_trajectory = to_streamed_response_wrapper(
            trajectories.get_filer_trajectory,
        )
        self.get_probabilities = to_streamed_response_wrapper(
            trajectories.get_probabilities,
        )


class AsyncTrajectoriesResourceWithStreamingResponse:
    def __init__(self, trajectories: AsyncTrajectoriesResource) -> None:
        self._trajectories = trajectories

        self.list = async_to_streamed_response_wrapper(
            trajectories.list,
        )
        self.get_filer_trajectory = async_to_streamed_response_wrapper(
            trajectories.get_filer_trajectory,
        )
        self.get_probabilities = async_to_streamed_response_wrapper(
            trajectories.get_probabilities,
        )
