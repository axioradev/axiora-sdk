# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .mcp import (
    McpResource,
    AsyncMcpResource,
    McpResourceWithRawResponse,
    AsyncMcpResourceWithRawResponse,
    McpResourceWithStreamingResponse,
    AsyncMcpResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["WellKnownResource", "AsyncWellKnownResource"]


class WellKnownResource(SyncAPIResource):
    @cached_property
    def mcp(self) -> McpResource:
        return McpResource(self._client)

    @cached_property
    def with_raw_response(self) -> WellKnownResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return WellKnownResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WellKnownResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return WellKnownResourceWithStreamingResponse(self)

    def retrieve_authorization_server_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """RFC 8414 Authorization Server Metadata."""
        return self._get(
            "/.well-known/oauth-authorization-server",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_protected_resource_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """RFC 9728 Protected Resource Metadata."""
        return self._get(
            "/.well-known/oauth-protected-resource",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncWellKnownResource(AsyncAPIResource):
    @cached_property
    def mcp(self) -> AsyncMcpResource:
        return AsyncMcpResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWellKnownResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWellKnownResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWellKnownResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncWellKnownResourceWithStreamingResponse(self)

    async def retrieve_authorization_server_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """RFC 8414 Authorization Server Metadata."""
        return await self._get(
            "/.well-known/oauth-authorization-server",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_protected_resource_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """RFC 9728 Protected Resource Metadata."""
        return await self._get(
            "/.well-known/oauth-protected-resource",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class WellKnownResourceWithRawResponse:
    def __init__(self, well_known: WellKnownResource) -> None:
        self._well_known = well_known

        self.retrieve_authorization_server_metadata = to_raw_response_wrapper(
            well_known.retrieve_authorization_server_metadata,
        )
        self.retrieve_protected_resource_metadata = to_raw_response_wrapper(
            well_known.retrieve_protected_resource_metadata,
        )

    @cached_property
    def mcp(self) -> McpResourceWithRawResponse:
        return McpResourceWithRawResponse(self._well_known.mcp)


class AsyncWellKnownResourceWithRawResponse:
    def __init__(self, well_known: AsyncWellKnownResource) -> None:
        self._well_known = well_known

        self.retrieve_authorization_server_metadata = async_to_raw_response_wrapper(
            well_known.retrieve_authorization_server_metadata,
        )
        self.retrieve_protected_resource_metadata = async_to_raw_response_wrapper(
            well_known.retrieve_protected_resource_metadata,
        )

    @cached_property
    def mcp(self) -> AsyncMcpResourceWithRawResponse:
        return AsyncMcpResourceWithRawResponse(self._well_known.mcp)


class WellKnownResourceWithStreamingResponse:
    def __init__(self, well_known: WellKnownResource) -> None:
        self._well_known = well_known

        self.retrieve_authorization_server_metadata = to_streamed_response_wrapper(
            well_known.retrieve_authorization_server_metadata,
        )
        self.retrieve_protected_resource_metadata = to_streamed_response_wrapper(
            well_known.retrieve_protected_resource_metadata,
        )

    @cached_property
    def mcp(self) -> McpResourceWithStreamingResponse:
        return McpResourceWithStreamingResponse(self._well_known.mcp)


class AsyncWellKnownResourceWithStreamingResponse:
    def __init__(self, well_known: AsyncWellKnownResource) -> None:
        self._well_known = well_known

        self.retrieve_authorization_server_metadata = async_to_streamed_response_wrapper(
            well_known.retrieve_authorization_server_metadata,
        )
        self.retrieve_protected_resource_metadata = async_to_streamed_response_wrapper(
            well_known.retrieve_protected_resource_metadata,
        )

    @cached_property
    def mcp(self) -> AsyncMcpResourceWithStreamingResponse:
        return AsyncMcpResourceWithStreamingResponse(self._well_known.mcp)
