from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from academia.settings import BASE_DIR


class EmailUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        email = kwargs["email"]
        email = self.normalize_email(email)
        password = kwargs["password"]
        kwargs.pop("password")

        if not email:
            raise ValeuError(_('Necessário um email válido'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        verbose_name=_('Email'),
        unique=True,
    )
    first_name = models.CharField(
        verbose_name=_('Nome'),
        max_length=50,
        blank=False,
        help_text=_('Informe seu nome'),
    )
    last_name = models.CharField(
        verbose_name=_('Sobrenome'),
        max_length=50,
        blank=False,
        help_text=_('Informe seu sobrenome'),
    )
    altura = models.CharField(
        verbose_name=_('Altura em cm'),
        max_length=6,
        blank=True,
    )
    peso = models.CharField(
        verbose_name=_('Peso em kg'),
        max_length=7,
        blank=True,
    )
    imc = models.DecimalField(
        verbose_name=_('IMC - Indice de massa corporal'),
        max_digits=5,
        decimal_places=3,
        blank=True,
        null=True,
    )
    agua = models.CharField(
        verbose_name=_('Quantidade minima de consumo de água por dia'),
        max_length=10,
        blank=True,
        null=True,
    )
    consumo_agua = models.CharField(
        verbose_name=_('Consumo de água hoje'),
        max_length=10,
        blank=True,
        null=True,
    )
    nascimento = models.CharField(
        verbose_name=_('Data de nascimento'),
        max_length=10,
    )
    idade = models.IntegerField(
        verbose_name=_('Idade'),
        blank=True,
        null=True,
    )
    genero = models.CharField(
        max_length=3,
        choices=settings.GENERO_CHOICES,
        default='1',
    )
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = EmailUserManager()


class Exercicio(models.Model):
    exercicio = models.CharField(
        'Exercicio', max_length=150
    )
    musculo = models.CharField(
        max_length=8,
        choices=settings.MUSCULO_CHOICES,
        default='1',
    )
    usuario = models.name = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.exercicio

    def __repr__(self):
        return self.exercicio

    class Meta:
        ordering = ['exercicio']
        verbose_name = 'Exercicio'
        verbose_name_plural = 'Exercicios'


class Registro(models.Model):
    exercicio = models.ForeignKey(
        Exercicio,
        on_delete=models.CASCADE,
        verbose_name=_('Exercício'),
    )
    series = models.IntegerField(
        verbose_name=_('Quantidade de series'),
        blank=True,
        null=True,
        default='-',
    )
    repeticao = models.IntegerField(
        verbose_name=_('Repetições por series'),
        blank=True,
        null=True,
        default='-',
    )
    tempo = models.CharField(
        verbose_name=_('Tempo gasto no exercicio'),
        max_length=10,
        blank=True,
        null=True,
        default='-',
    )
    distancia = models.CharField(
        verbose_name=_('Distancia percorrida'),
        max_length=10,
        blank=True,
        null=True,
        default='-',
    )
    peso = models.DecimalField(
        verbose_name=_('Peso em kg'),
        max_digits=7,
        decimal_places=3,
        blank=True,
        null=True,
        default='-',
    )

    usuario = models.name = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ['exercicio']
        verbose_name = 'Exercicio'
        verbose_name_plural = 'Exercicios'


class LogAgua(models.Model):
    consumo_agua = models.CharField(
        verbose_name=_('Consumo de água em ml'),
        max_length=10,
        blank=True,
        null=True,
    )

    data = models.DateTimeField()

    usuario = models.name = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.consumo_agua

    def __repr__(self):
        return self.consumo_agua

    class Meta:
        ordering = ['data']
        verbose_name = 'Log consumo de agua'
        verbose_name_plural = 'Logs consumo de agua'


class LogAguaDiario(models.Model):
    consumo_agua_dia = models.CharField(
        verbose_name=_('Consumo de água em ml'),
        max_length=10,
        blank=True,
        null=True,
    )

    data = models.DateTimeField()

    usuario = models.name = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.consumo_agua_dia

    def __repr__(self):
        return self.consumo_agua_dia

    class Meta:
        ordering = ['id']
        verbose_name = 'Log consumo de agua diario'
        verbose_name_plural = 'Logs consumo de agua diario'