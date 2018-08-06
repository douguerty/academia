import re, json
from . import models
from . import forms
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
from .utils import exercicio as utils_exercicio
from .utils import treinamento as utils_treinamento
from .utils import dashboard as utils_dashboard
from .utils import humor as utils_humor
from .forms import CustomUserCreationForm


def home(request):
    if request.user.is_authenticated:
        imc_ideal = 21.75
        ultima_data = utils_usuario.GetUltimoLogAgua(id=request.user.pk)
        hoje = datetime.now()
        consumo_diario = 0
        if ultima_data:
            dias = hoje.day-ultima_data.day
            if dias > 0:
                update_consumo_agua = utils_usuario.ZeraConsumo(id=request.user.pk)

        consumo_agua_diario = utils_usuario.GetUltimoConsumoDiario(id=request.user.pk)
        if consumo_agua_diario:
            consumo_diario = consumo_agua_diario
        else:
            consumo_diario = False

        usuario = utils_usuario.GetUsuario(id=request.user.pk)
        peso_ideal = 0
        diferenca_peso = 0
        peso_abaixo = 0
        for u in usuario:
            if u.imc is not None and u.imc != imc_ideal:
                peso_ideal = round(imc_ideal * ((float(u.altura)/100)*(float(u.altura)/100)), 3)
                if peso_ideal > float(u.peso):
                    diferenca_peso = round(peso_ideal - float(u.peso), 3)
                    peso_abaixo = True
                else:
                    diferenca_peso = round(float(u.peso) - peso_ideal, 3)
                    peso_abaixo = False

            if u.agua is not None:
                if u.consumo_agua is not None:
                    if float(u.agua) < float(u.consumo_agua):
                        agua = float(u.consumo_agua) - float(u.agua)
                        acima_do_minimo = True
                        percentual = 100
                    else:
                        agua = float(u.agua) - float(u.consumo_agua)
                        acima_do_minimo = False
                        percentual = int(round((float(u.consumo_agua) / float(u.agua)) * 100, 0))

                    context = {
                        'usuario': usuario, 'agua': agua,
                        'acima_do_minimo': acima_do_minimo,
                        'percentual': percentual, 'consumo_diario': consumo_diario,
                        'peso_ideal': peso_ideal, 'diferenca_peso': diferenca_peso,
                        'peso_abaixo': peso_abaixo
                    }
                else:
                    acima_do_minimo = False
                    agua = u.agua
                    percentual = 0
                    context = {
                        'usuario': usuario, 'agua': agua,
                        'acima_do_minimo': acima_do_minimo,
                        'percentual': percentual, 'consumo_diario': consumo_diario,
                        'peso_ideal': peso_ideal, 'diferenca_peso': diferenca_peso,
                        'peso_abaixo': peso_abaixo
                    }
            else:
                context = {
                    'usuario': usuario
                }
        return render(request, 'home.html', context)
    else:
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


