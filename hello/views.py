import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.views.generic.edit import FormView
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


class CreateView(FormView):
    form_class = PetitionForm
    template_name = 'create.html'
    success_url = reverse('results')

    def post(self, request, *args, **kwargs):
        form = self.pf(request.POST, request.FILES)
        if form.is_valid():
            desc_text = form.cleaned_data['desc_text']
            improvement = form.cleaned_data['improvement']
            title = form.cleaned_data['title_text']
            form.save()
            #petition = form.save(commit=False)
            #petition.desc_text = desc_text
            #petition.improvement = improvement
            #petition.title_text = title
            #petition.save()
            return self.form_valid(form)
            #return HttpResponseRedirect(reverse('results'))
        return self.form_invalid(form)
        #return render(request, self.template_name, {'form': form})

    def get(self, request, **kwargs):
        form = self.pf
        return render(request, self.template_name, {'form': form})


class ResultsView(View):
    def post(self, request):
        return HttpResponse("JEEEEEE")

    def get(self, request):
        return render(request, 'results.html')


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()

    petition = Petition()
    petition.save()
    petitions = Petition.objects.all()

    return render(request, 'db.html', {'greetings': greetings, 'petitions': petitions})
