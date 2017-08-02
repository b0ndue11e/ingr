from django.shortcuts import render
from .models import Events
from django.views.generic.detail import DetailView


class EventsDetailView(DetailView):
    model = Events
    template_name = 'events/detail.html'
    context_object_name = 'event'

    def get_queryset(self):
        qs = super().get_queryset()
        event_id = self.request.GET.get('event_id', None)
        if event_id:
            qs = qs.filter(event=event_id)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = Events.objects.filter(event=self.object.pk)
        return context


def event(request):
    return render(request, 'event.html')