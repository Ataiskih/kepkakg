from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    ListView,
    UpdateView,
)
from users_profiles.models import UserProfile


class UserProfileView(ListView):
    model = UserProfile
    template_name = 'user_profiles/profiles.html'
    context_object_name = 'profile'
        
    def get_queryset(self):
        profile = UserProfile.objects.filter(
            user=self.request.user
        )
        return profile

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserProfileView, self).dispatch(*args, **kwargs)

    # def get_contex_data(self, **kwargs):
    #     username = self.kwargs['username']
    #     profile = UserProfile.objects.get(
    #         username=username
    #     )
    #     context = super().get_contex_data(**kwargs)
    #     context['profile'] = UserProfile.objects.get(
    #         username=username
    #     )
    #     return context

class UserProfileUpdate(UpdateView):
    model = UserProfile
    fields = [
        'user',
        'first_name',
        'last_name',
        'avatar',
        'gender',
        'birthday',
        'email',
        'phone',
    ]
    
    template_name = 'user_profiles/profiles.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)