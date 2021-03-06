from core import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields = ('id', 'email', 'first_name', 'last_name', 'altura',
            'peso', 'imc', 'agua', 'consumo_agua', 'nascimento', 'idade',
            'genero'
        )

class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exercicio
        fields = ('__all__')

class TreinamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Treinamento
        fields = ('__all__')

class LogAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LogAgua
        fields = ('__all__')

class LogAguaDiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LogAguaDiario
        fields = ('__all__')