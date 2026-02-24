# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .meta import Meta
from .._models import BaseModel
from .health_score import HealthScore

__all__ = ["CompanyRetrieveHealthResponse"]


class CompanyRetrieveHealthResponse(BaseModel):
    data: HealthScore

    meta: Meta
