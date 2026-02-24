# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import SectorListResponse, SectorRetrieveStatsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSectors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Axiora) -> None:
        sector = client.sectors.list()
        assert_matches_type(SectorListResponse, sector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Axiora) -> None:
        response = client.sectors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sector = response.parse()
        assert_matches_type(SectorListResponse, sector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Axiora) -> None:
        with client.sectors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sector = response.parse()
            assert_matches_type(SectorListResponse, sector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_stats(self, client: Axiora) -> None:
        sector = client.sectors.retrieve_stats(
            sector_name="sector_name",
        )
        assert_matches_type(SectorRetrieveStatsResponse, sector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_stats_with_all_params(self, client: Axiora) -> None:
        sector = client.sectors.retrieve_stats(
            sector_name="sector_name",
            fiscal_year=0,
        )
        assert_matches_type(SectorRetrieveStatsResponse, sector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_stats(self, client: Axiora) -> None:
        response = client.sectors.with_raw_response.retrieve_stats(
            sector_name="sector_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sector = response.parse()
        assert_matches_type(SectorRetrieveStatsResponse, sector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_stats(self, client: Axiora) -> None:
        with client.sectors.with_streaming_response.retrieve_stats(
            sector_name="sector_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sector = response.parse()
            assert_matches_type(SectorRetrieveStatsResponse, sector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_stats(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sector_name` but received ''"):
            client.sectors.with_raw_response.retrieve_stats(
                sector_name="",
            )


class TestAsyncSectors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAxiora) -> None:
        sector = await async_client.sectors.list()
        assert_matches_type(SectorListResponse, sector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAxiora) -> None:
        response = await async_client.sectors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sector = await response.parse()
        assert_matches_type(SectorListResponse, sector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAxiora) -> None:
        async with async_client.sectors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sector = await response.parse()
            assert_matches_type(SectorListResponse, sector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_stats(self, async_client: AsyncAxiora) -> None:
        sector = await async_client.sectors.retrieve_stats(
            sector_name="sector_name",
        )
        assert_matches_type(SectorRetrieveStatsResponse, sector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_stats_with_all_params(self, async_client: AsyncAxiora) -> None:
        sector = await async_client.sectors.retrieve_stats(
            sector_name="sector_name",
            fiscal_year=0,
        )
        assert_matches_type(SectorRetrieveStatsResponse, sector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_stats(self, async_client: AsyncAxiora) -> None:
        response = await async_client.sectors.with_raw_response.retrieve_stats(
            sector_name="sector_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sector = await response.parse()
        assert_matches_type(SectorRetrieveStatsResponse, sector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_stats(self, async_client: AsyncAxiora) -> None:
        async with async_client.sectors.with_streaming_response.retrieve_stats(
            sector_name="sector_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sector = await response.parse()
            assert_matches_type(SectorRetrieveStatsResponse, sector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_stats(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sector_name` but received ''"):
            await async_client.sectors.with_raw_response.retrieve_stats(
                sector_name="",
            )
