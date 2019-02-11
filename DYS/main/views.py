from django.shortcuts import render

from django.views import View


class MainPageView(View):

    def get(self, request):

        return render(request, 'main/index.html')


class RegisterView(View):

    def get(self, request):

        return render(request, 'main/register.html')


class LoginView(View):

    def get(self, request):

        return render(request, 'main/login.html')


class DashboardView(View):

    def get(self, request):

        return render(request, 'main/form.html')


