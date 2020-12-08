from django.db import models
from django.utils import timezone


# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(default=timezone.now)


