from django.shortcuts import render, redirect
from .models import Event
from .forms import EventModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

class EventDetailView(DetailView):
    model = Event
    template_name = 'event/detail.html'
    context_object_name = 'event'

    def get_queryset(self):
        qs = super().get_queryset()
        event_id = self.request.GET.get('event_id', None)
        if event_id:
            qs = qs.filter(event=event_id)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = Event.objects.filter(event=self.object.pk)
        return context
def event(request):
    return render(request, 'event.html')