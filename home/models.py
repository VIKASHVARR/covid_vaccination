from django.db import models

class district(models.Model):
    name=models.CharField(max_length=30)
    date=models.DateField()
    no_of_centers=models.IntegerField()
    timing=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class centers(models.Model):
    center_name=models.CharField(max_length=30)
    city=models.ForeignKey(district,on_delete=models.CASCADE)
    vaccine=models.CharField(max_length=30)
    dose_avva=models.IntegerField()
    
    def __str__(self):
        return self.center_name
    
class list(models.Model):
    name=models.CharField(max_length=30)
    vaccine=models.CharField(max_length=30)
    area=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
