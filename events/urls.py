from django.conf.urls import  url
from . import views
from .views import event

app_name = 'events'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.EventsDetailView.as_view(), name='detail'),
]