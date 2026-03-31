# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        bulk,
        keys,
        batch,
        oauth,
        usage,
        health,
        screen,
        voting,
        compare,
        filings,
        sectors,
        buybacks,
        coverage,
        earnings,
        rankings,
        sections,
        waitlist,
        webhooks,
        companies,
        freshness,
        investors,
        ownership,
        watchlist,
        timeseries,
        well_known,
        translations,
        relationships,
        shareholdings,
        capital_allocation,
    )
    from .resources.bulk import BulkResource, AsyncBulkResource
    from .resources.keys import KeysResource, AsyncKeysResource
    from .resources.batch import BatchResource, AsyncBatchResource
    from .resources.usage import UsageResource, AsyncUsageResource
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.screen import ScreenResource, AsyncScreenResource
    from .resources.voting import VotingResource, AsyncVotingResource
    from .resources.compare import CompareResource, AsyncCompareResource
    from .resources.filings import FilingsResource, AsyncFilingsResource
    from .resources.sectors import SectorsResource, AsyncSectorsResource
    from .resources.buybacks import BuybacksResource, AsyncBuybacksResource
    from .resources.coverage import CoverageResource, AsyncCoverageResource
    from .resources.earnings import EarningsResource, AsyncEarningsResource
    from .resources.rankings import RankingsResource, AsyncRankingsResource
    from .resources.sections import SectionsResource, AsyncSectionsResource
    from .resources.waitlist import WaitlistResource, AsyncWaitlistResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.freshness import FreshnessResource, AsyncFreshnessResource
    from .resources.investors import InvestorsResource, AsyncInvestorsResource
    from .resources.ownership import OwnershipResource, AsyncOwnershipResource
    from .resources.watchlist import WatchlistResource, AsyncWatchlistResource
    from .resources.timeseries import TimeseriesResource, AsyncTimeseriesResource
    from .resources.oauth.oauth import OAuthResource, AsyncOAuthResource
    from .resources.translations import TranslationsResource, AsyncTranslationsResource
    from .resources.relationships import RelationshipsResource, AsyncRelationshipsResource
    from .resources.shareholdings import ShareholdingsResource, AsyncShareholdingsResource
    from .resources.capital_allocation import CapitalAllocationResource, AsyncCapitalAllocationResource
    from .resources.companies.companies import CompaniesResource, AsyncCompaniesResource
    from .resources.well_known.well_known import WellKnownResource, AsyncWellKnownResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Axiora", "AsyncAxiora", "Client", "AsyncClient"]


