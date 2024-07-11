from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models.base import Base

class Routine(Base):
    __tablename__ = 'routine'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    routine_key = Column(String)
    created_at = Column(DateTime)
    deactivated_on = Column(DateTime)