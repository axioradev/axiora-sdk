# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import (
    FilingListResponse,
    FilingCalendarResponse,
    FilingRetrieveResponse,
    FilingRetrieveTranslationsResponse,
)
from axiora._utils import parse_date, parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFilings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Axiora) -> None:
        filing = client.filings.retrieve(
            "doc_id",
        )
        assert_matches_type(FilingRetrieveResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Axiora) -> None:
        response = client.filings.with_raw_response.retrieve(
            "doc_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filing = response.parse()
        assert_matches_type(FilingRetrieveResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Axiora) -> None:
        with client.filings.with_streaming_response.retrieve(
            "doc_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filing = response.parse()
            assert_matches_type(FilingRetrieveResponse, filing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.filings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Axiora) -> None:
        filing = client.filings.list()
        assert_matches_type(FilingListResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Axiora) -> None:
        filing = client.filings.list(
            company_code="company_code",
            cursor="cursor",
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
            doc_type="doc_type",
            limit=1,
            offset=0,
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(FilingListResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Axiora) -> None:
        response = client.filings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filing = response.parse()
        assert_matches_type(FilingListResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Axiora) -> None:
        with client.filings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filing = response.parse()
            assert_matches_type(FilingListResponse, filing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calendar(self, client: Axiora) -> None:
        filing = client.filings.calendar(
            month="7321-69",
        )
        assert_matches_type(FilingCalendarResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_calendar(self, client: Axiora) -> None:
        response = client.filings.with_raw_response.calendar(
            month="7321-69",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filing = response.parse()
        assert_matches_type(FilingCalendarResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_calendar(self, client: Axiora) -> None:
        with client.filings.with_streaming_response.calendar(
            month="7321-69",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filing = response.parse()
            assert_matches_type(FilingCalendarResponse, filing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_translations(self, client: Axiora) -> None:
        filing = client.filings.retrieve_translations(
            doc_id="doc_id",
        )
        assert_matches_type(FilingRetrieveTranslationsResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_translations_with_all_params(self, client: Axiora) -> None:
        filing = client.filings.retrieve_translations(
            doc_id="doc_id",
            section="section",
        )
        assert_matches_type(FilingRetrieveTranslationsResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_translations(self, client: Axiora) -> None:
        response = client.filings.with_raw_response.retrieve_translations(
            doc_id="doc_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filing = response.parse()
        assert_matches_type(FilingRetrieveTranslationsResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_translations(self, client: Axiora) -> None:
        with client.filings.with_streaming_response.retrieve_translations(
            doc_id="doc_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filing = response.parse()
            assert_matches_type(FilingRetrieveTranslationsResponse, filing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_translations(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.filings.with_raw_response.retrieve_translations(
                doc_id="",
            )


class TestAsyncFilings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAxiora) -> None:
        filing = await async_client.filings.retrieve(
            "doc_id",
        )
        assert_matches_type(FilingRetrieveResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAxiora) -> None:
        response = await async_client.filings.with_raw_response.retrieve(
            "doc_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filing = await response.parse()
        assert_matches_type(FilingRetrieveResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAxiora) -> None:
        async with async_client.filings.with_streaming_response.retrieve(
            "doc_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filing = await response.parse()
            assert_matches_type(FilingRetrieveResponse, filing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.filings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAxiora) -> None:
        filing = await async_client.filings.list()
        assert_matches_type(FilingListResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAxiora) -> None:
        filing = await async_client.filings.list(
            company_code="company_code",
            cursor="cursor",
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
            doc_type="doc_type",
            limit=1,
            offset=0,
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(FilingListResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAxiora) -> None:
        response = await async_client.filings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filing = await response.parse()
        assert_matches_type(FilingListResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAxiora) -> None:
        async with async_client.filings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filing = await response.parse()
            assert_matches_type(FilingListResponse, filing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calendar(self, async_client: AsyncAxiora) -> None:
        filing = await async_client.filings.calendar(
            month="7321-69",
        )
        assert_matches_type(FilingCalendarResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_calendar(self, async_client: AsyncAxiora) -> None:
        response = await async_client.filings.with_raw_response.calendar(
            month="7321-69",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filing = await response.parse()
        assert_matches_type(FilingCalendarResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_calendar(self, async_client: AsyncAxiora) -> None:
        async with async_client.filings.with_streaming_response.calendar(
            month="7321-69",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filing = await response.parse()
            assert_matches_type(FilingCalendarResponse, filing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_translations(self, async_client: AsyncAxiora) -> None:
        filing = await async_client.filings.retrieve_translations(
            doc_id="doc_id",
        )
        assert_matches_type(FilingRetrieveTranslationsResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_translations_with_all_params(self, async_client: AsyncAxiora) -> None:
        filing = await async_client.filings.retrieve_translations(
            doc_id="doc_id",
            section="section",
        )
        assert_matches_type(FilingRetrieveTranslationsResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_translations(self, async_client: AsyncAxiora) -> None:
        response = await async_client.filings.with_raw_response.retrieve_translations(
            doc_id="doc_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filing = await response.parse()
        assert_matches_type(FilingRetrieveTranslationsResponse, filing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_translations(self, async_client: AsyncAxiora) -> None:
        async with async_client.filings.with_streaming_response.retrieve_translations(
            doc_id="doc_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filing = await response.parse()
            assert_matches_type(FilingRetrieveTranslationsResponse, filing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_translations(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.filings.with_raw_response.retrieve_translations(
                doc_id="",
            )
