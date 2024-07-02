import falcon
import logging

from sqlalchemy.exc import NoResultFound

from exceptions import ClientException
from mappers.routine import RoutineMapper
from models.routine import Routine

class ExecutionController(object):
    def __init__(self, db_session):
        self.logger = logging.getLogger(__name__)
        self.db_session = db_session

    # TODO: Implement Controller