# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .translation import Translation

__all__ = ["FilingRetrieveTranslationsResponse"]


class FilingRetrieveTranslationsResponse(BaseModel):
    data: List[Translation]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
