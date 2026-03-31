# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import (
    OwnershipListMoversResponse,
    OwnershipListSignalsResponse,
    OwnershipListCrossHoldingsResponse,
    OwnershipGetProbabilityTableResponse,
    OwnershipListActivistCampaignsResponse,
    OwnershipListUnwindingScoreboardResponse,
)
from axiora._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOwnership:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_probability_table(self, client: Axiora) -> None:
        ownership = client.ownership.get_probability_table()
        assert_matches_type(OwnershipGetProbabilityTableResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_probability_table(self, client: Axiora) -> None:
        response = client.ownership.with_raw_response.get_probability_table()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(OwnershipGetProbabilityTableResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_probability_table(self, client: Axiora) -> None:
        with client.ownership.with_streaming_response.get_probability_table() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(OwnershipGetProbabilityTableResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_activist_campaigns(self, client: Axiora) -> None:
        ownership = client.ownership.list_activist_campaigns()
        assert_matches_type(OwnershipListActivistCampaignsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_activist_campaigns_with_all_params(self, client: Axiora) -> None:
        ownership = client.ownership.list_activist_campaigns(
            limit=1,
        )
        assert_matches_type(OwnershipListActivistCampaignsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_activist_campaigns(self, client: Axiora) -> None:
        response = client.ownership.with_raw_response.list_activist_campaigns()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(OwnershipListActivistCampaignsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_activist_campaigns(self, client: Axiora) -> None:
        with client.ownership.with_streaming_response.list_activist_campaigns() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(OwnershipListActivistCampaignsResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_cross_holdings(self, client: Axiora) -> None:
        ownership = client.ownership.list_cross_holdings()
        assert_matches_type(OwnershipListCrossHoldingsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_cross_holdings_with_all_params(self, client: Axiora) -> None:
        ownership = client.ownership.list_cross_holdings(
            cursor="cursor",
            limit=1,
            offset=0,
        )
        assert_matches_type(OwnershipListCrossHoldingsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_cross_holdings(self, client: Axiora) -> None:
        response = client.ownership.with_raw_response.list_cross_holdings()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(OwnershipListCrossHoldingsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_cross_holdings(self, client: Axiora) -> None:
        with client.ownership.with_streaming_response.list_cross_holdings() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(OwnershipListCrossHoldingsResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_movers(self, client: Axiora) -> None:
        ownership = client.ownership.list_movers()
        assert_matches_type(OwnershipListMoversResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_movers_with_all_params(self, client: Axiora) -> None:
        ownership = client.ownership.list_movers(
            cursor="cursor",
            days=1,
            limit=1,
            min_delta_pct=0,
            offset=0,
            trajectory_type="trajectory_type",
        )
        assert_matches_type(OwnershipListMoversResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_movers(self, client: Axiora) -> None:
        response = client.ownership.with_raw_response.list_movers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(OwnershipListMoversResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_movers(self, client: Axiora) -> None:
        with client.ownership.with_streaming_response.list_movers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(OwnershipListMoversResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_signals(self, client: Axiora) -> None:
        ownership = client.ownership.list_signals()
        assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_signals_with_all_params(self, client: Axiora) -> None:
        ownership = client.ownership.list_signals(
            cursor="cursor",
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
            filer_code="filer_code",
            include_trivial=True,
            limit=1,
            offset=0,
            signal_type="signal_type",
        )
        assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_signals(self, client: Axiora) -> None:
        response = client.ownership.with_raw_response.list_signals()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_signals(self, client: Axiora) -> None:
        with client.ownership.with_streaming_response.list_signals() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_unwinding_scoreboard(self, client: Axiora) -> None:
        ownership = client.ownership.list_unwinding_scoreboard()
        assert_matches_type(OwnershipListUnwindingScoreboardResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_unwinding_scoreboard_with_all_params(self, client: Axiora) -> None:
        ownership = client.ownership.list_unwinding_scoreboard(
            limit=1,
        )
        assert_matches_type(OwnershipListUnwindingScoreboardResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_unwinding_scoreboard(self, client: Axiora) -> None:
        response = client.ownership.with_raw_response.list_unwinding_scoreboard()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(OwnershipListUnwindingScoreboardResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_unwinding_scoreboard(self, client: Axiora) -> None:
        with client.ownership.with_streaming_response.list_unwinding_scoreboard() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(OwnershipListUnwindingScoreboardResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOwnership:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_probability_table(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.ownership.get_probability_table()
        assert_matches_type(OwnershipGetProbabilityTableResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_probability_table(self, async_client: AsyncAxiora) -> None:
        response = await async_client.ownership.with_raw_response.get_probability_table()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(OwnershipGetProbabilityTableResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_probability_table(self, async_client: AsyncAxiora) -> None:
        async with async_client.ownership.with_streaming_response.get_probability_table() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(OwnershipGetProbabilityTableResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_activist_campaigns(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.ownership.list_activist_campaigns()
        assert_matches_type(OwnershipListActivistCampaignsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_activist_campaigns_with_all_params(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.ownership.list_activist_campaigns(
            limit=1,
        )
        assert_matches_type(OwnershipListActivistCampaignsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_activist_campaigns(self, async_client: AsyncAxiora) -> None:
        response = await async_client.ownership.with_raw_response.list_activist_campaigns()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(OwnershipListActivistCampaignsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_activist_campaigns(self, async_client: AsyncAxiora) -> None:
        async with async_client.ownership.with_streaming_response.list_activist_campaigns() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(OwnershipListActivistCampaignsResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_cross_holdings(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.ownership.list_cross_holdings()
        assert_matches_type(OwnershipListCrossHoldingsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_cross_holdings_with_all_params(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.ownership.list_cross_holdings(
            cursor="cursor",
            limit=1,
            offset=0,
        )
        assert_matches_type(OwnershipListCrossHoldingsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_cross_holdings(self, async_client: AsyncAxiora) -> None:
        response = await async_client.ownership.with_raw_response.list_cross_holdings()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(OwnershipListCrossHoldingsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_cross_holdings(self, async_client: AsyncAxiora) -> None:
        async with async_client.ownership.with_streaming_response.list_cross_holdings() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(OwnershipListCrossHoldingsResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_movers(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.ownership.list_movers()
        assert_matches_type(OwnershipListMoversResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_movers_with_all_params(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.ownership.list_movers(
            cursor="cursor",
            days=1,
            limit=1,
            min_delta_pct=0,
            offset=0,
            trajectory_type="trajectory_type",
        )
        assert_matches_type(OwnershipListMoversResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_movers(self, async_client: AsyncAxiora) -> None:
        response = await async_client.ownership.with_raw_response.list_movers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(OwnershipListMoversResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_movers(self, async_client: AsyncAxiora) -> None:
        async with async_client.ownership.with_streaming_response.list_movers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(OwnershipListMoversResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_signals(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.ownership.list_signals()
        assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_signals_with_all_params(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.ownership.list_signals(
            cursor="cursor",
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
            filer_code="filer_code",
            include_trivial=True,
            limit=1,
            offset=0,
            signal_type="signal_type",
        )
        assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_signals(self, async_client: AsyncAxiora) -> None:
        response = await async_client.ownership.with_raw_response.list_signals()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_signals(self, async_client: AsyncAxiora) -> None:
        async with async_client.ownership.with_streaming_response.list_signals() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_unwinding_scoreboard(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.ownership.list_unwinding_scoreboard()
        assert_matches_type(OwnershipListUnwindingScoreboardResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_unwinding_scoreboard_with_all_params(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.ownership.list_unwinding_scoreboard(
            limit=1,
        )
        assert_matches_type(OwnershipListUnwindingScoreboardResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_unwinding_scoreboard(self, async_client: AsyncAxiora) -> None:
        response = await async_client.ownership.with_raw_response.list_unwinding_scoreboard()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(OwnershipListUnwindingScoreboardResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_unwinding_scoreboard(self, async_client: AsyncAxiora) -> None:
        async with async_client.ownership.with_streaming_response.list_unwinding_scoreboard() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(OwnershipListUnwindingScoreboardResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True
