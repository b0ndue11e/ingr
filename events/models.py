from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text='Название мероприятия')
    date = models.DateField(help_text='Дата проведения мероприятия')
    description = models.TextField(help_text='Описание мероприятия', blank=True)
    registration = models.BooleanField(help_text='Регистрация на мероприятие: обзательна или нет')
    location = models.CharField(max_length=255, help_text='Место проведения мероприятия')


    def __str__(self):
        return self.name