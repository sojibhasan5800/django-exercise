from django.db import models
from authors.models import author
# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=15)
    about = models.TextField()
    author = models.OneToOneField(author,on_delete=models.CASCADE, default=None)
     
    def __str__(self):
        return f"Profile_nickname: {self.name}"