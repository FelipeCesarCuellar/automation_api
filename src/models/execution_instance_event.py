from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class ExecutionInstanceEvent(Base):
    __tablename__ = 'execution_instance_event'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    execution_instance_event_key = Column(String)
    execution_instance_id = Column(Integer, ForeignKey('execution_instance.id'))
    executed_at = Column(String)

    execution_instance = relationship('ExecutionInstance')