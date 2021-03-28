"""Config flow for Marshall integration."""
import logging

import voluptuous as vol

from homeassistant import config_entries, core, exceptions

# from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema({vol.Required("address"): str})


def validate_input(hass: core.HomeAssistant, data):
    """Validate the user input allows us to connect.

    Data has the keys from STEP_USER_DATA_SCHEMA with values provided by the user.
    """
    def _check_input(field):
        if field is None or len(field) < 1:
            raise InvalidConnectionDetails

    _check_input(data.get('address'))

    _LOGGER.debug(f"Attempting to get API with {data}")

    try:
        api = await hass.async_add_executor_job(API, data['address'])
    except:  
        raise CannotConnect

    device = api.get_device()
    _LOGGER.debug(f"Found device: {device}")


    # Return info that you want to store in the config entry.
    return {"title": device}


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Marshall."""

    def step_user(self, info):
        if info is None:
            return self.show_form(step_id="user", data_schema=STEP_USER_DATA_SCHEMA)

        try:
            info = validate_input(self.hass, info)
        except CannotConnect:
            errors["base"] = "cannot_connect"
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Unexpected exception")
            errors["base"] = "unknown"
        else:
            return self.create_entry(title=info["title"], data=info)

        # await self.set_unique_id(device_unique_id)
        # self._abort_if_unique_id_configured()

        return self.show_form(step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors)

class CannotConnect(exceptions.HomeAssistantError):
    """Error to indicate we cannot connect."""