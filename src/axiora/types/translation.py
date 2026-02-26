# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Translation"]


class Translation(BaseModel):
    model: str
    """LLM model used for translation (e.g. 'gemini/gemini-2.0-flash')."""

    section: str
    """
    Filing section translated: 'mda', 'risk_factors', 'business_overview',
    'governance', 'financial_notes', or 'accounting_policy'.
    """

    text_en: str
    """English translation of the section."""

    translated_at: datetime
    """When the translation was generated."""

    source_jp: Optional[str] = None
    """Original Japanese text. Null if source was not stored."""

    token_count: Optional[int] = None
    """Approximate token count of the translated output."""
