from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm

from users_profiles.forms import CreateUserForm
from order.models import *


def registration(request):
	if request.user.is_authenticated:
		return redirect('products')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('login')

		context = {'form':form}
		return render(request, 'users_profiles/registration.html', context)


def login(request):
    context = {}
	if request.user.is_authenticated:
		return redirect('products')
	else:
		if request.method == 'POST':
            form = auth.forms.AuthenticationForm(request)
            if form.is_valid():
                user = form.get_user()
                auth.login(request, user)
                return redirect('products')
    

    context["form"] = auth.forms.AuthenticationForm()
	return render(request, 'users_profile/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('login')


@require_http_methods(["POST"])
def change_password(request):
    form = PasswordChangeForm(user=request.user, data=request.POST)
    if form.is_valid():
        form.save()
    
    return redirect('login')


def profile(request, pk):
    context = {}
    context["user"] = User.objects.get(id=pk)
    context["orders"] = Order.objects.filter(customer.user=context["user"])

    return render(request, "users_profile/profile.html", context)