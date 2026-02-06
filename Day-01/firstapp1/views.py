from django.http import HttpResponse
from datetime import datetime


def hello(request):
    return HttpResponse ("Allah Hu Akbar")


def time(request):
    return HttpResponse(f'It is {str(datetime.now())[:10]} today')