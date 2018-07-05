import re
import json
from . import models
from datetime import date, datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, Http404, HttpResponseNotAllowed, JsonResponse
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.urls import reverse_lazy, reverse
from .utils import usuario as utils_usuario

from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'home.html')


def login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('core:home'))

    kwargs['extra_context'] = {'next': reverse('core:home')}
    kwargs['template_name'] = 'login.html'
    return login(request, *args, **kwargs)


def logout_view(request, *args, **kwargs):
    kwargs['next_page'] = reverse('core:home')
    return logout(request, *args, **kwargs)


class RegistrationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('core:login')
    template_name = "nova_conta.html"


def info_pessoal(request):
    if request.user.is_authenticated:
        usuario = utils_usuario.GetUsuario(id=request.user.pk)
        context = {
            'usuario': usuario
        }
        return render(request, 'info_pessoal.html', context)
    else:
        return HttpResponseRedirect(reverse('core:home'))