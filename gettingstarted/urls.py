from django.conf.urls import include, url, static
import gettingstarted.settings as settings
from django.views.generic import CreateView, DetailView
from django.conf import settings
from hello import views
from hello.models import Petition
from django.views.generic import ListView
from django.contrib import admin
admin.autodiscover()



# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.IndexView.as_view(), name='login'),
    url(r'^petitions/$', views.PetitionsView.as_view(), name='petitions'),
    url(r'^petition/(?P<id>\d+)/$', DetailView.as_view(model=Petition), name='petition-detail'),
    url(r'^create/$', views.model_form_upload, name='create'),
    url(r'^results/$', ListView.as_view(model=Petition), name='results'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^db', views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url("^soc/", include("social_django.urls", namespace="social")),
]

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)