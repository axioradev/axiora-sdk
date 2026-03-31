# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import WatchlistAddResponse, WatchlistListResponse, WatchlistRemoveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWatchlist:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Axiora) -> None:
        watchlist = client.watchlist.list()
        assert_matches_type(WatchlistListResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Axiora) -> None:
        response = client.watchlist.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = response.parse()
        assert_matches_type(WatchlistListResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Axiora) -> None:
        with client.watchlist.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = response.parse()
            assert_matches_type(WatchlistListResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Axiora) -> None:
        watchlist = client.watchlist.add(
            entity_code="x",
            entity_type="investor",
        )
        assert_matches_type(WatchlistAddResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: Axiora) -> None:
        watchlist = client.watchlist.add(
            entity_code="x",
            entity_type="investor",
            entity_name="entity_name",
        )
        assert_matches_type(WatchlistAddResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Axiora) -> None:
        response = client.watchlist.with_raw_response.add(
            entity_code="x",
            entity_type="investor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = response.parse()
        assert_matches_type(WatchlistAddResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Axiora) -> None:
        with client.watchlist.with_streaming_response.add(
            entity_code="x",
            entity_type="investor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = response.parse()
            assert_matches_type(WatchlistAddResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Axiora) -> None:
        watchlist = client.watchlist.remove(
            0,
        )
        assert_matches_type(WatchlistRemoveResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Axiora) -> None:
        response = client.watchlist.with_raw_response.remove(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = response.parse()
        assert_matches_type(WatchlistRemoveResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Axiora) -> None:
        with client.watchlist.with_streaming_response.remove(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = response.parse()
            assert_matches_type(WatchlistRemoveResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWatchlist:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAxiora) -> None:
        watchlist = await async_client.watchlist.list()
        assert_matches_type(WatchlistListResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAxiora) -> None:
        response = await async_client.watchlist.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = await response.parse()
        assert_matches_type(WatchlistListResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAxiora) -> None:
        async with async_client.watchlist.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = await response.parse()
            assert_matches_type(WatchlistListResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncAxiora) -> None:
        watchlist = await async_client.watchlist.add(
            entity_code="x",
            entity_type="investor",
        )
        assert_matches_type(WatchlistAddResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncAxiora) -> None:
        watchlist = await async_client.watchlist.add(
            entity_code="x",
            entity_type="investor",
            entity_name="entity_name",
        )
        assert_matches_type(WatchlistAddResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncAxiora) -> None:
        response = await async_client.watchlist.with_raw_response.add(
            entity_code="x",
            entity_type="investor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = await response.parse()
        assert_matches_type(WatchlistAddResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncAxiora) -> None:
        async with async_client.watchlist.with_streaming_response.add(
            entity_code="x",
            entity_type="investor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = await response.parse()
            assert_matches_type(WatchlistAddResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncAxiora) -> None:
        watchlist = await async_client.watchlist.remove(
            0,
        )
        assert_matches_type(WatchlistRemoveResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncAxiora) -> None:
        response = await async_client.watchlist.with_raw_response.remove(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = await response.parse()
        assert_matches_type(WatchlistRemoveResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncAxiora) -> None:
        async with async_client.watchlist.with_streaming_response.remove(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = await response.parse()
            assert_matches_type(WatchlistRemoveResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True
