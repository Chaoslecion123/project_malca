from django import forms
from .models import User

class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True,max_length=50,
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'username',
                                'placeholder':'Username'
                            }))

    password = forms.CharField(required=True,
                            widget=forms.PasswordInput(attrs={
                                                        'class':'form-control',
                                                        'id':'password',
                                                        'placeholder':'Contraseña'
                                                    }))

    password2 = forms.CharField(
                label='confimar password',
                required=True,
                widget=forms.PasswordInput(
                attrs={
                    'class':'form-control',
                    'id':'password',
                    'placeholder':'Contraseña'
                }))

    schools_type = forms.ChoiceField(
        choices=(
            (0, 'Sistemas'),
            (1, 'Industrial'),
        ),
        required=False,
        label='Tipo de Escuela',
    )

    # profile_type = forms.ChoiceField(
    #     choices=(
    #         (0, 'Administrador'),
    #         (1, 'Estudiante'),
    #     ),
    #     required=False,
    #     label='Tipo de Perfil',
    # )

    def save(self):
        return User.objects.create_user(
            username=self.cleaned_data.get('username'),
            password=self.cleaned_data.get('password'),
            schools_type=self.cleaned_data.get('schools_type'),
            # self.cleaned_data.get('profile_type')
        )
