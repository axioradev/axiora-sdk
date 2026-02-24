# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FilingRetrieveTranslationsParams"]


class FilingRetrieveTranslationsParams(TypedDict, total=False):
    section: Optional[str]
    """Filter by section name"""
