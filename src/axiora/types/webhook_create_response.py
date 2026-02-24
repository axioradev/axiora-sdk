# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel

__all__ = ["WebhookCreateResponse", "Data"]


class Data(BaseModel):
    id: int

    active: bool

    created_at: str

    events: List[str]

    secret: str

    url: str


class WebhookCreateResponse(BaseModel):
    data: Data

    meta: Meta
