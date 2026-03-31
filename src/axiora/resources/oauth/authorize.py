# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.oauth import authorize_show_params, authorize_validate_params
from ..._base_client import make_request_options

__all__ = ["AuthorizeResource", "AsyncAuthorizeResource"]


class AuthorizeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthorizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AuthorizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthorizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AuthorizeResourceWithStreamingResponse(self)

    def show(
        self,
        *,
        client_id: str,
        code_challenge: str,
        redirect_uri: str,
        code_challenge_method: str | Omit = omit,
        resource: str | Omit = omit,
        response_type: str | Omit = omit,
        scope: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Show the authorization form.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/html", **(extra_headers or {})}
        return self._get(
            "/oauth/authorize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "client_id": client_id,
                        "code_challenge": code_challenge,
                        "redirect_uri": redirect_uri,
                        "code_challenge_method": code_challenge_method,
                        "resource": resource,
                        "response_type": response_type,
                        "scope": scope,
                        "state": state,
                    },
                    authorize_show_params.AuthorizeShowParams,
                ),
            ),
            cast_to=str,
        )

    def validate(
        self,
        *,
        api_key: str,
        client_id: str,
        code_challenge: str,
        csrf_token: str,
        redirect_uri: str,
        code_challenge_method: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Validate API key and issue authorization code.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/oauth/authorize",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "client_id": client_id,
                    "code_challenge": code_challenge,
                    "csrf_token": csrf_token,
                    "redirect_uri": redirect_uri,
                    "code_challenge_method": code_challenge_method,
                    "state": state,
                },
                authorize_validate_params.AuthorizeValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAuthorizeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthorizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/axioradev/axiora-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthorizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthorizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/axioradev/axiora-sdk#with_streaming_response
        """
        return AsyncAuthorizeResourceWithStreamingResponse(self)

    async def show(
        self,
        *,
        client_id: str,
        code_challenge: str,
        redirect_uri: str,
        code_challenge_method: str | Omit = omit,
        resource: str | Omit = omit,
        response_type: str | Omit = omit,
        scope: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Show the authorization form.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/html", **(extra_headers or {})}
        return await self._get(
            "/oauth/authorize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "client_id": client_id,
                        "code_challenge": code_challenge,
                        "redirect_uri": redirect_uri,
                        "code_challenge_method": code_challenge_method,
                        "resource": resource,
                        "response_type": response_type,
                        "scope": scope,
                        "state": state,
                    },
                    authorize_show_params.AuthorizeShowParams,
                ),
            ),
            cast_to=str,
        )

    async def validate(
        self,
        *,
        api_key: str,
        client_id: str,
        code_challenge: str,
        csrf_token: str,
        redirect_uri: str,
        code_challenge_method: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Validate API key and issue authorization code.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/oauth/authorize",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "client_id": client_id,
                    "code_challenge": code_challenge,
                    "csrf_token": csrf_token,
                    "redirect_uri": redirect_uri,
                    "code_challenge_method": code_challenge_method,
                    "state": state,
                },
                authorize_validate_params.AuthorizeValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AuthorizeResourceWithRawResponse:
    def __init__(self, authorize: AuthorizeResource) -> None:
        self._authorize = authorize

        self.show = to_raw_response_wrapper(
            authorize.show,
        )
        self.validate = to_raw_response_wrapper(
            authorize.validate,
        )


class AsyncAuthorizeResourceWithRawResponse:
    def __init__(self, authorize: AsyncAuthorizeResource) -> None:
        self._authorize = authorize

        self.show = async_to_raw_response_wrapper(
            authorize.show,
        )
        self.validate = async_to_raw_response_wrapper(
            authorize.validate,
        )


class AuthorizeResourceWithStreamingResponse:
    def __init__(self, authorize: AuthorizeResource) -> None:
        self._authorize = authorize

        self.show = to_streamed_response_wrapper(
            authorize.show,
        )
        self.validate = to_streamed_response_wrapper(
            authorize.validate,
        )


class AsyncAuthorizeResourceWithStreamingResponse:
    def __init__(self, authorize: AsyncAuthorizeResource) -> None:
        self._authorize = authorize

        self.show = async_to_streamed_response_wrapper(
            authorize.show,
        )
        self.validate = async_to_streamed_response_wrapper(
            authorize.validate,
        )
