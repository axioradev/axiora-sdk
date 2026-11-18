# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import identifier_list_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.identifier_list_response import IdentifierListResponse

__all__ = ["IdentifiersResource", "AsyncIdentifiersResource"]


class IdentifiersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdentifiersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return IdentifiersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentifiersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return IdentifiersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentifierListResponse:
        """
        Resolve an identifier of unknown kind to the entity it names.

        Answers what the identifier IS (`name`, `entity_id`, cross-references) and
        where it WORKS (`roles`, and a `links` map from each role to the endpoint
        that serves it), so a caller holding an unfamiliar string reaches the data
        in one follow-up request instead of probing resources until one answers.

        Args:
          id: Any identifier form. Accepted forms: an EDINET code (E12345), a securities code (7203), a 13-digit corporate number (法人番号), or an investor identifier as returned by /v1/investors/search.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/identifiers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                    },
                    identifier_list_params.IdentifierListParams,
                ),
            ),
            cast_to=IdentifierListResponse,
        )


class AsyncIdentifiersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdentifiersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncIdentifiersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentifiersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncIdentifiersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentifierListResponse:
        """
        Resolve an identifier of unknown kind to the entity it names.

        Answers what the identifier IS (`name`, `entity_id`, cross-references) and
        where it WORKS (`roles`, and a `links` map from each role to the endpoint
        that serves it), so a caller holding an unfamiliar string reaches the data
        in one follow-up request instead of probing resources until one answers.

        Args:
          id: Any identifier form. Accepted forms: an EDINET code (E12345), a securities code (7203), a 13-digit corporate number (法人番号), or an investor identifier as returned by /v1/investors/search.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/identifiers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                    },
                    identifier_list_params.IdentifierListParams,
                ),
            ),
            cast_to=IdentifierListResponse,
        )


class IdentifiersResourceWithRawResponse:
    def __init__(self, identifiers: IdentifiersResource) -> None:
        self._identifiers = identifiers

        self.list = to_raw_response_wrapper(
            identifiers.list,
        )


class AsyncIdentifiersResourceWithRawResponse:
    def __init__(self, identifiers: AsyncIdentifiersResource) -> None:
        self._identifiers = identifiers

        self.list = async_to_raw_response_wrapper(
            identifiers.list,
        )


class IdentifiersResourceWithStreamingResponse:
    def __init__(self, identifiers: IdentifiersResource) -> None:
        self._identifiers = identifiers

        self.list = to_streamed_response_wrapper(
            identifiers.list,
        )


class AsyncIdentifiersResourceWithStreamingResponse:
    def __init__(self, identifiers: AsyncIdentifiersResource) -> None:
        self._identifiers = identifiers

        self.list = async_to_streamed_response_wrapper(
            identifiers.list,
        )
