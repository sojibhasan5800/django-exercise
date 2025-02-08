from django.db import models
from catagories.models import catagori
from authors.models import author
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    catagori = models.ManyToManyField(catagori)
    author = models.ForeignKey(author,on_delete=models.CASCADE)
    def __str__(self):
        return f"Heading: {self.title}"