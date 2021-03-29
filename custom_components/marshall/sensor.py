import logging

from homeassistant.helpers.entity import Entity
from datetime import timedelta

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=1)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    _LOGGER.debug("Initializing sensor platform")
    add_entities([MarshallNameSensor(), MarshallVolumeSensor()])


class MarshallNameSensor(Entity):

    def __init__(self):
        """Initialize the sensor."""
        # _LOGGER.debug("Initializing Marshall input sensor")
        self._state = 0

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
        self._state = self.hass.data[DOMAIN]['device'].get_name()


class MarshallVolumeSensor(Entity):

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Marshall Volume'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        self._state = self.hass.data[DOMAIN]['device'].get_volume()