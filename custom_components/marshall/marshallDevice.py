import asyncio
import logging

from homeassistant.core import HomeAssistant
from .marshallAPI import API
from .marshallAPIValue import (
    SysInfoFriendlyname
)

_LOGGER = logging.getLogger(__name__)

def get_device(hass: HomeAssistant, address):
    return MarshallDevice(address, API(address))

class MarshallDevice(object):
    def __init__(self, address, api):
        _LOGGER.debug("init device")
        self._address = address
        self._api = api

    def get_name(self):
        _LOGGER.debug("get_name called")
        return self._api._api_get_multiple(SysInfoFriendlyname)
