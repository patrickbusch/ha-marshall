import datetime
import json
import logging
import requests

# from .error import SmartboxError

_MIN_TOKEN_LIFETIME = 1

_LOGGER = logging.getLogger(__name__)


class API(object):
    def __init__(self, address):
        self._address = address
        self._host = f"http://{self._address}/fsapi/"

    def get_device(self):
        #TODO response = self._api_request()
        return "DEVICE NAME xyz"