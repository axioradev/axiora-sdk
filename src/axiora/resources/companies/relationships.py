# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.companies import relationship_list_interlocks_params, relationship_get_relationships_params
from ...types.companies.relationship_list_interlocks_response import RelationshipListInterlocksResponse
from ...types.companies.relationship_get_relationships_response import RelationshipGetRelationshipsResponse

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

    def get_relationships(
        self,
        code: str,
        *,
        fiscal_year: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipGetRelationshipsResponse:
        """
        Get unified relationship graph for a company.

        Returns board members, major shareholders, holdings by this entity, board
        interlocks (directors serving on multiple boards), and cross-holdings.

        Args:
          code: EDINET code (e.g. 'E02144') or securities code (e.g. '7203')

          fiscal_year: Fiscal year for board data. Defaults to latest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/relationships", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"fiscal_year": fiscal_year},
                    relationship_get_relationships_params.RelationshipGetRelationshipsParams,
                ),
            ),
            cast_to=RelationshipGetRelationshipsResponse,
        )

    def list_interlocks(
        self,
        code: str,
        *,
        fiscal_year: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipListInterlocksResponse:
        """
        Get board interlocks for a company.

        Returns directors who serve on this company's board AND at least one other
        company's board in the same fiscal year.

        Args:
          code: EDINET code (e.g. 'E02144') or securities code (e.g. '7203')

          fiscal_year: Fiscal year. Defaults to latest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v1/companies/{code}/relationships/interlocks", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"fiscal_year": fiscal_year}, relationship_list_interlocks_params.RelationshipListInterlocksParams
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

    async def get_relationships(
        self,
        code: str,
        *,
        fiscal_year: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipGetRelationshipsResponse:
        """
        Get unified relationship graph for a company.

        Returns board members, major shareholders, holdings by this entity, board
        interlocks (directors serving on multiple boards), and cross-holdings.

        Args:
          code: EDINET code (e.g. 'E02144') or securities code (e.g. '7203')

          fiscal_year: Fiscal year for board data. Defaults to latest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/relationships", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"fiscal_year": fiscal_year},
                    relationship_get_relationships_params.RelationshipGetRelationshipsParams,
                ),
            ),
            cast_to=RelationshipGetRelationshipsResponse,
        )

    async def list_interlocks(
        self,
        code: str,
        *,
        fiscal_year: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipListInterlocksResponse:
        """
        Get board interlocks for a company.

        Returns directors who serve on this company's board AND at least one other
        company's board in the same fiscal year.

        Args:
          code: EDINET code (e.g. 'E02144') or securities code (e.g. '7203')

          fiscal_year: Fiscal year. Defaults to latest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v1/companies/{code}/relationships/interlocks", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"fiscal_year": fiscal_year}, relationship_list_interlocks_params.RelationshipListInterlocksParams
                ),
            ),
            cast_to=RelationshipListInterlocksResponse,
        )


class RelationshipsResourceWithRawResponse:
    def __init__(self, relationships: RelationshipsResource) -> None:
        self._relationships = relationships

        self.get_relationships = to_raw_response_wrapper(
            relationships.get_relationships,
        )
        self.list_interlocks = to_raw_response_wrapper(
            relationships.list_interlocks,
        )


class AsyncRelationshipsResourceWithRawResponse:
    def __init__(self, relationships: AsyncRelationshipsResource) -> None:
        self._relationships = relationships

        self.get_relationships = async_to_raw_response_wrapper(
            relationships.get_relationships,
        )
        self.list_interlocks = async_to_raw_response_wrapper(
            relationships.list_interlocks,
        )


class RelationshipsResourceWithStreamingResponse:
    def __init__(self, relationships: RelationshipsResource) -> None:
        self._relationships = relationships

        self.get_relationships = to_streamed_response_wrapper(
            relationships.get_relationships,
        )
        self.list_interlocks = to_streamed_response_wrapper(
            relationships.list_interlocks,
        )


class AsyncRelationshipsResourceWithStreamingResponse:
    def __init__(self, relationships: AsyncRelationshipsResource) -> None:
        self._relationships = relationships

        self.get_relationships = async_to_streamed_response_wrapper(
            relationships.get_relationships,
        )
        self.list_interlocks = async_to_streamed_response_wrapper(
            relationships.list_interlocks,
        )
