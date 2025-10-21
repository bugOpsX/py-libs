"""
Feature: Weather Information Module
Description:
Fetches current weather details (temperature, humidity, and description)
for a given city using the OpenWeatherMap API.
"""

import requests

API_URL = "https://api.openweathermap.org/data/2.5/weather"
# ⚠️ Replace this with your actual API key from https://openweathermap.org/api
API_KEY = "YOUR_API_KEY_HERE"


def get_weather(city_name):
    """
    Fetch current weather info for a given city.
    
    Returns:
        dict: {temperature (°C), humidity (%), description (str)} 
        or None if city not found.
    """
    try:
        params = {
            "q": city_name,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(API_URL, params=params)
        response.raise_for_status()

        data = response.json()
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].capitalize()
        }
        return weather_info

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"❌ City '{city_name}' not found.")
        else:
            print(f"❌ HTTP Error: {http_err}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Network Error: {e}")
        return None


if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    result = get_weather(city)
    if result:
        print(f"\n🌍 Weather in {result['city']}:")
        print(f"🌡 Temperature: {result['temperature']}°C")
        print(f"💧 Humidity: {result['humidity']}%")
        print(f"☁️ Description: {result['description']}")
