from django.db import models

# Create your models here.


class Todo(models.Model):
    date = models.DateField()
    task = models.TextField()
