# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..meta import Meta
from ..._models import BaseModel

__all__ = ["OwnershipGetChartResponse", "Data", "DataPoint"]


class DataPoint(BaseModel):
    base_date: date
    """Date of the filing"""

    holding_ratio_pct: float
    """Holding ratio as percentage"""

    delta_pct: Optional[float] = None
    """Change from previous point in pp"""

    doc_id: Optional[str] = None
    """EDINET document ID"""

    purpose: Optional[str] = None
    """Purpose of holding"""


class Data(BaseModel):
    filer_code: str
    """EDINET code of the filer"""

    points: List[DataPoint]
    """Timeline points sorted by date"""

    source: str
    """'trajectory' or 'shareholding'"""

    filer_name: Optional[str] = None
    """Name of the filer"""

    latest_holding_pct: Optional[float] = None
    """Most recent holding ratio"""

    trajectory_type: Optional[str] = None
    """accumulating, exiting, stable, new_position"""


class OwnershipGetChartResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
