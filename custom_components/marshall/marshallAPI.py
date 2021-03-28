import datetime
import json
import logging
import requests
import xml.etree.ElementTree as ET

PIN = "1234"
OKAY_STATE = "FS_OK"

_LOGGER = logging.getLogger(__name__)
        # http://192.168.1.33/fsapi/GET_MULTIPLE?pin=1234&node=netremote.sys.info.friendlyname

class API(object):
    def __init__(self, address):
        _LOGGER.debug("init API")
        self._address = address
        self._host = f"http://{self._address}/fsapi/"

    def _api_get_multiple(self, nodes):
        url = f"{self._host}GET_MULTIPLE?pin={PIN}"
        for node in nodes:
            url += f"&node={node}"
        _LOGGER.debug(f"getting URL {url}")
        response = requests.get(url)
        response.raise_for_status()
        return self._parse_get_multiple_response(response)

    # def _api_set(self, node, value):
    #     url = f"{self._host}SET/{node}?pin={PIN}&value={value}"
    #     response = requests.get(url)
    #     response.raise_for_status()
    #     content = response.content
    #     return content

    # def _api_list_get_next(self, node, max_items):
    #     url = f"{self._host}LIST_GET_NEXT/{node}/-1?pin={PIN}&maxItems={max_items}"
    #     response = requests.get(url)
    #     response.raise_for_status()
    #     content = response.content
    #     return content

    def _parse_get_multiple_response(self, response):
        xml = ET.fromstring(response.content)

        _LOGGER.debug(f"xml {xml}")

        result_dict = {}
        
        for child in xml:
            self._parse_api_response(child, result_dict)

        _LOGGER.debug(result_dict)

        return result_dict

    def _parse_api_response(self, response, result_dict):
        _LOGGER.debug(response)
        node = response.find('node').text
        status = response.find('status').text

        if (status != OKAY_STATE):
            result_dict[node] = "ERROR"
        else:
            text = response.find('value')[0].text
            result_dict[node] = text  

# <fsapiGetMultipleResponse>
# <fsapiResponse>
# <node>netremote.sys.info.friendlyname</node>
# <status>FS_OK</status>
# <value><c8_array>Ricks Marshall Stanmore</c8_array></value>
# </fsapiResponse>
# </fsapiGetMultipleResponse>
