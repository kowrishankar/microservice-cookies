from django.shortcuts import render
from .models import ClickEvent
import json
from django.http import HttpResponse
from django.core import serializers

# Create your views here.


def writeToDB(body):
    print('Writing to Event Store DB...')
    endpointPayloadData = json.loads(body)

    print(endpointPayloadData)

    endpoint = endpointPayloadData['endpoint']
    epoch = endpointPayloadData['epoch']
    id = endpointPayloadData['id']
    time = endpointPayloadData['time']
    click_url = endpointPayloadData['click_url']

    ce = ClickEvent(click_url=click_url, endpoint=endpoint, epoch=epoch, uuid=id, time=time)
    ce.save()

    print('Written to EventStore...')

def getData(request):
    records = ClickEvent.objects.order_by('epoch')
    return HttpResponse(serializers.serialize('json', records))