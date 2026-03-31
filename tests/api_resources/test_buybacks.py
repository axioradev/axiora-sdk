# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import (
    BuybackListLatestResponse,
    BuybackListAccelerationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBuybacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_accelerations(self, client: Axiora) -> None:
        buyback = client.buybacks.list_accelerations()
        assert_matches_type(BuybackListAccelerationsResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_accelerations_with_all_params(self, client: Axiora) -> None:
        buyback = client.buybacks.list_accelerations(
            limit=1,
        )
        assert_matches_type(BuybackListAccelerationsResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_accelerations(self, client: Axiora) -> None:
        response = client.buybacks.with_raw_response.list_accelerations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        buyback = response.parse()
        assert_matches_type(BuybackListAccelerationsResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_accelerations(self, client: Axiora) -> None:
        with client.buybacks.with_streaming_response.list_accelerations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            buyback = response.parse()
            assert_matches_type(BuybackListAccelerationsResponse, buyback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_latest(self, client: Axiora) -> None:
        buyback = client.buybacks.list_latest()
        assert_matches_type(BuybackListLatestResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_latest_with_all_params(self, client: Axiora) -> None:
        buyback = client.buybacks.list_latest(
            cursor="cursor",
            limit=1,
            offset=0,
            sector="sector",
        )
        assert_matches_type(BuybackListLatestResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_latest(self, client: Axiora) -> None:
        response = client.buybacks.with_raw_response.list_latest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        buyback = response.parse()
        assert_matches_type(BuybackListLatestResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_latest(self, client: Axiora) -> None:
        with client.buybacks.with_streaming_response.list_latest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            buyback = response.parse()
            assert_matches_type(BuybackListLatestResponse, buyback, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBuybacks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_accelerations(self, async_client: AsyncAxiora) -> None:
        buyback = await async_client.buybacks.list_accelerations()
        assert_matches_type(BuybackListAccelerationsResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_accelerations_with_all_params(self, async_client: AsyncAxiora) -> None:
        buyback = await async_client.buybacks.list_accelerations(
            limit=1,
        )
        assert_matches_type(BuybackListAccelerationsResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_accelerations(self, async_client: AsyncAxiora) -> None:
        response = await async_client.buybacks.with_raw_response.list_accelerations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        buyback = await response.parse()
        assert_matches_type(BuybackListAccelerationsResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_accelerations(self, async_client: AsyncAxiora) -> None:
        async with async_client.buybacks.with_streaming_response.list_accelerations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            buyback = await response.parse()
            assert_matches_type(BuybackListAccelerationsResponse, buyback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_latest(self, async_client: AsyncAxiora) -> None:
        buyback = await async_client.buybacks.list_latest()
        assert_matches_type(BuybackListLatestResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_latest_with_all_params(self, async_client: AsyncAxiora) -> None:
        buyback = await async_client.buybacks.list_latest(
            cursor="cursor",
            limit=1,
            offset=0,
            sector="sector",
        )
        assert_matches_type(BuybackListLatestResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_latest(self, async_client: AsyncAxiora) -> None:
        response = await async_client.buybacks.with_raw_response.list_latest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        buyback = await response.parse()
        assert_matches_type(BuybackListLatestResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_latest(self, async_client: AsyncAxiora) -> None:
        async with async_client.buybacks.with_streaming_response.list_latest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            buyback = await response.parse()
            assert_matches_type(BuybackListLatestResponse, buyback, path=["response"])

        assert cast(Any, response.is_closed) is True
