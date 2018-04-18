import pika
from multiprocessing import Process
from . import views

def on_request(channel, method_frame, header_frame, body):
    print('Response picked from queue...')
    views.writeToDB(body)

def one_time_startup():
    print('Listening to the queue')
    p = Process(target=start)
    p.start()

def start():
    print('Connection created...')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='eventStore')

    channel.basic_consume(on_request, queue='eventStore', no_ack=True)
    channel.start_consuming()
