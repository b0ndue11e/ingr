from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from weapon.models import Weapon, Instruction

def weapons_list(request):
    weapon = Weapon.objects.all()
    instruction = Instruction.objects.all()
    return render(request, 'weapon.html', {'weapons_list': weapon, 'instuctions_list': instruction})
