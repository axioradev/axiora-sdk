# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import RankingRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRankings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Axiora) -> None:
        ranking = client.rankings.retrieve(
            metric="metric",
        )
        assert_matches_type(RankingRetrieveResponse, ranking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Axiora) -> None:
        ranking = client.rankings.retrieve(
            metric="metric",
            fiscal_year=0,
            limit=1,
            offset=0,
            order="desc",
            sector="sector",
        )
        assert_matches_type(RankingRetrieveResponse, ranking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Axiora) -> None:
        response = client.rankings.with_raw_response.retrieve(
            metric="metric",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ranking = response.parse()
        assert_matches_type(RankingRetrieveResponse, ranking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Axiora) -> None:
        with client.rankings.with_streaming_response.retrieve(
            metric="metric",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ranking = response.parse()
            assert_matches_type(RankingRetrieveResponse, ranking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric` but received ''"):
            client.rankings.with_raw_response.retrieve(
                metric="",
            )


class TestAsyncRankings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAxiora) -> None:
        ranking = await async_client.rankings.retrieve(
            metric="metric",
        )
        assert_matches_type(RankingRetrieveResponse, ranking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAxiora) -> None:
        ranking = await async_client.rankings.retrieve(
            metric="metric",
            fiscal_year=0,
            limit=1,
            offset=0,
            order="desc",
            sector="sector",
        )
        assert_matches_type(RankingRetrieveResponse, ranking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAxiora) -> None:
        response = await async_client.rankings.with_raw_response.retrieve(
            metric="metric",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ranking = await response.parse()
        assert_matches_type(RankingRetrieveResponse, ranking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAxiora) -> None:
        async with async_client.rankings.with_streaming_response.retrieve(
            metric="metric",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ranking = await response.parse()
            assert_matches_type(RankingRetrieveResponse, ranking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric` but received ''"):
            await async_client.rankings.with_raw_response.retrieve(
                metric="",
            )
