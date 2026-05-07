# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ontology_list_fields_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.ontology_list_fields_response import OntologyListFieldsResponse
from ..types.ontology_retrieve_field_response import OntologyRetrieveFieldResponse
from ..types.ontology_retrieve_version_response import OntologyRetrieveVersionResponse

__all__ = ["OntologyResource", "AsyncOntologyResource"]


class OntologyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OntologyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return OntologyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OntologyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return OntologyResourceWithStreamingResponse(self)

    def retrieve_version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OntologyRetrieveVersionResponse:
        """Return the current ontology semantic version.

        Bumped on breaking changes to field labeling, unit handling, or
        validation. Pin against this version when correlating historical
        responses.
        """
        return self._get(
            "/v1/ontology/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OntologyRetrieveVersionResponse,
        )

    def list_fields(
        self,
        *,
        category: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OntologyListFieldsResponse:
        """List all field definitions, optionally filtered by category.

        Args:
          category: Filter by field category. One of: 'income_statement', 'balance_sheet',
              'cash_flow', 'per_share', 'ratio', 'dei', 'other'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/ontology/fields",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"category": category},
                    ontology_list_fields_params.OntologyListFieldsParams,
                ),
            ),
            cast_to=OntologyListFieldsResponse,
        )

    def retrieve_field(
        self,
        field_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OntologyRetrieveFieldResponse:
        """Get the full definition for a single field.

        Returns the canonical field name, English/Japanese labels, category,
        and per-accounting-standard mappings (JP-GAAP / IFRS / US-GAAP) with
        any semantic notes about cross-standard differences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not field_name:
            raise ValueError(f"Expected a non-empty value for `field_name` but received {field_name!r}")
        return self._get(
            path_template("/v1/ontology/fields/{field_name}", field_name=field_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OntologyRetrieveFieldResponse,
        )


class AsyncOntologyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOntologyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOntologyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOntologyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncOntologyResourceWithStreamingResponse(self)

    async def retrieve_version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OntologyRetrieveVersionResponse:
        """Return the current ontology semantic version.

        Bumped on breaking changes to field labeling, unit handling, or
        validation. Pin against this version when correlating historical
        responses.
        """
        return await self._get(
            "/v1/ontology/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OntologyRetrieveVersionResponse,
        )

    async def list_fields(
        self,
        *,
        category: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OntologyListFieldsResponse:
        """List all field definitions, optionally filtered by category.

        Args:
          category: Filter by field category. One of: 'income_statement', 'balance_sheet',
              'cash_flow', 'per_share', 'ratio', 'dei', 'other'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/ontology/fields",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category": category},
                    ontology_list_fields_params.OntologyListFieldsParams,
                ),
            ),
            cast_to=OntologyListFieldsResponse,
        )

    async def retrieve_field(
        self,
        field_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OntologyRetrieveFieldResponse:
        """Get the full definition for a single field.

        Returns the canonical field name, English/Japanese labels, category,
        and per-accounting-standard mappings (JP-GAAP / IFRS / US-GAAP) with
        any semantic notes about cross-standard differences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not field_name:
            raise ValueError(f"Expected a non-empty value for `field_name` but received {field_name!r}")
        return await self._get(
            path_template("/v1/ontology/fields/{field_name}", field_name=field_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OntologyRetrieveFieldResponse,
        )


class OntologyResourceWithRawResponse:
    def __init__(self, ontology: OntologyResource) -> None:
        self._ontology = ontology

        self.retrieve_version = to_raw_response_wrapper(ontology.retrieve_version)
        self.list_fields = to_raw_response_wrapper(ontology.list_fields)
        self.retrieve_field = to_raw_response_wrapper(ontology.retrieve_field)


class AsyncOntologyResourceWithRawResponse:
    def __init__(self, ontology: AsyncOntologyResource) -> None:
        self._ontology = ontology

        self.retrieve_version = async_to_raw_response_wrapper(ontology.retrieve_version)
        self.list_fields = async_to_raw_response_wrapper(ontology.list_fields)
        self.retrieve_field = async_to_raw_response_wrapper(ontology.retrieve_field)


class OntologyResourceWithStreamingResponse:
    def __init__(self, ontology: OntologyResource) -> None:
        self._ontology = ontology

        self.retrieve_version = to_streamed_response_wrapper(ontology.retrieve_version)
        self.list_fields = to_streamed_response_wrapper(ontology.list_fields)
        self.retrieve_field = to_streamed_response_wrapper(ontology.retrieve_field)


class AsyncOntologyResourceWithStreamingResponse:
    def __init__(self, ontology: AsyncOntologyResource) -> None:
        self._ontology = ontology

        self.retrieve_version = async_to_streamed_response_wrapper(ontology.retrieve_version)
        self.list_fields = async_to_streamed_response_wrapper(ontology.list_fields)
        self.retrieve_field = async_to_streamed_response_wrapper(ontology.retrieve_field)
