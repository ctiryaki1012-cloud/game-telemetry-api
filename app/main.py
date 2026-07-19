from fastapi import FastAPI
from fastapi import Header, HTTPException, Depends
from app.schemas import EventCreate
from app.database import SessionLocal, engine
from app.models import Event

Event.metadata.create_all(bind=engine)

app = FastAPI()

API_KEY = "24072005"

def verify_api_key(x_api_key: str = Header()):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Geçersiz API Key")

@app.post("/events")
def create_event(event: EventCreate, api_key: str = Depends(verify_api_key)):
    db = SessionLocal()

    new_event = Event(
        user_id=event.user_id,
        event_type=event.event_type,
        platform=event.platform,
        session_id=event.session_id,
        client_ts=event.client_ts
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return {
        "message": "Event başarıyla kaydedildi.",
        "event": new_event
    }


@app.get("/events")
def get_events(api_key: str = Depends(verify_api_key)):
    db = SessionLocal()
    events = db.query(Event).all()
    return events