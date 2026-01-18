from pydantic import BaseModel
from typing import Optional, List


class Event(BaseModel):
    id: int
    title: str
    description: str
    date: str
    location: str
    flyer_filename: Optional[str] = None
    rsvps: List[str] = []


class RSVP(BaseModel):
    name: str
    email: str
