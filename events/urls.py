from django.conf.urls import  url
from . import views
from .views import event

app_name = 'events'

urlpatterns = [
    url(r'^event/$', event),
    url(r'^(?P<pk>\d+)$', views.EventDetailView.as_view(), name='detail')
]