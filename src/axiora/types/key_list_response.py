# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .key_response import KeyResponse

__all__ = ["KeyListResponse"]


class KeyListResponse(BaseModel):
    has_ever_created: bool

    keys: List[KeyResponse]
