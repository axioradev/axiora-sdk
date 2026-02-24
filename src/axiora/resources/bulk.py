# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import bulk_export_financials_csv_params, bulk_export_financials_json_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.bulk_export_financials_json_response import BulkExportFinancialsJsonResponse

__all__ = ["BulkResource", "AsyncBulkResource"]


class BulkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return BulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return BulkResourceWithStreamingResponse(self)

    def export_financials_csv(
        self,
        *,
        fields: Optional[str] | Omit = omit,
        fiscal_year: Optional[int] | Omit = omit,
        sector: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Export financial data as CSV.

        Returns companies' financial data in a flat CSV format suitable for analysis in
        pandas, Excel, or any data tool. At least one filter (sector or fiscal_year) is
        required.

        Args:
          fields: Comma-separated fields (default: all)

          fiscal_year: Filter by fiscal year

          sector: Filter by sector

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/v1/bulk/financials.csv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "fiscal_year": fiscal_year,
                        "sector": sector,
                    },
                    bulk_export_financials_csv_params.BulkExportFinancialsCsvParams,
                ),
            ),
            cast_to=NoneType,
        )

    def export_financials_json(
        self,
        *,
        fields: Optional[str] | Omit = omit,
        fiscal_year: Optional[int] | Omit = omit,
        sector: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkExportFinancialsJsonResponse:
        """
        Export financial data as JSON array.

        Returns companies' financial data as a JSON array, one object per company-year.
        At least one filter (sector or fiscal_year) is required.

        Args:
          fields: Comma-separated fields (default: all)

          fiscal_year: Filter by fiscal year

          sector: Filter by sector

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/bulk/financials.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "fiscal_year": fiscal_year,
                        "sector": sector,
                    },
                    bulk_export_financials_json_params.BulkExportFinancialsJsonParams,
                ),
            ),
            cast_to=BulkExportFinancialsJsonResponse,
        )


class AsyncBulkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncBulkResourceWithStreamingResponse(self)

    async def export_financials_csv(
        self,
        *,
        fields: Optional[str] | Omit = omit,
        fiscal_year: Optional[int] | Omit = omit,
        sector: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Export financial data as CSV.

        Returns companies' financial data in a flat CSV format suitable for analysis in
        pandas, Excel, or any data tool. At least one filter (sector or fiscal_year) is
        required.

        Args:
          fields: Comma-separated fields (default: all)

          fiscal_year: Filter by fiscal year

          sector: Filter by sector

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/v1/bulk/financials.csv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "fiscal_year": fiscal_year,
                        "sector": sector,
                    },
                    bulk_export_financials_csv_params.BulkExportFinancialsCsvParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def export_financials_json(
        self,
        *,
        fields: Optional[str] | Omit = omit,
        fiscal_year: Optional[int] | Omit = omit,
        sector: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkExportFinancialsJsonResponse:
        """
        Export financial data as JSON array.

        Returns companies' financial data as a JSON array, one object per company-year.
        At least one filter (sector or fiscal_year) is required.

        Args:
          fields: Comma-separated fields (default: all)

          fiscal_year: Filter by fiscal year

          sector: Filter by sector

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/bulk/financials.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "fiscal_year": fiscal_year,
                        "sector": sector,
                    },
                    bulk_export_financials_json_params.BulkExportFinancialsJsonParams,
                ),
            ),
            cast_to=BulkExportFinancialsJsonResponse,
        )


class BulkResourceWithRawResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.export_financials_csv = to_raw_response_wrapper(
            bulk.export_financials_csv,
        )
        self.export_financials_json = to_raw_response_wrapper(
            bulk.export_financials_json,
        )


class AsyncBulkResourceWithRawResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.export_financials_csv = async_to_raw_response_wrapper(
            bulk.export_financials_csv,
        )
        self.export_financials_json = async_to_raw_response_wrapper(
            bulk.export_financials_json,
        )


class BulkResourceWithStreamingResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.export_financials_csv = to_streamed_response_wrapper(
            bulk.export_financials_csv,
        )
        self.export_financials_json = to_streamed_response_wrapper(
            bulk.export_financials_json,
        )


class AsyncBulkResourceWithStreamingResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.export_financials_csv = async_to_streamed_response_wrapper(
            bulk.export_financials_csv,
        )
        self.export_financials_json = async_to_streamed_response_wrapper(
            bulk.export_financials_json,
        )
