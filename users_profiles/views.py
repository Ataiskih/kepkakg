from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users_profiles.models import (
    UserProfile,
    User,
)
from django.shortcuts import get_object_or_404
from users_profiles.forms import UserForm


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'user_profiles/profiles.html'
    success_url = '/'
    fields = '__all__'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserForm(
            instance=self.request.user
        )
        return context

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = self.request.user
        form = request.POST
        user.username = form['username']
        user.first_name = form['first_name']
        user.last_name = form['last_name']
        user.email = form['new_email']
        user.save()
        return response

    def dispatch(self, request, *args, **kwargs):
        profile = UserProfile.objects.get(id=kwargs['pk'])
        if request.user != profile.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
