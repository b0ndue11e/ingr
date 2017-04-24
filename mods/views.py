from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from mods.models import Mod, Instruction

def mods_list(request):
    mods = Mod.objects.all()
    instructions = Instruction.objects.all()
    return render(request, 'mods.html', {'mods_list': mods, 'instructions_list': instructions})