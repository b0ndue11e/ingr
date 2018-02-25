from django.shortcuts import render, redirect
from .models import EventReg, Events
from django import forms
from django.views.generic.detail import DetailView
from django.contrib import messages


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


class ModelEventRegForm(forms.ModelForm):
    class Meta:
        model = EventReg
        exclude = ['comment']
        labels = {'name': 'Имя', 'surname': 'Фамилия', 'age': 'Возраст',
                  'nickname': 'Псевдоним', 'mail': 'Почтовый адрес',
                  'attendance': 'Присутствие', 'reg_to': 'Ивент'}


def regform(request, pk):
    pk = id
    if request.method == 'POST':
        event_regform = ModelEventRegForm(request.POST)
        if event_regform.is_valid():
            instance = event_regform.save()
            messages.success(request, 'Вы успешно зарегистрированы!')
            return redirect('./')

    else:
        event_regform = ModelEventRegForm(initial={'attendance': 'yes'})

    return render(request, 'events/reg.html', {'form': event_regform})
