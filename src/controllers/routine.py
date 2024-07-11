import falcon
import logging

from sqlalchemy.exc import NoResultFound
from datetime import datetime

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

    def delete_routine_by_key(self, routine_key):
        try:
            routine = self.db_session.query(Routine).filter(Routine.routine_key == routine_key).one()
            
        except NoResultFound:
            raise ClientException(f'Routine not found', f'No routine found for routine key {routine_key}', falcon.HTTP_404)
            
        routine.deactivated_on = datetime.now()
        self.db_session.commit()

        return RoutineMapper.toDTO(routine)

    def retrieve_all_routines(self):
        routines = self.db_session.query(Routine).all()
            
        return [RoutineMapper.toDTO(routine) for routine in routines]

    def create_new_routine(self, routine_source):
        routine_model = RoutineMapper.toModel(routine_source)
        self.logger.info("Hi bro")
        self.db_session.add(routine_model)
        self.db_session.commit()

        return RoutineMapper.toDTO(routine_model)