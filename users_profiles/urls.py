from django.urls import path
from users_profiles.views import (
    UserProfileView,
)


urlpatterns = [
    path('<username>/', UserProfileView.as_view(), name='profile'),
]
