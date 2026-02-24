# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["HealthScore"]


class HealthScore(BaseModel):
    components: Dict[str, float]

    computed_at: datetime

    edinet_code: str

    fiscal_year: int

    flags: List[str]

    industry_adjustment: float

    score: int

    data_source: Optional[str] = None

    methodology: Optional[str] = None
