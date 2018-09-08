from django.db import models

# Create your models here.


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    nume = models.CharField(max_length=50)
    phonenumber = models.IntegerField()
    mail = models.CharField(max_length=50)

    class Meta:
        db_table = "personmodel"

    def __str__(self):
        return self.nume


# $~python manage.py makemigration
# $~python magage.py migrate (now it migrates)
