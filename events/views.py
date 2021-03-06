from django.shortcuts import render, redirect, get_object_or_404
from .models import EventReg, Events
from django import forms
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.core.mail import send_mail


class EventsDetailView(DetailView):
    model = Events
    template_name = 'events/detail.html'
    context_object_name = 'event'

    def get_queryset(self):
        qs = super().get_queryset()
        event_name = self.request.GET.get('event_name', None)
        if event_name:
            qs = qs.filter(event=event_name)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = Events.objects.filter(name=self.object.name)
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


def register(request, pk):
    post = request.method == 'POST'
    data = request.POST
    reg_to = get_object_or_404(Events, id=pk)
    event_regform = ModelEventRegForm(data or None)
    if post and event_regform.is_valid():
        reg = event_regform.save(commit=True)
        reg.reg_to = reg_to
        reg.save
        messages.success(request, 'Вы успешно зарегистрированы!')
        subject = 'Ingress Events Team'
        mail = request.POST.get('mail', '')
        info = """Ваша заявка на участие в мероприятии принята! 
                    Надеемся вы хорошо проведете время. Спасибо за регистрацию. До встречи!"""
        send_mail(subject, info, '', [mail], fail_silently=False)
        return redirect('../')

    else:
        event_regform = ModelEventRegForm(initial={'attendance': 'yes'})

    return render(request, 'events/reg.html', {'form': event_regform})

