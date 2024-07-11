from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from models.base import Base

class ExecutionInstance(Base):
    __tablename__ = 'execution_instance'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    execution_instance_key = Column(String)
    execution_id = Column(Integer, ForeignKey('execution.id'))
    created_at = Column(DateTime)
    trigger_at = Column(DateTime)
    triggered_at = Column(DateTime)

    execution = relationship('Execution')