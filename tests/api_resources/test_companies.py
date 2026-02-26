# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import (
    ListResponse,
    CompanyRetrieveResponse,
    CompanyRetrievePeersResponse,
    CompanyRetrieveGrowthResponse,
    CompanyRetrieveHealthResponse,
    CompanyRetrieveRatiosResponse,
    CompanyRetrieveFinancialsResponse,
)
from axiora._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompanies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Axiora) -> None:
        company = client.companies.retrieve(
            code="code",
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Axiora) -> None:
        company = client.companies.retrieve(
            code="code",
            expand="expand",
            peer_limit=1,
            years=1,
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Axiora) -> None:
        response = client.companies.with_raw_response.retrieve(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Axiora) -> None:
        with client.companies.with_streaming_response.retrieve(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.with_raw_response.retrieve(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Axiora) -> None:
        company = client.companies.list()
        assert_matches_type(ListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Axiora) -> None:
        company = client.companies.list(
            cursor="cursor",
            limit=1,
            name="name",
            offset=0,
            sector="sector",
            securities_code="securities_code",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Axiora) -> None:
        response = client.companies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(ListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Axiora) -> None:
        with client.companies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(ListResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_financials(self, client: Axiora) -> None:
        company = client.companies.retrieve_financials(
            code="code",
        )
        assert_matches_type(CompanyRetrieveFinancialsResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_financials_with_all_params(self, client: Axiora) -> None:
        company = client.companies.retrieve_financials(
            code="code",
            fields="fields",
            years=1,
        )
        assert_matches_type(CompanyRetrieveFinancialsResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_financials(self, client: Axiora) -> None:
        response = client.companies.with_raw_response.retrieve_financials(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyRetrieveFinancialsResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_financials(self, client: Axiora) -> None:
        with client.companies.with_streaming_response.retrieve_financials(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyRetrieveFinancialsResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_financials(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.with_raw_response.retrieve_financials(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_growth(self, client: Axiora) -> None:
        company = client.companies.retrieve_growth(
            code="code",
        )
        assert_matches_type(CompanyRetrieveGrowthResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_growth_with_all_params(self, client: Axiora) -> None:
        company = client.companies.retrieve_growth(
            code="code",
            years=2,
        )
        assert_matches_type(CompanyRetrieveGrowthResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_growth(self, client: Axiora) -> None:
        response = client.companies.with_raw_response.retrieve_growth(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyRetrieveGrowthResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_growth(self, client: Axiora) -> None:
        with client.companies.with_streaming_response.retrieve_growth(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyRetrieveGrowthResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_growth(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.with_raw_response.retrieve_growth(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_health(self, client: Axiora) -> None:
        company = client.companies.retrieve_health(
            "code",
        )
        assert_matches_type(CompanyRetrieveHealthResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_health(self, client: Axiora) -> None:
        response = client.companies.with_raw_response.retrieve_health(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyRetrieveHealthResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_health(self, client: Axiora) -> None:
        with client.companies.with_streaming_response.retrieve_health(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyRetrieveHealthResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_health(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.with_raw_response.retrieve_health(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_peers(self, client: Axiora) -> None:
        company = client.companies.retrieve_peers(
            code="code",
        )
        assert_matches_type(CompanyRetrievePeersResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_peers_with_all_params(self, client: Axiora) -> None:
        company = client.companies.retrieve_peers(
            code="code",
            limit=1,
        )
        assert_matches_type(CompanyRetrievePeersResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_peers(self, client: Axiora) -> None:
        response = client.companies.with_raw_response.retrieve_peers(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyRetrievePeersResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_peers(self, client: Axiora) -> None:
        with client.companies.with_streaming_response.retrieve_peers(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyRetrievePeersResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_peers(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.with_raw_response.retrieve_peers(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_ratios(self, client: Axiora) -> None:
        company = client.companies.retrieve_ratios(
            code="code",
        )
        assert_matches_type(CompanyRetrieveRatiosResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_ratios_with_all_params(self, client: Axiora) -> None:
        company = client.companies.retrieve_ratios(
            code="code",
            years=1,
        )
        assert_matches_type(CompanyRetrieveRatiosResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_ratios(self, client: Axiora) -> None:
        response = client.companies.with_raw_response.retrieve_ratios(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyRetrieveRatiosResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_ratios(self, client: Axiora) -> None:
        with client.companies.with_streaming_response.retrieve_ratios(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyRetrieveRatiosResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_ratios(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.with_raw_response.retrieve_ratios(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Axiora) -> None:
        company = client.companies.search(
            q="x",
        )
        assert_matches_type(ListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Axiora) -> None:
        company = client.companies.search(
            q="x",
            limit=1,
        )
        assert_matches_type(ListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Axiora) -> None:
        response = client.companies.with_raw_response.search(
            q="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(ListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Axiora) -> None:
        with client.companies.with_streaming_response.search(
            q="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(ListResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompanies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.retrieve(
            code="code",
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.retrieve(
            code="code",
            expand="expand",
            peer_limit=1,
            years=1,
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.with_raw_response.retrieve(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.with_streaming_response.retrieve(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.with_raw_response.retrieve(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.list()
        assert_matches_type(ListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.list(
            cursor="cursor",
            limit=1,
            name="name",
            offset=0,
            sector="sector",
            securities_code="securities_code",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(ListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(ListResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_financials(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.retrieve_financials(
            code="code",
        )
        assert_matches_type(CompanyRetrieveFinancialsResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_financials_with_all_params(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.retrieve_financials(
            code="code",
            fields="fields",
            years=1,
        )
        assert_matches_type(CompanyRetrieveFinancialsResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_financials(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.with_raw_response.retrieve_financials(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyRetrieveFinancialsResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_financials(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.with_streaming_response.retrieve_financials(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyRetrieveFinancialsResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_financials(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.with_raw_response.retrieve_financials(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_growth(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.retrieve_growth(
            code="code",
        )
        assert_matches_type(CompanyRetrieveGrowthResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_growth_with_all_params(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.retrieve_growth(
            code="code",
            years=2,
        )
        assert_matches_type(CompanyRetrieveGrowthResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_growth(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.with_raw_response.retrieve_growth(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyRetrieveGrowthResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_growth(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.with_streaming_response.retrieve_growth(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyRetrieveGrowthResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_growth(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.with_raw_response.retrieve_growth(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_health(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.retrieve_health(
            "code",
        )
        assert_matches_type(CompanyRetrieveHealthResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_health(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.with_raw_response.retrieve_health(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyRetrieveHealthResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_health(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.with_streaming_response.retrieve_health(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyRetrieveHealthResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_health(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.with_raw_response.retrieve_health(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_peers(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.retrieve_peers(
            code="code",
        )
        assert_matches_type(CompanyRetrievePeersResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_peers_with_all_params(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.retrieve_peers(
            code="code",
            limit=1,
        )
        assert_matches_type(CompanyRetrievePeersResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_peers(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.with_raw_response.retrieve_peers(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyRetrievePeersResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_peers(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.with_streaming_response.retrieve_peers(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyRetrievePeersResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_peers(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.with_raw_response.retrieve_peers(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_ratios(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.retrieve_ratios(
            code="code",
        )
        assert_matches_type(CompanyRetrieveRatiosResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_ratios_with_all_params(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.retrieve_ratios(
            code="code",
            years=1,
        )
        assert_matches_type(CompanyRetrieveRatiosResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_ratios(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.with_raw_response.retrieve_ratios(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyRetrieveRatiosResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_ratios(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.with_streaming_response.retrieve_ratios(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyRetrieveRatiosResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_ratios(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.with_raw_response.retrieve_ratios(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.search(
            q="x",
        )
        assert_matches_type(ListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncAxiora) -> None:
        company = await async_client.companies.search(
            q="x",
            limit=1,
        )
        assert_matches_type(ListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.with_raw_response.search(
            q="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(ListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.with_streaming_response.search(
            q="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(ListResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True
