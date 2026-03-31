# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import relationship_list_interlocks_params
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
from ..types.relationship_list_interlocks_response import RelationshipListInterlocksResponse

__all__ = ["RelationshipsResource", "AsyncRelationshipsResource"]


class RelationshipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelationshipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return RelationshipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelationshipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return RelationshipsResourceWithStreamingResponse(self)

    def list_interlocks(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        fiscal_year: Optional[int] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipListInterlocksResponse:
        """
        Get market-wide board interlocks.

        Returns all directors who serve on multiple company boards in a given fiscal
        year, paginated. Directors with high confidence (DOB match) are listed first.

        Args:
          cursor: Opaque cursor for keyset pagination

          fiscal_year: Fiscal year. Defaults to latest available.

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/relationships/interlocks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "fiscal_year": fiscal_year,
                        "limit": limit,
                        "offset": offset,
                    },
                    relationship_list_interlocks_params.RelationshipListInterlocksParams,
                ),
            ),
            cast_to=RelationshipListInterlocksResponse,
        )


class AsyncRelationshipsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelationshipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRelationshipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelationshipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncRelationshipsResourceWithStreamingResponse(self)

    async def list_interlocks(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        fiscal_year: Optional[int] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipListInterlocksResponse:
        """
        Get market-wide board interlocks.

        Returns all directors who serve on multiple company boards in a given fiscal
        year, paginated. Directors with high confidence (DOB match) are listed first.

        Args:
          cursor: Opaque cursor for keyset pagination

          fiscal_year: Fiscal year. Defaults to latest available.

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/relationships/interlocks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "fiscal_year": fiscal_year,
                        "limit": limit,
                        "offset": offset,
                    },
                    relationship_list_interlocks_params.RelationshipListInterlocksParams,
                ),
            ),
            cast_to=RelationshipListInterlocksResponse,
        )


class RelationshipsResourceWithRawResponse:
    def __init__(self, relationships: RelationshipsResource) -> None:
        self._relationships = relationships

        self.list_interlocks = to_raw_response_wrapper(
            relationships.list_interlocks,
        )


class AsyncRelationshipsResourceWithRawResponse:
    def __init__(self, relationships: AsyncRelationshipsResource) -> None:
        self._relationships = relationships

        self.list_interlocks = async_to_raw_response_wrapper(
            relationships.list_interlocks,
        )


class RelationshipsResourceWithStreamingResponse:
    def __init__(self, relationships: RelationshipsResource) -> None:
        self._relationships = relationships

        self.list_interlocks = to_streamed_response_wrapper(
            relationships.list_interlocks,
        )


class AsyncRelationshipsResourceWithStreamingResponse:
    def __init__(self, relationships: AsyncRelationshipsResource) -> None:
        self._relationships = relationships

        self.list_interlocks = async_to_streamed_response_wrapper(
            relationships.list_interlocks,
        )
