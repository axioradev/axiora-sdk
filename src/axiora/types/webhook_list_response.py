# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel

__all__ = ["WebhookListResponse", "Data"]


class Data(BaseModel):
    id: int
    """Webhook ID."""

    active: bool
    """Whether the webhook is currently active."""

    created_at: str
    """When the webhook was created (ISO 8601)."""

    events: List[str]
    """Subscribed event types (e.g. ['new_filing', 'amendment'])."""

    url: str
    """HTTPS URL that receives webhook deliveries."""


class WebhookListResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
