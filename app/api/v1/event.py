from fastapi import APIRouter, status, Form, UploadFile, File
from typing import Annotated, Optional, List
from app.schemas.event_schema import EventCreate, Event
from app.core.db import events



event_router = APIRouter()

#create event
@event_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_event(    
    title: str = Form(...),
    description: str = Form(...),
    date: str = Form(...),
    location: str = Form(...),
    flyer_filename: Optional[UploadFile] = File(None)
):
    event_id = len(events) + 1
    new_event = {
        "id": event_id,
        "title": title,
        "description": description,
        "date": date,
        "location": location,
        "flyer": flyer_filename,
        "rsvps": []
    }

    events.append(new_event)

    return {"Message": "Event created successfully", "Data": new_event}

# getting all events
@event_router.get("/")
def get_all_events():
    return events