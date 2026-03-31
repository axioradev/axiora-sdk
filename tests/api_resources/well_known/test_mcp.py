# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_server_card(self, client: Axiora) -> None:
        mcp = client.well_known.mcp.retrieve_server_card()
        assert_matches_type(object, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_server_card(self, client: Axiora) -> None:
        response = client.well_known.mcp.with_raw_response.retrieve_server_card()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(object, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_server_card(self, client: Axiora) -> None:
        with client.well_known.mcp.with_streaming_response.retrieve_server_card() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(object, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMcp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_server_card(self, async_client: AsyncAxiora) -> None:
        mcp = await async_client.well_known.mcp.retrieve_server_card()
        assert_matches_type(object, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_server_card(self, async_client: AsyncAxiora) -> None:
        response = await async_client.well_known.mcp.with_raw_response.retrieve_server_card()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(object, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_server_card(self, async_client: AsyncAxiora) -> None:
        async with async_client.well_known.mcp.with_streaming_response.retrieve_server_card() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(object, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True
