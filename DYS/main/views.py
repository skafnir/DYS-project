from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views import View

from main.forms import LoginForm


class MainPageView(View):

    def get(self, request):
        return render(request, 'main/index.html')


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
        text = 'Hasła niezgodne'
        return render(request, 'main/register.html', {"text": text})


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'main/dashboard.html')


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'main/profile.html')

    def post(self, request):
        username = request.POST.get("login")
        email = request.POST.get('email')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('password2')
        u = User.objects.get(username=request.user)
        users = User.objects.all()
        usernames = []
        emails = []
        for i in users:
            emails.append(i.email)
            usernames.append(i.username)

        if username and email and name and surname:
            if username in usernames and username != request.user.username:
                text = 'Zajęta nazwa użytkownika'
                return render(request, 'main/profile.html', {"text": text})
            elif email in emails and email != request.user.email:
                text = 'Podany email już istnieje'
                return render(request, 'main/profile.html', {"text": text})
            else:
                u.username = username
                u.email = email
                u.first_name = name
                u.last_name = surname
                u.save()
                text = 'Udana edycja danych'
                return render(request, 'main/profile.html', {"text": text})

        if password and confirmPassword and password == confirmPassword:
            u.set_password(password)
            update_session_auth_hash(request, u)  # doesnt log out after change
            u.save()
            text2 = 'Hasło zostało zmienione'
            return render(request, 'main/profile.html', {"text2": text2})
        text2 = 'Hasła niezgodne lub pole pozostawione puste'
        return render(request, 'main/profile.html', {"text2": text2})
