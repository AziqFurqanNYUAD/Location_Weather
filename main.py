import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Replace with your actual API keys
IP2LOCATION_API_KEY = os.getenv("ip2_apikey")
WEATHER_API_KEY = os.getenv("weather_apikey")


# Function to get the user's public IP address
def get_user_ip():
    url = "https://api.ipify.org?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        ip_data = response.json()
        return ip_data.get("ip")
    else:
        print("Error fetching IP address.")
        return None

# Function to get geolocation details from IP2Location API
def get_geolocation(ip_address):
    url = f"https://api.ip2location.io/?key={IP2LOCATION_API_KEY}&ip={ip_address}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = {
            "city": data.get("city_name"),
            "country": data.get("country_name"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
        }
        return location
    else:
        print("Error fetching geolocation data.")
        return None

# Function to get weather details from WeatherAPI
def get_weather_data(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "temperature": data["current"]["temp_c"],  # Temperature in Celsius
            "humidity": data["current"]["humidity"],  # Humidity in percentage
            "condition": data["current"]["condition"]["text"],  # Weather condition description
        }
        return weather
    else:
        print("Error fetching weather data.")
        return None

# Main function to get both geolocation and weather details
def main():
    ip_address = get_user_ip()
    if ip_address:
        print(f"User's IP Address: {ip_address}")

        # Get geolocation
        location = get_geolocation(ip_address)
        if location:
            print(f"Geolocation Data for IP: {ip_address}")
            print(f"City: {location['city']}, Country: {location['country']}")
            print(f"Latitude: {location['latitude']}, Longitude: {location['longitude']}")

            # Get weather data
            weather = get_weather_data(location['city'])
            if weather:
                print(f"\nWeather Information for {location['city']}:")
                print(f"Temperature: {weather['temperature']}°C")
                print(f"Humidity: {weather['humidity']}%")
                print(f"Condition: {weather['condition']}")
            else:
                print("Unable to fetch weather data.")
        else:
            print("Unable to fetch geolocation data.")
    else:
        print("Unable to fetch user IP address.")

# Run the main function
main()
