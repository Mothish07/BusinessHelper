from django.db import models

# Create your models here.
class purchase_Update(models.Model):
    shopName = models.CharField(max_length=100,null=False,blank=False)
    price = models.IntegerField()
