from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views import View

from main.forms import LoginForm


class MainPageView(View):

    def get(self, request):
        return render(request, 'main/index.html')


class RegisterView(View):

    def get(self, request):
        return render(request, 'main/register.html')


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'main/login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form['login'].value(),
                                password=form['password'].value())
            if user:
                login(request, user)
                return redirect('dashboard')
            return render(request, 'main/login.html')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('main-page')


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'main/form.html')


class RegisterView(View):

    def get(self, request):
        return render(request, 'main/register.html')

    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get("login")
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('password2')
        users = User.objects.all()
        usernames = []
        emails = []
        for i in users:
            emails.append(i.email)
            usernames.append(i.username)
        if name and surname and username and email and password and confirmPassword and password == confirmPassword:
            if username in usernames:
                text = 'Podany użytkownik już istnieje'
                return render(request, 'main/register.html', {"text": text})
            elif email in emails:
                text = 'Podany email już istnieje'
                return render(request, 'main/register.html', {"text": text})
            else:
                User.objects.create_user(first_name=name,
                                         last_name=surname,
                                         username=username,
                                         email=email,
                                         password=password,
                                         )
                return redirect('login')
        text = 'Żle powtórzone hasło'
        return render(request, 'app/register.html', {"text": text})
