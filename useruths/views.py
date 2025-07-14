from django.shortcuts import redirect, render
from useruths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from useruths.models import User


def register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Her {username}, Your Account Was Create Succesfully")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect("Comercio:index")

    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, "useruths/sign-up.html", context)

def login_view(request):

    if request.user.is_authenticated:
        return redirect("Comercio:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in")
                return redirect("Comercio:index")
            else:
                messages.warning(request, "User does not exist")

        except:
            messages.warning(request, f"User with {email} does not exist")




    return render(request, "useruths/sign-in.html")

def logout_view(request):
    logout(request)
    return redirect("useruths:sign-in")

