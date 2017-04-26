from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django import forms
from django.contrib import messages
from events.models import EventReg

def index(request):
    return render(request, 'index.html')

def weapon(request):
    return render(request, 'weapon.html')

def history(request):
    return render(request, 'history.html')

def contacts(request):
    return render(request, 'contacts.html')

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