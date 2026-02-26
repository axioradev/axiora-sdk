# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from .meta import Meta
from .._models import BaseModel

__all__ = ["BulkExportFinancialsJsonResponse", "Data"]


class Data(BaseModel):
    edinet_code: str
    """EDINET submitter code."""

    fiscal_year: int
    """Fiscal year."""

    name_jp: str
    """Company name in Japanese."""

    accounting_standard: Optional[str] = None
    """Accounting standard: 'Japan GAAP', 'IFRS', or 'US GAAP'."""

    name_en: Optional[str] = None
    """Company name in English."""

    period_end: Optional[str] = None
    """Last day of the fiscal period (ISO 8601)."""

    sector: Optional[str] = None
    """TSE 33-sector classification in Japanese."""

    securities_code: Optional[str] = None
    """TSE securities code."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class BulkExportFinancialsJsonResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
