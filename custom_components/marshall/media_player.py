import logging

from homeassistant.components.media_player.const import (
    MEDIA_TYPE_MUSIC,
    SUPPORT_NEXT_TRACK,
    SUPPORT_PAUSE,
    SUPPORT_PLAY,
    SUPPORT_PLAY_MEDIA,
    SUPPORT_PREVIOUS_TRACK,
    SUPPORT_SELECT_SOURCE,
    SUPPORT_SHUFFLE_SET,
    SUPPORT_STOP,
    SUPPORT_TURN_OFF,
    SUPPORT_TURN_ON,
    SUPPORT_VOLUME_MUTE,
    SUPPORT_VOLUME_SET,
)
from homeassistant.components.media_player import MediaPlayerEntity
from datetime import timedelta

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(seconds=30)

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
            'sources': ['SRC1', 'SRC2'],
            'source': 'SRC1'
        }

    @property
    def supported_features(self):
        return (SUPPORT_VOLUME_MUTE | SUPPORT_VOLUME_SET | SUPPORT_PAUSE | SUPPORT_PLAY | SUPPORT_PREVIOUS_TRACK | SUPPORT_NEXT_TRACK | SUPPORT_SELECT_SOURCE)

    @property
    def media_content_type(self):
        return MEDIA_TYPE_MUSIC

    # @property
    # def media_content_type(self):
    #     """Return the content type of current playing media."""
    #     if self.state in [STATE_PLAYING, STATE_PAUSED]:
    #         return MEDIA_TYPE_MUSIC
    #     return STATE_STANDBY

    @property
    def device_class(self):
        return 'speaker'

    @property
    def name(self):
        return self._state['name']

    @property
    def is_on(self):
        return self._state['power']

    @property
    def volume_level(self):
        return self._state['volume']

    @property
    def is_volume_muted(self):
        return self._state['mute']

    # @property
    # def source(self):
    #     """Name of the current input source."""
    #     return None

    # @property
    # def source_list(self):
    #     """List of available input sources."""
    #     return self._source_list

    # @property
    # def state(self):
    #     """Return the state of the device."""
    #     if not self.available:
    #         return STATE_UNAVAILABLE
    #     if self._media_player_state == "PLAYING":
    #         return STATE_PLAYING
    #     if self._media_player_state == "PAUSED":
    #         return STATE_PAUSED
    #     if self._media_player_state == "IDLE":
    #         return STATE_IDLE
    #     return STATE_STANDBY

    # @property
    # def media_artist(self):
    #     """Return the artist of current playing media, music track only."""
    #     return self._media_artist

    # @property
    # def media_title(self):
    #     """Return the title of current playing media."""
    #     return self._media_title
    # None

    # def media_play(self):
    #     """Send play command."""
    #     raise NotImplementedError()

    # def media_pause(self):
    #     """Send pause command."""
    #     raise NotImplementedError()

    # def media_previous_track(self):
    #     """Send previous track command."""
    #     raise NotImplementedError()

    # def media_next_track(self):
    #     """Send next track command."""
    #     raise NotImplementedError()

    # def select_source(self, source):
    #     """Select input source."""
    #     raise NotImplementedError()

    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        self._state = self.hass.data[DOMAIN]['device'].get_state()
