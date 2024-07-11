import falcon
import logging

from sqlalchemy.exc import NoResultFound

from exceptions import ClientException

from mappers.execution import ExecutionMapper

from models.routine import Routine
from models.execution import Execution

class ExecutionController(object):
    def __init__(self, db_session):
        self.logger = logging.getLogger(__name__)
        self.db_session = db_session

    def retrieve_execution_by_key(self, execution_key):
        try:
            execution = self.db_session.query(Execution).filter(Execution.execution_key == execution_key).one()
            
        except NoResultFound:
            raise ClientException(f'Execution not found', f'No execution found for execution key {execution_key}', falcon.HTTP_404)
            
        return ExecutionMapper.toDTO(execution)

    def delete_execution_by_key(self, execution_key):
        try:
            execution = self.db_session.query(Execution).filter(Execution.execution_key == execution_key).one()
            
        except NoResultFound:
            raise ClientException(f'Execution not found', f'No execution found for execution key {execution_key}', falcon.HTTP_404)
            
        self.db_session.delete(execution)
        self.db_session.commit()

        return

    def retrieve_all_executions(self):
        executions = self.db_session.query(Execution).all()
            
        return [ExecutionMapper.toDTO(execution) for execution in executions]

    def create_new_execution(self, execution_source):
        routine_model = self.db_session.query(Routine).filter(Routine.routine_key == execution_source['routine_key']).one()
        execution_source['routine_id'] = routine_model.id
        execution_model = ExecutionMapper.toModel(execution_source)

        self.db_session.add(execution_model)
        self.db_session.commit()

        return ExecutionMapper.toDTO(execution_model)