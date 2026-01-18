from pydantic import BaseModel


class RSVP(BaseModel):
    name: str
    email: str