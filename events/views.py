from django.shortcuts import render, redirect
from .models import Events, EventReg
from django import forms
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
        context['event'] = Events.objects.filter(id=self.object.pk)
        return context


def event(request):
    return render(request, 'event.html')


#class ModelEventRegForm(forms.ModelChoiceField):
#    class Meta:
#        model = EventReg


class EventRegForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    surname = forms.CharField(label='Фамилия', max_length=255)
    age = forms.CharField(label='Возраст', max_length=3)
    nickname = forms.CharField(label='Псевдоним', max_length=14)
    mail = forms.EmailField(label='Почтовый адрес')
    attendance = forms.ChoiceField(label='Присутствие', choices=(('yes', 'Online'),
                                                                 ('no', 'Offline')))
    comment = forms.CharField(label='Комментарий', required=False)
    

def regform(request):
    if request.method == 'POST':
        event_regform = EventRegForm(request.POST)
        if event_regform.is_valid():
            return redirect('/events/reg/')

    else:
        event_regform = EventRegForm()

    return render(request,'events/reg.html', {'form': event_regform})
