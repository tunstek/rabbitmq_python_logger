import pika

# Basic listener from https://www.rabbitmq.com/tutorials/tutorial-five-python.html

rabbitmq_ip = '172.17.0.2'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_ip))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

binding_keys = ['logs.example.*']
for binding_key in binding_keys:
    channel.queue_bind(exchange='logs', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()