# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V2RetrieveCompanyParams"]


class V2RetrieveCompanyParams(TypedDict, total=False):
    include: object
    """holders,trends,financials,votes,board,signals"""
