# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import (
    BulkExportFinancialsJsonResponse,
)
from axiora._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_ownership_signals(self, client: Axiora, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/bulk/ownership_signals.parquet").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        bulk = client.bulk.export_ownership_signals()
        assert bulk.is_closed
        assert bulk.json() == {"foo": "bar"}
        assert cast(Any, bulk.is_closed) is True
        assert isinstance(bulk, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_ownership_signals(self, client: Axiora, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/bulk/ownership_signals.parquet").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        bulk = client.bulk.with_raw_response.export_ownership_signals()

        assert bulk.is_closed is True
        assert bulk.http_request.headers.get("X-Stainless-Lang") == "python"
        assert bulk.json() == {"foo": "bar"}
        assert isinstance(bulk, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_ownership_signals(self, client: Axiora, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/bulk/ownership_signals.parquet").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.bulk.with_streaming_response.export_ownership_signals() as bulk:
            assert not bulk.is_closed
            assert bulk.http_request.headers.get("X-Stainless-Lang") == "python"

            assert bulk.json() == {"foo": "bar"}
            assert cast(Any, bulk.is_closed) is True
            assert isinstance(bulk, StreamedBinaryAPIResponse)

        assert cast(Any, bulk.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_ownership_trajectories(self, client: Axiora, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/bulk/ownership_trajectories.parquet").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        bulk = client.bulk.export_ownership_trajectories()
        assert bulk.is_closed
        assert bulk.json() == {"foo": "bar"}
        assert cast(Any, bulk.is_closed) is True
        assert isinstance(bulk, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_ownership_trajectories(self, client: Axiora, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/bulk/ownership_trajectories.parquet").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        bulk = client.bulk.with_raw_response.export_ownership_trajectories()

        assert bulk.is_closed is True
        assert bulk.http_request.headers.get("X-Stainless-Lang") == "python"
        assert bulk.json() == {"foo": "bar"}
        assert isinstance(bulk, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_ownership_trajectories(self, client: Axiora, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/bulk/ownership_trajectories.parquet").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.bulk.with_streaming_response.export_ownership_trajectories() as bulk:
            assert not bulk.is_closed
            assert bulk.http_request.headers.get("X-Stainless-Lang") == "python"

            assert bulk.json() == {"foo": "bar"}
            assert cast(Any, bulk.is_closed) is True
            assert isinstance(bulk, StreamedBinaryAPIResponse)

        assert cast(Any, bulk.is_closed) is True


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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_ownership_signals(self, async_client: AsyncAxiora, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/bulk/ownership_signals.parquet").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        bulk = await async_client.bulk.export_ownership_signals()
        assert bulk.is_closed
        assert await bulk.json() == {"foo": "bar"}
        assert cast(Any, bulk.is_closed) is True
        assert isinstance(bulk, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_ownership_signals(
        self, async_client: AsyncAxiora, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/bulk/ownership_signals.parquet").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        bulk = await async_client.bulk.with_raw_response.export_ownership_signals()

        assert bulk.is_closed is True
        assert bulk.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await bulk.json() == {"foo": "bar"}
        assert isinstance(bulk, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_ownership_signals(
        self, async_client: AsyncAxiora, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/bulk/ownership_signals.parquet").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.bulk.with_streaming_response.export_ownership_signals() as bulk:
            assert not bulk.is_closed
            assert bulk.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await bulk.json() == {"foo": "bar"}
            assert cast(Any, bulk.is_closed) is True
            assert isinstance(bulk, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, bulk.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_ownership_trajectories(
        self, async_client: AsyncAxiora, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/bulk/ownership_trajectories.parquet").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        bulk = await async_client.bulk.export_ownership_trajectories()
        assert bulk.is_closed
        assert await bulk.json() == {"foo": "bar"}
        assert cast(Any, bulk.is_closed) is True
        assert isinstance(bulk, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_ownership_trajectories(
        self, async_client: AsyncAxiora, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/bulk/ownership_trajectories.parquet").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        bulk = await async_client.bulk.with_raw_response.export_ownership_trajectories()

        assert bulk.is_closed is True
        assert bulk.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await bulk.json() == {"foo": "bar"}
        assert isinstance(bulk, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_ownership_trajectories(
        self, async_client: AsyncAxiora, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/bulk/ownership_trajectories.parquet").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.bulk.with_streaming_response.export_ownership_trajectories() as bulk:
            assert not bulk.is_closed
            assert bulk.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await bulk.json() == {"foo": "bar"}
            assert cast(Any, bulk.is_closed) is True
            assert isinstance(bulk, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, bulk.is_closed) is True
