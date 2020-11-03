from django import forms
from users_profiles.models import (
    UserProfile,
    User
)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['id']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['id']