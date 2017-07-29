from django.shortcuts import render, get_object_or_404
from events.models import Event
from .forms import EventModelForm
from django.views.generic.detail import DetailView

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'event_list': events})

def event_detail(request):
    event = Event.objects.all()
    return render(request, 'event/detail.html', {'event': event})