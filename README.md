# weather-streaming-kafka

# Kafka Docker Setup with Python Producer and Consumer

## Prerequisites

- Docker installed on your machine.
- OpenWeatherMap API key. You can obtain one by signing up at [OpenWeatherMap](https://openweathermap.org/api) and generating an API key.

## Instructions

### 1. Project Directory Setup

Organize your project directory as follows:

```bash
weather-data-streaming-project/
│
├── python/
│   ├── producer.py
│   ├── consumer.py
└── docker-compose.yml
```

### 2. Docker Compose Setup

Update your `docker-compose.yml` file to configure the Kafka container and ensure the Python code files are properly mounted in the containers:

```bash
version: '3'

services:
  zookeeper:
    image: wurstmeister/zookeeper
    container_name: zookeeper
    ports:
      - "2181:2181"

  kafka:
    image: wurstmeister/kafka
    container_name: kafka
    ports:
      - "your_ip_adress:9092:9092"
    environment:
      KAFKA_ADVERTISED_HOST_NAME: your_ip_adress
      KAFKA_ADVERTISED_PORT: 9092
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
    volumes:
      - ./python:/app
```
### 3. Start Docker Containers

Run the following command in the project directory to start the Kafka and Zookeeper containers:

```bash
docker-compose up -d
```
### 4. Access Kafka Container

To install Python, the 'requests' module, and configure your OpenWeatherMap API key, access the Kafka container:

```bash
docker exec -it kafka /bin/sh
```
### 5.  Install Python, 'requests', 'confluent_kafka' and Configure API Key

Inside the Kafka container, install Python, the 'requests' module, and set your OpenWeatherMap API key:

```bash
apt update
apt add python3
pip install requests
pip install confluent_kafka
export OPENWEATHERMAP_API_KEY=your_api_key_here
```

Replace your_api_key_here with your actual OpenWeatherMap API key.

### 6. Run Python Scripts

Exit the Kafka container's shell:

```bash
exit
```
Now, you can run your Python producer and consumer scripts:

```bash
docker exec -it kafka python3 /app/producer.py
docker exec -it kafka python3 /app/consumer.py
```
### 7. Observing Output

The producer will fetch weather data from OpenWeatherMap using your API key and send it to the Kafka topic. The consumer will read and print the messages.

That's it! Your Kafka producer and consumer are now running inside Docker containers and interacting with your Kafka cluster, fetching weather data from OpenWeatherMap.

<img width="534" alt="Capture" src="https://github.com/aybstain/weather-streaming-kafka/assets/103702856/9ac70b69-bd4f-4514-b069-c11659a48450">

<img width="545" alt="Capture1" src="https://github.com/aybstain/weather-streaming-kafka/assets/103702856/6f19ed85-62e5-4536-ad76-ec628bf61d87">















