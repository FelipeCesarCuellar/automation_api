from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from models.base import Base

class Routine(Base):
    __tablename__ = 'routine'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    routine_key = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    deactivated_on = Column(DateTime, nullable=True)