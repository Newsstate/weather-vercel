from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
import os

app = FastAPI()

# Get API key from environment variable
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "YOUR_API_KEY_HERE")

@app.get("/weather")
def get_weather(city: str = "Delhi"):
    """
    Fetch live weather data from WeatherAPI.com
    Example: /weather?city=London
    """
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"
    
    try:
        response = requests.get(url)
        data = response.json()
        return JSONResponse(content=data)
    except Exception as e:
        return {"error": str(e)}
