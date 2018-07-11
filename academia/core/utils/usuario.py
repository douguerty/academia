from core.models import MyUser, LogAgua
from django.http import HttpResponse
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
        log = LogAgua.objects.all()
        print(log)
        for u in usuario:
            if u.consumo_agua is not None:
                consumo_agua_atual = float(u.consumo_agua) + float(consumo_agua)
            else:
                consumo_agua_atual = float(consumo_agua)

        usuario.update(consumo_agua=consumo_agua_atual)

        return True
    else:
        return False