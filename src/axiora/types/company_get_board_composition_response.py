# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .._models import BaseModel
from .board_member import BoardMember

__all__ = ["CompanyGetBoardCompositionResponse", "Data"]


class Data(BaseModel):
    """The requested resource object."""

    edinet_code: str
    """EDINET code"""

    fiscal_year: int
    """Fiscal year"""

    outside_director_count: int
    """Outside directors + auditors"""

    total_auditors: int
    """Number of auditors"""

    total_directors: int
    """Number of directors"""

    total_executive_officers: int
    """Number of executive officers"""

    female_count: Optional[int] = None
    """Female count"""

    female_ratio_pct: Optional[float] = None
    """Female ratio (%)"""

    independent_director_ratio_pct: Optional[float] = None
    """Independent director ratio (%)"""

    male_count: Optional[int] = None
    """Male count"""

    officers: Optional[List[BoardMember]] = None
    """Individual officers"""

    securities_code: Optional[str] = None
    """Securities code"""


class CompanyGetBoardCompositionResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
