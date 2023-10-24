import time
import requests
from confluent_kafka import Producer

# Kafka producer configuration
producer_config = {
    'bootstrap.servers': 'your_ip_adress:9092',  # Use your host machine's IP
    'client.id': 'weather-producer'
}

# Create a Kafka producer
producer = Producer(producer_config)

# OpenWeatherMap API configuration
api_key = 'your_api_key'
city = 'Rabat'  # Replace with the name of your city
weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

while True:
    try:
        response = requests.get(weather_url)
        data = response.json()

        # Extract temperature, wind, and precipitation data
        temperature = data['main']['temp']
        wind_speed = data['wind']['speed']
        precipitation = data.get('rain', 0)

        # Send the data to the Kafka topic
        producer.produce('weather-data-topic', key='weather', value=f'Temperature: {temperature}°C, Wind: {wind_speed} m/s, Precipitation: {precipitation} mm')

        # Wait for a while before fetching data again
        time.sleep(60)  # Fetch data every minute

    except Exception as e:
        print(f"Error: {e}")

# Clean up
producer.flush()
