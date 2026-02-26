# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .company import Company
from .._models import BaseModel

__all__ = ["ListResponse"]


class ListResponse(BaseModel):
    data: List[Company]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
