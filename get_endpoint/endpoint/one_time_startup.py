import pika
from multiprocessing import Process
from . import views

def on_request(channel, method_frame, header_frame, body):
    print('Request picked from queue...')
    responseBody = views.getEndpoint(body)

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='endpointResponses')

    channel.basic_publish(exchange='', routing_key='endpointResponses', body=responseBody)
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