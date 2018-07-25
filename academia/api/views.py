from django.shortcuts import render
from core import models
from rest_framework import viewsets
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.MyUser.objects.all().order_by('-pk')
    serializer_class = serializers.UserSerializer


class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = models.Exercicio.objects.all().order_by('-pk')
    serializer_class = serializers.ExercicioSerializer


class TreinamentoViewSet(viewsets.ModelViewSet):
    queryset = models.Treinamento.objects.all().order_by('-pk')
    serializer_class = serializers.TreinamentoSerializer


class LogAguaViewSet(viewsets.ModelViewSet):
    queryset = models.LogAgua.objects.all().order_by('-pk')
    serializer_class = serializers.LogAguaSerializer


class LogAguaDiarioViewSet(viewsets.ModelViewSet):
    queryset = models.LogAguaDiario.objects.all().order_by('-pk')
    serializer_class = serializers.LogAguaDiarioSerializer