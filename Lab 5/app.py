import pika
import sys


host = "localhost"
port = 5672
credentials = pika.PlainCredentials("guest", "guest")

try:
    host = sys.argv[1]
    port = int(sys.argv[2])
    credentials = pika.PlainCredentials(sys.argv[3], sys.argv[4])
except IndexError:
    pass

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=port, credentials=credentials)
)
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
