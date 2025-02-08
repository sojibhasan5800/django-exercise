from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class author(models.Model):
    name = models.CharField(max_length=15)
    bio = models.TextField()
    number = models.CharField(max_length=11 ,validators=[MinLengthValidator(11)])

    def __str__(self):
        return f"Author: {self.name}"

