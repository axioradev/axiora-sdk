# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["BatchIdentifiersResponse", "DataProvenance", "Data"]


class DataProvenance(BaseModel):
    """
    Why the identifier fields hold the values they hold.

    A null identifier is only usable if the consumer can tell "we checked and
    there is none" from "we never looked". These three fields carry that
    distinction structurally so it does not have to be inferred from prose.
    """

    entity_registry: str
    """
    Where the ENTITY-level fields (`lei`, `entity_id`, `name`) come from. 'entity_registry': a resolved entity record backs this identifier. 'none': the identifier is known only from filing data, so `lei` and `entity_id` are unknown rather than absent.
    """

    explanation: str
    """The same statement in prose. Always present."""

    market_identifiers: str
    """
    Where `securities_code`, `isin` and `jpx_code` come from, and what their nulls mean. 'market_cross_reference': served from the listed-issuer cross-reference. 'unlisted': this filer is not listed, so it has none to carry. 'unmapped': listed, but not yet cross-referenced, so they are unknown to us. 'not_an_issuer': the identifier names an entity with no issuer facet, so they do not apply.
    """


class Data(BaseModel):
    confidence: Optional[float] = None
    """Match confidence (0.0 to 1.0). Null when there is no match to score."""

    edinet_code: Optional[str] = None
    """
    EDINET submitter code (e.g. 'E02144'). Null only when the identifier names an entity that has never filed under one of its own, which is possible for a group of co-filing investors.
    """

    entity_id: Optional[str] = None
    """Stable key of the resolved entity behind this identifier. Null when no resolved entity record covers it."""

    isin: Optional[str] = None
    """ISIN (12-character international securities ID)."""

    jpx_code: Optional[str] = None
    """JPX issuer code."""

    lei: Optional[str] = None
    """
    Legal Entity Identifier (20 characters). An entity-level identifier, so it is served from the resolved entity record and never from the listed-issuer cross-reference. Null when no entity record backs this identifier, or when that record carries no LEI; `provenance.entity_registry` says which.
    """

    links: Optional[Dict[str, str]] = None
    """Role to the endpoint path that answers for this entity in that role."""

    match_method: Optional[str] = None
    """
    How the market identifiers were matched (e.g. 'exact', 'fuzzy'). Null when this company is not in the listed-issuer cross-reference; `provenance.market_identifiers` says why.
    """

    matched_at: Optional[datetime] = None
    """When the market identifiers were last matched. Null when never matched."""

    name: Optional[str] = None
    """The entity's name, as filed (Japanese)."""

    name_en: Optional[str] = None
    """English name, where we hold one."""

    provenance: DataProvenance
    """
    Why the identifier fields hold the values they hold.

    A null identifier is only usable if the consumer can tell "we checked and
    there is none" from "we never looked". These three fields carry that
    distinction structurally so it does not have to be inferred from prose.
    """

    roles: Optional[List[str]] = None
    """
    Every role this entity holds: 'issuer' (company endpoints answer for it) and/or 'investor' (it files shareholding reports). An entity is legitimately both, so this is always a list.
    """

    securities_code: Optional[str] = None
    """TSE securities code (e.g. '7203')."""


class BatchIdentifiersResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Dict[str, object]
    """Pagination and request metadata."""
