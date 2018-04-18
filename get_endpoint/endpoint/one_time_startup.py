import pika
from multiprocessing import Process
from . import views

def on_request(channel, method_frame, header_frame, body):
    print('Request picked from queue...')
    responseBody = views.getEndpoint(body)

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='endpointResponses')
    channel.queue_declare(queue='eventStore')

    channel.exchange_declare(exchange='gareth', exchange_type='fanout')

    channel.queue_bind('endpointResponses', 'gareth')
    channel.queue_bind('eventStore', 'gareth')

    channel.basic_publish(exchange='gareth', body=responseBody, routing_key='')
    connection.close()
    print('Response Message published...')

def one_time_startup():
    print('Listening to the queue')
    p = Process(target=start)
    p.start()

def start():
    print('Connection created...')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='endpointRequests')

    channel.basic_consume(on_request, queue='endpointRequests', no_ack=True)
    channel.start_consuming()