# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .meta import Meta
from .filing import Filing
from .._models import BaseModel

__all__ = ["FilingRetrieveResponse"]


class FilingRetrieveResponse(BaseModel):
    data: Filing

    meta: Meta
