# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import CapitalAllocationListRankingResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCapitalAllocation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_ranking(self, client: Axiora) -> None:
        capital_allocation = client.capital_allocation.list_ranking()
        assert_matches_type(CapitalAllocationListRankingResponse, capital_allocation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_ranking_with_all_params(self, client: Axiora) -> None:
        capital_allocation = client.capital_allocation.list_ranking(
            classification="classification",
            cursor="cursor",
            limit=1,
            offset=0,
            sector="sector",
        )
        assert_matches_type(CapitalAllocationListRankingResponse, capital_allocation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_ranking(self, client: Axiora) -> None:
        response = client.capital_allocation.with_raw_response.list_ranking()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capital_allocation = response.parse()
        assert_matches_type(CapitalAllocationListRankingResponse, capital_allocation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_ranking(self, client: Axiora) -> None:
        with client.capital_allocation.with_streaming_response.list_ranking() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capital_allocation = response.parse()
            assert_matches_type(CapitalAllocationListRankingResponse, capital_allocation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCapitalAllocation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_ranking(self, async_client: AsyncAxiora) -> None:
        capital_allocation = await async_client.capital_allocation.list_ranking()
        assert_matches_type(CapitalAllocationListRankingResponse, capital_allocation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_ranking_with_all_params(self, async_client: AsyncAxiora) -> None:
        capital_allocation = await async_client.capital_allocation.list_ranking(
            classification="classification",
            cursor="cursor",
            limit=1,
            offset=0,
            sector="sector",
        )
        assert_matches_type(CapitalAllocationListRankingResponse, capital_allocation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_ranking(self, async_client: AsyncAxiora) -> None:
        response = await async_client.capital_allocation.with_raw_response.list_ranking()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capital_allocation = await response.parse()
        assert_matches_type(CapitalAllocationListRankingResponse, capital_allocation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_ranking(self, async_client: AsyncAxiora) -> None:
        async with async_client.capital_allocation.with_streaming_response.list_ranking() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capital_allocation = await response.parse()
            assert_matches_type(CapitalAllocationListRankingResponse, capital_allocation, path=["response"])

        assert cast(Any, response.is_closed) is True
