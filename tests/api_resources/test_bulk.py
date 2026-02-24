# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import (
    BulkExportFinancialsJsonResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export_financials_csv(self, client: Axiora) -> None:
        bulk = client.bulk.export_financials_csv()
        assert bulk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export_financials_csv_with_all_params(self, client: Axiora) -> None:
        bulk = client.bulk.export_financials_csv(
            fields="fields",
            fiscal_year=1900,
            sector="sector",
        )
        assert bulk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_export_financials_csv(self, client: Axiora) -> None:
        response = client.bulk.with_raw_response.export_financials_csv()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert bulk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_export_financials_csv(self, client: Axiora) -> None:
        with client.bulk.with_streaming_response.export_financials_csv() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert bulk is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export_financials_json(self, client: Axiora) -> None:
        bulk = client.bulk.export_financials_json()
        assert_matches_type(BulkExportFinancialsJsonResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export_financials_json_with_all_params(self, client: Axiora) -> None:
        bulk = client.bulk.export_financials_json(
            fields="fields",
            fiscal_year=1900,
            sector="sector",
        )
        assert_matches_type(BulkExportFinancialsJsonResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_export_financials_json(self, client: Axiora) -> None:
        response = client.bulk.with_raw_response.export_financials_json()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkExportFinancialsJsonResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_export_financials_json(self, client: Axiora) -> None:
        with client.bulk.with_streaming_response.export_financials_json() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkExportFinancialsJsonResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBulk:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export_financials_csv(self, async_client: AsyncAxiora) -> None:
        bulk = await async_client.bulk.export_financials_csv()
        assert bulk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export_financials_csv_with_all_params(self, async_client: AsyncAxiora) -> None:
        bulk = await async_client.bulk.export_financials_csv(
            fields="fields",
            fiscal_year=1900,
            sector="sector",
        )
        assert bulk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_export_financials_csv(self, async_client: AsyncAxiora) -> None:
        response = await async_client.bulk.with_raw_response.export_financials_csv()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert bulk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_export_financials_csv(self, async_client: AsyncAxiora) -> None:
        async with async_client.bulk.with_streaming_response.export_financials_csv() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert bulk is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export_financials_json(self, async_client: AsyncAxiora) -> None:
        bulk = await async_client.bulk.export_financials_json()
        assert_matches_type(BulkExportFinancialsJsonResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export_financials_json_with_all_params(self, async_client: AsyncAxiora) -> None:
        bulk = await async_client.bulk.export_financials_json(
            fields="fields",
            fiscal_year=1900,
            sector="sector",
        )
        assert_matches_type(BulkExportFinancialsJsonResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_export_financials_json(self, async_client: AsyncAxiora) -> None:
        response = await async_client.bulk.with_raw_response.export_financials_json()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkExportFinancialsJsonResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_export_financials_json(self, async_client: AsyncAxiora) -> None:
        async with async_client.bulk.with_streaming_response.export_financials_json() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkExportFinancialsJsonResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True
