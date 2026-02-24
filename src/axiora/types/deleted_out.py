# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .meta import Meta
from .._models import BaseModel

__all__ = ["DeletedOut", "Data"]


class Data(BaseModel):
    id: int

    deleted: bool


class DeletedOut(BaseModel):
    data: Data

    meta: Meta
