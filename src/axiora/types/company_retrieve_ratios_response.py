# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .ratio import Ratio
from .._models import BaseModel

__all__ = ["CompanyRetrieveRatiosResponse"]


class CompanyRetrieveRatiosResponse(BaseModel):
    data: List[Ratio]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
