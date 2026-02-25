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
        usage,
        health,
        screen,
        compare,
        filings,
        sectors,
        coverage,
        rankings,
        webhooks,
        companies,
        freshness,
        timeseries,
        translations,
    )
    from .resources.bulk import BulkResource, AsyncBulkResource
    from .resources.keys import KeysResource, AsyncKeysResource
    from .resources.usage import UsageResource, AsyncUsageResource
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.screen import ScreenResource, AsyncScreenResource
    from .resources.compare import CompareResource, AsyncCompareResource
    from .resources.filings import FilingsResource, AsyncFilingsResource
    from .resources.sectors import SectorsResource, AsyncSectorsResource
    from .resources.coverage import CoverageResource, AsyncCoverageResource
    from .resources.rankings import RankingsResource, AsyncRankingsResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.companies import CompaniesResource, AsyncCompaniesResource
    from .resources.freshness import FreshnessResource, AsyncFreshnessResource
    from .resources.timeseries import TimeseriesResource, AsyncTimeseriesResource
    from .resources.translations import TranslationsResource, AsyncTranslationsResource

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
    def with_raw_response(self) -> AxioraWithRawResponse:
        return AxioraWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AxioraWithStreamedResponse:
        return AxioraWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
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
    def with_raw_response(self) -> AsyncAxioraWithRawResponse:
        return AsyncAxioraWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAxioraWithStreamedResponse:
        return AsyncAxioraWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
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


Client = Axiora

AsyncClient = AsyncAxiora
