from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django import forms
from django.contrib import messages
from events.models import EventReg, Event

def index(request):
    return render(request, 'index.html')

def weapon(request):
    return render(request, 'weapon.html')

def history(request):
    return render(request, 'history.html')

def contacts(request):
    return render(request, 'contacts.html')

def event(request):
    return render(request, 'event.html')