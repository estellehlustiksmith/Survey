from django.conf import settings
from django.db import models

class Post(models.Model):
    question1= models.TextField()
    question2= models.TextField()
    question3= models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
