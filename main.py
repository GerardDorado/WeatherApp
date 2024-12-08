import pandas as pd
import io
from input.input import add_aditional_fields, create_cities_list, create_params_list
from service.weather_service import fetch_weather_data

#Ask the user to create the list of cities
cities = create_cities_list()

#Ask the user to add the parameters that is interested about
hourly_params = create_params_list()

#Get the data from the OpenMeteo API
response_data = fetch_weather_data(cities, hourly_params)

#Create the DataFrame from the data
weather_data = pd.read_csv(io.StringIO(response_data), usecols= lambda x: x != "time")

#Replace the cities id with the cities names
weather_data["location_id"] = weather_data["location_id"].map(lambda id: cities[id]["City"] )

#Ask the user to create additional fields (Temperature in F or Wind speed in MPH)
weather_data = add_aditional_fields(weather_data)

#Create a CSV file from the DataFrame
weather_data.to_csv("weather_data.csv", index=False)
print("CSV created")

#Prints the Dataframe
print(weather_data)
