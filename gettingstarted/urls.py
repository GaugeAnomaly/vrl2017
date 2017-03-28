from django.conf.urls import include, url
import gettingstarted.settings as settings
from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^all$', hello.views.all, name='all'),
    url(r'^initiative$', hello.views.create, name='create'),
    url(r'^results$', hello.views.results, name='results'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
