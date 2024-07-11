from datetime import datetime

import falcon
import logging

from sqlalchemy.exc import NoResultFound

from exceptions import ClientException

# from mappers.routine import RoutineMapper
# from models.routine import Routine

from mappers.execution_instance import ExecutionInstanceMapper
from mappers.execution_instance_event import ExecutionInstanceEventMapper

from models.execution_instance import ExecutionInstance

class ScheduleController(object):
    def __init__(self, db_session):
        self.logger = logging.getLogger(__name__)
        self.db_session = db_session

    # def build_routines(self):
    #     routines = self.db_session.query(Routine).filter(Routine.deactivated_on is None).all()

    def run_single_execution(self):
        execution_instance = self.db_session.query(ExecutionInstance).filter(ExecutionInstance.trigger_at <= datetime.now()).first()

        if execution_instance is None:
            raise ClientException(f'No execution to process', f'No execution to process at current time', falcon.HTTP_204)
        
        execution_instance.triggered_at = datetime.now()

        execution_instance_event_model = ExecutionInstanceEventMapper.toModel(execution_instance_event_source = {'execution_instance_id': execution_instance.id})

        self.db_session.add(execution_instance_event_model)
        self.db_session.commit()

        return ExecutionInstanceMapper.toDTO(execution_instance)