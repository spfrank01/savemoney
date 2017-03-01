from django.db import models

# Create your models here.
class SaveMoney(models.Model):
    detail = models.CharField(max_length=200)
    money = models.IntegerField(default=0)
    dateTime = models.DateTimeField('date published')

    def __str__(self): #How To Get data
        return self.detail

    def get_abs(self):
        return abs(self.money)
