import logging

from homeassistant.components.media_player.const import (
    MEDIA_TYPE_MUSIC,
    SUPPORT_PAUSE,
    SUPPORT_PLAY,
    SUPPORT_PLAY_MEDIA,
    SUPPORT_SELECT_SOURCE,
    SUPPORT_STOP,
    SUPPORT_VOLUME_MUTE,
    SUPPORT_VOLUME_SET,
)
from homeassistant.const import (
    STATE_OFF,
    STATE_PAUSED,
    STATE_PLAYING,
    STATE_STANDBY,
    STATE_IDLE
)
from homeassistant.components.media_player import MediaPlayerEntity
from datetime import timedelta

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(seconds=5)

SUPPORT_MARSHALL = (
    SUPPORT_VOLUME_MUTE
    | SUPPORT_VOLUME_SET
    | SUPPORT_PAUSE
    | SUPPORT_PLAY
    | SUPPORT_SELECT_SOURCE
)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the media player platform."""
    _LOGGER.debug("Initializing media player platform")
    add_entities([MarshallPlayer()])


class MarshallPlayer(MediaPlayerEntity):

    def __init__(self):
        """Initialize the media player."""
        self._state = {
            'power': False,
            'name': "Marshall",
            'volume': 0,
            'mute': False,
            'artist': None,
            'title': None,
            'state': None,
            'sources': [''],
            'source': '',
            'mac_address': '',
            'play_status': 0
        }

    @property
    def supported_features(self):
        return SUPPORT_MARSHALL

    @property
    def media_content_type(self):
        return MEDIA_TYPE_MUSIC

    @property
    def device_class(self):
        return 'speaker'

    @property
    def unique_id(self):
        return self._state['mac_address']

    @property
    def name(self):
        return self._state['name']

    @property
    def state(self):
        """ Exception is off """
        if self._state['power']:
            if self._state['play_state'] == '2':
                return STATE_PLAYING
            elif self._state['play_state'] == '3':
                return STATE_PAUSED
            else:
                return STATE_IDLE
        else:
            return STATE_STANDBY

    @property
    def volume_level(self):
        return self._state['volume']

    @property
    def is_volume_muted(self):
        return self._state['mute']

    @property
    def source(self):
        return self._state['source']

    @property
    def source_list(self):
        return self._state['sources']

    @property
    def media_artist(self):
        return self._state['artist']

    @property
    def media_title(self):
        return self._state['title']

    def media_play(self):
        """Send play command."""
        self.hass.data[DOMAIN]['device'].set_play()
        self._state['play_state'] = '2'

    def media_pause(self):
        """Send pause command."""
        self.hass.data[DOMAIN]['device'].set_pause()
        self._state['play_state'] = '3'

    def media_stop(self):
        """Send pause command."""
        self.hass.data[DOMAIN]['device'].set_stop()
        self._state['play_state'] = '0'

    # def media_previous_track(self):
    #     """Send previous track command."""
    #     self.hass.data[DOMAIN]['device'].set_prev_track()
    #     self.update()

    # def media_next_track(self):        
    #     """Send next track command."""
    #     self.hass.data[DOMAIN]['device'].set_next_track()
    #     self.update()

    def select_source(self, source):
        """Select input source."""
        self.hass.data[DOMAIN]['device'].set_source(source)
        self._state['source'] = source
        self._state['play_state'] = '2'

    def set_volume_level(self, volume):
        self.hass.data[DOMAIN]['device'].set_volume(volume)
        self._state['volume'] = volume

    def update(self):
        """Fetch new state data for the media player.
        This is the only method that should fetch new data for Home Assistant.
        """
        self._state = self.hass.data[DOMAIN]['device'].get_state()
