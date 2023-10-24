from confluent_kafka import Consumer, KafkaError

# Kafka consumer configuration
consumer_config = {
    'bootstrap.servers': 'your_ip_adress:9092',  # Use your host machine's IP
    'group.id': 'weather-consumer',
    'auto.offset.reset': 'earliest'
}

# Create a Kafka consumer
consumer = Consumer(consumer_config)

# Subscribe to the Kafka topic
consumer.subscribe(['weather-data-topic'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of partition')
        else:
            print('Error: {}'.format(msg.error()))
    else:
        print('Received message: {}'.format(msg.value()))

# Clean up
consumer.close()
