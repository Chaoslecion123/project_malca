from django.contrib import admin
from .models import Profesor, User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as LegacyUserAdmin

# Register your models here.


class UserAdmin(LegacyUserAdmin):

    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',

            )
        }),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'is_teacher',
                'is_student',

            )
        }),
        (_('Información personal'), {
            'fields': (
                'first_name',
                'last_name',
                # 'mother_last_name',
            )
        }),
        (_('Important dates'), {
            'fields':
            (
                'last_login',
                'date_joined'
            )
        }), )



admin.site.register(User,UserAdmin)
admin.site.register(Profesor)
