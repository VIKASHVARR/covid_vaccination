from django.db import models

# Create your models here.
class Indianspots(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField()
    price=models.TextField(max_length=20)
    days=models.IntegerField()
    desc=models.TextField(max_length=200,default=None)
    

    def __str__(self):
        return self.name

class Foreignspots(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField()
    price=models.TextField(max_length=20)
    days=models.IntegerField()
    desc=models.TextField(max_length=200,default=None)
    

    def __str__(self):
        return self.name
class Travel(models.Model):
    name=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    price=models.TextField(max_length=20)
    days=models.IntegerField()

    def __str__(self):
        return self.name