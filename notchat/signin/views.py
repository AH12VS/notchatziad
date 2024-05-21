from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SigninForm
from django.contrib import messages


def signin_view(request):
    if request.user.is_authenticated:
        return redirect("home:home_page")

    form = SigninForm()
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd["email"]
            passwd = cd["passwd"]
            user = authenticate(request, email=email, password=passwd)
            if user != None and user.is_active:
                login(request, user)
                messages.success(request, "Signed In Successfully")
                return redirect("home:home_page")
            else:
                form.add_error(None, "Email or Password is wrong")
                messages.error(request, "Email or Password is wrong")

        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)

    return render(request, "signin/signin.html")