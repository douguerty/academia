from core.models import MyUser, LogAgua, LogAguaDiario
from django.http import HttpResponse
from datetime import date, datetime, timedelta
import json

def GetUsuario(id):
    usuario = MyUser.objects.filter(pk=id)
    if usuario:
        return usuario
    else:
        return False


def UpdateUsuario(id=None, nome=None, sobrenome=None, genero=None, nascimento=None,
                    idade=None, altura=None, peso=None):
    imc = peso / ((altura / 100) * (altura / 100))
    agua = peso * 35

    if id is not None:
        usuario = MyUser.objects.filter(pk=id)
        usuario.update(first_name=nome, last_name=sobrenome, genero=genero,
                        nascimento=nascimento, idade=idade, altura=altura,
                        peso=peso, imc=imc, agua=agua)
        return True
    else:
        return False


def ConsumoAgua(id, consumo_agua):
    if id is not None:
        usuario = MyUser.objects.filter(pk=id)
        user = MyUser.objects.get(pk=id)
        log = LogAgua(consumo_agua=consumo_agua, usuario=user, data=datetime.now())
        log.save()
        for u in usuario:
            if u.consumo_agua is not None:
                consumo_agua_atual = float(u.consumo_agua) + float(consumo_agua)
            else:
                consumo_agua_atual = float(consumo_agua)

        usuario.update(consumo_agua=consumo_agua_atual)

        return True
    else:
        return False


def GetUltimoLogAgua(id):
    if id is not None:
        log = LogAgua.objects.filter(usuario=id).last()
        if log:
            return log.data
        else:
            return None
    else:
        return False


def ZeraConsumo(id):
    if id is not None:
        usuario = MyUser.objects.filter(pk=id)
        user = MyUser.objects.get(pk=id)
        log = LogAgua.objects.filter(usuario=id).last()
        if log:
            data = log.data
        for u in usuario:
            consumo_diario = float(u.consumo_agua)
        
        if consumo_diario > 0:
            log_diario = LogAguaDiario(consumo_agua_dia=consumo_diario, data=data, usuario=user)
            log_diario.save()
        usuario.update(consumo_agua=0)
        return True
    else:
        return False


def GetUltimoConsumoDiario(id):
    if id is not None:
        log_diario = LogAguaDiario.objects.filter(usuario=id).last()
        if log_diario:
            return log_diario.consumo_agua_dia
        else:
            return False
    else:
        return False


def GetRelatorioAgua(id):
    if id is not None:
        relatorio = LogAguaDiario.objects.filter(usuario=id).order_by('-id')
    else:
        return False