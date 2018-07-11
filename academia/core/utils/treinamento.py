from core.models import Registro
from django.http import HttpResponse
import json

def GetTreinamento(usuario):
    treinamentos = Registro.objects.filter(usuario=usuario)
    if treinamentos:
        return treinamentos
    else:
        return False


def DeleteTreinamento(id_treinamento, usuario):
    treinamento = Registro.objects.filter(pk=id_treinamento, usuario=usuario)
    treinamento.delete()
    return True