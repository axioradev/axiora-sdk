# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .._models import BaseModel
from .subsidiary import Subsidiary

__all__ = ["CompanyRetrieveSubsidiariesResponse", "Data", "DataCompany"]


class DataCompany(BaseModel):
    """The parent company."""

    edinet_code: str
    """EDINET submitter code (e.g. 'E02144')."""

    name: str
    """Company name."""

    securities_code: Optional[str] = None
    """TSE securities code, 4 digits."""


class Data(BaseModel):
    """Subsidiary registry from a parent's annual 関係会社 disclosure."""

    company: DataCompany
    """The parent company."""

    subsidiaries: List[Subsidiary]
    """Disclosed subsidiaries / equity-method affiliates."""

    subsidiary_count: int
    """Total number of disclosed subsidiaries."""


class CompanyRetrieveSubsidiariesResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Pagination and request metadata."""
