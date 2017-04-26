from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from events.models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'event_list': events})
