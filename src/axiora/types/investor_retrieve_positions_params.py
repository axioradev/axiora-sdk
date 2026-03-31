# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["InvestorRetrievePositionsParams"]


class InvestorRetrievePositionsParams(TypedDict, total=False):
    limit: int

    trajectory_type: Optional[str]
    """Filter: accumulating, exiting, stable, new_position"""
