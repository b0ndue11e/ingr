from django.conf.urls import url
from . import views

app_name = 'events'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.EventsDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/reg/$', views.register)
]
