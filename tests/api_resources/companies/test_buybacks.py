# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora._utils import parse_date
from axiora.types.companies import BuybackListResponse, BuybackGetAnalysisResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBuybacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Axiora) -> None:
        buyback = client.companies.buybacks.list(
            code="code",
        )
        assert_matches_type(BuybackListResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Axiora) -> None:
        buyback = client.companies.buybacks.list(
            code="code",
            cursor="cursor",
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
            limit=1,
            offset=0,
        )
        assert_matches_type(BuybackListResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Axiora) -> None:
        response = client.companies.buybacks.with_raw_response.list(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        buyback = response.parse()
        assert_matches_type(BuybackListResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Axiora) -> None:
        with client.companies.buybacks.with_streaming_response.list(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            buyback = response.parse()
            assert_matches_type(BuybackListResponse, buyback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.buybacks.with_raw_response.list(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_analysis(self, client: Axiora) -> None:
        buyback = client.companies.buybacks.get_analysis(
            "code",
        )
        assert_matches_type(BuybackGetAnalysisResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_analysis(self, client: Axiora) -> None:
        response = client.companies.buybacks.with_raw_response.get_analysis(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        buyback = response.parse()
        assert_matches_type(BuybackGetAnalysisResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_analysis(self, client: Axiora) -> None:
        with client.companies.buybacks.with_streaming_response.get_analysis(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            buyback = response.parse()
            assert_matches_type(BuybackGetAnalysisResponse, buyback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_analysis(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.buybacks.with_raw_response.get_analysis(
                "",
            )


class TestAsyncBuybacks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAxiora) -> None:
        buyback = await async_client.companies.buybacks.list(
            code="code",
        )
        assert_matches_type(BuybackListResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAxiora) -> None:
        buyback = await async_client.companies.buybacks.list(
            code="code",
            cursor="cursor",
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
            limit=1,
            offset=0,
        )
        assert_matches_type(BuybackListResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.buybacks.with_raw_response.list(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        buyback = await response.parse()
        assert_matches_type(BuybackListResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.buybacks.with_streaming_response.list(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            buyback = await response.parse()
            assert_matches_type(BuybackListResponse, buyback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.buybacks.with_raw_response.list(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_analysis(self, async_client: AsyncAxiora) -> None:
        buyback = await async_client.companies.buybacks.get_analysis(
            "code",
        )
        assert_matches_type(BuybackGetAnalysisResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_analysis(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.buybacks.with_raw_response.get_analysis(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        buyback = await response.parse()
        assert_matches_type(BuybackGetAnalysisResponse, buyback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_analysis(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.buybacks.with_streaming_response.get_analysis(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            buyback = await response.parse()
            assert_matches_type(BuybackGetAnalysisResponse, buyback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_analysis(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.buybacks.with_raw_response.get_analysis(
                "",
            )
