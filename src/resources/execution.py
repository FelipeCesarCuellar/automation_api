import falcon
import logging

from controllers.execution_event import ExecutionEventController
from exceptions import ClientException

class RoutineResource(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    # TODO: Implement Routes