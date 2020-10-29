from django.urls import path
from users_profiles.views import (
    UserProfileView,
    UserProfileUpdate,
)


urlpatterns = [
    path('<username>/', UserProfileView.as_view(), name='profile'),
    path('edit/<int:pk>/', UserProfileUpdate.as_view(), name='edit-profile'),
]
