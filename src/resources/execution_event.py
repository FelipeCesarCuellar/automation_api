import falcon
import logging

from controllers.execution_event import ExecutionEventController
from exceptions import ClientException

class ExecutionEventResource(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def on_get_list(self, req, resp):
        self.logger.info(f'Retrieving all execution events')
        try:
            execution_event_controller = ExecutionEventController(req.context.db_session)
            response = execution_event_controller.retrieve_all_execution_events()
        except ClientException as x:
            resp.media = x.get()
            resp.status = x.http_status()
            return
        
        resp.media = response
        resp.status = falcon.HTTP_200

    def on_get_by_key(self, req, resp, execution_event_key):
        self.logger.info(f'Retrieving execution event for execution_event key {execution_event_key}')
        
        try:
            execution_event_controller = ExecutionEventController(req.context.db_session)
            response = execution_event_controller.retrieve_execution_event_by_key(execution_event_key=execution_event_key)
        except ClientException as x:
            resp.media = x.get()
            resp.status = x.http_status()
            return
        
        resp.media = response
        resp.status = falcon.HTTP_200

    def on_delete_by_key(self, req, resp, execution_event_key):
        self.logger.info(f'Deleting execution event with execution event key {execution_event_key}')
        
        try:
            execution_event_controller = ExecutionEventController(req.context.db_session)
            response = execution_event_controller.delete_execution_event_by_key(execution_event_key=execution_event_key)
        except ClientException as x:
            resp.media = x.get()
            resp.status = x.http_status()
            return
        
        resp.media = response
        resp.status = falcon.HTTP_200
        
    def on_post(self, req, resp):
        self.logger.info(f'Posting execution event {req.media}')

        try:
            execution_event_controller = ExecutionEventController(req.context.db_session)
            response = execution_event_controller.create_new_execution_event(req.media)
        except ClientException as x:
            resp.media = x.get()
            resp.status = x.http_status()
            return
        
        resp.media = response
        resp.status = falcon.HTTP_200
