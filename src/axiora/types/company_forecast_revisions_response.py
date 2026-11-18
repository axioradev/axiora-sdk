# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "CompanyForecastRevisionsResponse",
    "DataRevisionPrevious",
    "DataRevisionCurrent",
    "DataRevisionIssuerMetric",
    "DataRevision",
    "Data",
    "Source",
    "Meta",
]


class DataRevisionPrevious(BaseModel):
    """Monetary amounts are integer JPY; EPS is JPY per share."""

    bank_ordinary_revenues: Optional[int] = None

    eps: Optional[float] = None

    gross_operating_revenues: Optional[int] = None

    net_income: Optional[int] = None

    operating_income: Optional[int] = None

    operating_revenues: Optional[int] = None

    ordinary_income: Optional[int] = None

    profit: Optional[int] = None

    profit_before_tax: Optional[int] = None

    revenue: Optional[int] = None


class DataRevisionCurrent(BaseModel):
    """Monetary amounts are integer JPY; EPS is JPY per share."""

    bank_ordinary_revenues: Optional[int] = None

    eps: Optional[float] = None

    gross_operating_revenues: Optional[int] = None

    net_income: Optional[int] = None

    operating_income: Optional[int] = None

    operating_revenues: Optional[int] = None

    ordinary_income: Optional[int] = None

    profit: Optional[int] = None

    profit_before_tax: Optional[int] = None

    revenue: Optional[int] = None


class DataRevisionIssuerMetric(BaseModel):
    """
    A company-defined guidance line (EBITDA, 事業利益, コア営業利益) under the label the issuer
    printed, never mapped to a statutory field. Integer JPY.
    """

    current: Optional[int] = None

    label: str

    previous: Optional[int] = None


class DataRevision(BaseModel):
    accounting_standard: Literal["JP-GAAP", "IFRS"]

    current: DataRevisionCurrent
    """Monetary amounts are integer JPY; EPS is JPY per share."""

    current_unreported_fields: List[str]

    is_consolidated: bool

    issuer_metrics: Optional[List[DataRevisionIssuerMetric]] = None

    period_end: date

    period_start: date

    period_type: Literal["FY", "Q2"]

    previous: DataRevisionPrevious
    """Monetary amounts are integer JPY; EPS is JPY per share."""

    previous_unreported_fields: List[str]


class Data(BaseModel):
    company_name: str

    fiscal_year_end: date

    notes: str

    notice: str

    published_at: datetime

    reason: str

    revisions: List[DataRevision]

    securities_code: str

    tdnet_pdf_url: str

    title: str


class Source(BaseModel):
    disposition: Literal["parsed", "archive_only", "held"]

    published_at: datetime

    tdnet_pdf_url: str

    title: str


class Meta(BaseModel):
    archive_only_count: int

    caveats: List[str]

    computation_version: Optional[str] = None

    data_as_of: Optional[datetime] = None
    """Latest captured source publication time; null when source_total is zero."""

    held_count: int

    limit: int

    offset: int

    ontology_version: Optional[str] = None

    parsed_count: int

    request_id: str

    securities_code: str

    source_total: int

    total: int


class CompanyForecastRevisionsResponse(BaseModel):
    data: List[Data]

    meta: Meta

    sources: List[Source]
