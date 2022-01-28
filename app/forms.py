from atexit import register

from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import register


class CreateUserForm(UserCreationForm):

    class Meta:
        model = register
        fields = ['username', 'password1', 'password2']
