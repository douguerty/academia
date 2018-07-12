from core.models import Exercicio
from django.http import HttpResponse
import json

def GetExercicio(usuario):
    exercicios = Exercicio.objects.filter(usuario=usuario)
    if exercicios:
        return exercicios
    else:
        return False


def DeleteExercicio(id_exercicio, usuario):
    exercicio = Exercicio.objects.filter(pk=id_exercicio, usuario=usuario)
    exercicio.delete()
    return True