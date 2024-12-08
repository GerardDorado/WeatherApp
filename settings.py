import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

OPENWEATHER_API_KEY=os.environ.get("OPENWEATHER_API_KEY")
