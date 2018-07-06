from core.models import MyUser
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

    if id is not None:
        usuario = MyUser.objects.filter(pk=id)
        usuario.update(first_name=nome, last_name=sobrenome, genero=genero,
                        nascimento=nascimento, idade=idade, altura=altura,
                        peso=peso, imc=imc)
        return True
    else:
        return False