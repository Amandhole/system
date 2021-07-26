from django.db import models

# Create your models here.
class Data(models.Model):
    title=models.CharField(max_length=50)
    price=models.FloatField()
    author=models.CharField(max_length=50)
    publisher=models.CharField(max_length=50)


    def __str__(self):
      return self.title