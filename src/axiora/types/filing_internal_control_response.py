# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FilingInternalControlResponse", "Data"]


class Data(BaseModel):
    amends_doc_id: Optional[str] = None

    cabinet_ordinance: Optional[str] = None

    cfo: Optional[str] = None

    company_name: Optional[str] = None

    company_name_en: Optional[str] = None

    doc_id: str

    doc_type: Literal["235", "236"]

    document_form: Optional[str] = None

    edinet_code: Optional[str] = None

    effectiveness: Optional[Literal["effective", "not_effective", "unknown"]] = None

    evaluation_date: Optional[date] = None

    filing_date: Optional[date] = None

    hq_address: Optional[str] = None

    material_weakness: Optional[bool] = None

    parse_warnings: Optional[List[str]] = None

    place_of_filing: Optional[str] = None

    representative: Optional[str] = None

    result_of_evaluation_text: Optional[str] = None

    security_code: Optional[str] = None


class FilingInternalControlResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Dict[str, object]
    """Request metadata."""
