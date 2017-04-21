from django.contrib import admin
from weapon.models import Weapon

class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

admin.site.register(Weapon, WeaponAdmin)

# Register your models here.
