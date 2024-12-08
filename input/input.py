from pandas import DataFrame
from settings import OPENWEATHER_API_KEY
from utils import constant_manager
from service.geolocation_service import get_city_coord
from matplotlib import pyplot as plt

def create_cities_list() -> list:
    constants = constant_manager.ConstantManager()
    cities = constants.DEFAULT_CITIES

    #Ask input to the user to add/remove cities and add or remove values to fetch
    while True:
        print("Current List of cities to fetch data about:")

        for i in range(len(cities)):
            print(cities[i]["City"])

        print("\nAdd/Remove cities from the list")
        print("1 - Add")
        print("2 - Remove")
        print("3 - Done")

        user_input = input("Enter your choice: ")
        if user_input == "1":
            if(OPENWEATHER_API_KEY == None):
                print("Openweather API Key is not defined")
                continue

            user_input = input("Enter the name / postal code of the city to add: ")
            try:
                city_name, lat, lon = get_city_coord(user_input)
                cities.append({"City": city_name, "Latitude": lat, "Longitude": lon})
            except:
                print("Error trying to fetch the city coordinates, try again later")
                continue

        elif user_input == "2":
            city_name = input("Enter the name of the city to remove: ")
            cities = [city for city in cities if city["City"] != city_name]

        elif user_input == "3":
            return cities

def create_params_list() -> list:
    constants = constant_manager.ConstantManager()

    #Ask input to the user to add/remove cities and add or remove values to fetch
    param_selection = {
        "1": {"name": constants.TEMPERATURE, "selected": True},
        "2": {"name": constants.HUMIDITY, "selected": True},
        "3": {"name": constants.WIND_SPEED, "selected": True}
    }

    while True:
        print("\nSelect/Deselect the values you are interested in:")
        for key, value in param_selection.items():
            checkbox = "[X]" if value["selected"] else "[ ]"
            print(f"{key} - {checkbox} {value['name']}")
        print("4 - Done")

        choice = input("Enter your choice (1-4): ")
        if choice in ["1", "2", "3"]:
            param_selection[choice]["selected"] = not param_selection[choice]["selected"]
        elif choice == "4":
            # Update hourly_params based on selections
            return [details["name"] for _, details in param_selection.items() if details["selected"]]

def add_aditional_fields(weather_data: DataFrame) -> DataFrame:
    constants = constant_manager.ConstantManager()

    if constants.CSV_TEMP_CELSIUS in weather_data.columns:
        choice = input("Do you want to see the temperature measured in Farenheit? \n 1 - Yes \n 2 - No \n")

        if choice == "1":
            print("Added Farenheit")
            weather_data[constants.CSV_TEMP_FARENHEIT] = weather_data[constants.CSV_TEMP_CELSIUS].map(lambda c : format(((c * 1.8) + 32), ".2f"))

    if constants.CSV_WS_KM_H in weather_data.columns:
        choice = input("Do you want to see the wind speed measured in Miles/H? \n 1 - Yes \n 2 - No \n")

        if choice == "1":
            print("Added Windspeed")
            weather_data[constants.CSV_WS_MPH] = weather_data[constants.CSV_WS_KM_H].map(lambda s: format(s * 0.62137, ".2f"))

    return weather_data

def show_graph(weather_data: DataFrame):
    constants = constant_manager.ConstantManager()

    option = input(f"What data do you want to see? \n 1 - {constants.CSV_TEMP_CELSIUS} \n 2 - {constants.CSV_WS_KM_H} \n 3 - {constants.HUMIDITY}\n")

    if option == "1":
        option = constants.CSV_TEMP_CELSIUS
    elif option == "2":
        option = constants.CSV_WS_KM_H
    elif option == "3":
        option = constants.CSV_HUMIDITY

    weather_data.plot(kind= "bar", x= "location_id", y= option)

    plt.style.use('_mpl-gallery')

    plt.show()

def handle_options(weather_data: DataFrame):
    while True:
        option = input("Choose an option \n 1 - Show data graphs \n 2 - Exit\n")
        if option == "1":
            show_graph(weather_data)
        if option == "2":
            break
