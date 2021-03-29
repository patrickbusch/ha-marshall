"""The Marshall integration."""
import logging

# import voluptuous as vol

# import homeassistant.helpers.config_validation as cv
# from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .marshallDevice import get_device

_LOGGER = logging.getLogger(__name__)

CONF_ADDRESSES = 'addresses'

PLATFORMS = ["binary_sensor", "sensor", "media_player"]

def setup(hass: HomeAssistant, config: dict):
    """Set up the Marshall component."""
    hass.data.setdefault(DOMAIN, {})

    _LOGGER.debug("Setting up Marshall integration")

    addresses_cfg = config[DOMAIN][CONF_ADDRESSES]
    _LOGGER.debug(f"addresses: {addresses_cfg}")

    for address in addresses_cfg:
        device = get_device(hass, address['address'])
        hass.data[DOMAIN] = {
            'device': device
        }
 
    for component in PLATFORMS:
        hass.helpers.discovery.load_platform(component, DOMAIN, {}, config)

    _LOGGER.debug("Finished setting up Marshall integration")

    return True


# async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
#     """Set up Marshall from a config entry."""
#     # TODO: implement
#     return False


# async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
#     """Unload a config entry."""
#     # TODO: implement
#     return False
