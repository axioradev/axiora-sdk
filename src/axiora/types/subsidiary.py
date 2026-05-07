# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Subsidiary"]


class Subsidiary(BaseModel):
    holdings_filing_count: int
    """Number of 大量保有報告書 (5%+ shareholding reports) the entity has filed."""

    joint_filing_partner_count: int
    """Number of distinct other entities this subsidiary has co-filed with."""

    name: str
    """Subsidiary's Japanese name as disclosed."""

    address: Optional[str] = None
    """Address as written in the filing."""

    business: Optional[str] = None
    """Business / 事業の内容 cell — free text."""

    capital: Optional[str] = None
    """Capital cell verbatim — e.g. '10,000 百万円'."""

    country: Optional[str] = None
    """ISO 3166-1 alpha-2 derived from address.

    Null when address is not parseable.
    """

    cross_validation: Optional[str] = None
    """Bidirectional validation outcome between the parent's disclosure of this
    subsidiary and the subsidiary's own annual report.

    Possible values:

    - **`bidirectional_match`** — both sides agree on the parent's stake.
      Highest confidence: two independent filings point to the same number.
    - **`voting_pct_mismatch`** — parent reports X%, subsidiary reports Y%.
      Material disagreement (timing, accounting, or a real reporting error).
      Surfacing these is the integrity layer's whole point.
    - **`parent_only`** — the subsidiary isn't an independent EDINET filer
      (e.g., a non-listed wholly-owned sub), so the parent's disclosure is the
      only source. No second-source confirmation, no flag of disagreement.
    - **`null`** — cross-validation hasn't run for this row (older data, or
      the join key didn't resolve).
    """

    currency: Optional[str] = None
    """ISO 4217 alpha-3 derived from capital.

    Null when the cell is not parseable.
    """

    relationship_type: Optional[str] = None
    """The accounting relationship between parent and subsidiary, as classified
    in the parent's filing.

    Possible values:

    - **`consolidated_subsidiary`** — parent owns >50% of voting rights and
      consolidates the subsidiary into its financials.
    - **`equity_method_affiliate`** — parent owns 20–50% and uses the equity
      method (proportional share of profits/losses on the parent's books).
    - **`equity_method_subsidiary`** — consolidated by the equity method
      (rare; specific reporting structure).
    - **`non_consolidated_subsidiary`** — owned but not consolidated
      (typically immaterial or under exclusion criteria).
    - **`parent`** — this row IS the filer's parent, not a child.
    - **`other_related`** — その他の関係会社; doesn't fit the above buckets.
    - **`unknown`** — section header was unclassifiable.
    """

    source_filing: Optional[str] = None
    """EDINET doc_id the disclosure was extracted from.

    Auditable: every row traces to a source filing.
    """

    subsidiary_edinet_code: Optional[str] = None
    """EDINET code if the subsidiary itself files separately.

    Null when the subsidiary is not an independent filer.
    """

    voting_delta_pp: Optional[float] = None
    """Absolute pp difference in voting% when both filers report it.

    Surfaces material disagreements.
    """

    voting_pct: Optional[float] = None
    """Voting % in [0, 100] from 議決権所有割合."""
