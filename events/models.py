from django.db import models


class Events(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text='Название мероприятия')
    date = models.DateField(help_text='Дата проведения мероприятия')
    description = models.TextField(help_text='Описание мероприятия', blank=True)
    registration = models.BooleanField(help_text='Регистрация на мероприятие: обзательна или нет')
    location = models.CharField(max_length=255, help_text='Место проведения мероприятия')

    def __str__(self):
        return self.name


class EventReg(models.Model):
    event = models.ForeignKey('Events', on_delete='id', null=True, blank=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.CharField(max_length=3)
    nickname = models.CharField(max_length=14)
    mail = models.EmailField(max_length=50, unique=True)
    attendance = models.CharField(max_length=7, choices=(('yes', 'Online'),
                                                         ('no', 'Offline')))
    comment = models.TextField()
    registation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
