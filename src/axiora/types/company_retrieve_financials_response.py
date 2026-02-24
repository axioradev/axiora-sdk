# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .financial import Financial

__all__ = ["CompanyRetrieveFinancialsResponse"]


class CompanyRetrieveFinancialsResponse(BaseModel):
    data: List[Financial]

    meta: Meta
