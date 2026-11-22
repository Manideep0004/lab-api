import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

ENV = os.getenv("APP_ENV", "dev")


class Event(BaseModel):
    name: str
    payload: dict = {}


@app.get("/health")
def health():
    return {"status": "ok", "env": ENV}


@app.post("/event")
def create_event(event: Event):
    return {"received": event.name, "env": ENV}


