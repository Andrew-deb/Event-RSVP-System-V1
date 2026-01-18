from pydantic import BaseModel
from typing import Annotated, Optional, List
from fastapi import Form, File, UploadFile


class EventBase(BaseModel):
    title: Annotated[str, Form()]
    description: Annotated[str, Form()]
    date: Annotated[str, Form()]
    location: Annotated[str, Form()]
    flyer_filename: Annotated[Optional[UploadFile], File(None)] = None
    


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: Annotated[int, Form()]
    rsvps: List[str] = []



class RSVP(BaseModel):
    name: Annotated[str, Form()]
    email: Annotated[str, Form()]
