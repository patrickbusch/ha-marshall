import asyncio
import logging
import re

from homeassistant.core import HomeAssistant
from .marshallAPI import API

_LOGGER = logging.getLogger(__name__)

# _AWAY_STATUS_UPDATE_RE = re.compile(r'^/mgr/away_status')
# _NODE_STATUS_UPDATE_RE = re.compile(r'^/([^/]+)/(\d+)/status')


def get_device(hass: HomeAssistant, address):
    # api = hass.add_executor_job(API, address)
    return create_marshall_device(hass, address, API(address))

def create_marshall_device(hass, address, session):
    device = MarshallDevice(address, session)
    # await device.initialise_nodes(hass)
    return device


class MarshallDevice(object):
    def __init__(self, address, api):
        self._address = address
        self._api = api
