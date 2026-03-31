# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["RelationshipListInterlocksResponse", "Data", "DataCompany"]


class DataCompany(BaseModel):
    edinet_code: str
    """EDINET code of the other company"""

    name: Optional[str] = None
    """Company name"""

    securities_code: Optional[str] = None
    """Securities code"""

    title: Optional[str] = None
    """Director's title at this company"""


class Data(BaseModel):
    confidence: str
    """'high' (DOB matches) or 'low' (DOB null on either side)"""

    name: str
    """Director name"""

    companies: Optional[List[DataCompany]] = None
    """Other companies where this director serves"""

    date_of_birth: Optional[str] = None
    """Date of birth (Japanese format)"""


class RelationshipListInterlocksResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
