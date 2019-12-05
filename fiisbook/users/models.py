from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class SchoolsType:
    SISTEMAS = 0
    INDUSTRIAL = 1

    CHOICES = (
        (SISTEMAS,_('Sistemas')),
        (INDUSTRIAL,_('Industrial')),
    )

class ProfileType:
    ADMINISTRADOR = 0
    ESTUDIANTE = 1

    CHOICES = (
        (ADMINISTRADOR, _('Administrador')),
        (ESTUDIANTE,_('Estudiante')),
    )


class User(AbstractUser):
    schools_type = models.IntegerField(
        default=SchoolsType.SISTEMAS,
        choices=SchoolsType.CHOICES,
    )
    profile_type = models.IntegerField(
        default=ProfileType.ESTUDIANTE,
        choices=ProfileType.CHOICES,
    )

    is_teacher = models.BooleanField(
        default=False,
        help_text=_(
            'Indica si el usuario es profesor.'
        )
    )

    is_student = models.BooleanField(
        default=False,
        help_text=_(
            'Indica si el usuario es estudiante.'
        )
    )

    def get_full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)

    def __str__(self):
        return  self.get_full_name()


class Profesor(models.Model):
    name  = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
