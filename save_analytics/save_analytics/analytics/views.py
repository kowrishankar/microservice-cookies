import time

from django.shortcuts import render
from django.http import HttpResponse
from .models import ClickEvent
import requests
import json
import pika

# Create your views here.
def sendClick(request):
    print('Connection created...')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='endpointRequests')

    clickUrl = request.POST.get('clickUrl')

    body = {
        'ip_address': 'janine',
        'time': time.time(),
        'click_url': clickUrl
    }

    channel.basic_publish(exchange='', routing_key='endpointRequests', body=json.dumps(body))
    connection.close()
    print('Message published...')

    return HttpResponse('analytic event broadcast')


def writeToDB(body):
    endpointPayloadData = json.loads(body)

    print(endpointPayloadData)

    endpoint = endpointPayloadData['endpoint']
    epoch = endpointPayloadData['epoch']
    id = endpointPayloadData['id']
    time = endpointPayloadData['time']
    click_url = endpointPayloadData['click_url']

    ce = ClickEvent(click_url=click_url, endpoint=endpoint, epoch=epoch, uuid=id, time=time)
    ce.save()

    print('Written to DB...')

def getData(request):
    return HttpResponse(ClickEvent.objects.all().values())
