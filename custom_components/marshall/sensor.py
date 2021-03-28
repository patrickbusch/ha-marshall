import logging

from homeassistant.helpers.entity import Entity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    _LOGGER.debug("Initializing sensor platform")
    add_entities([MarshallInputSensor("")])


class MarshallInputSensor(Entity):

    def __init__(self, data):
        """Initialize the sensor."""
        _LOGGER.debug("Initializing Marshall input sensor")
        self._data = data
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Marshall Device Name'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        # http://192.168.1.33/fsapi/GET_MULTIPLE?pin=1234&node=netremote.sys.info.friendlyname
        self._state = self.hass.data[DOMAIN]['address']