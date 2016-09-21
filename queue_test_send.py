import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='orders')

message = ' '.join(sys.argv[1:]) or 'a random order'
channel.basic_publish(exchange='', routing_key='orders',
                      body=message, properties=pika.BasicProperties(delivery_mode=2))
print(' [x] sent order')

connection.close()
