# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CompanyRetrieveGrowthParams"]


class CompanyRetrieveGrowthParams(TypedDict, total=False):
    split_adjusted: bool
    """Adjust EPS for detected stock splits before computing growth.

    Set to false for raw unadjusted values.
    """

    years: int
