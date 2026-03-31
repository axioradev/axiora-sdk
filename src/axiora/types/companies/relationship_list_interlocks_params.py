# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["RelationshipListInterlocksParams"]


class RelationshipListInterlocksParams(TypedDict, total=False):
    fiscal_year: Optional[int]
    """Fiscal year. Defaults to latest."""
