from sqlalchemy import Column, Integer, String ,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from models.base import Base

class Execution(Base):
    __tablename__ = 'execution'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    execution_key = Column(String)
    created_at = Column(String)
    execution_data = Column(JSONB)
    routine_id = Column(Integer, ForeignKey('routine.id'))
    trigger_at = Column(String)

    routine = relationship('Routine', back_populates='executions')
    events = relationship('ExecutionEvent', back_populates='execution')