@csrf_exempt
def info_pessoal(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            nome = request.POST.get('nome', None)
            sobrenome = request.POST.get('sobrenome', None)
            genero = request.POST.get('genero', None)
            nascimento = request.POST.get('nascimento', None)
            idade = request.POST.get('idade', None)
            altura = request.POST.get('altura', None)
            peso = request.POST.get('peso', None)
            id = request.user.pk

            altura = float(altura)
            peso = float(peso)

            update = utils_usuario.UpdateUsuario(id=id, nome=nome, sobrenome=sobrenome,
                                                genero=genero, nascimento=nascimento,
                                                idade=idade, altura=altura, peso=peso
                                        )
            if update:
                retorno = {
                    'update': True
                }
                return HttpResponse(
                    json.dumps(retorno), content_type='application/json'
                )
            else:
                retorno = {
                    'update': False
                }
                return HttpResponse(
                    json.dumps(retorno), content_type='application/json'
                )
        else:
            usuario = utils_usuario.GetUsuario(id=request.user.pk)
            context = {
                'usuario': usuario
            }
            return render(request, 'info_pessoal.html', context)
    else:
        return HttpResponseRedirect(reverse('core:home'))


def exercicio(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.ExercicioForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.usuario = request.user
                form.save()
                return HttpResponseRedirect(reverse('core:exercicios'))
        else:
            form = forms.ExercicioForm()
        return render(request, 'exercicio.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('core:home'))


def exercicios(request):
    if request.user.is_authenticated:
        exercicios = utils_exercicio.GetExercicio(usuario=request.user)
        if exercicios:
            context = {
                'exercicios': exercicios
            }
            return render(request, 'exercicios.html', context)
        else:
            return render(request, 'exercicios.html')
    else:
        return HttpResponseRedirect(reverse('core:home'))


def exercicio_edit(request, id=None):
    if request.user.is_authenticated:
        exercicio = models.Exercicio.objects.get(pk=id)
        if request.method == 'POST':
            form = forms.ExercicioForm(request.POST, instance=exercicio)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('core:exercicios'))
            
        else:
            form = forms.ExercicioForm(instance=exercicio)

        return render(request, 'exercicio.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('core:home'))


@csrf_exempt
def exercicio_delete(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id_exercicio = request.POST.get('id', None)
            usuario = request.user

            delete = utils_exercicio.DeleteExercicio(
                                id_exercicio=id_exercicio, usuario=usuario
                            )
            if delete:
                retorno = {
                    'delete': True
                }
                return HttpResponse(
                    json.dumps(retorno), content_type='application/json'
                )
            else:
                retorno = {
                    'delete': False
                }
                return HttpResponse(
                    json.dumps(retorno), content_type='application/json'
                )
    else:
        return HttpResponseRedirect(reverse('core:home'))


def treinamento(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.TreinamentoForm(request.user, request.POST)
            if form.is_valid:
                form.save()
                return HttpResponseRedirect(reverse('core:treinamentos'))
        else:
            form = forms.TreinamentoForm(request.user)
        return render(request, 'treinamento.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('core:home'))


def treinamentos(request):
    if request.user.is_authenticated:
        treinamentos = utils_treinamento.GetTreinamento(usuario=request.user)
        if treinamentos:
            context = {
                'treinamentos': treinamentos
            }
            return render(request, 'treinamentos.html', context)
        else:
            return render(request, 'treinamentos.html')
    else:
        return HttpResponseRedirect(reverse('core:home'))


def treinamento_edit(request, id=None):
    if request.user.is_authenticated:
        treinamento = models.Treinamento.objects.get(pk=id)
        if request.method == 'POST':
            form = forms.TreinamentoForm(request.user, request.POST, instance=treinamento)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('core:treinamentos'))
            
        else:
            form = forms.TreinamentoForm(request.user, instance=treinamento)

        return render(request, 'treinamento.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('core:home'))


@csrf_exempt
def treinamento_delete(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id_treinamento = request.POST.get('id', None)
            usuario = request.user

            delete = utils_treinamento.DeleteTreinamento(
                                id_treinamento=id_treinamento, usuario=usuario
                            )
            if delete:
                retorno = {
                    'delete': True
                }
                return HttpResponse(
                    json.dumps(retorno), content_type='application/json'
                )
            else:
                retorno = {
                    'delete': False
                }
                return HttpResponse(
                    json.dumps(retorno), content_type='application/json'
                )
    else:
        return HttpResponseRedirect(reverse('core:home'))
    

def consumo_agua(request):
    if request.user.is_authenticated:
        form = forms.AguaForm()
        if request.method == 'POST':
            consumo_agua = request.POST.get('consumo_agua', None)
            if form.is_valid:
                update = utils_usuario.ConsumoAgua(id=request.user.pk, consumo_agua=consumo_agua)
                if update:
                   return HttpResponseRedirect(reverse('core:home')) 

        return render(request, 'consumo_agua.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('core:home'))


def relatorio_agua(request):
    if request.user.is_authenticated:
        relatorio_agua = utils_usuario.GetRelatorioAgua(id=request.user.pk)
        if relatorio_agua:
            context = {
                'relatorio': relatorio_agua
            }
            return render(request, 'relatorio_agua.html', context)    
        return render(request, 'relatorio_agua.html')
    else:
        return HttpResponseRedirect(reverse('core:home'))


@csrf_exempt
def dashboard(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.POST.get('user', None)
            chart = request.POST.get('chart', None)
            data_de = request.POST.get('data_de', None)
            data_ate = request.POST.get('data_ate', None)
            dashboard = utils_dashboard.GetDashboard(id=user, chart=chart,
                                                    data_de=data_de, data_ate=data_ate
                                                )
            if dashboard:
                return HttpResponse(
                    json.dumps(dashboard), content_type='application/json'
                )
            else:
                retorno = {
                    'error': True
                }
                return HttpResponse(
                    json.dumps(retorno), content_type='application/json'
                )
        return render(request, 'dashboard.html')
    else:
        return HttpResponseRedirect(reverse('core:home'))


@csrf_exempt
def humor(request):
    if request.user.is_authenticated:
        usuario = request.user
        if request.method == 'POST':
            user = request.POST.get('usuario', None)
            humor = request.POST.get('humor', None)
            data = request.POST.get('data', None)
            if data == 'None' or data is None:
                data = datetime.now()
                
            estado_emocional = utils_humor.SaveHumor(id=usuario, humor=humor, data=data)
            if estado_emocional:
                retorno = {
                    'error': False
                }
                return HttpResponse(
                    json.dumps(retorno), content_type='application/json'
                )
            else:
                retorno = {
                    'error': True
                }
                return HttpResponse(
                    json.dumps(retorno), content_type='application/json'
                )
        return render(request, 'humor.html')
    else:
        return HttpResponseRedirect(reverse('core:home'))