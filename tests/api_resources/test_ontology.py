# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora.types import (
    OntologyListFieldsResponse,
    OntologyRetrieveFieldResponse,
    OntologyRetrieveVersionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOntology:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_version(self, client: Axiora) -> None:
        ontology = client.ontology.retrieve_version()
        assert_matches_type(OntologyRetrieveVersionResponse, ontology, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_version(self, client: Axiora) -> None:
        response = client.ontology.with_raw_response.retrieve_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ontology = response.parse()
        assert_matches_type(OntologyRetrieveVersionResponse, ontology, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_version(self, client: Axiora) -> None:
        with client.ontology.with_streaming_response.retrieve_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ontology = response.parse()
            assert_matches_type(OntologyRetrieveVersionResponse, ontology, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_fields(self, client: Axiora) -> None:
        ontology = client.ontology.list_fields()
        assert_matches_type(OntologyListFieldsResponse, ontology, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_fields_with_all_params(self, client: Axiora) -> None:
        ontology = client.ontology.list_fields(
            category="category",
        )
        assert_matches_type(OntologyListFieldsResponse, ontology, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_fields(self, client: Axiora) -> None:
        response = client.ontology.with_raw_response.list_fields()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ontology = response.parse()
        assert_matches_type(OntologyListFieldsResponse, ontology, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_fields(self, client: Axiora) -> None:
        with client.ontology.with_streaming_response.list_fields() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ontology = response.parse()
            assert_matches_type(OntologyListFieldsResponse, ontology, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_field(self, client: Axiora) -> None:
        ontology = client.ontology.retrieve_field(
            "field_name",
        )
        assert_matches_type(OntologyRetrieveFieldResponse, ontology, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_field(self, client: Axiora) -> None:
        response = client.ontology.with_raw_response.retrieve_field(
            "field_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ontology = response.parse()
        assert_matches_type(OntologyRetrieveFieldResponse, ontology, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_field(self, client: Axiora) -> None:
        with client.ontology.with_streaming_response.retrieve_field(
            "field_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ontology = response.parse()
            assert_matches_type(OntologyRetrieveFieldResponse, ontology, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_field(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_name` but received ''"):
            client.ontology.with_raw_response.retrieve_field(
                "",
            )


class TestAsyncOntology:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_version(self, async_client: AsyncAxiora) -> None:
        ontology = await async_client.ontology.retrieve_version()
        assert_matches_type(OntologyRetrieveVersionResponse, ontology, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_version(self, async_client: AsyncAxiora) -> None:
        response = await async_client.ontology.with_raw_response.retrieve_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ontology = await response.parse()
        assert_matches_type(OntologyRetrieveVersionResponse, ontology, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_version(self, async_client: AsyncAxiora) -> None:
        async with async_client.ontology.with_streaming_response.retrieve_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ontology = await response.parse()
            assert_matches_type(OntologyRetrieveVersionResponse, ontology, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_fields(self, async_client: AsyncAxiora) -> None:
        ontology = await async_client.ontology.list_fields()
        assert_matches_type(OntologyListFieldsResponse, ontology, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_fields_with_all_params(self, async_client: AsyncAxiora) -> None:
        ontology = await async_client.ontology.list_fields(
            category="category",
        )
        assert_matches_type(OntologyListFieldsResponse, ontology, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_fields(self, async_client: AsyncAxiora) -> None:
        response = await async_client.ontology.with_raw_response.list_fields()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ontology = await response.parse()
        assert_matches_type(OntologyListFieldsResponse, ontology, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_fields(self, async_client: AsyncAxiora) -> None:
        async with async_client.ontology.with_streaming_response.list_fields() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ontology = await response.parse()
            assert_matches_type(OntologyListFieldsResponse, ontology, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_field(self, async_client: AsyncAxiora) -> None:
        ontology = await async_client.ontology.retrieve_field(
            "field_name",
        )
        assert_matches_type(OntologyRetrieveFieldResponse, ontology, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_field(self, async_client: AsyncAxiora) -> None:
        response = await async_client.ontology.with_raw_response.retrieve_field(
            "field_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ontology = await response.parse()
        assert_matches_type(OntologyRetrieveFieldResponse, ontology, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_field(self, async_client: AsyncAxiora) -> None:
        async with async_client.ontology.with_streaming_response.retrieve_field(
            "field_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ontology = await response.parse()
            assert_matches_type(OntologyRetrieveFieldResponse, ontology, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_field(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_name` but received ''"):
            await async_client.ontology.with_raw_response.retrieve_field(
                "",
            )
