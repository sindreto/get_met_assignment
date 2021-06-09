import unittest

import requests
import pandas as pd

from get_met import get_met


EXPECTED_COLUMNS = (
    'air_pressure_at_sea_level',
    'air_temperature',
    'cloud_area_fraction',
    'relative_humidity',
    'wind_from_direction',
    'wind_speed'
)


class TestGetMet(unittest.TestCase):

    def test_invalid_lat_lon(self):
        with self.assertRaises(requests.HTTPError):
            get_met(lat=1000, lon=1000)

    def test_successful_call(self):
        data = get_met(lat=58.934338, lon=5.7473823)

        # Check correct return type
        self.assertIsInstance(data, pd.DataFrame)

        # Check presence of data
        self.assertGreater(len(data.index), 0)

        # Check correct columns (order does not matter)
        for column in EXPECTED_COLUMNS:
            self.assertIn(column, data.columns)

        # Check correct index type
        self.assertIsInstance(data.index, pd.DatetimeIndex)

        # Check that the index is timezone aware
        self.assertIsNotNone(data.index.tz)


if __name__ == '__main__':
    unittest.main()
