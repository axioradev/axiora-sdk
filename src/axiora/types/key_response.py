# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["KeyResponse"]


class KeyResponse(BaseModel):
    id: int

    created_at: str

    key_prefix: str

    label: Optional[str] = None

    last_used_at: Optional[str] = None

    tier: str
