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
    description: str

    name: str

    operator: str

    url: str


class DataExchangeBreakdown(BaseModel):
    companies: int

    listing: str


class DataFilingType(BaseModel):
    count: int

    doc_type: str

    label: str


class DataFiscalYearDepth(BaseModel):
    companies: int

    filings: int

    fiscal_year: int


class DataFiscalYearRange(BaseModel):
    max: Optional[int] = None

    min: Optional[int] = None


class DataMetricCoverage(BaseModel):
    count: int

    coverage_pct: float

    total_filings: int


class DataSectorBreakdown(BaseModel):
    companies: int

    sector: str


class DataTotals(BaseModel):
    companies: int

    filings: int

    financial_data_points: int

    financial_metrics: int

    listed_companies: int

    translated_sections: int


class Data(BaseModel):
    accounting_standards: Dict[str, int]

    data_source: DataDataSource

    exchange_breakdown: List[DataExchangeBreakdown]

    filing_types: List[DataFilingType]

    fiscal_year_depth: List[DataFiscalYearDepth]

    fiscal_year_range: DataFiscalYearRange

    metric_coverage: Dict[str, DataMetricCoverage]

    sector_breakdown: List[DataSectorBreakdown]

    totals: DataTotals

    latest_filing_at: Optional[str] = None


class CoverageRetrieveResponse(BaseModel):
    data: Data

    meta: Meta
