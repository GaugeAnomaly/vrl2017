from django.conf.urls import include, url, static
import gettingstarted.settings as settings
from django.conf import settings
import hello.views
from django.contrib import admin
admin.autodiscover()



# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.IndexView.as_view(), name='index'),
    url(r'^$', hello.views.IndexView.as_view(), name='login'),
    url(r'^petitions/$', hello.views.PetitionsView.as_view(), name='petitions'),
    url(r'^create/$', hello.views.CreateView.as_view(), name='create'),
    url(r'^results/$', hello.views.ResultsView.as_view(), name='results'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)