from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    adress = models.TextField()
    number = models.IntegerField(default=10)
    
    def __str__(self):
        return f"Name :{self.name}"
    