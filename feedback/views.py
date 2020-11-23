from django.shortcuts import render
from django.views.decorators.http import require_POST
from .forms import FeedbackForm

@require_POST
def feedback(request):
    context = {}
    form = FeedbackForm(request.POST)
    if form.is_valid():
        feedback = form.save()
        if request.user.is_authenticated:
            feedback.user = request.user
            feedback.save()

        context["message"] = "Ваш отзыв принят, спасибо!"
        context["type"] = "success"
        return render(request, "product/message.html", context)

    context["message"] = "Форма заполнена неверно("
    context["type"] = "warning"
    return render(request, "product/message.html", context)

