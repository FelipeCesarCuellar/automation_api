import falcon
import logging

class HealthcheckResource(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def on_get(self, req, resp, place_holder=""):
        self.logger.info("I'm Alive!")
        resp.media = {
            "hello": "world!"
        }
        resp.status = falcon.HTTP_200