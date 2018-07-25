from core.models import Treinamento
from django.http import HttpResponse
import json

def GetTreinamento(usuario):
    treinamentos = Treinamento.objects.filter(usuario=usuario).order_by('-data')
    if treinamentos:
        return treinamentos
    else:
        return False


def DeleteTreinamento(id_treinamento, usuario):
    treinamento = Treinamento.objects.filter(pk=id_treinamento, usuario=usuario)
    treinamento.delete()
    return True