from sqlalchemy import Column, Integer, String
from models.base import Base

class Routine(Base):
    __tablename__ = 'routine'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    routine_key = Column(String)
    created_at = Column(String)
    deactivated_on = Column(String)