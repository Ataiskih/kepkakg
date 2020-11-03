from django import forms
from users_profiles.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['id']
