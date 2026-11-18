# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "V2RetrieveCompanyResponse",
    "DataFactsUnionMember0ValueSubject",
    "DataFactsUnionMember0ValueSource",
    "DataFactsUnionMember0Value",
    "Data",
    "Meta",
]


class DataFactsUnionMember0ValueSubject(BaseModel):
    entity: str
    """Entity ID, e.g. 'company:E00883'."""

    role: str
    """Role in the fact, e.g. 'holder' or 'issuer'."""


class DataFactsUnionMember0ValueSource(BaseModel):
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


class DataFactsUnionMember0Value(BaseModel):
    held_reason: Optional[str] = None

    id: str
    """Stable fact ID."""

    known_at: Optional[str] = None
    """When the market could first know it."""

    source: DataFactsUnionMember0ValueSource

    status: Literal["confirmed", "held"]

    subjects: List[DataFactsUnionMember0ValueSubject]

    superseded_by: Optional[str] = None

    type: str

    valid_as_of: Optional[str] = None
    """Date the fact describes."""

    value: Dict[str, object]


class Data(BaseModel):
    attributes: Optional[Dict[str, object]] = None

    facts: Optional[Dict[str, List[DataFactsUnionMember0Value]]] = None

    facts_more: Optional[Dict[str, str]] = None
    """For an included fact type capped at 50: the /v2/facts link for the rest."""

    held_reason: Optional[str] = None

    id: str
    """Entity ID, e.g. 'company:E00883' or 'holder:E06485'."""

    ids: Optional[Dict[str, Optional[str]]] = None
    """
    Every public identifier held for the entity (EDINET code, securities code, 法人番号, LEI, the v1 filer code). Any of them works as input. Null means none is held.
    """

    name: Optional[str] = None

    name_jp: Optional[str] = None

    status: Optional[Literal["confirmed", "held"]] = None

    type: str


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


class V2RetrieveCompanyResponse(BaseModel):
    data: Data

    meta: Meta
