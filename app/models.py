from sqlalchemy import Column, Integer, String
from app.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    event_type = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    session_id = Column(String, nullable=False)
    client_ts = Column(Integer, nullable=False)