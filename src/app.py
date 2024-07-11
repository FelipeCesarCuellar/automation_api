import falcon
import logging

from constants import ENV_VARS
from middlewares.session_manager import SessionManager
from resources.health_check import HealthcheckResource
from resources.routine import RoutineResource
from resources.execution import ExecutionResource
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from resources.schedule import ScheduleResource



logging.basicConfig(format='%(process)d - [%(name)s] [%(levelname)s] %(message)s', level=logging.DEBUG)

engine = create_engine(("postgresql://" + ENV_VARS['DB_USER'] + ":" + ENV_VARS['DB_PASSWORD'] + "@" + ENV_VARS['DB_HOST'] + ":" + ENV_VARS['DB_PORT'] + "/" + ENV_VARS["DB_NAME"]),
                       echo=False, pool_size=5, max_overflow=2, connect_args={"options": "-c statement_timeout=120000"}, pool_pre_ping=True)

session_maker = sessionmaker(bind=engine)

api = falcon.App(middleware=[SessionManager(session_maker)])

healthcheck_resource = HealthcheckResource()
api.add_route('/automation', healthcheck_resource)
api.add_route('/automation/{placeholder}', healthcheck_resource)

routine_resource = RoutineResource()
api.add_route('/automation/routine', routine_resource)
api.add_route('/automation/routines', routine_resource, suffix='list')
api.add_route('/automation/routine/{routine_key}', routine_resource, suffix='by_key')

execution_resource = ExecutionResource()
api.add_route('/automation/execution', execution_resource)
api.add_route('/automation/executions', execution_resource, suffix='list')
api.add_route('/automation/execution/{execution_key}', execution_resource, suffix='by_key')

schedule_resource = ScheduleResource()
api.add_route('/automation/schedule', schedule_resource, suffix='run_execution')