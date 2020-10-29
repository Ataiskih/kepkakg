from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from users_profiles.models import (
    UserProfile,
    User,
)
from django.shortcuts import get_object_or_404


class UserProfileView(ListView, LoginRequiredMixin):
    model = UserProfile
    template_name = 'user_profiles/profiles.html'
    context_object_name = 'profile'

    # def get_queryset(self):
    #     profile = UserProfile.objects.filter(
    #         user=self.request.user
    #     )
    #     return profile

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.request.user)
        return UserProfile.objects.filter(user=self.user)
    
    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user'] = self.user 
        return context

# нужна форма c миксином юрл слаг в модели или pk
class UserProfileUpdate(UpdateView, LoginRequiredMixin):
    model = UserProfile
    template_name = 'user_profiles/profiles.html'
    fields = [
        'phone',
    ]
