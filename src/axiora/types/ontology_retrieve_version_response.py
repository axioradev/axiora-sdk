# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .meta import Meta
from .._models import BaseModel

__all__ = ["OntologyRetrieveVersionResponse", "Data"]


class Data(BaseModel):
    """Current ontology version."""

    version: str
    """Semantic version string (e.g. '2.0.0').

    Bumped on breaking changes to field labeling, unit handling, or
    validation. Pin against this version when correlating historical
    responses.
    """


class OntologyRetrieveVersionResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Pagination and request metadata."""
