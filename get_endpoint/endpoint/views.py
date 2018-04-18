from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time
import uuid
import json
import requests
from circuitbreaker import circuit, CircuitBreakerMonitor
from requests import RequestException

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


@circuit(failure_threshold=5, recovery_timeout=5, expected_exception=RequestException)
def getDataFromAnalytics(request):
    return HttpResponse(requests.get('http://127.0.0.1:8000/getData').text)

def getCBStats(request):
    all_closed = CircuitBreakerMonitor.all_closed()
    html = "<h1> Circuit breaker Status: "

    if all_closed is False:
        html += "Open"
    else:
        html += "Closed"

    html += "</h1>"

    return HttpResponse(html)
