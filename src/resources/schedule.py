import falcon
import logging

from controllers.schedule import ScheduleController
from exceptions import ClientException

class ScheduleResource(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def on_put_run_execution(self, req, resp):
        self.logger.info(f'Running a single execution')
        try:
            schedule_controller = ScheduleController(req.context.db_session)
            response = schedule_controller.run_single_execution()
        except ClientException as x:
            resp.media = x.get()
            resp.status = x.http_status()
            return
        
        resp.media = response
        resp.status = falcon.HTTP_200