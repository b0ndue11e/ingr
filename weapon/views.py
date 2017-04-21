from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from weapon.models import Weapon

def weapons_list(request):
    weapon = Weapon.objects.all()
    return render(request, 'weapon.html', {'weapons_list': weapon})
