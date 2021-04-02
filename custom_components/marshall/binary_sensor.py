import logging

from homeassistant.components.binary_sensor import BinarySensorEntity
from datetime import timedelta

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(seconds=5)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the binary sensor platform."""
    _LOGGER.debug("Initializing binary sensor platform")
    add_entities([MarshallPowerSensor()])


class MarshallPowerSensor(BinarySensorEntity):

    def __init__(self):
        """Initialize the sensor."""
        self._state = False

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Marshall Power State'

    @property
    def is_on(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_class(self):
        """Return the class of the sensor."""
        return 'power'

    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        self._state = self.hass.data[DOMAIN]['device'].get_power()
