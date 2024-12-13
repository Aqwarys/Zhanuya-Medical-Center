from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Role  # Подключаем вашу кастомную модель

class UserRegistrationForm(UserCreationForm):
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = forms.ChoiceField(choices=gender_choices, required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1900, 2025)))
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=False)

    class Meta:
        model = User  # Укажите вашу кастомную модель User
        fields = ('first_name', 'last_name', 'email', 'role', 'gender', 'date_of_birth', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)