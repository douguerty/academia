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
    altura = models.DecimalField(
        verbose_name=_('Altura em cm'),
        max_digits=5,
        decimal_places=2,
    )
    peso = models.DecimalField(
        verbose_name=_('Peso em kg'),
        max_digits=6,
        decimal_places=3,
    )
    imc = models.DecimalField(
        verbose_name=_('IMC - Indice de massa corporal'),
        max_digits=5,
        decimal_places=3,
    )
    nascimento = models.CharField(
        verbose_name=_('Data de nascimento'),
        max_length=10,
    )
    idade = models.IntegerField(
        verbose_name=_('Idade'),
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