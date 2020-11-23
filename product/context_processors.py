from product.models import Category
from feedback.forms import FeedbackForm


def category(request):
    context = {}
    context["categories"] = Category.objects.order_by("name")
    context["feedback_form"] = FeedbackForm()
    return context