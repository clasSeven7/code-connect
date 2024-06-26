from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


class CustomLoginView(LoginView):
    template_name = '../templates/plataforma/auth/login.html'


class CustomRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = '../templates/plataforma/auth/register.html'
    success_url = '/'


class CustomLogoutView(LogoutView):
    next_page = '/'
