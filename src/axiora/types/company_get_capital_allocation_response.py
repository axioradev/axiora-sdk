# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .meta import Meta
from .._models import BaseModel
from .capital_allocation import CapitalAllocation

__all__ = ["CompanyGetCapitalAllocationResponse"]


class CompanyGetCapitalAllocationResponse(BaseModel):
    data: CapitalAllocation
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
