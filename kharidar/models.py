from django.db import models
from django.contrib.auth.models import User
from forooshande.models import Ja




class Kharidar(User):
    wallet = models.FloatField()



class Reserve(models.Model):
    kharidar = models.ForeignKey(Kharidar , on_delete=models.PROTECT)
    ja = models.ForeignKey(Ja , on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()








