# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["HealthCheckDeepResponse"]


class HealthCheckDeepResponse(BaseModel):
    checks: Dict[str, str]
    """Individual subsystem statuses (e.g. {'database': 'ok', 'cache': 'ok'})."""

    status: str
    """Overall service status: 'ok' or 'degraded'."""
