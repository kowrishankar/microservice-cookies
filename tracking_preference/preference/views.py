from django.shortcuts import render
from .models import Account

# Create your views here.

def read(request):
    username = request.GET.get('username')
    model = Account.objects.filter(username=username)

    if model.count() is 0:
        return {
            ""
        }
    else:
        # cookie exists