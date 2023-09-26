from django.db import models

# Create your models here.
from datetime import datetime
class post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=20000)
    d_time = models.DateTimeField(default=datetime.now(),blank=True)