# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import translation_search_params
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
from ..types.translation_search_response import TranslationSearchResponse

__all__ = ["TranslationsResource", "AsyncTranslationsResource"]


class TranslationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TranslationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#accessing-raw-response-data-eg-headers
        """
        return TranslationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranslationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#with_streaming_response
        """
        return TranslationsResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        q: str,
        fiscal_year: Optional[int] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        section: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranslationSearchResponse:
        """
        Full-text search across translated filing content.

        Returns relevant matches with highlighted snippets, ranked by relevance. Uses
        PostgreSQL tsvector/tsquery for full-text search.

        Args:
          q: Search query

          fiscal_year: Filter by fiscal year

          section: Filter by section

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/translations/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "fiscal_year": fiscal_year,
                        "limit": limit,
                        "offset": offset,
                        "section": section,
                    },
                    translation_search_params.TranslationSearchParams,
                ),
            ),
            cast_to=TranslationSearchResponse,
        )


class AsyncTranslationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTranslationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTranslationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranslationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/axiora-python#with_streaming_response
        """
        return AsyncTranslationsResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        q: str,
        fiscal_year: Optional[int] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        section: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranslationSearchResponse:
        """
        Full-text search across translated filing content.

        Returns relevant matches with highlighted snippets, ranked by relevance. Uses
        PostgreSQL tsvector/tsquery for full-text search.

        Args:
          q: Search query

          fiscal_year: Filter by fiscal year

          section: Filter by section

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/translations/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "fiscal_year": fiscal_year,
                        "limit": limit,
                        "offset": offset,
                        "section": section,
                    },
                    translation_search_params.TranslationSearchParams,
                ),
            ),
            cast_to=TranslationSearchResponse,
        )


class TranslationsResourceWithRawResponse:
    def __init__(self, translations: TranslationsResource) -> None:
        self._translations = translations

        self.search = to_raw_response_wrapper(
            translations.search,
        )


class AsyncTranslationsResourceWithRawResponse:
    def __init__(self, translations: AsyncTranslationsResource) -> None:
        self._translations = translations

        self.search = async_to_raw_response_wrapper(
            translations.search,
        )


class TranslationsResourceWithStreamingResponse:
    def __init__(self, translations: TranslationsResource) -> None:
        self._translations = translations

        self.search = to_streamed_response_wrapper(
            translations.search,
        )


class AsyncTranslationsResourceWithStreamingResponse:
    def __init__(self, translations: AsyncTranslationsResource) -> None:
        self._translations = translations

        self.search = async_to_streamed_response_wrapper(
            translations.search,
        )
