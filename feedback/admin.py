from django.contrib import admin
from feedback.models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    fields = ['date', 'name', 'text', 'user', 'email', 'answer']