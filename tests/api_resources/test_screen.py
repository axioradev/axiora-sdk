# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import ScreenRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScreen:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Axiora) -> None:
        screen = client.screen.retrieve()
        assert_matches_type(ScreenRetrieveResponse, screen, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Axiora) -> None:
        screen = client.screen.retrieve(
            fiscal_year=1900,
            limit=1,
            net_income_max=0,
            net_income_min=0,
            offset=0,
            operating_income_max=0,
            operating_income_min=0,
            revenue_max=0,
            revenue_min=0,
            roa_max=0,
            roa_min=0,
            roe_max=0,
            roe_min=0,
            sector="sector",
            sort="sort",
        )
        assert_matches_type(ScreenRetrieveResponse, screen, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Axiora) -> None:
        response = client.screen.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screen = response.parse()
        assert_matches_type(ScreenRetrieveResponse, screen, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Axiora) -> None:
        with client.screen.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screen = response.parse()
            assert_matches_type(ScreenRetrieveResponse, screen, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScreen:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAxiora) -> None:
        screen = await async_client.screen.retrieve()
        assert_matches_type(ScreenRetrieveResponse, screen, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAxiora) -> None:
        screen = await async_client.screen.retrieve(
            fiscal_year=1900,
            limit=1,
            net_income_max=0,
            net_income_min=0,
            offset=0,
            operating_income_max=0,
            operating_income_min=0,
            revenue_max=0,
            revenue_min=0,
            roa_max=0,
            roa_min=0,
            roe_max=0,
            roe_min=0,
            sector="sector",
            sort="sort",
        )
        assert_matches_type(ScreenRetrieveResponse, screen, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAxiora) -> None:
        response = await async_client.screen.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screen = await response.parse()
        assert_matches_type(ScreenRetrieveResponse, screen, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAxiora) -> None:
        async with async_client.screen.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screen = await response.parse()
            assert_matches_type(ScreenRetrieveResponse, screen, path=["response"])

        assert cast(Any, response.is_closed) is True
