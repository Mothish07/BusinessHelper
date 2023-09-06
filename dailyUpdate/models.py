from django.db import models

# Create your models here.
class daily_Update(models.Model):
    sales = models.IntegerField()
    spend = models.IntegerField()