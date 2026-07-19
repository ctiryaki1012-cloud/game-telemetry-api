from pydantic import BaseModel

class EventCreate(BaseModel):
    user_id: str
    event_type: str
    platform: str
    session_id: str
    client_ts: int