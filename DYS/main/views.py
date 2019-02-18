from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
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


