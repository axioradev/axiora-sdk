# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["BatchFetchFinancialsParams"]


class BatchFetchFinancialsParams(TypedDict, total=False):
    codes: Required[SequenceNotStr[str]]
    """List of EDINET or securities codes (1–100)."""

    fields: Optional[SequenceNotStr[str]]
    """Financial fields to include. Null returns all fields."""

    years: int
    """Number of fiscal years per company."""
