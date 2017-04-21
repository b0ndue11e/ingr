from django.db import models

class Mod(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text='Название модификатора')
    short_name = models.CharField(max_length=10, unique=True,help_text='Короткое описание')
    descriprion = models.TextField(help_text='Полное, или доступное, описания предмета или его действия')
    common = models.CharField(max_length=5, blank=True, help_text='Степень воздействия если предмет очень частый ')
    rare = models.CharField(max_length=50, blank=True, help_text='Степень воздействия если предмет редкий')
    very_rare = models.CharField(max_length=50, blank=True, help_text='Степень воздействия если предмет очень редкий')
    image = models.ImageField(upload_to='ingr/static/images/mods')

    def __str__(self):
        return self.name