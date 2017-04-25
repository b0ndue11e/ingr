from django.db import models

class Weapon(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text='Название оружия')
    description = models.TextField(help_text='Полное, или доступное, описание предмета или его действий')
    type_choices = (('Virus', 'Захватывающее'), ('Weapon', 'Разрушающее'))
    type = models.CharField(max_length=6, choices=type_choices, default='Weapon', help_text=
                            'Выберите тип оружия Разрущающее или Захватывающее')
    image = models.ImageField(upload_to='weapons/', blank=True, null=True)


class Instruction(models.Model):
    name = models.CharField(max_length=255)
    xmp_use= models.TextField(blank=True, null=True)
    ultra_xmp_use = models.TextField(blank=True, null=True)
    virus_use = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
