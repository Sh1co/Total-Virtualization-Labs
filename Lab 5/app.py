# Inspired by : https://www.rabbitmq.com/tutorials/tutorial-three-python.html

import pika
import sys
import time


host = "localhost"
port = 5672
credentials = pika.PlainCredentials("guest", "guest")

try:
    host = sys.argv[1]
    port = int(sys.argv[2])
    credentials = pika.PlainCredentials(sys.argv[3], sys.argv[4])
except IndexError:
    pass
for i in range(5):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, port=port, credentials=credentials)
        )
    except pika.exceptions.AMQPConnectionError:
        print(f"Connect attempt #{i+1} failed, trying again in 5 secs.")
        time.sleep(5)
    else:
        break

channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange="logs", queue=queue_name)

print(" [*] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
