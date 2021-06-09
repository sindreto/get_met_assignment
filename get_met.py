import requests
import pandas as pd


FORECAST_URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact"


def get_met(lat: float, lon: float) -> pd.DataFrame:
    """
    Retreive forecast from met.no weather API

    :param lat: Latitude of location
    :param lon: Longitude of location
    :return: DataFrame with weather parameters and datetime index
    """

    # Your code here
