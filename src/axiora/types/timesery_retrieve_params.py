# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TimeseryRetrieveParams"]


class TimeseryRetrieveParams(TypedDict, total=False):
    codes: Required[str]
    """Comma-separated EDINET or securities codes (max 5)"""

    metric: str
    """Financial metric to chart"""

    years: int
