# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .filing import Filing
from .._models import BaseModel

__all__ = ["FilingListResponse"]


class FilingListResponse(BaseModel):
    data: List[Filing]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
