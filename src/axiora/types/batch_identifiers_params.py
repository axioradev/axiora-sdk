# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["BatchIdentifiersParams"]


class BatchIdentifiersParams(TypedDict, total=False):
    ids: Required[SequenceNotStr[str]]
    """Identifiers to resolve (1-100). Any mix of EDINET codes, securities codes and investor identifiers."""
