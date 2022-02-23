from django import forms
from django.contrib.auth.models import User

from water.models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

    # def clean(self):



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
