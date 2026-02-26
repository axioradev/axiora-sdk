# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Meta"]


class Meta(BaseModel):
    request_id: str
    """Unique request identifier for tracing and support (e.g. 'req_abc123')."""

    limit: Optional[int] = None
    """Maximum records returned per page."""

    next_cursor: Optional[str] = None
    """Opaque cursor for the next page (keyset pagination). Null on the last page."""

    offset: Optional[int] = None
    """Number of records skipped (offset-based pagination)."""

    total: Optional[int] = None
    """Total number of matching records (list endpoints only)."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
