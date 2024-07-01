import falcon
import logging

from controllers.routine import RoutineController
from exceptions import ClientException

class RoutineResource(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def on_get_list(self, req, resp):
        self.logger.info(f'Retrieving all routines')
        try:
            routine_controller = RoutineController(req.context.db_session)
            response = routine_controller.retrieve_all_routines()
        except ClientException as x:
            resp.media = x.get()
            resp.status = x.http_status()
            return
        
        resp.media = response
        resp.status = falcon.HTTP_200

    def on_get_by_key(self, req, resp, routine_key):
        self.logger.info(f'Retrieving routine for routine key {routine_key}')
        
        try:
            routine_controller = RoutineController(req.context.db_session)
            response = routine_controller.retrieve_routine_by_key(routine_key=routine_key)
        except ClientException as x:
            resp.media = x.get()
            resp.status = x.http_status()
            return
        
        resp.media = response
        resp.status = falcon.HTTP_200

    def on_delete_by_key(self, req, resp, routine_key):
        self.logger.info(f'Deleting routine with routine key {routine_key}')
        
        try:
            routine_controller = RoutineController(req.context.db_session)
            response = routine_controller.delete_routine_by_key(routine_key=routine_key)
        except ClientException as x:
            resp.media = x.get()
            resp.status = x.http_status()
            return
        
        resp.media = response
        resp.status = falcon.HTTP_200
        
    def on_post(self, req, resp):
        self.logger.info(f'Posting routine {req.media}')

        try:
            routine_controller = RoutineController(req.context.db_session)
            response = routine_controller.create_new_routine(req.media)
        except ClientException as x:
            resp.media = x.get()
            resp.status = x.http_status()
            return
        
        resp.media = response
        resp.status = falcon.HTTP_200

    