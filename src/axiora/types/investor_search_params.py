# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InvestorSearchParams"]


class InvestorSearchParams(TypedDict, total=False):
    q: Required[str]
    """Search by investor name or EDINET code"""

    limit: int
