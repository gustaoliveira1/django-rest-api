from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    data_de_nascimento = models.DateField()

    objects = UserManager()

    USERNAME_FIELD = "email"