# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["ListResponseSection", "Data"]


class Data(BaseModel):
    char_count: int
    """Character count of the Japanese text."""

    label_en: str
    """Human-readable English label for the section."""

    label_jp: str
    """Japanese label for the section."""

    section: str
    """Section key (e.g. 'mda', 'risk_factors')."""

    text_jp: str
    """Full Japanese text of the section. No truncation."""

    text_en: Optional[str] = None
    """English translation, if available. Null when not yet translated."""


class ListResponseSection(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
