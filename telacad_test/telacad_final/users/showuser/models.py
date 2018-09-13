from django.db import models

# Create your models here.
class Users(models.Model):
    """"
    Tabela trebuie sa contina first_name, last_name,  number_of_ login.
    Creati un model mapat la aceasta tabela si-nregistrati-l in admin
    """
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    logins = models.IntegerField()