# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from axiora import Axiora, AsyncAxiora
from tests.utils import assert_matches_type
from axiora._utils import parse_date
from axiora.types.companies.ownership import (
    TrajectoryListResponse,
    TrajectoryGetProbabilitiesResponse,
    TrajectoryGetFilerTrajectoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrajectories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Axiora) -> None:
        trajectory = client.companies.ownership.trajectories.list(
            code="code",
        )
        assert_matches_type(TrajectoryListResponse, trajectory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Axiora) -> None:
        trajectory = client.companies.ownership.trajectories.list(
            code="code",
            cursor="cursor",
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
            limit=1,
            offset=0,
            trajectory_type="trajectory_type",
        )
        assert_matches_type(TrajectoryListResponse, trajectory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Axiora) -> None:
        response = client.companies.ownership.trajectories.with_raw_response.list(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trajectory = response.parse()
        assert_matches_type(TrajectoryListResponse, trajectory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Axiora) -> None:
        with client.companies.ownership.trajectories.with_streaming_response.list(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trajectory = response.parse()
            assert_matches_type(TrajectoryListResponse, trajectory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.ownership.trajectories.with_raw_response.list(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_filer_trajectory(self, client: Axiora) -> None:
        trajectory = client.companies.ownership.trajectories.get_filer_trajectory(
            filer_code="filer_code",
            code="code",
        )
        assert_matches_type(TrajectoryGetFilerTrajectoryResponse, trajectory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_filer_trajectory(self, client: Axiora) -> None:
        response = client.companies.ownership.trajectories.with_raw_response.get_filer_trajectory(
            filer_code="filer_code",
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trajectory = response.parse()
        assert_matches_type(TrajectoryGetFilerTrajectoryResponse, trajectory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_filer_trajectory(self, client: Axiora) -> None:
        with client.companies.ownership.trajectories.with_streaming_response.get_filer_trajectory(
            filer_code="filer_code",
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trajectory = response.parse()
            assert_matches_type(TrajectoryGetFilerTrajectoryResponse, trajectory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_filer_trajectory(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.ownership.trajectories.with_raw_response.get_filer_trajectory(
                filer_code="filer_code",
                code="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filer_code` but received ''"):
            client.companies.ownership.trajectories.with_raw_response.get_filer_trajectory(
                filer_code="",
                code="code",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_probabilities(self, client: Axiora) -> None:
        trajectory = client.companies.ownership.trajectories.get_probabilities(
            filer_code="filer_code",
            code="code",
        )
        assert_matches_type(TrajectoryGetProbabilitiesResponse, trajectory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_probabilities(self, client: Axiora) -> None:
        response = client.companies.ownership.trajectories.with_raw_response.get_probabilities(
            filer_code="filer_code",
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trajectory = response.parse()
        assert_matches_type(TrajectoryGetProbabilitiesResponse, trajectory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_probabilities(self, client: Axiora) -> None:
        with client.companies.ownership.trajectories.with_streaming_response.get_probabilities(
            filer_code="filer_code",
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trajectory = response.parse()
            assert_matches_type(TrajectoryGetProbabilitiesResponse, trajectory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_probabilities(self, client: Axiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.companies.ownership.trajectories.with_raw_response.get_probabilities(
                filer_code="filer_code",
                code="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filer_code` but received ''"):
            client.companies.ownership.trajectories.with_raw_response.get_probabilities(
                filer_code="",
                code="code",
            )


class TestAsyncTrajectories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAxiora) -> None:
        trajectory = await async_client.companies.ownership.trajectories.list(
            code="code",
        )
        assert_matches_type(TrajectoryListResponse, trajectory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAxiora) -> None:
        trajectory = await async_client.companies.ownership.trajectories.list(
            code="code",
            cursor="cursor",
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
            limit=1,
            offset=0,
            trajectory_type="trajectory_type",
        )
        assert_matches_type(TrajectoryListResponse, trajectory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.ownership.trajectories.with_raw_response.list(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trajectory = await response.parse()
        assert_matches_type(TrajectoryListResponse, trajectory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.ownership.trajectories.with_streaming_response.list(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trajectory = await response.parse()
            assert_matches_type(TrajectoryListResponse, trajectory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.ownership.trajectories.with_raw_response.list(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_filer_trajectory(self, async_client: AsyncAxiora) -> None:
        trajectory = await async_client.companies.ownership.trajectories.get_filer_trajectory(
            filer_code="filer_code",
            code="code",
        )
        assert_matches_type(TrajectoryGetFilerTrajectoryResponse, trajectory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_filer_trajectory(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.ownership.trajectories.with_raw_response.get_filer_trajectory(
            filer_code="filer_code",
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trajectory = await response.parse()
        assert_matches_type(TrajectoryGetFilerTrajectoryResponse, trajectory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_filer_trajectory(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.ownership.trajectories.with_streaming_response.get_filer_trajectory(
            filer_code="filer_code",
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trajectory = await response.parse()
            assert_matches_type(TrajectoryGetFilerTrajectoryResponse, trajectory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_filer_trajectory(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.ownership.trajectories.with_raw_response.get_filer_trajectory(
                filer_code="filer_code",
                code="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filer_code` but received ''"):
            await async_client.companies.ownership.trajectories.with_raw_response.get_filer_trajectory(
                filer_code="",
                code="code",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_probabilities(self, async_client: AsyncAxiora) -> None:
        trajectory = await async_client.companies.ownership.trajectories.get_probabilities(
            filer_code="filer_code",
            code="code",
        )
        assert_matches_type(TrajectoryGetProbabilitiesResponse, trajectory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_probabilities(self, async_client: AsyncAxiora) -> None:
        response = await async_client.companies.ownership.trajectories.with_raw_response.get_probabilities(
            filer_code="filer_code",
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trajectory = await response.parse()
        assert_matches_type(TrajectoryGetProbabilitiesResponse, trajectory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_probabilities(self, async_client: AsyncAxiora) -> None:
        async with async_client.companies.ownership.trajectories.with_streaming_response.get_probabilities(
            filer_code="filer_code",
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trajectory = await response.parse()
            assert_matches_type(TrajectoryGetProbabilitiesResponse, trajectory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_probabilities(self, async_client: AsyncAxiora) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.companies.ownership.trajectories.with_raw_response.get_probabilities(
                filer_code="filer_code",
                code="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filer_code` but received ''"):
            await async_client.companies.ownership.trajectories.with_raw_response.get_probabilities(
                filer_code="",
                code="code",
            )
