# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import (
    V2SearchResponse,
    V2ListFactsResponse,
    V2ListTypesResponse,
    V2ListChangesResponse,
    V2ListFilingsResponse,
    V2ListEntitiesResponse,
    V2ListPositionsResponse,
    V2RetrieveEntityResponse,
    V2RetrieveFilingResponse,
    V2RetrieveHolderResponse,
    V2RetrieveCompanyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_changes(self, client: Axiora) -> None:
        v2 = client.v2.list_changes(
            since="since",
        )
        assert_matches_type(V2ListChangesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_changes_with_all_params(self, client: Axiora) -> None:
        v2 = client.v2.list_changes(
            since="since",
            type="type",
            entity="entity",
            limit=1,
        )
        assert_matches_type(V2ListChangesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_changes(self, client: Axiora) -> None:
        response = client.v2.with_raw_response.list_changes(
            since="since",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ListChangesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_changes(self, client: Axiora) -> None:
        with client.v2.with_streaming_response.list_changes(
            since="since",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ListChangesResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_company(self, client: Axiora) -> None:
        v2 = client.v2.retrieve_company(
            "code",
        )
        assert_matches_type(V2RetrieveCompanyResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_company_with_all_params(self, client: Axiora) -> None:
        v2 = client.v2.retrieve_company(
            "code",
            include="include",
        )
        assert_matches_type(V2RetrieveCompanyResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_company(self, client: Axiora) -> None:
        response = client.v2.with_raw_response.retrieve_company(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2RetrieveCompanyResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_company(self, client: Axiora) -> None:
        with client.v2.with_streaming_response.retrieve_company(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2RetrieveCompanyResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_company(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.v2.with_raw_response.retrieve_company(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_entities(self, client: Axiora) -> None:
        v2 = client.v2.list_entities(
            type="type",
        )
        assert_matches_type(V2ListEntitiesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_entities_with_all_params(self, client: Axiora) -> None:
        v2 = client.v2.list_entities(
            type="type",
            q="q",
            limit=1,
            cursor="cursor",
        )
        assert_matches_type(V2ListEntitiesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_entities(self, client: Axiora) -> None:
        response = client.v2.with_raw_response.list_entities(
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ListEntitiesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_entities(self, client: Axiora) -> None:
        with client.v2.with_streaming_response.list_entities(
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ListEntitiesResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_entity(self, client: Axiora) -> None:
        v2 = client.v2.retrieve_entity(
            "entity_id",
        )
        assert_matches_type(V2RetrieveEntityResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_entity_with_all_params(self, client: Axiora) -> None:
        v2 = client.v2.retrieve_entity(
            "entity_id",
            include="include",
        )
        assert_matches_type(V2RetrieveEntityResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_entity(self, client: Axiora) -> None:
        response = client.v2.with_raw_response.retrieve_entity(
            "entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2RetrieveEntityResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_entity(self, client: Axiora) -> None:
        with client.v2.with_streaming_response.retrieve_entity(
            "entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2RetrieveEntityResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_entity(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.v2.with_raw_response.retrieve_entity(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_facts(self, client: Axiora) -> None:
        v2 = client.v2.list_facts()
        assert_matches_type(V2ListFactsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_facts_with_all_params(self, client: Axiora) -> None:
        v2 = client.v2.list_facts(
            type="type",
            entity="entity",
            role="role",
            since="since",
            until="until",
            as_of="as_of",
            limit=1,
            cursor="cursor",
        )
        assert_matches_type(V2ListFactsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_facts(self, client: Axiora) -> None:
        response = client.v2.with_raw_response.list_facts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ListFactsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_facts(self, client: Axiora) -> None:
        with client.v2.with_streaming_response.list_facts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ListFactsResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_filings(self, client: Axiora) -> None:
        v2 = client.v2.list_filings()
        assert_matches_type(V2ListFilingsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_filings_with_all_params(self, client: Axiora) -> None:
        v2 = client.v2.list_filings(
            q="q",
            limit=1,
            cursor="cursor",
        )
        assert_matches_type(V2ListFilingsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_filings(self, client: Axiora) -> None:
        response = client.v2.with_raw_response.list_filings()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ListFilingsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_filings(self, client: Axiora) -> None:
        with client.v2.with_streaming_response.list_filings() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ListFilingsResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_filing(self, client: Axiora) -> None:
        v2 = client.v2.retrieve_filing(
            "doc_id",
        )
        assert_matches_type(V2RetrieveFilingResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_filing(self, client: Axiora) -> None:
        response = client.v2.with_raw_response.retrieve_filing(
            "doc_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2RetrieveFilingResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_filing(self, client: Axiora) -> None:
        with client.v2.with_streaming_response.retrieve_filing(
            "doc_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2RetrieveFilingResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_filing(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.v2.with_raw_response.retrieve_filing(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_holder(self, client: Axiora) -> None:
        v2 = client.v2.retrieve_holder(
            "holder_code",
        )
        assert_matches_type(V2RetrieveHolderResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_holder_with_all_params(self, client: Axiora) -> None:
        v2 = client.v2.retrieve_holder(
            "holder_code",
            include="include",
        )
        assert_matches_type(V2RetrieveHolderResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_holder(self, client: Axiora) -> None:
        response = client.v2.with_raw_response.retrieve_holder(
            "holder_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2RetrieveHolderResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_holder(self, client: Axiora) -> None:
        with client.v2.with_streaming_response.retrieve_holder(
            "holder_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2RetrieveHolderResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_holder(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `holder_code` but received ''"):
            client.v2.with_raw_response.retrieve_holder(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_positions(self, client: Axiora) -> None:
        v2 = client.v2.list_positions()
        assert_matches_type(V2ListPositionsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_positions_with_all_params(self, client: Axiora) -> None:
        v2 = client.v2.list_positions(
            company="company",
            holder="holder",
            since="since",
            as_of="as_of",
            limit=1,
            cursor="cursor",
        )
        assert_matches_type(V2ListPositionsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_positions(self, client: Axiora) -> None:
        response = client.v2.with_raw_response.list_positions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ListPositionsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_positions(self, client: Axiora) -> None:
        with client.v2.with_streaming_response.list_positions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ListPositionsResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Axiora) -> None:
        v2 = client.v2.search(
            q="q",
        )
        assert_matches_type(V2SearchResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Axiora) -> None:
        v2 = client.v2.search(
            q="q",
            type="type",
            limit=1,
        )
        assert_matches_type(V2SearchResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Axiora) -> None:
        response = client.v2.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2SearchResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Axiora) -> None:
        with client.v2.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2SearchResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_types(self, client: Axiora) -> None:
        v2 = client.v2.list_types()
        assert_matches_type(V2ListTypesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_types(self, client: Axiora) -> None:
        response = client.v2.with_raw_response.list_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ListTypesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_types(self, client: Axiora) -> None:
        with client.v2.with_streaming_response.list_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ListTypesResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV2:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_changes(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.list_changes(
            since="since",
        )
        assert_matches_type(V2ListChangesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_changes_with_all_params(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.list_changes(
            since="since",
            type="type",
            entity="entity",
            limit=1,
        )
        assert_matches_type(V2ListChangesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_changes(self, async_client: AsyncAxiora) -> None:
        response = await async_client.v2.with_raw_response.list_changes(
            since="since",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2ListChangesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_changes(self, async_client: AsyncAxiora) -> None:
        async with async_client.v2.with_streaming_response.list_changes(
            since="since",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ListChangesResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_company(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.retrieve_company(
            "code",
        )
        assert_matches_type(V2RetrieveCompanyResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_company_with_all_params(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.retrieve_company(
            "code",
            include="include",
        )
        assert_matches_type(V2RetrieveCompanyResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_company(self, async_client: AsyncAxiora) -> None:
        response = await async_client.v2.with_raw_response.retrieve_company(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2RetrieveCompanyResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_company(self, async_client: AsyncAxiora) -> None:
        async with async_client.v2.with_streaming_response.retrieve_company(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2RetrieveCompanyResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_company(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.v2.with_raw_response.retrieve_company(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_entities(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.list_entities(
            type="type",
        )
        assert_matches_type(V2ListEntitiesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_entities_with_all_params(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.list_entities(
            type="type",
            q="q",
            limit=1,
            cursor="cursor",
        )
        assert_matches_type(V2ListEntitiesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_entities(self, async_client: AsyncAxiora) -> None:
        response = await async_client.v2.with_raw_response.list_entities(
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2ListEntitiesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_entities(self, async_client: AsyncAxiora) -> None:
        async with async_client.v2.with_streaming_response.list_entities(
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ListEntitiesResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_entity(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.retrieve_entity(
            "entity_id",
        )
        assert_matches_type(V2RetrieveEntityResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_entity_with_all_params(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.retrieve_entity(
            "entity_id",
            include="include",
        )
        assert_matches_type(V2RetrieveEntityResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_entity(self, async_client: AsyncAxiora) -> None:
        response = await async_client.v2.with_raw_response.retrieve_entity(
            "entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2RetrieveEntityResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_entity(self, async_client: AsyncAxiora) -> None:
        async with async_client.v2.with_streaming_response.retrieve_entity(
            "entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2RetrieveEntityResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_entity(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.v2.with_raw_response.retrieve_entity(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_facts(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.list_facts()
        assert_matches_type(V2ListFactsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_facts_with_all_params(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.list_facts(
            type="type",
            entity="entity",
            role="role",
            since="since",
            until="until",
            as_of="as_of",
            limit=1,
            cursor="cursor",
        )
        assert_matches_type(V2ListFactsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_facts(self, async_client: AsyncAxiora) -> None:
        response = await async_client.v2.with_raw_response.list_facts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2ListFactsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_facts(self, async_client: AsyncAxiora) -> None:
        async with async_client.v2.with_streaming_response.list_facts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ListFactsResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_filings(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.list_filings()
        assert_matches_type(V2ListFilingsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_filings_with_all_params(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.list_filings(
            q="q",
            limit=1,
            cursor="cursor",
        )
        assert_matches_type(V2ListFilingsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_filings(self, async_client: AsyncAxiora) -> None:
        response = await async_client.v2.with_raw_response.list_filings()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2ListFilingsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_filings(self, async_client: AsyncAxiora) -> None:
        async with async_client.v2.with_streaming_response.list_filings() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ListFilingsResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_filing(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.retrieve_filing(
            "doc_id",
        )
        assert_matches_type(V2RetrieveFilingResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_filing(self, async_client: AsyncAxiora) -> None:
        response = await async_client.v2.with_raw_response.retrieve_filing(
            "doc_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2RetrieveFilingResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_filing(self, async_client: AsyncAxiora) -> None:
        async with async_client.v2.with_streaming_response.retrieve_filing(
            "doc_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2RetrieveFilingResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_filing(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.v2.with_raw_response.retrieve_filing(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_holder(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.retrieve_holder(
            "holder_code",
        )
        assert_matches_type(V2RetrieveHolderResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_holder_with_all_params(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.retrieve_holder(
            "holder_code",
            include="include",
        )
        assert_matches_type(V2RetrieveHolderResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_holder(self, async_client: AsyncAxiora) -> None:
        response = await async_client.v2.with_raw_response.retrieve_holder(
            "holder_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2RetrieveHolderResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_holder(self, async_client: AsyncAxiora) -> None:
        async with async_client.v2.with_streaming_response.retrieve_holder(
            "holder_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2RetrieveHolderResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_holder(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `holder_code` but received ''"):
            await async_client.v2.with_raw_response.retrieve_holder(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_positions(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.list_positions()
        assert_matches_type(V2ListPositionsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_positions_with_all_params(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.list_positions(
            company="company",
            holder="holder",
            since="since",
            as_of="as_of",
            limit=1,
            cursor="cursor",
        )
        assert_matches_type(V2ListPositionsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_positions(self, async_client: AsyncAxiora) -> None:
        response = await async_client.v2.with_raw_response.list_positions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2ListPositionsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_positions(self, async_client: AsyncAxiora) -> None:
        async with async_client.v2.with_streaming_response.list_positions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ListPositionsResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.search(
            q="q",
        )
        assert_matches_type(V2SearchResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.search(
            q="q",
            type="type",
            limit=1,
        )
        assert_matches_type(V2SearchResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncAxiora) -> None:
        response = await async_client.v2.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2SearchResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncAxiora) -> None:
        async with async_client.v2.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2SearchResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_types(self, async_client: AsyncAxiora) -> None:
        v2 = await async_client.v2.list_types()
        assert_matches_type(V2ListTypesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_types(self, async_client: AsyncAxiora) -> None:
        response = await async_client.v2.with_raw_response.list_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2ListTypesResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_types(self, async_client: AsyncAxiora) -> None:
        async with async_client.v2.with_streaming_response.list_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ListTypesResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True
