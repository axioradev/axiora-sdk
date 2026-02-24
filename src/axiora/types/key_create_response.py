# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .key_response import KeyResponse

__all__ = ["KeyCreateResponse"]


class KeyCreateResponse(BaseModel):
    key: KeyResponse

    raw_key: str
