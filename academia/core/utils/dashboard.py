from core import models
from django.http import HttpResponse
import json


def GetDashboard(id):
    usuario = models.MyUser.objects.filter(pk=id)
    if usuario:
        for u in usuario:
            codigo = u.pk
            first_name = u.first_name
            last_name = u.last_name
            altura = u.altura
            peso = u.peso
            imc = str(u.imc)
            agua = u.agua
            consumo_agua = u.consumo_agua
            nascimento = u.nascimento
            idade = u.idade
            genero = u.genero

        usuario = {
            'usuario': codigo,
            'first_name': first_name,
            'last_name': last_name,
            'altura': altura,
            'peso': peso,
            'imc': imc,
            'agua': agua,
            'consumo_agua': consumo_agua,
            'nascimento': nascimento,
            'idade': idade,
            'genero': genero
        }

        dashboard = [
            usuario
        ]
        return dashboard
    else:
        return False