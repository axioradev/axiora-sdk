# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import (
    IdentifierListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIdentifiers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Axiora) -> None:
        identifier = client.identifiers.list(
            id="id",
        )
        assert_matches_type(IdentifierListResponse, identifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Axiora) -> None:
        response = client.identifiers.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identifier = response.parse()
        assert_matches_type(IdentifierListResponse, identifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Axiora) -> None:
        with client.identifiers.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identifier = response.parse()
            assert_matches_type(IdentifierListResponse, identifier, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIdentifiers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAxiora) -> None:
        identifier = await async_client.identifiers.list(
            id="id",
        )
        assert_matches_type(IdentifierListResponse, identifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAxiora) -> None:
        response = await async_client.identifiers.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identifier = await response.parse()
        assert_matches_type(IdentifierListResponse, identifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAxiora) -> None:
        async with async_client.identifiers.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identifier = await response.parse()
            assert_matches_type(IdentifierListResponse, identifier, path=["response"])

        assert cast(Any, response.is_closed) is True
