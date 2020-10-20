from django import forms
from users_profiles.models import UserProfile


class ProfileForm(forms.ModelForm):
    

    class Meta:
        model = UserProfile
        exclude = [
            'user',
        ]