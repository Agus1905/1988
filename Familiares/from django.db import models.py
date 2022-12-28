from django.db import models

class Familiares(models.Model)
     names = models.CharField(max_length=3)
     age =  models.IntegerField()
     civil_status = models.BooleanField()
     
