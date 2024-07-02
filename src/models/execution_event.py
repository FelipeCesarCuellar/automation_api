from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from models.base import Base

class ExecutionEvent(Base):
    __tablename__ = 'execution_event'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    execution_event_key = Column(String)
    execution_id = Column(Integer)
    created_at = Column(String)
    executed_at = Column(String)