from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/$', RedirectView.as_view(url='/logbook/')),
    url(r'^logbook/', include('logbook.urls', namespace='logbook')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
)
