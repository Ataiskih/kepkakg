from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users_profiles.models import UserProfile


class UserProfileAdmin(admin.StackedInline):
    model = UserProfile
    exclude = ['updated']


class UserAdmin(BaseUserAdmin):
    inlines = [UserProfileAdmin]
    exclude = ['updated']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
