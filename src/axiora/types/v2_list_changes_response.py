# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["V2ListChangesResponse", "DataSubject", "DataSource", "Data", "Meta"]


class DataSubject(BaseModel):
    entity: str
    """Entity ID, e.g. 'company:E00883'."""

    role: str
    """Role in the fact, e.g. 'holder' or 'issuer'."""


class DataSource(BaseModel):
    doc_id: Optional[str] = None
    """Filing the value came from."""

    doc_type: Optional[str] = None
    """Document type code, e.g. '350'."""

    filed_at: Optional[str] = None
    """When the filing was submitted (ISO 8601)."""

    quote: Optional[str] = None
    """Quoted line, where kept."""

    read_by: Optional[str] = None
    """'kiri' when Kiri read the value."""

    section: Optional[str] = None
    """Section of the filing, where kept."""

    url: Optional[str] = None
    """The filing on EDINET."""


class Data(BaseModel):
    held_reason: Optional[str] = None

    id: str
    """Stable fact ID."""

    known_at: Optional[str] = None
    """When the market could first know it."""

    source: DataSource

    status: Literal["confirmed", "held"]

    subjects: List[DataSubject]

    superseded_by: Optional[str] = None

    type: str

    valid_as_of: Optional[str] = None
    """Date the fact describes."""

    value: Dict[str, object]


class Meta(BaseModel):
    caveats: Optional[List[str]] = None

    data_as_of: Optional[str] = None
    """Source data date of the snapshot served."""

    data_version: Optional[str] = None
    """Snapshot version served."""

    deprecations: Optional[List[Dict[str, object]]] = None

    next_cursor: Optional[str] = None

    request_id: str

    resolved_from: Optional[str] = None
    """The identifier sent, when it was not the canonical id in data.id."""


class V2ListChangesResponse(BaseModel):
    data: List[Data]

    meta: Meta
