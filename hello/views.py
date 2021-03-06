import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Greeting, Petition
from .forms import PetitionForm


# Create your views here.
class IndexView(View):
    def post(self, request, *args, **kwargs):
        return HttpResponse("POST TO INDEXVIEW")
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
        return render(request, 'hello/petition_list.html', {'latest_petitions': latest_petitions})


class PetitionCreate(CreateView):
    model = Petition
    fields = ['title_text','votes','desc_text','improvement','picture']
    success_url = reverse_lazy('create')

    def get_success_url(self):
        return HttpResponse("FORM VALID")
        return reverse('index')

    def form_valid(self, form, **kwargs):
        return HttpResponse("FORM VALID")
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


"""
    def post(self, request, *args, **kwargs):
        return HttpResponse("POST TO CREATE")
        form_class = self.get_form_class()
        form = self.get_form(form_class)
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
        form = self.get_form_class()
        return render(request, self.template_name, {'form': form})
"""

def model_form_upload(request):
    if request.method == 'POST':
        form = PetitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PetitionForm()
    return render(request, 'hello/petition_form.html', {
        'form': form
    })

class ResultsView(ListView):
    model = Petition
    """
    def post(self, request, *args, **kwargs):
        return HttpResponse("JEEEEEE")

    def get(self, request):
        return HttpResponse("JEEEEEE")
        return render(request, 'results.html')"""


class PetitionDetailView(DetailView):
    model = Petition

    def get_context_data(self, **kwargs):
        context = super(PetitionDetailView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context


class AboutView(View):
    @staticmethod
    def get(request):
        return render(request, 'about.html')


def ajax(request):
    return render(request, 'ajax.html')

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()

    petition = Petition()
    petition.save()
    petitions = Petition.objects.all()

    return render(request, 'db.html', {'greetings': greetings, 'petitions': petitions})