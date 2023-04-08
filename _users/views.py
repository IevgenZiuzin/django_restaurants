from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from .forms import LoginForm


class ModeratorLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    authentication_form = LoginForm


def log_out(request):
    logout(request)
    return redirect('index')
