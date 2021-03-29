import asyncio
import logging

from datetime import datetime
from homeassistant.core import HomeAssistant
from .marshallAPI import API
from .marshallAPIValue import (
    SysInfoFriendlyname,
    SysPower,
    SysAudioVolume,
    SysAudioMute
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

        if (update_needed): 
            self._update()

        if (node in self._state.keys()):
            return self._state[node]
        else:
            return "ERROR"

    def _update(self):
        result = self._api._api_get_multiple([SysInfoFriendlyname, SysPower, SysAudioVolume, SysAudioMute])
        result['last_update'] = datetime.now()
        self._state.update(result)

    def get_name(self):
        return self._get_node(SysInfoFriendlyname)

    def get_power(self):
        return self._get_node(SysPower) == '1'

    def get_volume(self):
        steps = 33
        return round(float(self._get_node(SysAudioVolume)) / steps, 2)

    def get_mute(self):
        return self._get_node(SysAudioMute) == '1'

    def get_state(self):        
        return {
            'power': self.get_power(),
            'name': self.get_name(),
            'volume': self.get_volume(),
            'mute': self.get_mute()
        }
