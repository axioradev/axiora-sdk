# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = [
    "CoverageRetrieveResponse",
    "Data",
    "DataDataSource",
    "DataExchangeBreakdown",
    "DataFilingType",
    "DataFiscalYearDepth",
    "DataFiscalYearRange",
    "DataMetricCoverage",
    "DataSectorBreakdown",
    "DataTotals",
]


class DataDataSource(BaseModel):
    """Information about the upstream data source."""

    description: str
    """Human-readable description of the data source."""

    name: str
    """Data source name."""

    operator: str
    """Organization operating the data source."""

    url: str
    """URL of the data source."""


class DataExchangeBreakdown(BaseModel):
    companies: int
    """Number of companies in this segment."""

    listing: str
    """TSE market segment."""


class DataFilingType(BaseModel):
    count: int
    """Number of filings of this type."""

    doc_type: str
    """EDINET document type code."""

    label: str
    """Japanese label (e.g. '有価証券報告書')."""


class DataFiscalYearDepth(BaseModel):
    companies: int
    """Number of companies with data for this fiscal year."""

    filings: int
    """Number of filings for this fiscal year."""

    fiscal_year: int
    """Fiscal year."""


class DataFiscalYearRange(BaseModel):
    """Earliest and latest fiscal years available."""

    max: Optional[int] = None
    """Latest fiscal year in the dataset."""

    min: Optional[int] = None
    """Earliest fiscal year in the dataset."""


class DataMetricCoverage(BaseModel):
    count: int
    """Number of filings that have this metric."""

    coverage_pct: float
    """Percentage of filings with this metric (0-100)."""

    total_filings: int
    """Total filings checked."""


class DataSectorBreakdown(BaseModel):
    companies: int
    """Number of companies in this sector."""

    sector: str
    """TSE 33-sector name in Japanese."""


class DataTotals(BaseModel):
    """High-level coverage counts."""

    companies: int
    """Total companies in the database."""

    filings: int
    """Total parsed filings."""

    financial_data_points: int
    """Total non-null financial field values across all filings."""

    financial_metrics: int
    """Number of distinct financial metrics available."""

    listed_companies: int
    """Companies with a TSE securities code."""

    translated_sections: int
    """Total filing sections translated to English."""


class Data(BaseModel):
    """The requested resource object."""

    accounting_standards: Dict[str, int]
    """Count of filings per accounting standard."""

    data_source: DataDataSource
    """Information about the upstream data source."""

    exchange_breakdown: List[DataExchangeBreakdown]
    """Company count by TSE market segment."""

    filing_types: List[DataFilingType]
    """Filing count by document type."""

    fiscal_year_depth: List[DataFiscalYearDepth]
    """Per-year breakdown of companies and filings."""

    fiscal_year_range: DataFiscalYearRange
    """Earliest and latest fiscal years available."""

    metric_coverage: Dict[str, DataMetricCoverage]
    """Coverage percentage for each financial metric."""

    sector_breakdown: List[DataSectorBreakdown]
    """Company count by sector."""

    totals: DataTotals
    """High-level coverage counts."""

    latest_filing_at: Optional[str] = None
    """Timestamp of the most recent filing (ISO 8601)."""


class CoverageRetrieveResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
