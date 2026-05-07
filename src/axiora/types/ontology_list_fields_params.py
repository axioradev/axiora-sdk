# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OntologyListFieldsParams"]


class OntologyListFieldsParams(TypedDict, total=False):
    category: str
    """Filter by field category.

    One of: 'income_statement', 'balance_sheet', 'cash_flow', 'per_share',
    'ratio', 'dei', 'other'. Returns 422 for unknown values.
    """
