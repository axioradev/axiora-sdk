# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .meta import Meta
from .._models import BaseModel

__all__ = ["ListResponseVotingResult", "Data"]


class Data(BaseModel):
    edinet_code: str
    """EDINET submitter code."""

    proposal_number: int
    """Proposal number (1-based)."""

    agm_date: Optional[date] = None
    """AGM date (ISO 8601)."""

    approval_pct: Optional[float] = None
    """Approval percentage (0-100)."""

    candidate_name: Optional[str] = None
    """Candidate name (for director/auditor elections)."""

    proposal_description: Optional[str] = None
    """Description of the proposal."""

    result: Optional[str] = None
    """Vote result: '可決' (approved) or '否決' (rejected)."""

    securities_code: Optional[str] = None
    """TSE securities code."""

    votes_abstain: Optional[int] = None
    """Abstentions."""

    votes_against: Optional[int] = None
    """Votes against."""

    votes_for: Optional[int] = None
    """Votes in favor."""


class ListResponseVotingResult(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
