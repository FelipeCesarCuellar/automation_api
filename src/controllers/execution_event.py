import falcon
import logging

from sqlalchemy.exc import NoResultFound

from exceptions import ClientException
from mappers.execution_event import ExecutionEventMapper
from models.execution_event import ExecutionEvent

class ExecutionEventController(object):
    def __init__(self, db_session):
        self.logger = logging.getLogger(__name__)
        self.db_session = db_session

    def retrieve_execution_event_by_key(self, execution_event_key):
        try:
            execution_event = self.db_session.query(ExecutionEvent).filter(ExecutionEvent.execution_event_key == execution_event_key).one()
            
        except NoResultFound:
            raise ClientException(f'ExecutionEvent not found', f'No execution_event found for execution_event key {execution_event_key}', falcon.HTTP_404)
            
        return ExecutionEventMapper.toDTO(execution_event)

    def delete_execution_event_by_key(self, execution_event_key):
        try:
            execution_event = self.db_session.query(ExecutionEvent).filter(ExecutionEvent.execution_event_key == execution_event_key).one()
            
        except NoResultFound:
            raise ClientException(f'ExecutionEvent not found', f'No execution_event found for execution_event key {execution_event_key}', falcon.HTTP_404)
            
        self.db_session.delete(execution_event)
        self.db_session.commit()

        return

    def retrieve_all_execution_events(self):
        execution_events = self.db_session.query(ExecutionEvent).all()
            
        return [ExecutionEventMapper.toDTO(execution_event) for execution_event in execution_events]

    def create_new_execution_event(self, execution_event_source):
        execution_event_model = ExecutionEventMapper.toModel(execution_event_source)

        self.db_session.add(execution_event_model)
        self.db_session.commit()

        return ExecutionEventMapper.toDTO(execution_event_model)