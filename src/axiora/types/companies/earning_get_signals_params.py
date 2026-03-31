# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["EarningGetSignalsParams"]


class EarningGetSignalsParams(TypedDict, total=False):
    limit: int

    signal_type: Optional[str]
    """
    Filter: earnings_beat, earnings_miss, forecast_revision_up,
    forecast_revision_down, record_revenue, margin_expansion, margin_contraction
    """
