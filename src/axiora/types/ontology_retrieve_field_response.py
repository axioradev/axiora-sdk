# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .meta import Meta
from .._models import BaseModel
from .ontology_field import OntologyField

__all__ = ["OntologyRetrieveFieldResponse"]


class OntologyRetrieveFieldResponse(BaseModel):
    data: OntologyField
    """Full definition for the requested field."""

    meta: Meta
    """Pagination and request metadata."""
