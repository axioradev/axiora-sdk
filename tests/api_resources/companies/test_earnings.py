# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types.companies import (
    EarningGetSignalsResponse,
    EarningGetEarningsResponse,
    EarningGetSurpriseResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEarnings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_earnings(self, client: Axiora) -> None:
        earning = client.companies.earnings.get_earnings(
            code="code",
        )
        assert_matches_type(EarningGetEarningsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_earnings_with_all_params(self, client: Axiora) -> None:
        earning = client.companies.earnings.get_earnings(
            code="code",
            period_type="period_type",
            years=1,
        )
        assert_matches_type(EarningGetEarningsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_earnings(self, client: Axiora) -> None:
        response = client.companies.earnings.with_raw_response.get_earnings(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        earning = response.parse()
        assert_matches_type(EarningGetEarningsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_earnings(self, client: Axiora) -> None:
        with client.companies.earnings.with_streaming_response.get_earnings(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            earning = response.parse()
            assert_matches_type(EarningGetEarningsResponse, earning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_earnings(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.earnings.with_raw_response.get_earnings(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_signals(self, client: Axiora) -> None:
        earning = client.companies.earnings.get_signals(
            code="code",
        )
        assert_matches_type(EarningGetSignalsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_signals_with_all_params(self, client: Axiora) -> None:
        earning = client.companies.earnings.get_signals(
            code="code",
            limit=1,
            signal_type="signal_type",
        )
        assert_matches_type(EarningGetSignalsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_signals(self, client: Axiora) -> None:
        response = client.companies.earnings.with_raw_response.get_signals(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        earning = response.parse()
        assert_matches_type(EarningGetSignalsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_signals(self, client: Axiora) -> None:
        with client.companies.earnings.with_streaming_response.get_signals(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            earning = response.parse()
            assert_matches_type(EarningGetSignalsResponse, earning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_signals(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.earnings.with_raw_response.get_signals(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_surprise(self, client: Axiora) -> None:
        earning = client.companies.earnings.get_surprise(
            "code",
        )
        assert_matches_type(EarningGetSurpriseResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_surprise(self, client: Axiora) -> None:
        response = client.companies.earnings.with_raw_response.get_surprise(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        earning = response.parse()
        assert_matches_type(EarningGetSurpriseResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_surprise(self, client: Axiora) -> None:
        with client.companies.earnings.with_streaming_response.get_surprise(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            earning = response.parse()
            assert_matches_type(EarningGetSurpriseResponse, earning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_surprise(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.earnings.with_raw_response.get_surprise(
                "",
            )


class TestAsyncEarnings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_earnings(self, async_client: AsyncAxiora) -> None:
        earning = await async_client.companies.earnings.get_earnings(
            code="code",
        )
        assert_matches_type(EarningGetEarningsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_earnings_with_all_params(self, async_client: AsyncAxiora) -> None:
        earning = await async_client.companies.earnings.get_earnings(
            code="code",
            period_type="period_type",
            years=1,
        )
        assert_matches_type(EarningGetEarningsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_earnings(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.earnings.with_raw_response.get_earnings(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        earning = await response.parse()
        assert_matches_type(EarningGetEarningsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_earnings(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.earnings.with_streaming_response.get_earnings(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            earning = await response.parse()
            assert_matches_type(EarningGetEarningsResponse, earning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_earnings(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.earnings.with_raw_response.get_earnings(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_signals(self, async_client: AsyncAxiora) -> None:
        earning = await async_client.companies.earnings.get_signals(
            code="code",
        )
        assert_matches_type(EarningGetSignalsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_signals_with_all_params(self, async_client: AsyncAxiora) -> None:
        earning = await async_client.companies.earnings.get_signals(
            code="code",
            limit=1,
            signal_type="signal_type",
        )
        assert_matches_type(EarningGetSignalsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_signals(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.earnings.with_raw_response.get_signals(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        earning = await response.parse()
        assert_matches_type(EarningGetSignalsResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_signals(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.earnings.with_streaming_response.get_signals(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            earning = await response.parse()
            assert_matches_type(EarningGetSignalsResponse, earning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_signals(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.earnings.with_raw_response.get_signals(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_surprise(self, async_client: AsyncAxiora) -> None:
        earning = await async_client.companies.earnings.get_surprise(
            "code",
        )
        assert_matches_type(EarningGetSurpriseResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_surprise(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.earnings.with_raw_response.get_surprise(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        earning = await response.parse()
        assert_matches_type(EarningGetSurpriseResponse, earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_surprise(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.earnings.with_streaming_response.get_surprise(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            earning = await response.parse()
            assert_matches_type(EarningGetSurpriseResponse, earning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_surprise(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.earnings.with_raw_response.get_surprise(
                "",
            )
