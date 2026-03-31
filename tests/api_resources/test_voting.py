# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import ListResponseVotingResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoting:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_recent(self, client: Axiora) -> None:
        voting = client.voting.list_recent()
        assert_matches_type(ListResponseVotingResult, voting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_recent_with_all_params(self, client: Axiora) -> None:
        voting = client.voting.list_recent(
            cursor="cursor",
            limit=1,
            min_dissent_pct=0,
            offset=0,
        )
        assert_matches_type(ListResponseVotingResult, voting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_recent(self, client: Axiora) -> None:
        response = client.voting.with_raw_response.list_recent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voting = response.parse()
        assert_matches_type(ListResponseVotingResult, voting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_recent(self, client: Axiora) -> None:
        with client.voting.with_streaming_response.list_recent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voting = response.parse()
            assert_matches_type(ListResponseVotingResult, voting, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVoting:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_recent(self, async_client: AsyncAxiora) -> None:
        voting = await async_client.voting.list_recent()
        assert_matches_type(ListResponseVotingResult, voting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_recent_with_all_params(self, async_client: AsyncAxiora) -> None:
        voting = await async_client.voting.list_recent(
            cursor="cursor",
            limit=1,
            min_dissent_pct=0,
            offset=0,
        )
        assert_matches_type(ListResponseVotingResult, voting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_recent(self, async_client: AsyncAxiora) -> None:
        response = await async_client.voting.with_raw_response.list_recent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voting = await response.parse()
        assert_matches_type(ListResponseVotingResult, voting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_recent(self, async_client: AsyncAxiora) -> None:
        async with async_client.voting.with_streaming_response.list_recent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voting = await response.parse()
            assert_matches_type(ListResponseVotingResult, voting, path=["response"])

        assert cast(Any, response.is_closed) is True
