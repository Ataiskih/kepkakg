from django.urls import path
from users_profiles.views import (
    # UserProfileView,
    ProfileUpdate,
)


urlpatterns = [
    path('<int:pk>/', ProfileUpdate.as_view(), name='edit-profile'),
]
