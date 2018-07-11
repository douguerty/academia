from core.models import Registro
from django.http import HttpResponse
import json

def GetTreinamento(usuario):
    treinamentos = Registro.objects.filter(usuario=usuario)
    if treinamentos:
        return treinamentos
    else:
        return False