import datetime
import json
import logging
import requests

# from .error import SmartboxError

_MIN_TOKEN_LIFETIME = 1

_LOGGER = logging.getLogger(__name__)


class API(object):
    def __init__(self, address):
        _LOGGER.debug("init API")
        self._address = address
        self._host = f"http://{self._address}/fsapi/"

    def get_name(self):
        _LOGGER.debug("get_name called in api")
        return "DEVICE NAME xyz"
                #TODO response = self._api_request()