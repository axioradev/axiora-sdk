# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import (
    EarningListSignalsResponse,
    EarningRetrieveLatestResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEarnings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_signals(self, client: Axiora) -> None:
        earning = client.earnings.list_signals()
        assert_matches_type(EarningListSignalsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_signals_with_all_params(self, client: Axiora) -> None:
        earning = client.earnings.list_signals(
            limit=1,
            signal_type="signal_type",
        )
        assert_matches_type(EarningListSignalsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_signals(self, client: Axiora) -> None:
        response = client.earnings.with_raw_response.list_signals()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        earning = response.parse()
        assert_matches_type(EarningListSignalsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_signals(self, client: Axiora) -> None:
        with client.earnings.with_streaming_response.list_signals() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            earning = response.parse()
            assert_matches_type(EarningListSignalsResponse, earning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_latest(self, client: Axiora) -> None:
        earning = client.earnings.retrieve_latest()
        assert_matches_type(EarningRetrieveLatestResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_latest_with_all_params(self, client: Axiora) -> None:
        earning = client.earnings.retrieve_latest(
            limit=1,
            period_type="period_type",
        )
        assert_matches_type(EarningRetrieveLatestResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_latest(self, client: Axiora) -> None:
        response = client.earnings.with_raw_response.retrieve_latest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        earning = response.parse()
        assert_matches_type(EarningRetrieveLatestResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_latest(self, client: Axiora) -> None:
        with client.earnings.with_streaming_response.retrieve_latest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            earning = response.parse()
            assert_matches_type(EarningRetrieveLatestResponse, earning, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEarnings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_signals(self, async_client: AsyncAxiora) -> None:
        earning = await async_client.earnings.list_signals()
        assert_matches_type(EarningListSignalsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_signals_with_all_params(self, async_client: AsyncAxiora) -> None:
        earning = await async_client.earnings.list_signals(
            limit=1,
            signal_type="signal_type",
        )
        assert_matches_type(EarningListSignalsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_signals(self, async_client: AsyncAxiora) -> None:
        response = await async_client.earnings.with_raw_response.list_signals()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        earning = await response.parse()
        assert_matches_type(EarningListSignalsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_signals(self, async_client: AsyncAxiora) -> None:
        async with async_client.earnings.with_streaming_response.list_signals() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            earning = await response.parse()
            assert_matches_type(EarningListSignalsResponse, earning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_latest(self, async_client: AsyncAxiora) -> None:
        earning = await async_client.earnings.retrieve_latest()
        assert_matches_type(EarningRetrieveLatestResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_latest_with_all_params(self, async_client: AsyncAxiora) -> None:
        earning = await async_client.earnings.retrieve_latest(
            limit=1,
            period_type="period_type",
        )
        assert_matches_type(EarningRetrieveLatestResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_latest(self, async_client: AsyncAxiora) -> None:
        response = await async_client.earnings.with_raw_response.retrieve_latest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        earning = await response.parse()
        assert_matches_type(EarningRetrieveLatestResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_latest(self, async_client: AsyncAxiora) -> None:
        async with async_client.earnings.with_streaming_response.retrieve_latest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            earning = await response.parse()
            assert_matches_type(EarningRetrieveLatestResponse, earning, path=["response"])

        assert cast(Any, response.is_closed) is True
