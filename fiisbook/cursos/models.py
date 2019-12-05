from django.db import models
from users.models import Profesor
from django.utils import timezone


class Curso(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    start = models.DateTimeField(
        default=timezone.now(),
        blank=True
    )
    end = models.DateTimeField(
        blank=True,
        null=True,
    )
    teacher = models.ManyToManyField(Profesor,blank=True)
    document = models.FileField(upload_to='documents/',blank=True)


    def __str__(self):
        return self.name

class Interfaz(models.Model):
    curso = models.ForeignKey(Curso,
                related_name='interfaz',
                on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    document = models.FileField(upload_to='documents/',blank=True,null=True)
    photo = models.ImageField(upload_to='fotos/',blank=True,null=True)

    def __str__(self):
        return self.curso.name