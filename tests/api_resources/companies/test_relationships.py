# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types.companies import (
    RelationshipListInterlocksResponse,
    RelationshipGetRelationshipsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRelationships:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_relationships(self, client: Axiora) -> None:
        relationship = client.companies.relationships.get_relationships(
            code="code",
        )
        assert_matches_type(RelationshipGetRelationshipsResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_relationships_with_all_params(self, client: Axiora) -> None:
        relationship = client.companies.relationships.get_relationships(
            code="code",
            fiscal_year=2000,
        )
        assert_matches_type(RelationshipGetRelationshipsResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_relationships(self, client: Axiora) -> None:
        response = client.companies.relationships.with_raw_response.get_relationships(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = response.parse()
        assert_matches_type(RelationshipGetRelationshipsResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_relationships(self, client: Axiora) -> None:
        with client.companies.relationships.with_streaming_response.get_relationships(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = response.parse()
            assert_matches_type(RelationshipGetRelationshipsResponse, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_relationships(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.relationships.with_raw_response.get_relationships(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_interlocks(self, client: Axiora) -> None:
        relationship = client.companies.relationships.list_interlocks(
            code="code",
        )
        assert_matches_type(RelationshipListInterlocksResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_interlocks_with_all_params(self, client: Axiora) -> None:
        relationship = client.companies.relationships.list_interlocks(
            code="code",
            fiscal_year=2000,
        )
        assert_matches_type(RelationshipListInterlocksResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_interlocks(self, client: Axiora) -> None:
        response = client.companies.relationships.with_raw_response.list_interlocks(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = response.parse()
        assert_matches_type(RelationshipListInterlocksResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_interlocks(self, client: Axiora) -> None:
        with client.companies.relationships.with_streaming_response.list_interlocks(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = response.parse()
            assert_matches_type(RelationshipListInterlocksResponse, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_interlocks(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.relationships.with_raw_response.list_interlocks(
                code="",
            )


class TestAsyncRelationships:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_relationships(self, async_client: AsyncAxiora) -> None:
        relationship = await async_client.companies.relationships.get_relationships(
            code="code",
        )
        assert_matches_type(RelationshipGetRelationshipsResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_relationships_with_all_params(self, async_client: AsyncAxiora) -> None:
        relationship = await async_client.companies.relationships.get_relationships(
            code="code",
            fiscal_year=2000,
        )
        assert_matches_type(RelationshipGetRelationshipsResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_relationships(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.relationships.with_raw_response.get_relationships(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = await response.parse()
        assert_matches_type(RelationshipGetRelationshipsResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_relationships(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.relationships.with_streaming_response.get_relationships(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = await response.parse()
            assert_matches_type(RelationshipGetRelationshipsResponse, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_relationships(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.relationships.with_raw_response.get_relationships(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_interlocks(self, async_client: AsyncAxiora) -> None:
        relationship = await async_client.companies.relationships.list_interlocks(
            code="code",
        )
        assert_matches_type(RelationshipListInterlocksResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_interlocks_with_all_params(self, async_client: AsyncAxiora) -> None:
        relationship = await async_client.companies.relationships.list_interlocks(
            code="code",
            fiscal_year=2000,
        )
        assert_matches_type(RelationshipListInterlocksResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_interlocks(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.relationships.with_raw_response.list_interlocks(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = await response.parse()
        assert_matches_type(RelationshipListInterlocksResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_interlocks(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.relationships.with_streaming_response.list_interlocks(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = await response.parse()
            assert_matches_type(RelationshipListInterlocksResponse, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_interlocks(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.relationships.with_raw_response.list_interlocks(
                code="",
            )
