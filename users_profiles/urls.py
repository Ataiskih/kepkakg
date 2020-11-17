from django.urls import path
from users_profiles.views import *


urlpatterns = [
    path("registration/", registration, name="registration"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("change-password/", change_password, name='change-password'),
    path("profile/<int:pk>/", profile, name="profile"),
]