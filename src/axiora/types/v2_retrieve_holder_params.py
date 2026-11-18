# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V2RetrieveHolderParams"]


class V2RetrieveHolderParams(TypedDict, total=False):
    include: object
    """positions,trends,signals,group_positions"""
