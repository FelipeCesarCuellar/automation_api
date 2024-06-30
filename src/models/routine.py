from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from models.base import Base

class Routine(Base):
    __tablename__ = 'routine'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    routine_key = Column(String)
    trigger_data = Column(JSONB)
    steps_data = Column(JSONB)
    created_at = Column(String)