# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["WatchlistAddParams"]


class WatchlistAddParams(TypedDict, total=False):
    entity_code: Required[str]
    """Securities code or EDINET code"""

    entity_type: Required[str]
    """company or investor"""

    entity_name: Optional[str]
    """Display name"""
