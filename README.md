### A simple python application that retrieves weather data from a list of cities.

### How to run:
  - In a terminal run "python main.py"

### Pre-Requesites:
  - Python 3 or greater
  - matplotlib, pandas and dotenv modules installed
  - An openweather api key (Add it to the .env file)

### Functionality:
  - Fetches data from any city
  - Creates a csv file with different parameters specified by the user
  - Allows the user to display the data in a graph to compare the conditions of different cities

### Program structure:
The program has a basic structure of a main file that calls and coordinate the rest of the program

The basic structure is:

1. Build the list of cities: this calls (if needed) the geolocation_service.py that fetches the latitude and longitude of the new city to add or removes a city from the list
2. Fetch the data of the cities using the weather_service.py: this services calls the open-meteo api and fetches Wind Speed (KM/H), Temperature (Celsius) and Humidity (%)
3. Calculate more data: If the user wants, a column with the Temperature in Farenheit and the Wind Speed in MPH could be added, this columns are added doing a basic operation.
4. Write the data in a .csv File.
5. If the user wants, a graph could be displayed portraying the different fields.