class Axiora(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Axiora client instance.

        This automatically infers the `api_key` argument from the `AXIORA_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("AXIORA_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("AXIORA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.axiora.dev"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> HealthResource:
        from .resources.health import HealthResource

        return HealthResource(self)

    @cached_property
    def freshness(self) -> FreshnessResource:
        from .resources.freshness import FreshnessResource

        return FreshnessResource(self)

    @cached_property
    def companies(self) -> CompaniesResource:
        from .resources.companies import CompaniesResource

        return CompaniesResource(self)

    @cached_property
    def filings(self) -> FilingsResource:
        from .resources.filings import FilingsResource

        return FilingsResource(self)

    @cached_property
    def translations(self) -> TranslationsResource:
        from .resources.translations import TranslationsResource

        return TranslationsResource(self)

    @cached_property
    def screen(self) -> ScreenResource:
        from .resources.screen import ScreenResource

        return ScreenResource(self)

    @cached_property
    def rankings(self) -> RankingsResource:
        from .resources.rankings import RankingsResource

        return RankingsResource(self)

    @cached_property
    def sectors(self) -> SectorsResource:
        from .resources.sectors import SectorsResource

        return SectorsResource(self)

    @cached_property
    def compare(self) -> CompareResource:
        from .resources.compare import CompareResource

        return CompareResource(self)

    @cached_property
    def timeseries(self) -> TimeseriesResource:
        from .resources.timeseries import TimeseriesResource

        return TimeseriesResource(self)

    @cached_property
    def bulk(self) -> BulkResource:
        from .resources.bulk import BulkResource

        return BulkResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def usage(self) -> UsageResource:
        from .resources.usage import UsageResource

        return UsageResource(self)

    @cached_property
    def keys(self) -> KeysResource:
        from .resources.keys import KeysResource

        return KeysResource(self)

    @cached_property
    def coverage(self) -> CoverageResource:
        from .resources.coverage import CoverageResource

        return CoverageResource(self)

    @cached_property
    def batch(self) -> BatchResource:
        from .resources.batch import BatchResource

        return BatchResource(self)

    @cached_property
    def waitlist(self) -> WaitlistResource:
        from .resources.waitlist import WaitlistResource

        return WaitlistResource(self)

    @cached_property
    def sections(self) -> SectionsResource:
        from .resources.sections import SectionsResource

        return SectionsResource(self)

    @cached_property
    def buybacks(self) -> BuybacksResource:
        from .resources.buybacks import BuybacksResource

        return BuybacksResource(self)

    @cached_property
    def shareholdings(self) -> ShareholdingsResource:
        from .resources.shareholdings import ShareholdingsResource

        return ShareholdingsResource(self)

    @cached_property
    def ownership(self) -> OwnershipResource:
        from .resources.ownership import OwnershipResource

        return OwnershipResource(self)

    @cached_property
    def capital_allocation(self) -> CapitalAllocationResource:
        from .resources.capital_allocation import CapitalAllocationResource

        return CapitalAllocationResource(self)

    @cached_property
    def voting(self) -> VotingResource:
        from .resources.voting import VotingResource

        return VotingResource(self)

    @cached_property
    def earnings(self) -> EarningsResource:
        from .resources.earnings import EarningsResource

        return EarningsResource(self)

    @cached_property
    def investors(self) -> InvestorsResource:
        from .resources.investors import InvestorsResource

        return InvestorsResource(self)

    @cached_property
    def watchlist(self) -> WatchlistResource:
        from .resources.watchlist import WatchlistResource

        return WatchlistResource(self)

    @cached_property
    def relationships(self) -> RelationshipsResource:
        from .resources.relationships import RelationshipsResource

        return RelationshipsResource(self)

    @cached_property
    def well_known(self) -> WellKnownResource:
        from .resources.well_known import WellKnownResource

        return WellKnownResource(self)

    @cached_property
    def oauth(self) -> OAuthResource:
        from .resources.oauth import OAuthResource

        return OAuthResource(self)

    @cached_property
    def with_raw_response(self) -> AxioraWithRawResponse:
        return AxioraWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AxioraWithStreamedResponse:
        return AxioraWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncAxiora(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncAxiora client instance.

        This automatically infers the `api_key` argument from the `AXIORA_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("AXIORA_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("AXIORA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.axiora.dev"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> AsyncHealthResource:
        from .resources.health import AsyncHealthResource

        return AsyncHealthResource(self)

    @cached_property
    def freshness(self) -> AsyncFreshnessResource:
        from .resources.freshness import AsyncFreshnessResource

        return AsyncFreshnessResource(self)

    @cached_property
    def companies(self) -> AsyncCompaniesResource:
        from .resources.companies import AsyncCompaniesResource

        return AsyncCompaniesResource(self)

    @cached_property
    def filings(self) -> AsyncFilingsResource:
        from .resources.filings import AsyncFilingsResource

        return AsyncFilingsResource(self)

    @cached_property
    def translations(self) -> AsyncTranslationsResource:
        from .resources.translations import AsyncTranslationsResource

        return AsyncTranslationsResource(self)

    @cached_property
    def screen(self) -> AsyncScreenResource:
        from .resources.screen import AsyncScreenResource

        return AsyncScreenResource(self)

    @cached_property
    def rankings(self) -> AsyncRankingsResource:
        from .resources.rankings import AsyncRankingsResource

        return AsyncRankingsResource(self)

    @cached_property
    def sectors(self) -> AsyncSectorsResource:
        from .resources.sectors import AsyncSectorsResource

        return AsyncSectorsResource(self)

    @cached_property
    def compare(self) -> AsyncCompareResource:
        from .resources.compare import AsyncCompareResource

        return AsyncCompareResource(self)

    @cached_property
    def timeseries(self) -> AsyncTimeseriesResource:
        from .resources.timeseries import AsyncTimeseriesResource

        return AsyncTimeseriesResource(self)

    @cached_property
    def bulk(self) -> AsyncBulkResource:
        from .resources.bulk import AsyncBulkResource

        return AsyncBulkResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        from .resources.usage import AsyncUsageResource

        return AsyncUsageResource(self)

    @cached_property
    def keys(self) -> AsyncKeysResource:
        from .resources.keys import AsyncKeysResource

        return AsyncKeysResource(self)

    @cached_property
    def coverage(self) -> AsyncCoverageResource:
        from .resources.coverage import AsyncCoverageResource

        return AsyncCoverageResource(self)

    @cached_property
    def batch(self) -> AsyncBatchResource:
        from .resources.batch import AsyncBatchResource

        return AsyncBatchResource(self)

    @cached_property
    def waitlist(self) -> AsyncWaitlistResource:
        from .resources.waitlist import AsyncWaitlistResource

        return AsyncWaitlistResource(self)

    @cached_property
    def sections(self) -> AsyncSectionsResource:
        from .resources.sections import AsyncSectionsResource

        return AsyncSectionsResource(self)

    @cached_property
    def buybacks(self) -> AsyncBuybacksResource:
        from .resources.buybacks import AsyncBuybacksResource

        return AsyncBuybacksResource(self)

    @cached_property
    def shareholdings(self) -> AsyncShareholdingsResource:
        from .resources.shareholdings import AsyncShareholdingsResource

        return AsyncShareholdingsResource(self)

    @cached_property
    def ownership(self) -> AsyncOwnershipResource:
        from .resources.ownership import AsyncOwnershipResource

        return AsyncOwnershipResource(self)

    @cached_property
    def capital_allocation(self) -> AsyncCapitalAllocationResource:
        from .resources.capital_allocation import AsyncCapitalAllocationResource

        return AsyncCapitalAllocationResource(self)

    @cached_property
    def voting(self) -> AsyncVotingResource:
        from .resources.voting import AsyncVotingResource

        return AsyncVotingResource(self)

    @cached_property
    def earnings(self) -> AsyncEarningsResource:
        from .resources.earnings import AsyncEarningsResource

        return AsyncEarningsResource(self)

    @cached_property
    def investors(self) -> AsyncInvestorsResource:
        from .resources.investors import AsyncInvestorsResource

        return AsyncInvestorsResource(self)

    @cached_property
    def watchlist(self) -> AsyncWatchlistResource:
        from .resources.watchlist import AsyncWatchlistResource

        return AsyncWatchlistResource(self)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResource:
        from .resources.relationships import AsyncRelationshipsResource

        return AsyncRelationshipsResource(self)

    @cached_property
    def well_known(self) -> AsyncWellKnownResource:
        from .resources.well_known import AsyncWellKnownResource

        return AsyncWellKnownResource(self)

    @cached_property
    def oauth(self) -> AsyncOAuthResource:
        from .resources.oauth import AsyncOAuthResource

        return AsyncOAuthResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncAxioraWithRawResponse:
        return AsyncAxioraWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAxioraWithStreamedResponse:
        return AsyncAxioraWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AxioraWithRawResponse:
    _client: Axiora

    def __init__(self, client: Axiora) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithRawResponse:
        from .resources.health import HealthResourceWithRawResponse

        return HealthResourceWithRawResponse(self._client.health)

    @cached_property
    def freshness(self) -> freshness.FreshnessResourceWithRawResponse:
        from .resources.freshness import FreshnessResourceWithRawResponse

        return FreshnessResourceWithRawResponse(self._client.freshness)

    @cached_property
    def companies(self) -> companies.CompaniesResourceWithRawResponse:
        from .resources.companies import CompaniesResourceWithRawResponse

        return CompaniesResourceWithRawResponse(self._client.companies)

    @cached_property
    def filings(self) -> filings.FilingsResourceWithRawResponse:
        from .resources.filings import FilingsResourceWithRawResponse

        return FilingsResourceWithRawResponse(self._client.filings)

    @cached_property
    def translations(self) -> translations.TranslationsResourceWithRawResponse:
        from .resources.translations import TranslationsResourceWithRawResponse

        return TranslationsResourceWithRawResponse(self._client.translations)

    @cached_property
    def screen(self) -> screen.ScreenResourceWithRawResponse:
        from .resources.screen import ScreenResourceWithRawResponse

        return ScreenResourceWithRawResponse(self._client.screen)

    @cached_property
    def rankings(self) -> rankings.RankingsResourceWithRawResponse:
        from .resources.rankings import RankingsResourceWithRawResponse

        return RankingsResourceWithRawResponse(self._client.rankings)

    @cached_property
    def sectors(self) -> sectors.SectorsResourceWithRawResponse:
        from .resources.sectors import SectorsResourceWithRawResponse

        return SectorsResourceWithRawResponse(self._client.sectors)

    @cached_property
    def compare(self) -> compare.CompareResourceWithRawResponse:
        from .resources.compare import CompareResourceWithRawResponse

        return CompareResourceWithRawResponse(self._client.compare)

    @cached_property
    def timeseries(self) -> timeseries.TimeseriesResourceWithRawResponse:
        from .resources.timeseries import TimeseriesResourceWithRawResponse

        return TimeseriesResourceWithRawResponse(self._client.timeseries)

    @cached_property
    def bulk(self) -> bulk.BulkResourceWithRawResponse:
        from .resources.bulk import BulkResourceWithRawResponse

        return BulkResourceWithRawResponse(self._client.bulk)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def usage(self) -> usage.UsageResourceWithRawResponse:
        from .resources.usage import UsageResourceWithRawResponse

        return UsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def keys(self) -> keys.KeysResourceWithRawResponse:
        from .resources.keys import KeysResourceWithRawResponse

        return KeysResourceWithRawResponse(self._client.keys)

    @cached_property
    def coverage(self) -> coverage.CoverageResourceWithRawResponse:
        from .resources.coverage import CoverageResourceWithRawResponse

        return CoverageResourceWithRawResponse(self._client.coverage)

    @cached_property
    def batch(self) -> batch.BatchResourceWithRawResponse:
        from .resources.batch import BatchResourceWithRawResponse

        return BatchResourceWithRawResponse(self._client.batch)

    @cached_property
    def waitlist(self) -> waitlist.WaitlistResourceWithRawResponse:
        from .resources.waitlist import WaitlistResourceWithRawResponse

        return WaitlistResourceWithRawResponse(self._client.waitlist)

    @cached_property
    def sections(self) -> sections.SectionsResourceWithRawResponse:
        from .resources.sections import SectionsResourceWithRawResponse

        return SectionsResourceWithRawResponse(self._client.sections)

    @cached_property
    def buybacks(self) -> buybacks.BuybacksResourceWithRawResponse:
        from .resources.buybacks import BuybacksResourceWithRawResponse

        return BuybacksResourceWithRawResponse(self._client.buybacks)

    @cached_property
    def shareholdings(self) -> shareholdings.ShareholdingsResourceWithRawResponse:
        from .resources.shareholdings import ShareholdingsResourceWithRawResponse

        return ShareholdingsResourceWithRawResponse(self._client.shareholdings)

    @cached_property
    def ownership(self) -> ownership.OwnershipResourceWithRawResponse:
        from .resources.ownership import OwnershipResourceWithRawResponse

        return OwnershipResourceWithRawResponse(self._client.ownership)

    @cached_property
    def capital_allocation(self) -> capital_allocation.CapitalAllocationResourceWithRawResponse:
        from .resources.capital_allocation import CapitalAllocationResourceWithRawResponse

        return CapitalAllocationResourceWithRawResponse(self._client.capital_allocation)

    @cached_property
    def voting(self) -> voting.VotingResourceWithRawResponse:
        from .resources.voting import VotingResourceWithRawResponse

        return VotingResourceWithRawResponse(self._client.voting)

    @cached_property
    def earnings(self) -> earnings.EarningsResourceWithRawResponse:
        from .resources.earnings import EarningsResourceWithRawResponse

        return EarningsResourceWithRawResponse(self._client.earnings)

    @cached_property
    def investors(self) -> investors.InvestorsResourceWithRawResponse:
        from .resources.investors import InvestorsResourceWithRawResponse

        return InvestorsResourceWithRawResponse(self._client.investors)

    @cached_property
    def watchlist(self) -> watchlist.WatchlistResourceWithRawResponse:
        from .resources.watchlist import WatchlistResourceWithRawResponse

        return WatchlistResourceWithRawResponse(self._client.watchlist)

    @cached_property
    def relationships(self) -> relationships.RelationshipsResourceWithRawResponse:
        from .resources.relationships import RelationshipsResourceWithRawResponse

        return RelationshipsResourceWithRawResponse(self._client.relationships)

    @cached_property
    def well_known(self) -> well_known.WellKnownResourceWithRawResponse:
        from .resources.well_known import WellKnownResourceWithRawResponse

        return WellKnownResourceWithRawResponse(self._client.well_known)

    @cached_property
    def oauth(self) -> oauth.OAuthResourceWithRawResponse:
        from .resources.oauth import OAuthResourceWithRawResponse

        return OAuthResourceWithRawResponse(self._client.oauth)


class AsyncAxioraWithRawResponse:
    _client: AsyncAxiora

    def __init__(self, client: AsyncAxiora) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def freshness(self) -> freshness.AsyncFreshnessResourceWithRawResponse:
        from .resources.freshness import AsyncFreshnessResourceWithRawResponse

        return AsyncFreshnessResourceWithRawResponse(self._client.freshness)

    @cached_property
    def companies(self) -> companies.AsyncCompaniesResourceWithRawResponse:
        from .resources.companies import AsyncCompaniesResourceWithRawResponse

        return AsyncCompaniesResourceWithRawResponse(self._client.companies)

    @cached_property
    def filings(self) -> filings.AsyncFilingsResourceWithRawResponse:
        from .resources.filings import AsyncFilingsResourceWithRawResponse

        return AsyncFilingsResourceWithRawResponse(self._client.filings)

    @cached_property
    def translations(self) -> translations.AsyncTranslationsResourceWithRawResponse:
        from .resources.translations import AsyncTranslationsResourceWithRawResponse

        return AsyncTranslationsResourceWithRawResponse(self._client.translations)

    @cached_property
    def screen(self) -> screen.AsyncScreenResourceWithRawResponse:
        from .resources.screen import AsyncScreenResourceWithRawResponse

        return AsyncScreenResourceWithRawResponse(self._client.screen)

    @cached_property
    def rankings(self) -> rankings.AsyncRankingsResourceWithRawResponse:
        from .resources.rankings import AsyncRankingsResourceWithRawResponse

        return AsyncRankingsResourceWithRawResponse(self._client.rankings)

    @cached_property
    def sectors(self) -> sectors.AsyncSectorsResourceWithRawResponse:
        from .resources.sectors import AsyncSectorsResourceWithRawResponse

        return AsyncSectorsResourceWithRawResponse(self._client.sectors)

    @cached_property
    def compare(self) -> compare.AsyncCompareResourceWithRawResponse:
        from .resources.compare import AsyncCompareResourceWithRawResponse

        return AsyncCompareResourceWithRawResponse(self._client.compare)

    @cached_property
    def timeseries(self) -> timeseries.AsyncTimeseriesResourceWithRawResponse:
        from .resources.timeseries import AsyncTimeseriesResourceWithRawResponse

        return AsyncTimeseriesResourceWithRawResponse(self._client.timeseries)

    @cached_property
    def bulk(self) -> bulk.AsyncBulkResourceWithRawResponse:
        from .resources.bulk import AsyncBulkResourceWithRawResponse

        return AsyncBulkResourceWithRawResponse(self._client.bulk)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithRawResponse:
        from .resources.usage import AsyncUsageResourceWithRawResponse

        return AsyncUsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def keys(self) -> keys.AsyncKeysResourceWithRawResponse:
        from .resources.keys import AsyncKeysResourceWithRawResponse

        return AsyncKeysResourceWithRawResponse(self._client.keys)

    @cached_property
    def coverage(self) -> coverage.AsyncCoverageResourceWithRawResponse:
        from .resources.coverage import AsyncCoverageResourceWithRawResponse

        return AsyncCoverageResourceWithRawResponse(self._client.coverage)

    @cached_property
    def batch(self) -> batch.AsyncBatchResourceWithRawResponse:
        from .resources.batch import AsyncBatchResourceWithRawResponse

        return AsyncBatchResourceWithRawResponse(self._client.batch)

    @cached_property
    def waitlist(self) -> waitlist.AsyncWaitlistResourceWithRawResponse:
        from .resources.waitlist import AsyncWaitlistResourceWithRawResponse

        return AsyncWaitlistResourceWithRawResponse(self._client.waitlist)

    @cached_property
    def sections(self) -> sections.AsyncSectionsResourceWithRawResponse:
        from .resources.sections import AsyncSectionsResourceWithRawResponse

        return AsyncSectionsResourceWithRawResponse(self._client.sections)

    @cached_property
    def buybacks(self) -> buybacks.AsyncBuybacksResourceWithRawResponse:
        from .resources.buybacks import AsyncBuybacksResourceWithRawResponse

        return AsyncBuybacksResourceWithRawResponse(self._client.buybacks)

    @cached_property
    def shareholdings(self) -> shareholdings.AsyncShareholdingsResourceWithRawResponse:
        from .resources.shareholdings import AsyncShareholdingsResourceWithRawResponse

        return AsyncShareholdingsResourceWithRawResponse(self._client.shareholdings)

    @cached_property
    def ownership(self) -> ownership.AsyncOwnershipResourceWithRawResponse:
        from .resources.ownership import AsyncOwnershipResourceWithRawResponse

        return AsyncOwnershipResourceWithRawResponse(self._client.ownership)

    @cached_property
    def capital_allocation(self) -> capital_allocation.AsyncCapitalAllocationResourceWithRawResponse:
        from .resources.capital_allocation import AsyncCapitalAllocationResourceWithRawResponse

        return AsyncCapitalAllocationResourceWithRawResponse(self._client.capital_allocation)

    @cached_property
    def voting(self) -> voting.AsyncVotingResourceWithRawResponse:
        from .resources.voting import AsyncVotingResourceWithRawResponse

        return AsyncVotingResourceWithRawResponse(self._client.voting)

    @cached_property
    def earnings(self) -> earnings.AsyncEarningsResourceWithRawResponse:
        from .resources.earnings import AsyncEarningsResourceWithRawResponse

        return AsyncEarningsResourceWithRawResponse(self._client.earnings)

    @cached_property
    def investors(self) -> investors.AsyncInvestorsResourceWithRawResponse:
        from .resources.investors import AsyncInvestorsResourceWithRawResponse

        return AsyncInvestorsResourceWithRawResponse(self._client.investors)

    @cached_property
    def watchlist(self) -> watchlist.AsyncWatchlistResourceWithRawResponse:
        from .resources.watchlist import AsyncWatchlistResourceWithRawResponse

        return AsyncWatchlistResourceWithRawResponse(self._client.watchlist)

    @cached_property
    def relationships(self) -> relationships.AsyncRelationshipsResourceWithRawResponse:
        from .resources.relationships import AsyncRelationshipsResourceWithRawResponse

        return AsyncRelationshipsResourceWithRawResponse(self._client.relationships)

    @cached_property
    def well_known(self) -> well_known.AsyncWellKnownResourceWithRawResponse:
        from .resources.well_known import AsyncWellKnownResourceWithRawResponse

        return AsyncWellKnownResourceWithRawResponse(self._client.well_known)

    @cached_property
    def oauth(self) -> oauth.AsyncOAuthResourceWithRawResponse:
        from .resources.oauth import AsyncOAuthResourceWithRawResponse

        return AsyncOAuthResourceWithRawResponse(self._client.oauth)


class AxioraWithStreamedResponse:
    _client: Axiora

    def __init__(self, client: Axiora) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def freshness(self) -> freshness.FreshnessResourceWithStreamingResponse:
        from .resources.freshness import FreshnessResourceWithStreamingResponse

        return FreshnessResourceWithStreamingResponse(self._client.freshness)

    @cached_property
    def companies(self) -> companies.CompaniesResourceWithStreamingResponse:
        from .resources.companies import CompaniesResourceWithStreamingResponse

        return CompaniesResourceWithStreamingResponse(self._client.companies)

    @cached_property
    def filings(self) -> filings.FilingsResourceWithStreamingResponse:
        from .resources.filings import FilingsResourceWithStreamingResponse

        return FilingsResourceWithStreamingResponse(self._client.filings)

    @cached_property
    def translations(self) -> translations.TranslationsResourceWithStreamingResponse:
        from .resources.translations import TranslationsResourceWithStreamingResponse

        return TranslationsResourceWithStreamingResponse(self._client.translations)

    @cached_property
    def screen(self) -> screen.ScreenResourceWithStreamingResponse:
        from .resources.screen import ScreenResourceWithStreamingResponse

        return ScreenResourceWithStreamingResponse(self._client.screen)

    @cached_property
    def rankings(self) -> rankings.RankingsResourceWithStreamingResponse:
        from .resources.rankings import RankingsResourceWithStreamingResponse

        return RankingsResourceWithStreamingResponse(self._client.rankings)

    @cached_property
    def sectors(self) -> sectors.SectorsResourceWithStreamingResponse:
        from .resources.sectors import SectorsResourceWithStreamingResponse

        return SectorsResourceWithStreamingResponse(self._client.sectors)

    @cached_property
    def compare(self) -> compare.CompareResourceWithStreamingResponse:
        from .resources.compare import CompareResourceWithStreamingResponse

        return CompareResourceWithStreamingResponse(self._client.compare)

    @cached_property
    def timeseries(self) -> timeseries.TimeseriesResourceWithStreamingResponse:
        from .resources.timeseries import TimeseriesResourceWithStreamingResponse

        return TimeseriesResourceWithStreamingResponse(self._client.timeseries)

    @cached_property
    def bulk(self) -> bulk.BulkResourceWithStreamingResponse:
        from .resources.bulk import BulkResourceWithStreamingResponse

        return BulkResourceWithStreamingResponse(self._client.bulk)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def usage(self) -> usage.UsageResourceWithStreamingResponse:
        from .resources.usage import UsageResourceWithStreamingResponse

        return UsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def keys(self) -> keys.KeysResourceWithStreamingResponse:
        from .resources.keys import KeysResourceWithStreamingResponse

        return KeysResourceWithStreamingResponse(self._client.keys)

    @cached_property
    def coverage(self) -> coverage.CoverageResourceWithStreamingResponse:
        from .resources.coverage import CoverageResourceWithStreamingResponse

        return CoverageResourceWithStreamingResponse(self._client.coverage)

    @cached_property
    def batch(self) -> batch.BatchResourceWithStreamingResponse:
        from .resources.batch import BatchResourceWithStreamingResponse

        return BatchResourceWithStreamingResponse(self._client.batch)

    @cached_property
    def waitlist(self) -> waitlist.WaitlistResourceWithStreamingResponse:
        from .resources.waitlist import WaitlistResourceWithStreamingResponse

        return WaitlistResourceWithStreamingResponse(self._client.waitlist)

    @cached_property
    def sections(self) -> sections.SectionsResourceWithStreamingResponse:
        from .resources.sections import SectionsResourceWithStreamingResponse

        return SectionsResourceWithStreamingResponse(self._client.sections)

    @cached_property
    def buybacks(self) -> buybacks.BuybacksResourceWithStreamingResponse:
        from .resources.buybacks import BuybacksResourceWithStreamingResponse

        return BuybacksResourceWithStreamingResponse(self._client.buybacks)

    @cached_property
    def shareholdings(self) -> shareholdings.ShareholdingsResourceWithStreamingResponse:
        from .resources.shareholdings import ShareholdingsResourceWithStreamingResponse

        return ShareholdingsResourceWithStreamingResponse(self._client.shareholdings)

    @cached_property
    def ownership(self) -> ownership.OwnershipResourceWithStreamingResponse:
        from .resources.ownership import OwnershipResourceWithStreamingResponse

        return OwnershipResourceWithStreamingResponse(self._client.ownership)

    @cached_property
    def capital_allocation(self) -> capital_allocation.CapitalAllocationResourceWithStreamingResponse:
        from .resources.capital_allocation import CapitalAllocationResourceWithStreamingResponse

        return CapitalAllocationResourceWithStreamingResponse(self._client.capital_allocation)

    @cached_property
    def voting(self) -> voting.VotingResourceWithStreamingResponse:
        from .resources.voting import VotingResourceWithStreamingResponse

        return VotingResourceWithStreamingResponse(self._client.voting)

    @cached_property
    def earnings(self) -> earnings.EarningsResourceWithStreamingResponse:
        from .resources.earnings import EarningsResourceWithStreamingResponse

        return EarningsResourceWithStreamingResponse(self._client.earnings)

    @cached_property
    def investors(self) -> investors.InvestorsResourceWithStreamingResponse:
        from .resources.investors import InvestorsResourceWithStreamingResponse

        return InvestorsResourceWithStreamingResponse(self._client.investors)

    @cached_property
    def watchlist(self) -> watchlist.WatchlistResourceWithStreamingResponse:
        from .resources.watchlist import WatchlistResourceWithStreamingResponse

        return WatchlistResourceWithStreamingResponse(self._client.watchlist)

    @cached_property
    def relationships(self) -> relationships.RelationshipsResourceWithStreamingResponse:
        from .resources.relationships import RelationshipsResourceWithStreamingResponse

        return RelationshipsResourceWithStreamingResponse(self._client.relationships)

    @cached_property
    def well_known(self) -> well_known.WellKnownResourceWithStreamingResponse:
        from .resources.well_known import WellKnownResourceWithStreamingResponse

        return WellKnownResourceWithStreamingResponse(self._client.well_known)

    @cached_property
    def oauth(self) -> oauth.OAuthResourceWithStreamingResponse:
        from .resources.oauth import OAuthResourceWithStreamingResponse

        return OAuthResourceWithStreamingResponse(self._client.oauth)


class AsyncAxioraWithStreamedResponse:
    _client: AsyncAxiora

    def __init__(self, client: AsyncAxiora) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def freshness(self) -> freshness.AsyncFreshnessResourceWithStreamingResponse:
        from .resources.freshness import AsyncFreshnessResourceWithStreamingResponse

        return AsyncFreshnessResourceWithStreamingResponse(self._client.freshness)

    @cached_property
    def companies(self) -> companies.AsyncCompaniesResourceWithStreamingResponse:
        from .resources.companies import AsyncCompaniesResourceWithStreamingResponse

        return AsyncCompaniesResourceWithStreamingResponse(self._client.companies)

    @cached_property
    def filings(self) -> filings.AsyncFilingsResourceWithStreamingResponse:
        from .resources.filings import AsyncFilingsResourceWithStreamingResponse

        return AsyncFilingsResourceWithStreamingResponse(self._client.filings)

    @cached_property
    def translations(self) -> translations.AsyncTranslationsResourceWithStreamingResponse:
        from .resources.translations import AsyncTranslationsResourceWithStreamingResponse

        return AsyncTranslationsResourceWithStreamingResponse(self._client.translations)

    @cached_property
    def screen(self) -> screen.AsyncScreenResourceWithStreamingResponse:
        from .resources.screen import AsyncScreenResourceWithStreamingResponse

        return AsyncScreenResourceWithStreamingResponse(self._client.screen)

    @cached_property
    def rankings(self) -> rankings.AsyncRankingsResourceWithStreamingResponse:
        from .resources.rankings import AsyncRankingsResourceWithStreamingResponse

        return AsyncRankingsResourceWithStreamingResponse(self._client.rankings)

    @cached_property
    def sectors(self) -> sectors.AsyncSectorsResourceWithStreamingResponse:
        from .resources.sectors import AsyncSectorsResourceWithStreamingResponse

        return AsyncSectorsResourceWithStreamingResponse(self._client.sectors)

    @cached_property
    def compare(self) -> compare.AsyncCompareResourceWithStreamingResponse:
        from .resources.compare import AsyncCompareResourceWithStreamingResponse

        return AsyncCompareResourceWithStreamingResponse(self._client.compare)

    @cached_property
    def timeseries(self) -> timeseries.AsyncTimeseriesResourceWithStreamingResponse:
        from .resources.timeseries import AsyncTimeseriesResourceWithStreamingResponse

        return AsyncTimeseriesResourceWithStreamingResponse(self._client.timeseries)

    @cached_property
    def bulk(self) -> bulk.AsyncBulkResourceWithStreamingResponse:
        from .resources.bulk import AsyncBulkResourceWithStreamingResponse

        return AsyncBulkResourceWithStreamingResponse(self._client.bulk)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithStreamingResponse:
        from .resources.usage import AsyncUsageResourceWithStreamingResponse

        return AsyncUsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def keys(self) -> keys.AsyncKeysResourceWithStreamingResponse:
        from .resources.keys import AsyncKeysResourceWithStreamingResponse

        return AsyncKeysResourceWithStreamingResponse(self._client.keys)

    @cached_property
    def coverage(self) -> coverage.AsyncCoverageResourceWithStreamingResponse:
        from .resources.coverage import AsyncCoverageResourceWithStreamingResponse

        return AsyncCoverageResourceWithStreamingResponse(self._client.coverage)

    @cached_property
    def batch(self) -> batch.AsyncBatchResourceWithStreamingResponse:
        from .resources.batch import AsyncBatchResourceWithStreamingResponse

        return AsyncBatchResourceWithStreamingResponse(self._client.batch)

    @cached_property
    def waitlist(self) -> waitlist.AsyncWaitlistResourceWithStreamingResponse:
        from .resources.waitlist import AsyncWaitlistResourceWithStreamingResponse

        return AsyncWaitlistResourceWithStreamingResponse(self._client.waitlist)

    @cached_property
    def sections(self) -> sections.AsyncSectionsResourceWithStreamingResponse:
        from .resources.sections import AsyncSectionsResourceWithStreamingResponse

        return AsyncSectionsResourceWithStreamingResponse(self._client.sections)

    @cached_property
    def buybacks(self) -> buybacks.AsyncBuybacksResourceWithStreamingResponse:
        from .resources.buybacks import AsyncBuybacksResourceWithStreamingResponse

        return AsyncBuybacksResourceWithStreamingResponse(self._client.buybacks)

    @cached_property
    def shareholdings(self) -> shareholdings.AsyncShareholdingsResourceWithStreamingResponse:
        from .resources.shareholdings import AsyncShareholdingsResourceWithStreamingResponse

        return AsyncShareholdingsResourceWithStreamingResponse(self._client.shareholdings)

    @cached_property
    def ownership(self) -> ownership.AsyncOwnershipResourceWithStreamingResponse:
        from .resources.ownership import AsyncOwnershipResourceWithStreamingResponse

        return AsyncOwnershipResourceWithStreamingResponse(self._client.ownership)

    @cached_property
    def capital_allocation(self) -> capital_allocation.AsyncCapitalAllocationResourceWithStreamingResponse:
        from .resources.capital_allocation import AsyncCapitalAllocationResourceWithStreamingResponse

        return AsyncCapitalAllocationResourceWithStreamingResponse(self._client.capital_allocation)

    @cached_property
    def voting(self) -> voting.AsyncVotingResourceWithStreamingResponse:
        from .resources.voting import AsyncVotingResourceWithStreamingResponse

        return AsyncVotingResourceWithStreamingResponse(self._client.voting)

    @cached_property
    def earnings(self) -> earnings.AsyncEarningsResourceWithStreamingResponse:
        from .resources.earnings import AsyncEarningsResourceWithStreamingResponse

        return AsyncEarningsResourceWithStreamingResponse(self._client.earnings)

    @cached_property
    def investors(self) -> investors.AsyncInvestorsResourceWithStreamingResponse:
        from .resources.investors import AsyncInvestorsResourceWithStreamingResponse

        return AsyncInvestorsResourceWithStreamingResponse(self._client.investors)

    @cached_property
    def watchlist(self) -> watchlist.AsyncWatchlistResourceWithStreamingResponse:
        from .resources.watchlist import AsyncWatchlistResourceWithStreamingResponse

        return AsyncWatchlistResourceWithStreamingResponse(self._client.watchlist)

    @cached_property
    def relationships(self) -> relationships.AsyncRelationshipsResourceWithStreamingResponse:
        from .resources.relationships import AsyncRelationshipsResourceWithStreamingResponse

        return AsyncRelationshipsResourceWithStreamingResponse(self._client.relationships)

    @cached_property
    def well_known(self) -> well_known.AsyncWellKnownResourceWithStreamingResponse:
        from .resources.well_known import AsyncWellKnownResourceWithStreamingResponse

        return AsyncWellKnownResourceWithStreamingResponse(self._client.well_known)

    @cached_property
    def oauth(self) -> oauth.AsyncOAuthResourceWithStreamingResponse:
        from .resources.oauth import AsyncOAuthResourceWithStreamingResponse

        return AsyncOAuthResourceWithStreamingResponse(self._client.oauth)


Client = Axiora

AsyncClient = AsyncAxiora
