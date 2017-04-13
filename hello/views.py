import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .models import Greeting, Petition
from .forms import PetitionForm


# Create your views here.
class IndexView(View):
    def post(self, request):
        return render(request, 'home.html')
    
    @staticmethod
    def get(request):
        # r = requests.get('http://httpbin.org/status/418')
        # return HttpResponse(r.text)
        # return HttpResponse('Hello from Python!')
        return render(request, 'home.html')


class PetitionsView(View):
    @staticmethod
    def get(request):
        latest_petitions = Petition.objects.order_by('-pub_date')[:10]
        return render(request, 'petitions.html', {'latest_petitions': latest_petitions})


class CreateView(View):
    pf = PetitionForm
    template_name = 'create.html'

    def post(self, request):
        form = self.pf(request.POST, request.FILES)
        if form.is_valid():
            desc_text = form.cleaned_data['desc_text']
            improvement = form.cleaned_data['improvement']
            title = form.cleaned_data['title_text']
            form.save()
            petition = form.save(commit=False)
            petition.desc_text = desc_text
            petition.improvement = improvement
            petition.title_text = title
            petition.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = self.pf
        return render(request, self.template_name, {'form': form})


class ResultsView(View):
    @staticmethod
    def get(request):
        return render(request, 'results.html')


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()

    petition = Petition()
    petition.save()
    petitions = Petition.objects.all()

    return render(request, 'db.html', {'greetings': greetings, 'petitions': petitions})
