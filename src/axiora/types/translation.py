# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Translation"]


class Translation(BaseModel):
    model: str

    section: str

    text_en: str

    translated_at: datetime

    source_jp: Optional[str] = None

    token_count: Optional[int] = None
