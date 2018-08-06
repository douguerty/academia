from core import models
from django.http import HttpResponse
from datetime import datetime, timedelta
import json


def GetDashboard(id, chart=None, data_de=None, data_ate=None):
    if id:
        usuario = models.MyUser.objects.filter(pk=id)
        humor = models.Humor.objects.filter(usuario=id)
        bom = humor.filter(humor__in=('1', '2', '3', '4'))
        ruim = humor.filter(humor__in=('5', '7', '9', '10', '11', '12'))

        hoje = datetime.now()
        futuro_30 = hoje - timedelta(30)
        futuro_60 = futuro_30 - timedelta(30)
        futuro_90 = futuro_60 - timedelta(30)
        futuro_120 = futuro_90 - timedelta(30)

        bom_30 = bom.filter(data__range=(futuro_30, hoje)).count()
        bom_60 = bom.filter(data__range=(futuro_60, futuro_30)).count()
        bom_90 = bom.filter(data__range=(futuro_90, futuro_60)).count()
        bom_120 = bom.filter(data__range=(futuro_120, futuro_90)).count()
        bom_up_120 = bom.filter(data__lte=(futuro_120)).count()

        ruim_30 = ruim.filter(data__range=(futuro_30, hoje)).count()
        ruim_60 = ruim.filter(data__range=(futuro_60, futuro_30)).count()
        ruim_90 = ruim.filter(data__range=(futuro_90, futuro_60)).count()
        ruim_120 = ruim.filter(data__range=(futuro_120, futuro_90)).count()
        ruim_up_120 = ruim.filter(data__lte=(futuro_120)).count()



        if bom_30 + ruim_30 > 0:
            bom_30 = ((bom_30/(bom_30+ruim_30))*100)
        else:
            bom_30 = 0

        if bom_60 + ruim_60 > 0:
            bom_60 = ((bom_60/(bom_60+ruim_60))*100)
        else:
            bom_60 = 0

        if bom_90 + ruim_90 > 0:
            bom_90 = ((bom_90/(bom_90+ruim_90))*100)
        else:
            bom_90 = 0

        if bom_120 + ruim_120 > 0:
            bom_120 = ((bom_120/(bom_120+ruim_120))*100)
        else:
            bom_120 = 0

        if bom_up_120 + ruim_up_120 > 0:
            bom_up_120 = ((bom_up_120/(bom_up_120+ruim_up_120))*100)
        else:
            bom_up_120 = 0

        humores = {
            'bom_30': bom_30, 'bom_60': bom_60,
            'bom_90': bom_90, 'bom_120': bom_120,
            'bom_up_120': bom_up_120
        }

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
        else:
            usuario = {
                'usuario': False
            }
            return False

        if chart is not None:
            treinamentos = models.Treinamento.objects.filter(usuario=id)
            if treinamentos:
                if data_de is not None and data_ate is not None:
                    treinamentos = treinamentos.filter(
                        data__range=(data_de, data_ate)
                    )
                    for t in treinamentos:
                        exercicio = t.exercicio.exercicio
                        musculo = t.exercicio.musculo

                    treinamentos = {
                        'exercicio': exercicio,
                        'musculo': musculo
                    }
        else:
            treinamentos = {
                'treinamentos': False
            }

        dashboard = [
                usuario, humores, treinamentos
            ]
        return dashboard
    else:
        return False