from django.db import models

# Create your models here.

class Patient(models.Model):
    code=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    house=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    symptoms=models.TextField(max_length=10000)
    disease=models.TextField(max_length=10000)
    medicine=models.TextField(max_length=10000)
    date=models.DateTimeField(auto_now=False)
    
    def __str__(self):
        return self.code
    