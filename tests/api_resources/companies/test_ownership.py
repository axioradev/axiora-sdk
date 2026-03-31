# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types.companies import (
    OwnershipGetChartResponse,
    OwnershipGetNetworkResponse,
    OwnershipListSignalsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOwnership:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_chart(self, client: Axiora) -> None:
        ownership = client.companies.ownership.get_chart(
            "code",
        )
        assert_matches_type(OwnershipGetChartResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_chart(self, client: Axiora) -> None:
        response = client.companies.ownership.with_raw_response.get_chart(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(OwnershipGetChartResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_chart(self, client: Axiora) -> None:
        with client.companies.ownership.with_streaming_response.get_chart(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(OwnershipGetChartResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_chart(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.ownership.with_raw_response.get_chart(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_network(self, client: Axiora) -> None:
        ownership = client.companies.ownership.get_network(
            "code",
        )
        assert_matches_type(OwnershipGetNetworkResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_network(self, client: Axiora) -> None:
        response = client.companies.ownership.with_raw_response.get_network(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(OwnershipGetNetworkResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_network(self, client: Axiora) -> None:
        with client.companies.ownership.with_streaming_response.get_network(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(OwnershipGetNetworkResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_network(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.ownership.with_raw_response.get_network(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_signals(self, client: Axiora) -> None:
        ownership = client.companies.ownership.list_signals(
            code="code",
        )
        assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_signals_with_all_params(self, client: Axiora) -> None:
        ownership = client.companies.ownership.list_signals(
            code="code",
            cursor="cursor",
            include_trivial=True,
            limit=1,
            offset=0,
            signal_type="signal_type",
        )
        assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_signals(self, client: Axiora) -> None:
        response = client.companies.ownership.with_raw_response.list_signals(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_signals(self, client: Axiora) -> None:
        with client.companies.ownership.with_streaming_response.list_signals(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_signals(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.ownership.with_raw_response.list_signals(
                code="",
            )


class TestAsyncOwnership:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_chart(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.companies.ownership.get_chart(
            "code",
        )
        assert_matches_type(OwnershipGetChartResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_chart(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.ownership.with_raw_response.get_chart(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(OwnershipGetChartResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_chart(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.ownership.with_streaming_response.get_chart(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(OwnershipGetChartResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_chart(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.ownership.with_raw_response.get_chart(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_network(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.companies.ownership.get_network(
            "code",
        )
        assert_matches_type(OwnershipGetNetworkResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_network(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.ownership.with_raw_response.get_network(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(OwnershipGetNetworkResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_network(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.ownership.with_streaming_response.get_network(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(OwnershipGetNetworkResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_network(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.ownership.with_raw_response.get_network(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_signals(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.companies.ownership.list_signals(
            code="code",
        )
        assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_signals_with_all_params(self, async_client: AsyncAxiora) -> None:
        ownership = await async_client.companies.ownership.list_signals(
            code="code",
            cursor="cursor",
            include_trivial=True,
            limit=1,
            offset=0,
            signal_type="signal_type",
        )
        assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_signals(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.ownership.with_raw_response.list_signals(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_signals(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.ownership.with_streaming_response.list_signals(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(OwnershipListSignalsResponse, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_signals(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.ownership.with_raw_response.list_signals(
                code="",
            )
