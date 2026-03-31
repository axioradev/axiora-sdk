# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OwnershipListSignalsParams"]


class OwnershipListSignalsParams(TypedDict, total=False):
    cursor: Optional[str]
    """Opaque cursor for keyset pagination"""

    date_from: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Filter: detected_date on or after"""

    date_to: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Filter: detected_date on or before"""

    filer_code: Optional[str]
    """Filter by filer EDINET code (e.g. 'E03606' for SBI Holdings)"""

    include_trivial: bool
    """Include tier 3 (trivial) signals like new_position and exit_below_5pct.

    Default returns only tier 1 (actionable) and tier 2 (informational).
    """

    limit: int
    """Results per page"""

    offset: int
    """Results to skip (ignored when cursor is set)"""

    signal_type: Optional[str]
    """
    Filter: accumulation_streak, large_step_up, large_step_down, exit_below_5pct,
    activist_escalation, new_position, pace_acceleration, purpose_drift,
    coordinated_accumulation, systematic_exit
    """
