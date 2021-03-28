import asyncio
import logging

from datetime import (
    datetime,
    timedelta
)
from homeassistant.core import HomeAssistant
from .const import MIN_TIME_BETWEEN_UPDATES
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
        self._state = {}
        self._state['last_update'] = datetime.now()

    def _get_node(self, node):
        update_needed = False
        _LOGGER.debug(self._state.keys())
        if (node not in self._state.keys()):
            update_needed = True
        if (self._state['last_update'] + MIN_TIME_BETWEEN_UPDATES < datetime.now()):
            update_needed = True

        if (update_needed): 
            self._update()

        if (node in self._state.keys()):
            return self._state[node]
        else:
            return "ERROR"
    
    def _update(self):
        result = self._api._api_get_multiple(SysInfoFriendlyname)
        result['last_update'] = datetime.now()
        self._state.update(result)

    def get_name(self):
        _LOGGER.debug("get_name called")
        return self._get_node(SysInfoFriendlyname)
