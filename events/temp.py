class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EventListView(ListView):
    model = Event
    #paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        event_id = self.request.GET.get('event_id', None)
        if event_id:
            qs = qs.filter(event=event_id)
            return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        temp = self.request.GET.get('event_id')
        context['event_id'] = '?event_id=%s&' % temp if temp else '?'
        return context

    url(r'^$', views.EventListView.as_view(), name='list_view'),
    url(r'^(?P<pk>[\d]+)/$', views.EventDetailView.as_view(), name='detail')