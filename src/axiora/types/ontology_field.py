# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["OntologyField", "Standard"]


class Standard(BaseModel):
    """How the field is reported under one accounting standard."""

    supported: bool
    """True if values for this field can be reliably extracted under this standard."""

    label_jp: Optional[str] = None
    """The Japanese label that maps to this field under this accounting standard."""

    semantic_note: Optional[str] = None
    """Subtle differences in meaning across standards.

    E.g. JP-GAAP 売上高 vs IFRS 売上収益 — the same field name covers
    different underlying concepts.
    """


class OntologyField(BaseModel):
    category: str
    """Field category.

    One of: 'income_statement', 'balance_sheet', 'cash_flow', 'per_share',
    'ratio', 'dei', 'other'.
    """

    field_name: str
    """Stable canonical name used everywhere in the API (e.g. 'revenue', 'roe')."""

    label_en: str
    """English label."""

    label_jp: str
    """Japanese label as it typically appears in filings."""

    standards: Dict[str, Standard]
    """Per-accounting-standard mappings.

    Keys are 'JP-GAAP', 'IFRS', 'US-GAAP'. Each value documents how the
    field is reported under that standard, whether it's supported, and any
    semantic differences.
    """
