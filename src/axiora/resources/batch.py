# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import batch_identifiers_params, batch_fetch_financials_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.list_response_financial import ListResponseFinancial
from ..types.batch_identifiers_response import BatchIdentifiersResponse

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return BatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return BatchResourceWithStreamingResponse(self)

    def fetch_financials(
        self,
        *,
        codes: SequenceNotStr[str],
        fields: Optional[SequenceNotStr[str]] | Omit = omit,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseFinancial:
        """
        Fetch financials for multiple companies in one request.

        Accepts a mix of EDINET codes and securities codes. Returns up to `years` fiscal
        years per company, most recent first.

        Args:
          codes: List of EDINET or securities codes (1–100).

          fields: Financial fields to include. Null returns all fields.

          years: Number of fiscal years per company.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/batch/financials",
            body=maybe_transform(
                {
                    "codes": codes,
                    "fields": fields,
                    "years": years,
                },
                batch_fetch_financials_params.BatchFetchFinancialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListResponseFinancial,
        )

    def identifiers(
        self,
        *,
        ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchIdentifiersResponse:
        """
        Resolve up to 100 identifiers of any kind in one request.

        Every input is accounted for: identifiers that match no entity are named in
        `meta.unresolved` rather than dropped, so a caller can always reconcile the
        response against what they sent.

        Args:
          ids: Identifiers to resolve (1-100). Any mix of EDINET codes, securities codes and investor identifiers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/batch/identifiers",
            body=maybe_transform(
                {
                    "ids": ids,
                },
                batch_identifiers_params.BatchIdentifiersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchIdentifiersResponse,
        )


class AsyncBatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncBatchResourceWithStreamingResponse(self)

    async def fetch_financials(
        self,
        *,
        codes: SequenceNotStr[str],
        fields: Optional[SequenceNotStr[str]] | Omit = omit,
        years: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListResponseFinancial:
        """
        Fetch financials for multiple companies in one request.

        Accepts a mix of EDINET codes and securities codes. Returns up to `years` fiscal
        years per company, most recent first.

        Args:
          codes: List of EDINET or securities codes (1–100).

          fields: Financial fields to include. Null returns all fields.

          years: Number of fiscal years per company.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/batch/financials",
            body=await async_maybe_transform(
                {
                    "codes": codes,
                    "fields": fields,
                    "years": years,
                },
                batch_fetch_financials_params.BatchFetchFinancialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListResponseFinancial,
        )

    async def identifiers(
        self,
        *,
        ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchIdentifiersResponse:
        """
        Resolve up to 100 identifiers of any kind in one request.

        Every input is accounted for: identifiers that match no entity are named in
        `meta.unresolved` rather than dropped, so a caller can always reconcile the
        response against what they sent.

        Args:
          ids: Identifiers to resolve (1-100). Any mix of EDINET codes, securities codes and investor identifiers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/batch/identifiers",
            body=await async_maybe_transform(
                {
                    "ids": ids,
                },
                batch_identifiers_params.BatchIdentifiersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchIdentifiersResponse,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.fetch_financials = to_raw_response_wrapper(
            batch.fetch_financials,
        )
        self.identifiers = to_raw_response_wrapper(
            batch.identifiers,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.fetch_financials = async_to_raw_response_wrapper(
            batch.fetch_financials,
        )
        self.identifiers = async_to_raw_response_wrapper(
            batch.identifiers,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.fetch_financials = to_streamed_response_wrapper(
            batch.fetch_financials,
        )
        self.identifiers = to_streamed_response_wrapper(
            batch.identifiers,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.fetch_financials = async_to_streamed_response_wrapper(
            batch.fetch_financials,
        )
        self.identifiers = async_to_streamed_response_wrapper(
            batch.identifiers,
        )
