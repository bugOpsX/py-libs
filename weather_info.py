import requests
import os
from typing import Optional, Dict, List
from dataclasses import dataclass
from datetime import datetime


@dataclass
class WeatherData:
    """Data class to represent weather information for a city."""
    city: str
    country: str
    temperature: float
    feels_like: float
    humidity: int
    description: str
    main: str
    pressure: int
    visibility: int
    wind_speed: float
    timestamp: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def __str__(self) -> str:
        """Format weather data for display."""
        temp_c = self.temperature
        feels_c = self.feels_like
        
        border = "═" * 50
        return f"""
┌{border}┐
│ 🌍 Weather in {self.city}, {self.country}
│ 📅 {self.timestamp}
│
│ 🌡️  Temperature: {temp_c:.1f}°C (feels like {feels_c:.1f}°C)
│ 💧 Humidity: {self.humidity}%
│ 📊 Pressure: {self.pressure} hPa
│ 👁️  Visibility: {self.visibility/1000:.1f} km
│ 💨 Wind Speed: {self.wind_speed} m/s
│
│ ☁️  {self.main}: {self.description.title()}
└{border}┘
"""


class WeatherFetcher:
    """Fetches weather information using OpenWeatherMap API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize WeatherFetcher with API key.
        
        Args:
            api_key: OpenWeatherMap API key. If not provided, will try to read from 
                    OPENWEATHER_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv('OPENWEATHER_API_KEY')
        
        if not self.api_key:
            raise ValueError(
                "API key is required."
            )
        
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        
    def get_weather(self, city: str) -> Optional[WeatherData]:
        """
        Get weather data for a city.
        
        Args:
            city: Name of the city
            
        Returns:
            WeatherData object with weather information, or None if failed
        """
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # Celsius
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            return WeatherData(
                city=data['name'],
                country=data['sys']['country'],
                temperature=data['main']['temp'],
                feels_like=data['main']['feels_like'],
                humidity=data['main']['humidity'],
                description=data['weather'][0]['description'],
                main=data['weather'][0]['main'],
                pressure=data['main']['pressure'],
                visibility=data.get('visibility', 10000),
                wind_speed=data['wind'].get('speed', 0)
            )
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                print("Invalid API key. Please check your OpenWeatherMap API key.")
            elif e.response.status_code == 404:
                print(f"City '{city}' not found.")
            else:
                print(f"HTTP error: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    
    def get_multiple_cities_weather(self, cities: List[str]) -> Dict[str, Optional[WeatherData]]:
        """Get weather for multiple cities."""
        results = {}
        for city in cities:
            results[city] = self.get_weather(city)
        return results


def display_weather(weather_data: WeatherData, style: str = "detailed") -> None:
    """
    Display weather data in different styles.
    
    Args:
        weather_data: WeatherData object
        style: Display style ('detailed', 'simple', 'minimal')
    """
    if style == "simple":
        print(f"\n🌍 {weather_data.city}: {weather_data.temperature:.1f}°C, {weather_data.description}")
        print(f"💧 Humidity: {weather_data.humidity}% | 💨 Wind: {weather_data.wind_speed} m/s\n")
        
    elif style == "minimal":
        print(f"{weather_data.city}: {weather_data.temperature:.1f}°C ({weather_data.description})")
        
    else:  # detailed
        print(weather_data)


def temperature_advice(temperature: float) -> str:
    """Give clothing advice based on temperature."""
    if temperature < 0:
        return "🧥❄️ It's freezing! Wear heavy winter clothes, coat, gloves, and warm boots."
    elif temperature < 10:
        return "🧥 It's cold! Wear a warm jacket, long pants, and closed shoes."
    elif temperature < 20:
        return "🧤 It's cool. A light jacket or sweater would be good."
    elif temperature < 25:
        return "👕 Pleasant weather! T-shirt and light pants are perfect."
    elif temperature < 30:
        return "☀️ It's warm! Light clothing, shorts, and stay hydrated."
    else:
        return "🔥🌡️ It's hot! Wear minimal light clothing, use sunscreen, and drink lots of water!"


if __name__ == "__main__":
    print("🌤️ Weather Information Library")
    print("\nThis is a library module and should be imported into your project.")
    print("\n� Usage example:")
    print("   from weather_info import WeatherFetcher")
    print("   fetcher = WeatherFetcher()  # Reads OPENWEATHER_API_KEY from environment")
    print("   weather = fetcher.get_weather('London')")
    print("   print(weather)")
    print("\n📋 Setup:")
    print("   1. Get free API key: https://openweathermap.org/api")
    print("   2. Set environment variable: OPENWEATHER_API_KEY=your_key_here")