from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class ExecutionEvent(Base):
    __tablename__ = 'execution_event'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    execution_event_key = Column(String)
    execution_id = Column(Integer, ForeignKey('execution.id'))
    executed_at = Column(String)

    execution = relationship('Execution', back_populates='events')