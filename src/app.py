
import falcon
import logging

from resources.health_check import HealthcheckResource

logging.basicConfig(format='%(process)d - [%(name)s] [%(levelname)s] %(message)s', level=logging.DEBUG)

api = falcon.App()

healthcheck_resource = HealthcheckResource()
api.add_route('/automation', healthcheck_resource)
api.add_route('/automation/{placeholder}', healthcheck_resource)