# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FilingCalendarParams"]


class FilingCalendarParams(TypedDict, total=False):
    month: Required[str]
    """Month in YYYY-MM format (e.g. 2025-06)"""
