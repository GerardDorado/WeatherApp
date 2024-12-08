import requests as rq
from utils import url_builder, constant_manager

def fetch_weather_data(cities: list, hourly_params: list) -> str:
    constants = constant_manager.ConstantManager()
    params = {
        constants.CITIES: cities,
        constants.HOURLY_PARAMS: hourly_params
    }
    response = rq.get(url_builder.build(params))

    #Because the response is divided into multiple blocks, we split the response and read the second block (The one that contains the data we care about)
    return response.text.split("\n\n")[1]
