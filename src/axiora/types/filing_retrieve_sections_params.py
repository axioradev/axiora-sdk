# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FilingRetrieveSectionsParams"]


class FilingRetrieveSectionsParams(TypedDict, total=False):
    section: Optional[str]
    """Filter by section key.

    One of: mda, risk_factors, business_overview, strategy, sustainability,
    research_and_development, dividend_policy, governance, company_history,
    employees, critical_contracts, capital_expenditures, accounting_policy,
    segment_info, financial_instruments.
    """
