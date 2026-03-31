# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["RelationshipGetRelationshipsParams"]


class RelationshipGetRelationshipsParams(TypedDict, total=False):
    fiscal_year: Optional[int]
    """Fiscal year for board data. Defaults to latest."""
