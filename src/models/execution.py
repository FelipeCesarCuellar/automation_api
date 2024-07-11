from sqlalchemy import Column, Integer, String, ForeignKey, Time, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from models.base import Base

class Execution(Base):
    __tablename__ = 'execution'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    execution_key = Column(String)
    created_at = Column(DateTime)
    execution_data = Column(JSONB)
    routine_id = Column(Integer, ForeignKey('routine.id'))
    trigger_at = Column(Time)

    routine = relationship('Routine')