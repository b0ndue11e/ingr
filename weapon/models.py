from django.db import models

class Weapon(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text='Название оружия')
    description = models.TextField(help_text='Полное, или доступное, описание предмета или его действий')
    type_choices = (('Virus', 'Захватывающее'), ('Weapon', 'Разрушающее'))
    type = models.CharField(max_length=6, choices=type_choices, default='Weapon', help_text=
                            'Выберите тип оружия Разрущающее или Захватывающее')
    image = models.ImageField(upload_to='ingr/static/images/weapons')

    def __str__(self):
        return self.name