import falcon
import logging

from models.dummy import Dummy

class HealthcheckResource(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def on_get(self, req, resp, place_holder=""):
        self.logger.info("I'm Alive!")
        dummies = req.context.db_session.query(Dummy).all()
        for dummy in dummies:
            self.logger.info(dummy.name)
        resp.media = {
            "hello": "world!"
        }
        resp.status = falcon.HTTP_200