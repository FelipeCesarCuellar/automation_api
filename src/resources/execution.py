import falcon
import logging

from controllers.execution import ExecutionController
from exceptions import ClientException

class ExecutionResource(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def on_get_list(self, req, resp):
        self.logger.info(f'Retrieving all executions')
        try:
            execution_controller = ExecutionController(req.context.db_session)
            response = execution_controller.retrieve_all_executions()
        except ClientException as x:
            resp.media = x.get()
            resp.status = x.http_status()
            return
        
        resp.media = response
        resp.status = falcon.HTTP_200

    def on_get_by_key(self, req, resp, execution_key):
        self.logger.info(f'Retrieving execution for execution key {execution_key}')
        
        try:
            execution_controller = ExecutionController(req.context.db_session)
            response = execution_controller.retrieve_execution_by_key(execution_key=execution_key)
        except ClientException as x:
            resp.media = x.get()
            resp.status = x.http_status()
            return
        
        resp.media = response
        resp.status = falcon.HTTP_200

    def on_delete_by_key(self, req, resp, execution_key):
        self.logger.info(f'Deleting execution with execution key {execution_key}')
        
        try:
            execution_controller = ExecutionController(req.context.db_session)
            response = execution_controller.delete_execution_by_key(execution_key=execution_key)
        except ClientException as x:
            resp.media = x.get()
            resp.status = x.http_status()
            return
        
        resp.media = response
        resp.status = falcon.HTTP_200
        
    def on_post(self, req, resp):
        self.logger.info(f'Posting execution event {req.media}')

        try:
            execution_controller = ExecutionController(req.context.db_session)
            response = execution_controller.create_new_execution(req.media)
        except ClientException as x:
            resp.media = x.get()
            resp.status = x.http_status()
            return
        
        resp.media = response
        resp.status = falcon.HTTP_200