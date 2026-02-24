# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import TranslationSearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTranslations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Axiora) -> None:
        translation = client.translations.search(
            q="xx",
        )
        assert_matches_type(TranslationSearchResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Axiora) -> None:
        translation = client.translations.search(
            q="xx",
            fiscal_year=1900,
            limit=1,
            offset=0,
            section="section",
        )
        assert_matches_type(TranslationSearchResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Axiora) -> None:
        response = client.translations.with_raw_response.search(
            q="xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = response.parse()
        assert_matches_type(TranslationSearchResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Axiora) -> None:
        with client.translations.with_streaming_response.search(
            q="xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = response.parse()
            assert_matches_type(TranslationSearchResponse, translation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTranslations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncAxiora) -> None:
        translation = await async_client.translations.search(
            q="xx",
        )
        assert_matches_type(TranslationSearchResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncAxiora) -> None:
        translation = await async_client.translations.search(
            q="xx",
            fiscal_year=1900,
            limit=1,
            offset=0,
            section="section",
        )
        assert_matches_type(TranslationSearchResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncAxiora) -> None:
        response = await async_client.translations.with_raw_response.search(
            q="xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = await response.parse()
        assert_matches_type(TranslationSearchResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncAxiora) -> None:
        async with async_client.translations.with_streaming_response.search(
            q="xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = await response.parse()
            assert_matches_type(TranslationSearchResponse, translation, path=["response"])

        assert cast(Any, response.is_closed) is True
