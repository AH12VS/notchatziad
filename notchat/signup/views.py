from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users.models import UserModel
from .forms import SignupForm
from django.contrib import messages


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("home:home_page")

    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = UserModel()
            user.email = cd["email"]
            user.username = cd["username"]
            passwd = cd["passwd"]
            confirm_passwd = cd["confirm_passwd"]

            if str(passwd) == str(confirm_passwd):
                user.set_password(passwd)
                user.passwd = passwd

            user.is_active = True

            user.save()

            user = authenticate(request, email=user.email, password=passwd)
            login(request, user)

            messages.success(request, "Signed Up Successfully")
            return redirect("home:home_page")
        
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)


    return render(request, "signup/signup.html")
