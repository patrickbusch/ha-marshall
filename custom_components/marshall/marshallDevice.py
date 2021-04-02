import asyncio
import logging

from datetime import (
    datetime,
    timedelta
)
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
    NavPresetCurrentpreset,
    PlayStatus,
    PlayInfoArtist,
    PlayInfoName,
    NavActionSelectPreset,
    PlayControl
)

_LOGGER = logging.getLogger(__name__)
VOLUME_STEPS = 33

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

        if (self._state['last_update'] + timedelta(seconds=30) < datetime.now()):
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
        result = self._api._api_get_multiple([
            SysInfoFriendlyname, 
            SysPower, 
            SysAudioVolume, 
            SysAudioMute, 
            SysNetWlanMacaddress, 
            NavPresetCurrentpreset,
            PlayInfoArtist,
            PlayInfoName,
            PlayStatus
            ])
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
        return round(float(self._get_node(SysAudioVolume)) / VOLUME_STEPS, 2)

    def get_mute(self):
        return self._get_node(SysAudioMute) == '1'

    def get_source(self):
        source = int(self._get_node(NavPresetCurrentpreset))
        if source == 4294967295:
            return None
        elif source >= len(self._state['presets']):
            return None
        else:
            return self._state['presets'][int(source)]

    def get_sources(self):
        return self._state['presets']

    def get_title(self):
        return self._get_node(PlayInfoName)

    def get_artist(self):
        return self._get_node(PlayInfoArtist)

    def get_play_state(self):
        return self._get_node(PlayStatus)

    def set_next_track(self):
        self._api._api_set(PlayControl, 3)

    def set_prev_track(self):
        self._api._api_set(PlayControl, 4)

    def set_play(self):
        self._api._api_set(PlayControl, 0)

    def set_pause(self):
        self._api._api_set(PlayControl, 0)

    def set_stop(self):
        self._api._api_set(PlayControl, 0)

    def set_source(self, source):
        _LOGGER.debug(f"setting source to {source}")
        self._api._api_set(NavActionSelectPreset, self._state['presets'].index(source))

    def set_volume(self, volume):
        _LOGGER.debug(f"setting volume to {volume}")
        target = int(round(volume * VOLUME_STEPS, 0))
        self._api._api_set(SysAudioVolume, target)

    def get_state(self):        
        return {
            'power': self.get_power(),
            'name': self.get_name(),
            'volume': self.get_volume(),
            'mute': self.get_mute(),
            'sources': self.get_sources(),
            'mac_address': self.get_mac_address(),
            'artist': self.get_artist(),
            'title': self.get_title(),
            'play_state': self.get_play_state(),
            'source': self.get_source()
        }
