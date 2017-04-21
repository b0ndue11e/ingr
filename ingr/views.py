from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return render(request, 'index.html')

def weapon(request):
    return render(request, 'weapon.html')

def history(request):
    return render(request, 'history.html')

def contacts(request):
    return render(request, 'contacts.html')