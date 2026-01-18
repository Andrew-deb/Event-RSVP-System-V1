from fastapi import FastAPI
from app.api.v1.event import event_router


app = FastAPI()

app.include_router(event_router, prefix="/events", tags=["Event Routes"])
