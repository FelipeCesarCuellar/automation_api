
import falcon
import logging

from constants import ENV_VARS
from middlewares.session_manager import SessionManager
from resources.health_check import HealthcheckResource
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


logging.basicConfig(format='%(process)d - [%(name)s] [%(levelname)s] %(message)s', level=logging.DEBUG)

engine = create_engine(("postgresql://" + ENV_VARS['DB_USER'] + ":" + ENV_VARS['DB_PASSWORD'] + "@" + ENV_VARS['DB_HOST'] + ":" + ENV_VARS['DB_PORT'] + "/" + ENV_VARS["DB_NAME"]),
                       echo=False, pool_size=5, max_overflow=2, connect_args={"options": "-c statement_timeout=120000"}, pool_pre_ping=True)

session_maker = sessionmaker(bind=engine)

api = falcon.App(middleware=[SessionManager(session_maker)])

healthcheck_resource = HealthcheckResource()
api.add_route('/automation', healthcheck_resource)
api.add_route('/automation/{placeholder}', healthcheck_resource)

api.add_route('/routine', routine_resource)