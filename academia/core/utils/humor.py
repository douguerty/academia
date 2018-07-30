from core import models
from django.http import HttpResponse
import json


def SaveHumor(id, humor, data):
    if id and humor is not None:
        estado_emocional = models.Humor()
        estado_emocional.usuario = id
        estado_emocional.humor = humor
        estado_emocional.data = data
        estado_emocional.save()
        return estado_emocional
    else:
        return False