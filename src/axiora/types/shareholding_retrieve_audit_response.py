# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["ShareholdingRetrieveAuditResponse", "Data"]


class Data(BaseModel):
    """Full audit bundle for a single shareholding row."""

    realtime: Dict[str, object]
    """What was knowable at filing time.

    Includes predicted_category (= holding_purpose_category), confidence,
    alternative_label + probability, validated, as_of_date (= source.base_date).
    """

    shareholding_id: int
    """Row identifier."""

    source: Dict[str, object]
    """Filing reference.

    Includes doc_id (EDINET), filer EDINET code, issuer security code, and
    base_date. Every claim in this bundle traces to this filing.
    """

    classifier_version: Optional[str] = None
    """Stable token identifying the classifier state that produced
    realtime.predicted_category.

    Pin to a specific value for stable replay.
    """

    retrospective: Optional[Dict[str, object]] = None
    """What later evidence revealed.

    Same shape as realtime but predicted_category may differ when later filings
    from the same filer × issuer disclosed a more-active intent.
    evidence_cutoff_date marks the latest filing used. Null when no later
    evidence existed.
    """


class ShareholdingRetrieveAuditResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Pagination and request metadata."""
