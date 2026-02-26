# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CompanyRetrieveParams"]


class CompanyRetrieveParams(TypedDict, total=False):
    expand: Optional[str]
    """
    Comma-separated sub-resources to include: financials, ratios, growth, peers,
    segments, translations, health_score. Use 'all' for everything.
    """

    peer_limit: int
    """Max peers to return (default 10)"""

    years: int
