# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    v2_search_params,
    v2_list_facts_params,
    v2_list_changes_params,
    v2_list_filings_params,
    v2_list_entities_params,
    v2_list_positions_params,
    v2_retrieve_entity_params,
    v2_retrieve_holder_params,
    v2_retrieve_company_params,
)
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
from ..types.v2_search_response import V2SearchResponse
from ..types.v2_list_facts_response import V2ListFactsResponse
from ..types.v2_list_types_response import V2ListTypesResponse
from ..types.v2_list_changes_response import V2ListChangesResponse
from ..types.v2_list_filings_response import V2ListFilingsResponse
from ..types.v2_list_entities_response import V2ListEntitiesResponse
from ..types.v2_list_positions_response import V2ListPositionsResponse
from ..types.v2_retrieve_entity_response import V2RetrieveEntityResponse
from ..types.v2_retrieve_filing_response import V2RetrieveFilingResponse
from ..types.v2_retrieve_holder_response import V2RetrieveHolderResponse
from ..types.v2_retrieve_company_response import V2RetrieveCompanyResponse

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)

    def list_changes(
        self,
        *,
        since: str,
        type: object | Omit = omit,
        entity: object | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListChangesResponse:
        """
        What became known since a time, newest first, across the types the key may read.

        Args:
          since: Facts that became known after this time (ISO 8601).

          type: One fact type; all readable types if omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/changes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "since": since,
                        "type": type,
                        "entity": entity,
                        "limit": limit,
                    },
                    v2_list_changes_params.V2ListChangesParams,
                ),
            ),
            cast_to=V2ListChangesResponse,
        )

    def retrieve_company(
        self,
        code: str,
        *,
        include: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveCompanyResponse:
        """
        A company, with what you ask for.

        Args:
          include: holders,trends,financials,votes,board,signals

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/v2/companies/{code}", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include": include,
                    },
                    v2_retrieve_company_params.V2RetrieveCompanyParams,
                ),
            ),
            cast_to=V2RetrieveCompanyResponse,
        )

    def list_entities(
        self,
        *,
        type: str,
        q: object | Omit = omit,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListEntitiesResponse:
        """
        Entities of one type, optionally filtered by name or code.

        Args:
          type: Entity type: company, holder or filing.

          q: Name or code contains.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/entities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "type": type,
                        "q": q,
                        "limit": limit,
                        "cursor": cursor,
                    },
                    v2_list_entities_params.V2ListEntitiesParams,
                ),
            ),
            cast_to=V2ListEntitiesResponse,
        )

    def retrieve_entity(
        self,
        entity_id: str,
        *,
        include: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveEntityResponse:
        """
        One entity, optionally with facts of the listed types.

        Args:
          include: Comma-separated fact types; 50 each.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            path_template("/v2/entities/{entity_id}", entity_id=entity_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include": include,
                    },
                    v2_retrieve_entity_params.V2RetrieveEntityParams,
                ),
            ),
            cast_to=V2RetrieveEntityResponse,
        )

    def list_facts(
        self,
        *,
        type: object | Omit = omit,
        entity: object | Omit = omit,
        role: object | Omit = omit,
        since: object | Omit = omit,
        until: object | Omit = omit,
        as_of: object | Omit = omit,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListFactsResponse:
        """
        Facts of one type, newest known first.

        Args:
          type: Fact type (required). See /v2/types.

          entity: Entity ID, e.g. company:E00883.

          role: The entity's role in the fact, e.g. issuer.

          since: valid_as_of on or after (YYYY-MM-DD).

          until: valid_as_of on or before (YYYY-MM-DD).

          as_of: Point in time: only facts known by then.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/facts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "type": type,
                        "entity": entity,
                        "role": role,
                        "since": since,
                        "until": until,
                        "as_of": as_of,
                        "limit": limit,
                        "cursor": cursor,
                    },
                    v2_list_facts_params.V2ListFactsParams,
                ),
            ),
            cast_to=V2ListFactsResponse,
        )

    def list_filings(
        self,
        *,
        q: object | Omit = omit,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListFilingsResponse:
        """
        Filings, newest first.

        Args:
          q: Document ID or description contains.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/filings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                        "cursor": cursor,
                    },
                    v2_list_filings_params.V2ListFilingsParams,
                ),
            ),
            cast_to=V2ListFilingsResponse,
        )

    def retrieve_filing(
        self,
        doc_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveFilingResponse:
        """
        One filing's metadata and link.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not doc_id:
            raise ValueError(f"Expected a non-empty value for `doc_id` but received {doc_id!r}")
        return self._get(
            path_template("/v2/filings/{doc_id}", doc_id=doc_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2RetrieveFilingResponse,
        )

    def retrieve_holder(
        self,
        holder_code: str,
        *,
        include: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveHolderResponse:
        """
        A holder, with its positions and trends.

        Args:
          include: positions,trends,signals,group_positions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not holder_code:
            raise ValueError(f"Expected a non-empty value for `holder_code` but received {holder_code!r}")
        return self._get(
            path_template("/v2/holders/{holder_code}", holder_code=holder_code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include": include,
                    },
                    v2_retrieve_holder_params.V2RetrieveHolderParams,
                ),
            ),
            cast_to=V2RetrieveHolderResponse,
        )

    def list_positions(
        self,
        *,
        company: object | Omit = omit,
        holder: object | Omit = omit,
        since: object | Omit = omit,
        as_of: object | Omit = omit,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListPositionsResponse:
        """
        Position facts for a company, a holder, or one holder in one company.

        Args:
          company: Issuer: EDINET code, securities code or 法人番号.

          holder: Holder: EDINET code, LEI or any Axiora holder id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/positions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company": company,
                        "holder": holder,
                        "since": since,
                        "as_of": as_of,
                        "limit": limit,
                        "cursor": cursor,
                    },
                    v2_list_positions_params.V2ListPositionsParams,
                ),
            ),
            cast_to=V2ListPositionsResponse,
        )

    def search(
        self,
        *,
        q: str,
        type: object | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2SearchResponse:
        """
        Find a company or a holder.

        Args:
          q: Company name or code, or holder name.

          type: company or holder; both if omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "type": type,
                        "limit": limit,
                    },
                    v2_search_params.V2SearchParams,
                ),
            ),
            cast_to=V2SearchResponse,
        )

    def list_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListTypesResponse:
        """
        Every entity type and fact type: fields, units, roles, ID scheme, tier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2ListTypesResponse,
        )


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)

    async def list_changes(
        self,
        *,
        since: str,
        type: object | Omit = omit,
        entity: object | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListChangesResponse:
        """
        What became known since a time, newest first, across the types the key may read.

        Args:
          since: Facts that became known after this time (ISO 8601).

          type: One fact type; all readable types if omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/changes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "since": since,
                        "type": type,
                        "entity": entity,
                        "limit": limit,
                    },
                    v2_list_changes_params.V2ListChangesParams,
                ),
            ),
            cast_to=V2ListChangesResponse,
        )

    async def retrieve_company(
        self,
        code: str,
        *,
        include: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveCompanyResponse:
        """
        A company, with what you ask for.

        Args:
          include: holders,trends,financials,votes,board,signals

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/v2/companies/{code}", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include": include,
                    },
                    v2_retrieve_company_params.V2RetrieveCompanyParams,
                ),
            ),
            cast_to=V2RetrieveCompanyResponse,
        )

    async def list_entities(
        self,
        *,
        type: str,
        q: object | Omit = omit,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListEntitiesResponse:
        """
        Entities of one type, optionally filtered by name or code.

        Args:
          type: Entity type: company, holder or filing.

          q: Name or code contains.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/entities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "type": type,
                        "q": q,
                        "limit": limit,
                        "cursor": cursor,
                    },
                    v2_list_entities_params.V2ListEntitiesParams,
                ),
            ),
            cast_to=V2ListEntitiesResponse,
        )

    async def retrieve_entity(
        self,
        entity_id: str,
        *,
        include: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveEntityResponse:
        """
        One entity, optionally with facts of the listed types.

        Args:
          include: Comma-separated fact types; 50 each.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            path_template("/v2/entities/{entity_id}", entity_id=entity_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include": include,
                    },
                    v2_retrieve_entity_params.V2RetrieveEntityParams,
                ),
            ),
            cast_to=V2RetrieveEntityResponse,
        )

    async def list_facts(
        self,
        *,
        type: object | Omit = omit,
        entity: object | Omit = omit,
        role: object | Omit = omit,
        since: object | Omit = omit,
        until: object | Omit = omit,
        as_of: object | Omit = omit,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListFactsResponse:
        """
        Facts of one type, newest known first.

        Args:
          type: Fact type (required). See /v2/types.

          entity: Entity ID, e.g. company:E00883.

          role: The entity's role in the fact, e.g. issuer.

          since: valid_as_of on or after (YYYY-MM-DD).

          until: valid_as_of on or before (YYYY-MM-DD).

          as_of: Point in time: only facts known by then.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/facts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "type": type,
                        "entity": entity,
                        "role": role,
                        "since": since,
                        "until": until,
                        "as_of": as_of,
                        "limit": limit,
                        "cursor": cursor,
                    },
                    v2_list_facts_params.V2ListFactsParams,
                ),
            ),
            cast_to=V2ListFactsResponse,
        )

    async def list_filings(
        self,
        *,
        q: object | Omit = omit,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListFilingsResponse:
        """
        Filings, newest first.

        Args:
          q: Document ID or description contains.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/filings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                        "cursor": cursor,
                    },
                    v2_list_filings_params.V2ListFilingsParams,
                ),
            ),
            cast_to=V2ListFilingsResponse,
        )

    async def retrieve_filing(
        self,
        doc_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveFilingResponse:
        """
        One filing's metadata and link.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not doc_id:
            raise ValueError(f"Expected a non-empty value for `doc_id` but received {doc_id!r}")
        return await self._get(
            path_template("/v2/filings/{doc_id}", doc_id=doc_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2RetrieveFilingResponse,
        )

    async def retrieve_holder(
        self,
        holder_code: str,
        *,
        include: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveHolderResponse:
        """
        A holder, with its positions and trends.

        Args:
          include: positions,trends,signals,group_positions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not holder_code:
            raise ValueError(f"Expected a non-empty value for `holder_code` but received {holder_code!r}")
        return await self._get(
            path_template("/v2/holders/{holder_code}", holder_code=holder_code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include": include,
                    },
                    v2_retrieve_holder_params.V2RetrieveHolderParams,
                ),
            ),
            cast_to=V2RetrieveHolderResponse,
        )

    async def list_positions(
        self,
        *,
        company: object | Omit = omit,
        holder: object | Omit = omit,
        since: object | Omit = omit,
        as_of: object | Omit = omit,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListPositionsResponse:
        """
        Position facts for a company, a holder, or one holder in one company.

        Args:
          company: Issuer: EDINET code, securities code or 法人番号.

          holder: Holder: EDINET code, LEI or any Axiora holder id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/positions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "company": company,
                        "holder": holder,
                        "since": since,
                        "as_of": as_of,
                        "limit": limit,
                        "cursor": cursor,
                    },
                    v2_list_positions_params.V2ListPositionsParams,
                ),
            ),
            cast_to=V2ListPositionsResponse,
        )

    async def search(
        self,
        *,
        q: str,
        type: object | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2SearchResponse:
        """
        Find a company or a holder.

        Args:
          q: Company name or code, or holder name.

          type: company or holder; both if omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "type": type,
                        "limit": limit,
                    },
                    v2_search_params.V2SearchParams,
                ),
            ),
            cast_to=V2SearchResponse,
        )

    async def list_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListTypesResponse:
        """
        Every entity type and fact type: fields, units, roles, ID scheme, tier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2ListTypesResponse,
        )


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.list_changes = to_raw_response_wrapper(
            v2.list_changes,
        )
        self.retrieve_company = to_raw_response_wrapper(
            v2.retrieve_company,
        )
        self.list_entities = to_raw_response_wrapper(
            v2.list_entities,
        )
        self.retrieve_entity = to_raw_response_wrapper(
            v2.retrieve_entity,
        )
        self.list_facts = to_raw_response_wrapper(
            v2.list_facts,
        )
        self.list_filings = to_raw_response_wrapper(
            v2.list_filings,
        )
        self.retrieve_filing = to_raw_response_wrapper(
            v2.retrieve_filing,
        )
        self.retrieve_holder = to_raw_response_wrapper(
            v2.retrieve_holder,
        )
        self.list_positions = to_raw_response_wrapper(
            v2.list_positions,
        )
        self.search = to_raw_response_wrapper(
            v2.search,
        )
        self.list_types = to_raw_response_wrapper(
            v2.list_types,
        )


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.list_changes = async_to_raw_response_wrapper(
            v2.list_changes,
        )
        self.retrieve_company = async_to_raw_response_wrapper(
            v2.retrieve_company,
        )
        self.list_entities = async_to_raw_response_wrapper(
            v2.list_entities,
        )
        self.retrieve_entity = async_to_raw_response_wrapper(
            v2.retrieve_entity,
        )
        self.list_facts = async_to_raw_response_wrapper(
            v2.list_facts,
        )
        self.list_filings = async_to_raw_response_wrapper(
            v2.list_filings,
        )
        self.retrieve_filing = async_to_raw_response_wrapper(
            v2.retrieve_filing,
        )
        self.retrieve_holder = async_to_raw_response_wrapper(
            v2.retrieve_holder,
        )
        self.list_positions = async_to_raw_response_wrapper(
            v2.list_positions,
        )
        self.search = async_to_raw_response_wrapper(
            v2.search,
        )
        self.list_types = async_to_raw_response_wrapper(
            v2.list_types,
        )


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.list_changes = to_streamed_response_wrapper(
            v2.list_changes,
        )
        self.retrieve_company = to_streamed_response_wrapper(
            v2.retrieve_company,
        )
        self.list_entities = to_streamed_response_wrapper(
            v2.list_entities,
        )
        self.retrieve_entity = to_streamed_response_wrapper(
            v2.retrieve_entity,
        )
        self.list_facts = to_streamed_response_wrapper(
            v2.list_facts,
        )
        self.list_filings = to_streamed_response_wrapper(
            v2.list_filings,
        )
        self.retrieve_filing = to_streamed_response_wrapper(
            v2.retrieve_filing,
        )
        self.retrieve_holder = to_streamed_response_wrapper(
            v2.retrieve_holder,
        )
        self.list_positions = to_streamed_response_wrapper(
            v2.list_positions,
        )
        self.search = to_streamed_response_wrapper(
            v2.search,
        )
        self.list_types = to_streamed_response_wrapper(
            v2.list_types,
        )


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.list_changes = async_to_streamed_response_wrapper(
            v2.list_changes,
        )
        self.retrieve_company = async_to_streamed_response_wrapper(
            v2.retrieve_company,
        )
        self.list_entities = async_to_streamed_response_wrapper(
            v2.list_entities,
        )
        self.retrieve_entity = async_to_streamed_response_wrapper(
            v2.retrieve_entity,
        )
        self.list_facts = async_to_streamed_response_wrapper(
            v2.list_facts,
        )
        self.list_filings = async_to_streamed_response_wrapper(
            v2.list_filings,
        )
        self.retrieve_filing = async_to_streamed_response_wrapper(
            v2.retrieve_filing,
        )
        self.retrieve_holder = async_to_streamed_response_wrapper(
            v2.retrieve_holder,
        )
        self.list_positions = async_to_streamed_response_wrapper(
            v2.list_positions,
        )
        self.search = async_to_streamed_response_wrapper(
            v2.search,
        )
        self.list_types = async_to_streamed_response_wrapper(
            v2.list_types,
        )
