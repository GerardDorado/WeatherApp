import datetime

from utils.constant_manager import ConstantManager

constants = ConstantManager()

def build(params) -> str:
    url = "https://api.open-meteo.com/v1/forecast?"
    url = url + cities_params(params[constants.CITIES]) + date_params() + hourly_params(params[constants.HOURLY_PARAMS]) + "&format=csv"

    return url

def cities_params(cities) -> str:
    latitude = "&latitude="
    longitude = "&longitude="

    for city in cities:
        latitude = latitude + f"{city["Latitude"]},"
        longitude = longitude + f"{city["Longitude"]},"

    return latitude + longitude

def date_params(date = datetime.datetime.now()) -> str:
    iso_date = datetime.datetime.now().replace(microsecond=0).isoformat()
    return f"&start_hour={iso_date}&end_hour={iso_date}"

def hourly_params(params) -> str:

    return_str = ""
    for param in params:
        return_str = return_str + f"&hourly={param}"

    return return_str
