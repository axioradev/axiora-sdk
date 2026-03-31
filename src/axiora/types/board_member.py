# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BoardMember"]


class BoardMember(BaseModel):
    is_outside: bool
    """Outside/independent director"""

    name: str
    """Officer name"""

    role_type: str
    """board or exec"""

    date_of_birth: Optional[str] = None
    """Date of birth (Japanese format)"""

    shares_held_thousands: Optional[int] = None
    """Shares held (thousands)"""

    title: Optional[str] = None
    """Official title/position"""
