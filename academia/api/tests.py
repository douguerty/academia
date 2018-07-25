from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from core.models import MyUser, Exercicio


class TestUser(TestCase):

    def setUp(self):
        self.user = mommy.make(
            MyUser,
            email='alisson@teste.com',
            first_name='Teste',
            last_name='Testando',
            altura='1.79',
            peso='60',
            imc=10.0,
            agua='150',
            consumo_agua='1500',
            nascimento='14/04/1994',
            idade=20,
            genero='2'
        )
    def test_user_creation(self):
        self.assertTrue(isinstance(self.user, MyUser))
        self.assertEquals(self.user.__str__(), self.user.email)

class TestExercicio(TestCase):
    
    def setUp(self):
        self.user = mommy.make(
            MyUser,
            email='alisson@teste.com',
            first_name='Teste',
            last_name='Testando',
            altura='1.79',
            peso='60',
            imc=10.0,
            agua='150',
            consumo_agua='1500',
            nascimento='14/04/1994',
            idade=20,
            genero='2'
        )
        self.exercicio = mommy.make(Exercicio, exercicio='Panturrilha em pé', musculo='5', usuario=self.user)

    def test_exercicio_creation(self):
        self.assertTrue(isinstance(self.exercicio, Exercicio))
        self.assertEquals(self.exercicio.__str__(), self.exercicio.exercicio)