# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TrajectoryListParams"]


class TrajectoryListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Opaque cursor for keyset pagination"""

    date_from: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Filter: last_base_date on or after"""

    date_to: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Filter: last_base_date on or before"""

    limit: int
    """Results per page"""

    offset: int
    """Results to skip (ignored when cursor is set)"""

    trajectory_type: Optional[str]
    """Filter: accumulating, exiting, stable, new_position"""
