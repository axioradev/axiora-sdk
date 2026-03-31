# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import (
    InvestorSearchResponse,
    InvestorRetrievePositionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvestors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_positions(self, client: Axiora) -> None:
        investor = client.investors.retrieve_positions(
            code="code",
        )
        assert_matches_type(InvestorRetrievePositionsResponse, investor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_positions_with_all_params(self, client: Axiora) -> None:
        investor = client.investors.retrieve_positions(
            code="code",
            limit=1,
            trajectory_type="trajectory_type",
        )
        assert_matches_type(InvestorRetrievePositionsResponse, investor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_positions(self, client: Axiora) -> None:
        response = client.investors.with_raw_response.retrieve_positions(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        investor = response.parse()
        assert_matches_type(InvestorRetrievePositionsResponse, investor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_positions(self, client: Axiora) -> None:
        with client.investors.with_streaming_response.retrieve_positions(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            investor = response.parse()
            assert_matches_type(InvestorRetrievePositionsResponse, investor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_positions(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.investors.with_raw_response.retrieve_positions(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Axiora) -> None:
        investor = client.investors.search(
            q="x",
        )
        assert_matches_type(InvestorSearchResponse, investor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Axiora) -> None:
        investor = client.investors.search(
            q="x",
            limit=1,
        )
        assert_matches_type(InvestorSearchResponse, investor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Axiora) -> None:
        response = client.investors.with_raw_response.search(
            q="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        investor = response.parse()
        assert_matches_type(InvestorSearchResponse, investor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Axiora) -> None:
        with client.investors.with_streaming_response.search(
            q="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            investor = response.parse()
            assert_matches_type(InvestorSearchResponse, investor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInvestors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_positions(self, async_client: AsyncAxiora) -> None:
        investor = await async_client.investors.retrieve_positions(
            code="code",
        )
        assert_matches_type(InvestorRetrievePositionsResponse, investor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_positions_with_all_params(self, async_client: AsyncAxiora) -> None:
        investor = await async_client.investors.retrieve_positions(
            code="code",
            limit=1,
            trajectory_type="trajectory_type",
        )
        assert_matches_type(InvestorRetrievePositionsResponse, investor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_positions(self, async_client: AsyncAxiora) -> None:
        response = await async_client.investors.with_raw_response.retrieve_positions(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        investor = await response.parse()
        assert_matches_type(InvestorRetrievePositionsResponse, investor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_positions(self, async_client: AsyncAxiora) -> None:
        async with async_client.investors.with_streaming_response.retrieve_positions(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            investor = await response.parse()
            assert_matches_type(InvestorRetrievePositionsResponse, investor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_positions(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.investors.with_raw_response.retrieve_positions(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncAxiora) -> None:
        investor = await async_client.investors.search(
            q="x",
        )
        assert_matches_type(InvestorSearchResponse, investor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncAxiora) -> None:
        investor = await async_client.investors.search(
            q="x",
            limit=1,
        )
        assert_matches_type(InvestorSearchResponse, investor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncAxiora) -> None:
        response = await async_client.investors.with_raw_response.search(
            q="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        investor = await response.parse()
        assert_matches_type(InvestorSearchResponse, investor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncAxiora) -> None:
        async with async_client.investors.with_streaming_response.search(
            q="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            investor = await response.parse()
            assert_matches_type(InvestorSearchResponse, investor, path=["response"])

        assert cast(Any, response.is_closed) is True
