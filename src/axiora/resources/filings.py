# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date, datetime

import httpx

from ..types import filing_list_params, filing_calendar_params, filing_retrieve_translations_params
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
from ..types.filing_list_response import FilingListResponse
from ..types.filing_calendar_response import FilingCalendarResponse
from ..types.filing_retrieve_response import FilingRetrieveResponse
from ..types.filing_retrieve_translations_response import FilingRetrieveTranslationsResponse

__all__ = ["FilingsResource", "AsyncFilingsResource"]


class FilingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return FilingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return FilingsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        doc_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilingRetrieveResponse:
        """
        Get Filing

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not doc_id:
            raise ValueError(f"Expected a non-empty value for `doc_id` but received {doc_id!r}")
        return self._get(
            f"/v1/filings/{doc_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilingRetrieveResponse,
        )

    def list(
        self,
        *,
        company_code: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        date_from: Union[str, date, None] | Omit = omit,
        date_to: Union[str, date, None] | Omit = omit,
        doc_type: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        since: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilingListResponse:
        """
        List Filings

        Args:
          company_code: EDINET or securities code

          cursor: Opaque cursor for keyset pagination

          date_from: Start date (inclusive)

          date_to: End date (inclusive)

          doc_type: Document type code

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          since: Return filings received after this timestamp (ISO 8601). Use the sync_token from
              a previous response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/filings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_code": company_code,
                        "cursor": cursor,
                        "date_from": date_from,
                        "date_to": date_to,
                        "doc_type": doc_type,
                        "limit": limit,
                        "offset": offset,
                        "since": since,
                    },
                    filing_list_params.FilingListParams,
                ),
            ),
            cast_to=FilingListResponse,
        )

    def calendar(
        self,
        *,
        month: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilingCalendarResponse:
        """
        Filing calendar: companies with period_end in the given month.

        Useful for knowing which companies' annual reports are expected. Returns
        companies grouped by their fiscal year end date.

        Args:
          month: Month in YYYY-MM format (e.g. 2025-06)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/filings/calendar",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"month": month}, filing_calendar_params.FilingCalendarParams),
            ),
            cast_to=FilingCalendarResponse,
        )

    def retrieve_translations(
        self,
        doc_id: str,
        *,
        section: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilingRetrieveTranslationsResponse:
        """
        Retrieve English translations for a filing's text sections.

        Args:
          section: Filter by section name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not doc_id:
            raise ValueError(f"Expected a non-empty value for `doc_id` but received {doc_id!r}")
        return self._get(
            f"/v1/filings/{doc_id}/translations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"section": section}, filing_retrieve_translations_params.FilingRetrieveTranslationsParams
                ),
            ),
            cast_to=FilingRetrieveTranslationsResponse,
        )


class AsyncFilingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFilingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncFilingsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        doc_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilingRetrieveResponse:
        """
        Get Filing

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not doc_id:
            raise ValueError(f"Expected a non-empty value for `doc_id` but received {doc_id!r}")
        return await self._get(
            f"/v1/filings/{doc_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilingRetrieveResponse,
        )

    async def list(
        self,
        *,
        company_code: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        date_from: Union[str, date, None] | Omit = omit,
        date_to: Union[str, date, None] | Omit = omit,
        doc_type: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        since: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilingListResponse:
        """
        List Filings

        Args:
          company_code: EDINET or securities code

          cursor: Opaque cursor for keyset pagination

          date_from: Start date (inclusive)

          date_to: End date (inclusive)

          doc_type: Document type code

          limit: Results per page

          offset: Results to skip (ignored when cursor is set)

          since: Return filings received after this timestamp (ISO 8601). Use the sync_token from
              a previous response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/filings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "company_code": company_code,
                        "cursor": cursor,
                        "date_from": date_from,
                        "date_to": date_to,
                        "doc_type": doc_type,
                        "limit": limit,
                        "offset": offset,
                        "since": since,
                    },
                    filing_list_params.FilingListParams,
                ),
            ),
            cast_to=FilingListResponse,
        )

    async def calendar(
        self,
        *,
        month: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilingCalendarResponse:
        """
        Filing calendar: companies with period_end in the given month.

        Useful for knowing which companies' annual reports are expected. Returns
        companies grouped by their fiscal year end date.

        Args:
          month: Month in YYYY-MM format (e.g. 2025-06)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/filings/calendar",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"month": month}, filing_calendar_params.FilingCalendarParams),
            ),
            cast_to=FilingCalendarResponse,
        )

    async def retrieve_translations(
        self,
        doc_id: str,
        *,
        section: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilingRetrieveTranslationsResponse:
        """
        Retrieve English translations for a filing's text sections.

        Args:
          section: Filter by section name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not doc_id:
            raise ValueError(f"Expected a non-empty value for `doc_id` but received {doc_id!r}")
        return await self._get(
            f"/v1/filings/{doc_id}/translations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"section": section}, filing_retrieve_translations_params.FilingRetrieveTranslationsParams
                ),
            ),
            cast_to=FilingRetrieveTranslationsResponse,
        )


class FilingsResourceWithRawResponse:
    def __init__(self, filings: FilingsResource) -> None:
        self._filings = filings

        self.retrieve = to_raw_response_wrapper(
            filings.retrieve,
        )
        self.list = to_raw_response_wrapper(
            filings.list,
        )
        self.calendar = to_raw_response_wrapper(
            filings.calendar,
        )
        self.retrieve_translations = to_raw_response_wrapper(
            filings.retrieve_translations,
        )


class AsyncFilingsResourceWithRawResponse:
    def __init__(self, filings: AsyncFilingsResource) -> None:
        self._filings = filings

        self.retrieve = async_to_raw_response_wrapper(
            filings.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            filings.list,
        )
        self.calendar = async_to_raw_response_wrapper(
            filings.calendar,
        )
        self.retrieve_translations = async_to_raw_response_wrapper(
            filings.retrieve_translations,
        )


class FilingsResourceWithStreamingResponse:
    def __init__(self, filings: FilingsResource) -> None:
        self._filings = filings

        self.retrieve = to_streamed_response_wrapper(
            filings.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            filings.list,
        )
        self.calendar = to_streamed_response_wrapper(
            filings.calendar,
        )
        self.retrieve_translations = to_streamed_response_wrapper(
            filings.retrieve_translations,
        )


class AsyncFilingsResourceWithStreamingResponse:
    def __init__(self, filings: AsyncFilingsResource) -> None:
        self._filings = filings

        self.retrieve = async_to_streamed_response_wrapper(
            filings.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            filings.list,
        )
        self.calendar = async_to_streamed_response_wrapper(
            filings.calendar,
        )
        self.retrieve_translations = async_to_streamed_response_wrapper(
            filings.retrieve_translations,
        )
