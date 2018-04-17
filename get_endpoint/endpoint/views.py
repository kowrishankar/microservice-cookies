from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time
import uuid
import json

def getEndpoint(body):
    messageBody = json.loads(body)
    ip_addr = messageBody['ip_address']
    country = getCountry(ip_addr)
    endpoint = getEndpointForCountry(country)
    epoch = time.time()
    string_time = datetime.datetime.fromtimestamp(epoch).strftime('%c')
    id = uuid.uuid4().__str__()
    click_url = messageBody['click_url']

    return json.dumps({"endpoint": endpoint, "epoch": epoch, "time": string_time, "id": id, "click_url": click_url})

def getCountry(ip_addr):
    return 'GB'

def getEndpointForCountry(country):
    return "https://"
