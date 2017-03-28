import requests
from django.http import HttpResponse
from django.shortcuts import render

from .models import Greeting, Petition


# Create your views here.
def index(request):
    #r = requests.get('http://www.neti.ee')
    #r = requests.get('http://httpbin.org/status/418')
    #print(r.text)
    #return HttpResponse(r.text)
    # return HttpResponse('Hello from Python!')
    return render(request, 'home.html')

def all(request):
    return render(request, 'initiatives.html')

def create(request):
    return render(request, 'create.html')

def results(request):
    return render(request, 'results.html')


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()

    petition = Petition()
    petition.save()
    petitions = Petition.objects.all()

    return render(request, 'db.html', {'greetings': greetings, 'petitions': petitions})
