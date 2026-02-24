# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel

__all__ = ["WebhookListResponse", "Data"]


class Data(BaseModel):
    id: int

    active: bool

    created_at: str

    events: List[str]

    url: str


class WebhookListResponse(BaseModel):
    data: List[Data]

    meta: Meta
