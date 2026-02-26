# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from .._models import BaseModel

__all__ = ["Financial"]


class Financial(BaseModel):
    edinet_code: str
    """EDINET submitter code (e.g. 'E02144')."""

    fiscal_year: int
    """Fiscal year label. '2024' means the fiscal year ending in calendar year 2024."""

    period_end: date
    """Last day of the fiscal period (e.g. '2024-03-31')."""

    bps: Optional[float] = None
    """Book value per share in JPY.

    Equity attributable to owners ÷ shares outstanding.
    """

    capex: Optional[int] = None
    """Capital expenditure in JPY.

    Extracted from investing CF breakdown when available.
    """

    capital_stock: Optional[int] = None
    """Stated capital (資本金) in JPY."""

    cash_and_equivalents: Optional[int] = None
    """Cash and cash equivalents in JPY. BS item, not CF ending balance."""

    comprehensive_income: Optional[int] = None
    """Comprehensive income in JPY. Net income + other comprehensive income items."""

    cost_of_sales: Optional[int] = None
    """Cost of sales (売上原価) in JPY."""

    currency: Optional[str] = None
    """Currency code. Always 'JPY' — all monetary values are in Japanese yen."""

    current_assets: Optional[int] = None
    """Current assets (流動資産) in JPY."""

    current_liabilities: Optional[int] = None
    """Current liabilities (流動負債) in JPY."""

    data_source: Optional[str] = None
    """Data provenance."""

    deferred_tax_assets: Optional[int] = None
    """Deferred tax assets (繰延税金資産) in JPY."""

    depreciation: Optional[int] = None
    """Depreciation and amortization in JPY. May appear in PL notes or CF adjustments."""

    diluted_eps: Optional[float] = None
    """Diluted earnings per share in JPY.

    Accounts for convertible bonds, stock options, etc.
    """

    dividends_per_share: Optional[float] = None
    """Annual dividends per share in JPY (e.g.

    75.0). Sum of interim + year-end dividends.
    """

    eps: Optional[float] = None
    """Basic earnings per share in JPY (e.g.

    285.23). Net income ÷ weighted-average shares outstanding.
    """

    extraordinary_income: Optional[int] = None
    """Extraordinary income (特別利益) in JPY.

    JP-GAAP only; IFRS does not have this line item.
    """

    extraordinary_loss: Optional[int] = None
    """Extraordinary loss (特別損失) in JPY.

    JP-GAAP only; IFRS does not have this line item.
    """

    financing_cf: Optional[int] = None
    """Cash flow from financing activities in JPY.

    Negative means net repayment/dividends.
    """

    goodwill: Optional[int] = None
    """Goodwill (のれん) in JPY.

    IFRS reports separately; JP-GAAP includes in intangible assets.
    """

    gross_profit: Optional[int] = None
    """Gross profit (売上総利益) in JPY. Revenue minus cost of sales."""

    ibd_current: Optional[int] = None
    """Interest-bearing debt, current portion in JPY.

    Short-term borrowings + current portion of long-term debt.
    """

    ibd_noncurrent: Optional[int] = None
    """Interest-bearing debt, non-current portion in JPY.

    Long-term borrowings + bonds payable.
    """

    income_before_tax: Optional[int] = None
    """Income before income taxes (税引前当期純利益) in JPY."""

    intangible_assets: Optional[int] = None
    """Intangible assets (無形固定資産) in JPY. Includes goodwill for JP-GAAP filers."""

    interest_expense: Optional[int] = None
    """Interest expense (支払利息) in JPY."""

    interim_dividend: Optional[float] = None
    """Interim dividend per share in JPY. Subset of dividends_per_share."""

    inventories: Optional[int] = None
    """Inventories (棚卸資産) in JPY."""

    investing_cf: Optional[int] = None
    """Cash flow from investing activities in JPY.

    Typically negative (capital deployment).
    """

    investment_securities: Optional[int] = None
    """Investment securities (投資有価証券) in JPY."""

    is_consolidated: Optional[bool] = None
    """True if data comes from consolidated financial statements.

    False for standalone/parent-only filers (companies without subsidiaries).
    """

    net_assets: Optional[int] = None
    """Net assets (純資産) in JPY.

    JP-GAAP concept; includes non-controlling interests and stock acquisition
    rights.
    """

    net_income: Optional[int] = None
    """Net income attributable to owners of the parent in JPY. Null if not reported."""

    non_controlling_interests: Optional[int] = None
    """Non-controlling interests (非支配株主持分) in JPY. Null for standalone filers."""

    noncurrent_assets: Optional[int] = None
    """Non-current assets (固定資産) in JPY."""

    noncurrent_liabilities: Optional[int] = None
    """Non-current liabilities (固定負債) in JPY."""

    num_employees: Optional[int] = None
    """Number of employees (headcount). Unitless integer."""

    operating_cf: Optional[int] = None
    """Cash flow from operating activities in JPY."""

    operating_income: Optional[int] = None
    """Operating income (営業利益) in JPY.

    Null if not reported or if the filer uses a non-standard PL format.
    """

    ordinary_income: Optional[int] = None
    """Ordinary income (経常利益) in JPY.

    JP-GAAP specific; includes non-operating items. Null for IFRS/US-GAAP filers.
    """

    payout_ratio: Optional[float] = None
    """Dividend payout ratio as percentage (e.g.

    30.0 means 30%). Dividends ÷ net income.
    """

    pe_ratio: Optional[float] = None
    """Price-to-earnings ratio. Derived from market price ÷ EPS when available."""

    ppe: Optional[int] = None
    """Property, plant and equipment (有形固定資産) in JPY."""

    retained_earnings: Optional[int] = None
    """Retained earnings (利益剰余金) in JPY."""

    revenue: Optional[int] = None
    """Total revenue in JPY.

    IFRS filers report 'Revenue'; JP-GAAP reports '売上高' or '営業収益'. Null if
    not reported.
    """

    rnd_expenses: Optional[int] = None
    """Research and development expenses (研究開発費) in JPY.

    Disclosed in notes to financials.
    """

    roe: Optional[float] = None
    """Return on equity as percentage (e.g.

    12.5 means 12.5%). Null when equity or net income is unavailable.
    """

    sga: Optional[int] = None
    """Selling, general and administrative expenses (販管費) in JPY."""

    shares_issued: Optional[int] = None
    """Total shares issued (発行済株式総数). Includes treasury stock."""

    source_doc_id: Optional[str] = None
    """EDINET document ID of the source filing (e.g. 'S100ABCD')."""

    total_assets: Optional[int] = None
    """Total assets (総資産) in JPY."""

    total_equity: Optional[int] = None
    """Total equity including non-controlling interests in JPY."""

    total_liabilities: Optional[int] = None
    """Total liabilities (負債合計) in JPY."""

    trade_payables: Optional[int] = None
    """Trade payables (買掛金・支払手形) in JPY."""

    trade_receivables: Optional[int] = None
    """Trade receivables (売掛金・受取手形) in JPY."""

    treasury_stock: Optional[int] = None
    """Treasury stock (自己株式) in JPY. Reported as negative in equity section."""
