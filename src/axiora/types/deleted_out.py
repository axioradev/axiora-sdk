# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .meta import Meta
from .._models import BaseModel

__all__ = ["DeletedOut", "Data"]


class Data(BaseModel):
    """The requested resource object."""

    id: int
    """ID of the deleted resource."""

    deleted: bool
    """True if the resource was successfully deleted."""


class DeletedOut(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
