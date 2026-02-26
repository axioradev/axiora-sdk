# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .company import Company
from .._models import BaseModel

__all__ = ["Peer"]


class Peer(BaseModel):
    company: Company
    """Peer company details."""

    fiscal_year: int
    """Fiscal year of the peer data."""

    net_income: Optional[int] = None
    """Net income in JPY."""

    revenue: Optional[int] = None
    """Revenue in JPY."""
