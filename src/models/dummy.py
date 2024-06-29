from sqlalchemy  import Column, Integer, String
from models.base import Base

class Dummy(Base):
    __tablename__ = 'dummy'

    id   = Column(Integer, primary_key=True)
    name = Column(String)