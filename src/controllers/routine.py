import falcon
import logging

from sqlalchemy.exc import NoResultFound

from exceptions import ClientException
from mappers.routine import RoutineMapper
from models.routine import Routine

class RoutineController(object):
  def __init__(self, db_session):
    self.logger = logging.getLogger(__name__)
    self.db_session = db_session
  
  def retrieve_routine_by_key(self, routine_key):
    try:
      routine = self.db_session.query(Routine).filter(Routine.routine_key == routine_key).one()
      
    except NoResultFound:
      raise ClientException(f'Routine not found', f'No routine found for routine key {routine_key}', falcon.HTTP_404)
      
    return RoutineMapper.toDTO(routine)