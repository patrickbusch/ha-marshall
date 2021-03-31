import asyncio
import logging

from datetime import datetime
from homeassistant.core import HomeAssistant
from .marshallAPI import API
from .marshallAPIValue import (
    SysInfoFriendlyname,
    SysPower,
    SysAudioVolume,
    SysAudioMute,
    SysNetWlanMacaddress,
    NavState,
    NavPresets,
    NavPresetCurrentpreset
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
            self._set_nav_state()
            self._list_presets()
            self._update_get_multiple()
            self._state['last_update'] = datetime.now()

        if (node in self._state.keys()):
            return self._state[node]
        else:
            return "ERROR"

    def _update_get_multiple(self):
        result = self._api._api_get_multiple([SysInfoFriendlyname, SysPower, SysAudioVolume, SysAudioMute, SysNetWlanMacaddress, NavPresetCurrentpreset])
        self._state.update(result)

    def _set_nav_state(self):
        self._api._api_set(NavState, 1)

    def _list_presets(self):
        result = self._api._api_list_get_next(NavPresets, 7)
        self._state['presets'] = result


    def get_name(self):
        return self._get_node(SysInfoFriendlyname)

    def get_mac_address(self):
        return self._get_node(SysNetWlanMacaddress)

    def get_power(self):
        return self._get_node(SysPower) == '1'

    def get_volume(self):
        steps = 33
        return round(float(self._get_node(SysAudioVolume)) / steps, 2)

    def get_mute(self):
        return self._get_node(SysAudioMute) == '1'

    def get_source(self):
        return 'SRC1'

    def get_sources(self):
        return self._state['presets']


    def get_state(self):        
        return {
            'power': self.get_power(),
            'name': self.get_name(),
            'volume': self.get_volume(),
            'mute': self.get_mute(),
            'sources': ['SRC1', 'SRC2'],
            'source': self.get_source(),
            'mac_address': self.get_mac_address(),
            'sources': self.get_sources()
        }
