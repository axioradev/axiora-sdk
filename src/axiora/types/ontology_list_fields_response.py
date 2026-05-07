# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .ontology_field import OntologyField

__all__ = ["OntologyListFieldsResponse"]


class OntologyListFieldsResponse(BaseModel):
    data: List[OntologyField]
    """All fields, optionally filtered by category."""

    meta: Meta
    """Pagination and request metadata."""
