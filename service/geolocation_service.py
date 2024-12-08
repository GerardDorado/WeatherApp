import requests as rq

from settings import OPENWEATHER_API_KEY

def get_city_coord(input: str) -> tuple[str, float, float]:
    api_key = OPENWEATHER_API_KEY
    print(f"Getting Lat and Long from {input}")

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={input}&appid={api_key}"
    response = rq.get(url)

    if response.status_code != 200:
      raise Exception()

    data = response.json()

    return data[0]["name"], data[0]["lat"], data[0]["lon"]
