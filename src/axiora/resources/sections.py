# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.section_list_available_response import SectionListAvailableResponse

__all__ = ["SectionsResource", "AsyncSectionsResource"]


class SectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return SectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return SectionsResourceWithStreamingResponse(self)

    def list_available(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SectionListAvailableResponse:
        """List all section keys with their labels."""
        return self._get(
            "/v1/sections/available",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SectionListAvailableResponse,
        )


class AsyncSectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncSectionsResourceWithStreamingResponse(self)

    async def list_available(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SectionListAvailableResponse:
        """List all section keys with their labels."""
        return await self._get(
            "/v1/sections/available",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SectionListAvailableResponse,
        )


class SectionsResourceWithRawResponse:
    def __init__(self, sections: SectionsResource) -> None:
        self._sections = sections

        self.list_available = to_raw_response_wrapper(
            sections.list_available,
        )


class AsyncSectionsResourceWithRawResponse:
    def __init__(self, sections: AsyncSectionsResource) -> None:
        self._sections = sections

        self.list_available = async_to_raw_response_wrapper(
            sections.list_available,
        )


class SectionsResourceWithStreamingResponse:
    def __init__(self, sections: SectionsResource) -> None:
        self._sections = sections

        self.list_available = to_streamed_response_wrapper(
            sections.list_available,
        )


class AsyncSectionsResourceWithStreamingResponse:
    def __init__(self, sections: AsyncSectionsResource) -> None:
        self._sections = sections

        self.list_available = async_to_streamed_response_wrapper(
            sections.list_available,
        )
