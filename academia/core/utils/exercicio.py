from core.models import Exercicio
from django.http import HttpResponse
import json

def GetExercicio(usuario):
    exercicios = Exercicio.objects.filter(usuario=usuario)
    if exercicios:
        return exercicios
    else:
        return False


#def UpdateUsuario(id=None, nome=None, sobrenome=None, genero=None, nascimento=None,
#                    idade=None, altura=None, peso=None):
#    imc = peso / ((altura / 100) * (altura / 100))
#
#    if id is not None:
#        usuario = MyUser.objects.filter(pk=id)
#        usuario.update(first_name=nome, last_name=sobrenome, genero=genero,
#                        nascimento=nascimento, idade=idade, altura=altura,
#                        peso=peso, imc=imc)
#        return True
#    else:
#        return False