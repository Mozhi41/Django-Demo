from django.db import models

# Create your models here.

from django.db import models

class JsonData(models.Model):
    data = models.JSONField()