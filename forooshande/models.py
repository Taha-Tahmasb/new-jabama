from django.db import models
from django.contrib.auth.models import User




class Ja(models.Model):
    neighbor =models.CharField(max_length=20)
    address = models.TextField()
    description = models.TextField()
    cap = models.PositiveIntegerField()
    price = models.FloatField()




class Forooshandeh(User):
    wallet = models.FloatField()
    ja = models.ManyToManyField(Ja)


