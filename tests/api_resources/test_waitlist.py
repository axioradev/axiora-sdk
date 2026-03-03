# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWaitlist:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_join(self, client: Axiora) -> None:
        waitlist = client.waitlist.join(
            tier="tier",
        )
        assert_matches_type(object, waitlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_join_with_all_params(self, client: Axiora) -> None:
        waitlist = client.waitlist.join(
            tier="tier",
            email="email",
        )
        assert_matches_type(object, waitlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_join(self, client: Axiora) -> None:
        response = client.waitlist.with_raw_response.join(
            tier="tier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waitlist = response.parse()
        assert_matches_type(object, waitlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_join(self, client: Axiora) -> None:
        with client.waitlist.with_streaming_response.join(
            tier="tier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waitlist = response.parse()
            assert_matches_type(object, waitlist, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWaitlist:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_join(self, async_client: AsyncAxiora) -> None:
        waitlist = await async_client.waitlist.join(
            tier="tier",
        )
        assert_matches_type(object, waitlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_join_with_all_params(self, async_client: AsyncAxiora) -> None:
        waitlist = await async_client.waitlist.join(
            tier="tier",
            email="email",
        )
        assert_matches_type(object, waitlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_join(self, async_client: AsyncAxiora) -> None:
        response = await async_client.waitlist.with_raw_response.join(
            tier="tier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waitlist = await response.parse()
        assert_matches_type(object, waitlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_join(self, async_client: AsyncAxiora) -> None:
        async with async_client.waitlist.with_streaming_response.join(
            tier="tier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waitlist = await response.parse()
            assert_matches_type(object, waitlist, path=["response"])

        assert cast(Any, response.is_closed) is True
