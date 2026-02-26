# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel

__all__ = ["WebhookCreateResponse", "Data"]


class Data(BaseModel):
    """The requested resource object."""

    id: int
    """Webhook ID."""

    active: bool
    """Whether the webhook is currently active."""

    created_at: str
    """When the webhook was created (ISO 8601)."""

    events: List[str]
    """Subscribed event types (e.g. ['new_filing', 'amendment'])."""

    secret: str
    """HMAC-SHA256 signing secret (64 hex characters).

    Only returned once at creation time.
    """

    url: str
    """HTTPS URL that receives webhook deliveries."""


class WebhookCreateResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
