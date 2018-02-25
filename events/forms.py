from django import forms
from .models import Events, EventReg


class EventsModelForm(forms.ModelForm):
    class Meta:
        model = Events
        exclude = 0
