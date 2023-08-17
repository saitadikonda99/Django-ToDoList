from django.db import models
from django.utils import timezone
# Create your models here.


class Todo(models.Model):
    time = models.TimeField(default=timezone.now)  
    task = models.TextField()
