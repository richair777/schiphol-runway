"""Support for Schiphol Runway sensors."""
import urllib.request
from lxml import html
from datetime import timedelta

from homeassistant.helpers.entity import Entity

DOMAIN_DATA = "runway_data"

RUNWAY_TYPES = {
    "landing_runway": ["Landing Runway", None],
    "takeoff_runway": ["Take-off Runway", None],
}

# from homeassistant.helpers.event import async_track_time_interval

SCAN_INTERVAL = timedelta(minutes=1)


def setup_platform(hass, config, add_entities, discovery_info=None):
    rwydata = RunwayData(hass)
    # sensor = [RunwaySensor(rwydata)]
    # add_entities(sensor, True)
    add_entities(
        [
            RunwaySensor("Landing Runway", "landing"),
            RunwaySensor("Take-off Runway", "take-off"),
        ]
    )


class RunwaySensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, name, selector):
        """Initialize the sensor."""
        self._state = 'updating'
        # variable_info = RUNWAY_TYPES[condition]
        # self._condition_name = variable_info[0]
        self._name = name
        self._selector = selector
        # self.rwydata = rwydata

    @property
    def name(self):
        """Return the name of the sensor."""

        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def extract_runway(runway_list, runway_config):
        runway_config = self._selector
        rwy_selector0 = "" + runway_config
        rwy_selector1 = " " + runway_config
        rwy_selector2 = "-" + runway_config

        landing_element = [i for i in runway_list if rwy_selector0 in i]
        takeoff_element = [i for i in runway_list if rwy_selector0 in i]

        split1 = landing_element[0].split("airstrip-")
        split2a = split1[0].split(rwy_selector1)
        split2b = split1[1].split(rwy_selector2)

        rwy = [0, 0]
        rwy_nr = split2b[0]
        rwy_name = split2a[0]
        rwy[0] = rwy_nr
        rwy[1] = rwy_name

        runway_nr = rwy[0]

        return runway_nr

    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        # website to get the runways from
        runway_url = "http://www.lvnl.nl/nl/airtraffic"

        text = urllib.request.urlopen(runway_url).read().decode("utf8")
        htmltree = html.fromstring(text)
        runway_list = htmltree.xpath("//g/@class")

        runway_config = self._selector
        rwy_selector0 = "" + runway_config
        rwy_selector1 = " " + runway_config
        rwy_selector2 = "-" + runway_config

        landing_element = [i for i in runway_list if rwy_selector0 in i]
        takeoff_element = [i for i in runway_list if rwy_selector0 in i]

        split1 = landing_element[0].split("airstrip-")
        split2a = split1[0].split(rwy_selector1)
        split2b = split1[1].split(rwy_selector2)

        rwy = [0, 0]
        rwy_nr = split2b[0]
        rwy_name = split2a[0]
        rwy[0] = rwy_nr
        rwy[1] = rwy_name

        runway_nr = rwy[0]

        # l_rwy = extract_runway(runway_list,"landing")

        self._state = runway_nr
        # self.rwydata.update()
        # self._state = self.hass.rwydata
        # self._state = self._state + 1


class RunwayData:
    def __init__(self, hass):
        """Initialize the data object."""
        self.hass = hass

    def update(self):
        new_rwy_data = [88, 99]
        self.hass.rwydata = new_rwy_data
