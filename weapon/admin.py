from django.contrib import admin
from weapon.models import Weapon, Instruction
from django.db import models
from django.forms import widgets

class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Instruction)


# Register your models here.
