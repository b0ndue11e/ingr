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

class EventRegForm(forms.Form):
    name = forms.CharField(max_length=255, label='Имя (Name): ')
    surname = forms.CharField(max_length=255, label='Фамилия (Surname): ')
    age = forms.CharField(max_length=3, label='Возраст (Age): ')
    nickname = forms.CharField(max_length=14, label='Игровое имя (Nickname):')
    mail = forms.EmailField(max_length=50, label='Почтовый адрес (Mail): ')
    attendance = forms.ChoiceField(label='Участие (Attendance): ',
                                   choices=(('yes', 'Online'),
                                            ('no', 'Offline')),
                                   widget=forms.RadioSelect)

def reg(request):
    if request.method == "POST":
        regform = EventRegForm(request.POST)
        if regform.is_valid():
            data = regform.cleaned_data
            reg = EventReg()
            reg.name = data['name']
            reg.surname = data['surname']
            reg.age = data['age']
            reg.nickname = data['nickname']
            reg.mail = data['mail']
            reg.attendance = data['attendance']
            reg.save()
            messages.success(request)
            return redirect('/event/')
    else:
        regform = EventRegForm()
    return render(request, 'reg.html', {'form': regform})