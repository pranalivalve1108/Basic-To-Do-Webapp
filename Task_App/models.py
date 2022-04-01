from django.db import models

# Create your models here.
class List_Database(models.Model):
    Title=models.CharField(max_length=20,default=' ')
    Description=models.CharField(max_length=200,default=' ', null=False)
    