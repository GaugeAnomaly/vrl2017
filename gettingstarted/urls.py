from django.conf.urls import include, url, static
import gettingstarted.settings as settings
from django.views.generic import CreateView
from django.conf import settings
from hello import views
from django.contrib import admin
admin.autodiscover()



# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.IndexView.as_view(), name='login'),
    url(r'^petitions/$', views.PetitionsView.as_view(), name='petitions'),
    url(r'^petition/(?P<id>[0-9]+)/$', views.PetitionDetailView.as_view(), name='petition-detail'),
    url(r'^create/$', views.PetitionCreate.as_view(), name='create'),
    url(r'^results/$', views.ResultsView.as_view(), name='results'),
    url(r'^db', views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)