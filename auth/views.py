from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model, logout
from .forms import LoginForm, SignupForm


# Create your views here.

def auth(request):
    loginForm = LoginForm(request.POST or None)
    signupForm = SignupForm(request.POST or None)
    context = {
        'loginForm': loginForm,
        'signupForm': signupForm
    }
    return render(request, 'login.html', context)


def login_handler(request):
    loginForm = LoginForm(request.POST or None)
    if loginForm.is_valid():
        print(loginForm.cleaned_data)
        data = loginForm.cleaned_data
        email = data['email']
        password = data['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return redirect('/auth')


User = get_user_model()


def signup(request):
    signupForm = SignupForm(request.POST or None)
    if signupForm.is_valid():
        print(signupForm.cleaned_data)
        data = signupForm.cleaned_data
        name = data['name']
        email = data['email']
        password = data['password']
        if User.objects.create_user(email, f"{name}@quora.com", password) is not None:
            return redirect('/')
    return redirect('/auth')


def logout_handler(request):
    logout(request)
    print(f"user is authenticated {request.user.is_authenticated}")
    print("User is logout")
    print(f"user is authenticated {request.user.is_authenticated}")
    return redirect('/auth')
