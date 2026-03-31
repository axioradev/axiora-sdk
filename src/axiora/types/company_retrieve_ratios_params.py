# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CompanyRetrieveRatiosParams"]


class CompanyRetrieveRatiosParams(TypedDict, total=False):
    split_adjusted: bool
    """
    Adjust per-share values (EPS, BPS, DPS) for detected stock splits so the
    time-series is comparable. Set to false for raw unadjusted values.
    """

    years: int
