from django.db import models


# Create your models here.

class StuInfoModel(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=100,null=True)
    date = models.DateField(auto_now=True,null=True)

    def __str__(self):
        return f'{self.name}'


