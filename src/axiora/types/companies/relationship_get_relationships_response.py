# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..meta import Meta
from ..._models import BaseModel
from ..board_member import BoardMember

__all__ = [
    "RelationshipGetRelationshipsResponse",
    "Data",
    "DataBoardInterlock",
    "DataBoardInterlockCompany",
    "DataCrossHolding",
    "DataHolding",
    "DataMajorShareholder",
]


class DataBoardInterlockCompany(BaseModel):
    edinet_code: str
    """EDINET code of the other company"""

    name: Optional[str] = None
    """Company name"""

    securities_code: Optional[str] = None
    """Securities code"""

    title: Optional[str] = None
    """Director's title at this company"""


class DataBoardInterlock(BaseModel):
    confidence: str
    """'high' (DOB matches) or 'low' (DOB null on either side)"""

    name: str
    """Director name"""

    companies: Optional[List[DataBoardInterlockCompany]] = None
    """Other companies where this director serves"""

    date_of_birth: Optional[str] = None
    """Date of birth (Japanese format)"""


class DataCrossHolding(BaseModel):
    a_holds_b_pct: float
    """A's holding ratio in B (%)"""

    b_holds_a_pct: float
    """B's holding ratio in A (%)"""

    company_a_edinet_code: str
    """EDINET code of company A"""

    company_b_edinet_code: str
    """EDINET code of company B"""

    relationship_type: str
    """mutual or asymmetric"""

    cluster_id: Optional[int] = None
    """Cluster grouping ID"""

    company_a_name: Optional[str] = None
    """Name of company A"""

    company_a_securities_code: Optional[str] = None
    """Securities code of company A"""

    company_b_name: Optional[str] = None
    """Name of company B"""

    company_b_securities_code: Optional[str] = None
    """Securities code of company B"""


class DataHolding(BaseModel):
    holding_ratio_pct: Optional[float] = None
    """Holding ratio (%)"""

    issuer_name: Optional[str] = None
    """Name of the held company"""

    issuer_security_code: Optional[str] = None
    """Securities code of the held company"""

    trajectory_type: Optional[str] = None
    """accumulating, exiting, stable, new_position"""


class DataMajorShareholder(BaseModel):
    filer_canonical_code: Optional[str] = None
    """Filer EDINET code"""

    filer_name: Optional[str] = None
    """Filer/shareholder name"""

    holding_ratio_pct: Optional[float] = None
    """Latest holding ratio (%)"""

    purpose_category: Optional[str] = None
    """Investment purpose"""

    trajectory_type: Optional[str] = None
    """accumulating, exiting, stable, new_position"""


class Data(BaseModel):
    """The requested resource object."""

    company: Dict[str, object]
    """Company identifiers"""

    board_interlocks: Optional[List[DataBoardInterlock]] = None

    board_members: Optional[List[BoardMember]] = None

    cross_holdings: Optional[List[DataCrossHolding]] = None

    holdings: Optional[List[DataHolding]] = None

    major_shareholders: Optional[List[DataMajorShareholder]] = None


class RelationshipGetRelationshipsResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
