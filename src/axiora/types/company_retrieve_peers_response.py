# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .peer import Peer
from .._models import BaseModel

__all__ = ["CompanyRetrievePeersResponse"]


class CompanyRetrievePeersResponse(BaseModel):
    data: List[Peer]

    meta: Meta
