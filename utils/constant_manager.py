class ConstantManager():
    #Constants related to the param map
    CITIES = "cities"
    HOURLY_PARAMS = "hourly_params"

    #Constants related to the "hourly" param type for the weather API
    HUMIDITY = "relative_humidity_2m"
    WIND_SPEED = "wind_speed_10m"
    TEMPERATURE = "temperature_2m"

    #Constants that represent the colums of the result data frame
    CSV_TEMP_CELSIUS = "temperature_2m (°C)"
    CSV_TEMP_FARENHEIT = "temperature_2m (°F)"
    CSV_WS_KM_H = "wind_speed_10m (km/h)"
    CSV_WS_MPH = "wind_speed_10m (mph)"

    DEFAULT_CITIES = [
     {"City": "New York", "Latitude": 40.7128, "Longitude": -74.0060},
     {"City": "Tokyo", "Latitude": 35.6895, "Longitude": 139.6917},
     {"City": "London", "Latitude": 51.5074, "Longitude": -0.1278},
     {"City": "Paris", "Latitude": 48.8566, "Longitude": 2.3522},
     {"City": "Berlin", "Latitude": 52.5200, "Longitude": 13.4050},
     {"City": "Sydney", "Latitude": -33.8688, "Longitude": 151.2093},
     {"City": "Mumbai", "Latitude": 19.0760, "Longitude": 72.8777},
     {"City": "Cape Town", "Latitude": -33.9249, "Longitude": 18.4241},
     {"City": "Moscow", "Latitude": 55.7558, "Longitude": 37.6173},
     {"City": "Rio de Janeiro", "Latitude": -22.9068, "Longitude": -43.1729}
    ]

    #Method to avoid modifying the attributes of this class
    def __setattr__(self, name, value):
        raise TypeError("Constants are immutable")
