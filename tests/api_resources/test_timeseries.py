# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import TimeseryRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimeseries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Axiora) -> None:
        timesery = client.timeseries.retrieve(
            codes="codes",
        )
        assert_matches_type(TimeseryRetrieveResponse, timesery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Axiora) -> None:
        timesery = client.timeseries.retrieve(
            codes="codes",
            metric="metric",
            years=2,
        )
        assert_matches_type(TimeseryRetrieveResponse, timesery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Axiora) -> None:
        response = client.timeseries.with_raw_response.retrieve(
            codes="codes",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timesery = response.parse()
        assert_matches_type(TimeseryRetrieveResponse, timesery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Axiora) -> None:
        with client.timeseries.with_streaming_response.retrieve(
            codes="codes",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timesery = response.parse()
            assert_matches_type(TimeseryRetrieveResponse, timesery, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTimeseries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAxiora) -> None:
        timesery = await async_client.timeseries.retrieve(
            codes="codes",
        )
        assert_matches_type(TimeseryRetrieveResponse, timesery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAxiora) -> None:
        timesery = await async_client.timeseries.retrieve(
            codes="codes",
            metric="metric",
            years=2,
        )
        assert_matches_type(TimeseryRetrieveResponse, timesery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAxiora) -> None:
        response = await async_client.timeseries.with_raw_response.retrieve(
            codes="codes",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timesery = await response.parse()
        assert_matches_type(TimeseryRetrieveResponse, timesery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAxiora) -> None:
        async with async_client.timeseries.with_streaming_response.retrieve(
            codes="codes",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timesery = await response.parse()
            assert_matches_type(TimeseryRetrieveResponse, timesery, path=["response"])

        assert cast(Any, response.is_closed) is True
